// tiles.js — SCHERPE, CONSISTENTE KAART BIJ INZOOMEN.
//
// Het probleem: de bol draagt één plaatje van 4096×2048 px. Dat is ongeveer
// 10 km per pixel. Uitgezoomd prachtig, ingezoomd pap — je ziet niet meer welke
// baai Bunbury is of waar de Straat van Lombok precies loopt.
//
// De oplossing is wat Google Earth ook doet: TEGELS STREAMEN. Zodra je onder een
// bepaalde hoogte komt, berekent deze laag welk stukje aarde je bekijkt, laadt
// daarvoor een handvol scherpe tegels, en legt die als pleister over de bol.
//
// TWEE LAGEN (LAR-393):
//   SHELL   — de héle bol, altijd, met GROVE tegels. Hangt niet af van waar je
//             kijkt, dus stabiel en zonder naad. Dit vervangt visueel de
//             blue-marble-textuur zodra je inzoomt.
//   DETAIL  — een scherpe patch met FIJNE tegels in het midden van beeld, boven
//             op de shell. De grens tussen beide is scherp -> minder scherp van
//             DEZELFDE kaartbron, dus geen zichtbare kaartwissel meer.
// Vroeger was er alleen de detailpatch: die lag los boven op de blue-marble en
// rondom scheen de blue-marble door -> "twee kaarten naast elkaar".
//
// BRONNEN (Google Earth-tegels mogen niet — die zijn licentietechnisch dicht):
//   satelliet  Esri World Imagery      — tot straatniveau, attributie verplicht
//   kaart      OpenStreetMap           — mét plaatsnamen, havens, wegen (ODbL)
// Beide zijn gratis te gebruiken met bronvermelding (zie #attrib in index.html).
//
// TECHNISCH: webtegels zijn Web Mercator, de bol is een bol. Elke tegel krijgt
// daarom een eigen stukje bolgeometrie waarvan de breedtegraden exact volgens
// de Mercator-formule liggen. Anders schuift de kaart een paar kilometer op —
// en juist bij zeestraten valt dat meteen op.

const TileLayer = (function () {
  const C = CONFIG.tiles;
  const R = GLOBE.RADIUS;

  const group = new THREE.Group();
  GLOBE.globeGroup.add(group);
  const shellGroup = new THREE.Group();    // hele bol, grove tegels (geen naad)
  const detailGroup = new THREE.Group();   // scherpe patch in het midden van beeld
  group.add(shellGroup);
  group.add(detailGroup);

  const loader = new THREE.TextureLoader();
  loader.setCrossOrigin("anonymous");

  const cache = new Map();       // "src/z/x/y" -> texture
  const shellLive = new Map();   // "z/x/y" -> mesh (whole-globe shell)
  const detailLive = new Map();  // "z/x/y" -> mesh (viewport detail)
  let source = C.default;
  let shellKey = "";
  let detailKey = "";
  let enabled = true;

  const D2R = Math.PI / 180;
  const R2D = 180 / Math.PI;

  // ---------------------------------------------------- Mercator <-> lat/lon
  function latOfMercY(t) {                       // t = 0..1 van boven naar onder
    return Math.atan(Math.sinh(Math.PI * (1 - 2 * t))) * R2D;
  }
  function mercYOfLat(lat) {
    const s = Math.sin(lat * D2R);
    return 0.5 - Math.log((1 + s) / (1 - s)) / (4 * Math.PI);
  }

  function tileUrl(z, x, y) {
    const src = C.sources[source];
    const sub = src.subdomains
      ? src.subdomains[(x + y) % src.subdomains.length]
      : "";
    return src.url
      .replace("{s}", sub)
      .replace("{z}", z)
      .replace("{x}", x)
      .replace("{y}", y);
  }

  // ------------------------------------------------------------- GEOMETRIE
  // Eén tegel = een lapje bol. De hoekpunten volgen de Mercator-verdeling,
  // zodat de tegel precies past op de plek waar hij hoort. `lift` bepaalt hoe
  // ver boven het oppervlak (shell iets lager, detail iets hoger). `detail` is
  // het aantal onderverdelingen: grote shell-tegels hebben er meer nodig, anders
  // duiken hun platte facetten onder de bol.
  function tileGeometry(z, x, y, lift, detail) {
    const n = Math.pow(2, z);
    const N = detail;
    const lonL = (x / n) * 360 - 180;
    const lonR = ((x + 1) / n) * 360 - 180;

    const pos = [];
    const uv = [];
    const idx = [];

    for (let j = 0; j <= N; j++) {
      const tY = (y + j / N) / n;
      const lat = latOfMercY(tY);
      for (let i = 0; i <= N; i++) {
        const lon = lonL + (lonR - lonL) * (i / N);
        const v = latLonToVec3(lat, lon, R * lift);
        pos.push(v.x, v.y, v.z);
        uv.push(i / N, 1 - j / N);
      }
    }
    for (let j = 0; j < N; j++) {
      for (let i = 0; i < N; i++) {
        const a = j * (N + 1) + i;
        const b = a + 1;
        const c = a + (N + 1);
        const d = c + 1;
        idx.push(a, c, b, b, c, d);
      }
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
    geo.setAttribute("uv", new THREE.Float32BufferAttribute(uv, 2));
    geo.setIndex(idx);
    geo.computeVertexNormals();
    return geo;
  }

  // Zorg dat tegel z/x/y in `grp`/`liveMap` bestaat (en laad de textuur async).
  function ensureTile(grp, liveMap, z, x, y, lift, order, detail) {
    const id = `${z}/${x}/${y}`;
    if (liveMap.has(id)) return;

    const mesh = new THREE.Mesh(
      tileGeometry(z, x, y, lift, detail),
      new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false })
    );
    mesh.renderOrder = order;
    grp.add(mesh);
    liveMap.set(id, mesh);

    const cacheKey = source + "/" + id;
    if (cache.has(cacheKey)) {
      mesh.material.map = cache.get(cacheKey);
      mesh.material.needsUpdate = true;
      mesh.userData.fade = true;
    } else {
      loader.load(tileUrl(z, x, y), (tex) => {
        tex.encoding = THREE.sRGBEncoding;
        tex.anisotropy = GLOBE.renderer.capabilities.getMaxAnisotropy();
        tex.minFilter = THREE.LinearFilter;
        tex.generateMipmaps = false;
        cache.set(cacheKey, tex);
        if (mesh.parent) {
          mesh.material.map = tex;
          mesh.material.needsUpdate = true;
          mesh.userData.fade = true;
        }
      }, undefined, () => {
        // Meestal CORS: bij dubbelklikken op index.html (file://) weigeren
        // de tegelservers. Draai een lokale server, zie README.
        console.warn("tegel niet geladen:", tileUrl(z, x, y));
      });
    }
  }

  function pruneTiles(grp, liveMap, wanted) {
    liveMap.forEach((mesh, id) => {
      if (wanted.has(id)) return;
      grp.remove(mesh);
      mesh.geometry.dispose();
      mesh.material.dispose();
      liveMap.delete(id);
    });
  }

  function clearMap(grp, liveMap) {
    liveMap.forEach((mesh) => {
      grp.remove(mesh);
      mesh.geometry.dispose();
      mesh.material.dispose();
    });
    liveMap.clear();
  }

  // ------------------------------------------------------------- ZICHTBAARHEID
  // Welk punt van de bol kijkt de camera aan, en hoe groot is het zichtveld?
  function viewCentre() {
    const q = GLOBE.globeGroup.quaternion.clone().invert();
    const v = new THREE.Vector3(0, 0, 1).applyQuaternion(q);
    const lat = 90 - Math.acos(Math.max(-1, Math.min(1, v.y))) * R2D;
    const lon = Math.atan2(v.z, -v.x) * R2D - 180;
    return { lat, lon: ((lon + 540) % 360) - 180 };
  }

  // halve openingshoek van het zichtbare stuk bol, in graden
  function halfSpanDeg(z) {
    const d = Math.max(0.05, z - R);
    const halfFov = (GLOBE.camera.fov / 2) * D2R;
    return Math.atan((d * Math.tan(halfFov)) / R) * R2D;
  }

  // Welk tegel-zoomniveau geeft ongeveer `tilesAcross` scherpe tegels over beeld?
  function detailZoomFor(spanDeg) {
    const want = Math.log2((360 * C.tilesAcross) / (2 * spanDeg));
    return Math.max(C.minZ, Math.min(C.maxZ, Math.round(want)));
  }

  // Grove shell-zoom: een paar niveaus onder de detail-zoom, hard begrensd zodat
  // de héle bol nooit meer dan 4^shellMaxZ tegels kost (z=2 -> 16, z=3 -> 64).
  function shellZoomFor(detailZ) {
    return Math.max(C.shellMinZ, Math.min(C.shellMaxZ, detailZ - C.shellZBelowDetail));
  }

  // ------------------------------------------------------------------ SHELL
  // De hele bol met grove tegels. Onafhankelijk van de kijkrichting, dus de
  // sleutel is alleen bron + zoom: hij herbouwt niet bij het draaien.
  function updateShell(shellZ) {
    const key = `${source}/${shellZ}`;
    if (key === shellKey) return;
    shellKey = key;

    const n = Math.pow(2, shellZ);
    const y0 = Math.max(0, Math.floor(mercYOfLat(85) * n));
    const y1 = Math.min(n - 1, Math.floor(mercYOfLat(-85) * n));

    const wanted = new Set();
    for (let y = y0; y <= y1; y++) {
      for (let x = 0; x < n; x++) {
        wanted.add(`${shellZ}/${x}/${y}`);
        ensureTile(shellGroup, shellLive, shellZ, x, y, C.shellLift, 1, C.shellMeshDetail);
      }
    }
    pruneTiles(shellGroup, shellLive, wanted);
  }

  // ----------------------------------------------------------------- DETAIL
  // Scherpe patch rond het midden van beeld. Alleen zinvol als de detail-zoom
  // écht fijner is dan de shell.
  function updateDetail(camZ, detailZ, shellZ) {
    if (detailZ <= shellZ) {
      if (detailLive.size) { clearMap(detailGroup, detailLive); detailKey = ""; }
      return;
    }

    const span = halfSpanDeg(camZ);
    const { lat, lon } = viewCentre();
    const n = Math.pow(2, detailZ);

    // begrens het zichtbare gebied; bij hoge breedtegraden rekt lengtegraad op
    const latPad = Math.min(80, span * 1.25);
    const cosLat = Math.max(0.15, Math.cos(lat * D2R));
    const lonPad = Math.min(180, (span * 1.25) / cosLat);

    const x0 = Math.floor(((lon - lonPad + 180) / 360) * n);
    const x1 = Math.floor(((lon + lonPad + 180) / 360) * n);
    const y0 = Math.floor(mercYOfLat(Math.min(85, lat + latPad)) * n);
    const y1 = Math.floor(mercYOfLat(Math.max(-85, lat - latPad)) * n);

    const key = `${source}/${detailZ}/${x0},${x1},${y0},${y1}`;
    if (key === detailKey) return;      // niets veranderd -> niets doen
    detailKey = key;

    const wanted = new Set();
    let budget = C.maxTiles;

    for (let y = Math.max(0, y0); y <= Math.min(n - 1, y1) && budget > 0; y++) {
      for (let x = x0; x <= x1 && budget > 0; x++) {
        const xw = ((x % n) + n) % n;   // over de datumgrens heen blijven werken
        wanted.add(`${detailZ}/${xw}/${y}`);
        budget--;
        ensureTile(detailGroup, detailLive, detailZ, xw, y, C.detailLift, 2, C.meshDetail);
      }
    }
    pruneTiles(detailGroup, detailLive, wanted);
  }

  // ------------------------------------------------------------------ UPDATE
  function update() {
    const camZ = GLOBE.camera.position.z;

    // ver uitgezoomd: geen tegels, gewoon de mooie blue-marble bol
    if (!enabled || camZ > C.showBelowCameraZ) {
      if (shellLive.size || detailLive.size) {
        clearMap(shellGroup, shellLive);
        clearMap(detailGroup, detailLive);
        shellKey = ""; detailKey = "";
      }
      if (typeof Basemap !== "undefined") Basemap.setOverlayVisible(true);
      return;
    }
    // tegels aan -> de grove vectorkustlijnen uit (die zouden ernaast liggen)
    if (typeof Basemap !== "undefined") Basemap.setOverlayVisible(false);

    const detailZ = detailZoomFor(halfSpanDeg(camZ));
    const shellZ = shellZoomFor(detailZ);
    updateShell(shellZ);
    updateDetail(camZ, detailZ, shellZ);
  }

  // niet elk frame herberekenen — dat is zonde en het flikkert
  let acc = 0;
  function fadeIn(mesh) {
    if (mesh.userData.fade && mesh.material.opacity < 1) {
      mesh.material.opacity = Math.min(1, mesh.material.opacity + 0.06);
    }
  }
  GLOBE.onTick(() => {
    // zachte fade-in van geladen tegels
    shellLive.forEach(fadeIn);
    detailLive.forEach(fadeIn);
    acc += 0.016;
    if (acc < C.updateInterval) return;
    acc = 0;
    update();
  });

  function rebuildAll() {
    shellKey = ""; detailKey = "";
    clearMap(shellGroup, shellLive);
    clearMap(detailGroup, detailLive);
    update();
  }

  return {
    setSource(name) {
      if (!C.sources[name]) return;
      source = name;
      rebuildAll();
    },
    setEnabled(v) { enabled = !!v; rebuildAll(); },
    isEnabled: () => enabled,
    currentSource: () => source,
    attribution: () => C.sources[source].attribution,
  };
})();
