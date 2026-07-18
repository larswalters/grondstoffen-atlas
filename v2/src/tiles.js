// tiles.js — satellietbeeld dat scherp blijft tot straatniveau.
//
// Overgezet uit v1 (src/tiles.js), met dezelfde bron als earth3dmap.com:
// Esri World Imagery. Het principe is dat van Google Earth: één plaatje van de
// hele aarde wordt bij inzoomen altijd pap, dus streamen we TEGELS — kleine
// stukjes kaart op het detailniveau dat bij je kijkhoogte past.
//
// TWEE LAGEN (v1/LAR-393, bewust overgenomen):
//   SHELL   de héle bol met grove tegels. Hangt niet af van je kijkrichting,
//           dus stabiel en naadloos; vervangt visueel de blue-marble-textuur.
//   DETAIL  een scherpe patch in het midden van beeld, boven op de shell.
//           Grens = scherp -> minder scherp van DEZELFDE bron, geen kaartwissel.
//
// TWEE VALKUILEN die v1 duur heeft geleerd (LAR-479) en die hier bewaard zijn:
//   1. cos(lat) in detailZoomFor. Een Mercator-tegel op 60° breedte beslaat de
//      helft van de grond van eentje op de evenaar; zonder die term vraag je
//      hoe noordelijker hoe meer tegels voor dezelfde scherpte — verspilling
//      die bovendien het budget opblaast (Noorwegen kwam op 33% dekking uit).
//   2. De patch vult VAN HET MIDDEN NAAR BUITEN. Vult hij op volgorde (noord
//      naar zuid) en loopt het budget leeg, dan verlies je structureel de
//      onderste rijen. Van binnen naar buiten verlies je hooguit de rand.
//
// Web Mercator is plat, de bol is bol: elke tegel krijgt een eigen lapje
// bolgeometrie waarvan de breedtegraden exact volgens de Mercator-formule
// liggen. Anders schuift de kaart kilometers op — en juist bij zeestraten
// valt dat meteen op.

import * as THREE from "three";

const D2R = Math.PI / 180;
const R2D = 180 / Math.PI;

export const TILE_CONFIG = {
  bronnen: {
    satelliet: {
      url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
      attributie: "Satelliet: Esri, Maxar, Earthstar Geographics",
      maxZ: 19,
    },
    kaart: {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      subdomeinen: ["a", "b", "c"],
      attributie: "Kaart: © OpenStreetMap-bijdragers",
      maxZ: 19,
    },
  },

  tilesAcross: 4.5,   // hoeveel scherpe tegels ongeveer over het beeld
  minZ: 2,
  maxTiles: 96,       // noodrem voor de detailpatch, geen dagelijkse limiet
  meshDetail: 8,      // onderverdeling per detailtegel (Mercator-correctie)
  updateInterval: 0.2,

  shellMinZ: 2,
  // z3 = 64 tegels over de hele bol. Op z4 zijn het er 256 — vier keer zoveel
  // textuurgeheugen voor een laag die je bij diep inzoomen niet eens ziet
  // (de detailpatch ligt eroverheen). v1 zat om dezelfde reden op 3.
  shellMaxZ: 3,
  shellZBelowDetail: 3,
  // Grote shell-tegels hebben een FIJN raster nodig. Een z=3-tegel beslaat 45°
  // lengte en (rond de evenaar) ~41° breedte; met te weinig onderverdeling zijn
  // de facetten zo plat dat hun koorde ~2 km onder de bol duikt. v1 zat op 24 en
  // dat was empirisch bepaald — ik zette 'm bij het overzetten op 16 en dat is
  // precies het ringpatroon boven de pool dat Lars zag.
  shellMeshDetail: 24,

  // Tegels liggen praktisch OP het oppervlak; de bol eronder zakt in plaats
  // daarvan weg (zie setSphereSink in globe.js). Zo blijft diep inzoomen kloppen:
  // v1's `shellLift: 1.0016` is 3,8 km en daar zou je op 1 km hoogte onderuit komen.
  shellLift: 1.0,
  detailLift: 1.00002,   // haartje boven de shell; de volgorde doet het echte werk
};

export function createTileLayer(GLOBE) {
  const C = TILE_CONFIG;
  const R = GLOBE.radius;

  const group = new THREE.Group();
  const shellGroup = new THREE.Group();
  const detailGroup = new THREE.Group();
  group.add(shellGroup);
  group.add(detailGroup);
  GLOBE.globeGroup.add(group);

  const loader = new THREE.TextureLoader();
  loader.setCrossOrigin("anonymous");

  const cache = new Map();
  const shellLive = new Map();
  const detailLive = new Map();

  let bron = "satelliet";
  let shellKey = "";
  let detailKey = "";
  let aan = true;
  let geladen = 0;
  let mislukt = 0;

  // ---------------------------------------------------- Mercator <-> lat/lon
  function latOfMercY(t) {
    return Math.atan(Math.sinh(Math.PI * (1 - 2 * t))) * R2D;
  }
  function mercYOfLat(lat) {
    const s = Math.sin(lat * D2R);
    return 0.5 - Math.log((1 + s) / (1 - s)) / (4 * Math.PI);
  }

  // Zelfde afspraak als world.js en v1's latLonToVec3 — MOET gelijk zijn,
  // anders liggen tegels en kustlijnen niet op elkaar.
  function latLonNaarVec3(lat, lon, r) {
    const la = lat * D2R;
    const lo = lon * D2R;
    const cl = Math.cos(la);
    return new THREE.Vector3(r * cl * Math.cos(lo), r * Math.sin(la), -r * cl * Math.sin(lo));
  }

  function tegelUrl(z, x, y) {
    const src = C.bronnen[bron];
    const sub = src.subdomeinen ? src.subdomeinen[(x + y) % src.subdomeinen.length] : "";
    return src.url
      .replace("{s}", sub)
      .replace("{z}", z)
      .replace("{x}", x)
      .replace("{y}", y);
  }

  // ------------------------------------------------------------- geometrie
  function tegelGeometrie(z, x, y, lift, detail) {
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
        const v = latLonNaarVec3(lat, lon, R * lift);
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
    return geo;
  }

  function zorgVoorTegel(grp, live, z, x, y, lift, order, detail) {
    const id = `${z}/${x}/${y}`;
    if (live.has(id)) return;

    // BEGINT ONZICHTBAAR (opacity 0) en vaadt pas in zodra de textuur er is.
    // Anders schildert een nog-lege tegel als dichte vlek over de bol — dat gaf
    // horizontale banden en een ruitjespatroon boven de pool zolang er tegels
    // onderweg waren. v1 deed dit goed; bij het overzetten ben ik het kwijtgeraakt.
    const mesh = new THREE.Mesh(
      tegelGeometrie(z, x, y, lift, detail),
      new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false })
    );
    mesh.renderOrder = order;
    grp.add(mesh);
    live.set(id, mesh);

    const sleutel = bron + "/" + id;
    if (cache.has(sleutel)) {
      mesh.material.map = cache.get(sleutel);
      mesh.material.needsUpdate = true;
      mesh.userData.vaadIn = true;
      return;
    }

    loader.load(
      tegelUrl(z, x, y),
      (tex) => {
        // r185: colorSpace, niet meer encoding (dat was r128).
        tex.colorSpace = THREE.SRGBColorSpace;
        tex.anisotropy = GLOBE.renderer.capabilities.getMaxAnisotropy();
        tex.minFilter = THREE.LinearFilter;
        tex.generateMipmaps = false;
        cache.set(sleutel, tex);
        geladen++;
        if (mesh.parent) {
          mesh.material.map = tex;
          mesh.material.needsUpdate = true;
          mesh.userData.vaadIn = true;
        }
      },
      undefined,
      () => {
        // Mislukt (404 boven open oceaan op hoge zoom, of netwerk). Weghalen,
        // dan schijnt de laag eronder door in plaats van een gat te tonen.
        mislukt++;
        if (mesh.parent) {
          grp.remove(mesh);
          mesh.geometry.dispose();
          mesh.material.dispose();
          live.delete(id);
        }
      }
    );
  }

  function snoei(grp, live, gewenst) {
    live.forEach((mesh, id) => {
      if (gewenst.has(id)) return;
      grp.remove(mesh);
      mesh.geometry.dispose();
      mesh.material.dispose();
      live.delete(id);
    });
  }

  function leeg(grp, live) {
    live.forEach((mesh) => {
      grp.remove(mesh);
      mesh.geometry.dispose();
      mesh.material.dispose();
    });
    live.clear();
  }

  // ------------------------------------------------------------ zichtbaarheid
  function kijkMidden() {
    const q = GLOBE.globeGroup.quaternion.clone().invert();
    const v = new THREE.Vector3(0, 0, 1).applyQuaternion(q);
    const lat = Math.asin(Math.max(-1, Math.min(1, v.y))) * R2D;
    const lon = Math.atan2(-v.z, v.x) * R2D;
    return { lat, lon: ((lon + 540) % 360) - 180 };
  }

  // Halve openingshoek van het zichtbare stuk bol, in graden.
  function halveSpanDeg() {
    const d = Math.max(1e-5, GLOBE.getAltitude());
    const halfFov = (GLOBE.camera.fov / 2) * D2R;
    return Math.atan((d * Math.tan(halfFov)) / R) * R2D;
  }

  // SCHERMBREEDTE TELT MEE (zelfde fix als v1, commit c714297). `tilesAcross`
  // was een vaste 4,5 — dat is ~1.150 px brontextuur over de hele beeldbreedte,
  // ongeacht het scherm. Op een telefoon scherp, maar uitgesmeerd over een
  // monitor van 1920+ px wazig (Lars: "op de pc is het niet scherp"). Doel is
  // ~1 textuurpixel per schermpixel: beeldbreedte in device-pixels ÷ 256. De
  // vaste waarde blijft de ondergrens (en de terugval bij een verborgen canvas
  // met breedte 0); de cap 14 (≈ 3.584 px bron) dekt een ultrawide 2K op volle
  // scherpte en houdt 4K beschaafd.
  function tilesAcrossEff() {
    const px = GLOBE.renderer.domElement.width; // device-pixels (incl. pixelRatio)
    return Math.max(C.tilesAcross, Math.min(14, px / 256));
  }

  function detailZoomVoor(spanDeg, lat) {
    const cosLat = Math.max(0.15, Math.cos(lat * D2R));   // VALKUIL 1
    const wil = Math.log2((360 * tilesAcrossEff() * cosLat) / (2 * spanDeg));
    return Math.max(C.minZ, Math.min(C.bronnen[bron].maxZ, Math.round(wil)));
  }

  // Het budget schaalt MEE met de fijnere zoom (kwadratisch: 2× zo fijn = 4×
  // zoveel tegels in dezelfde patch) — anders is het budget op een groot scherm
  // opnieuw kleiner dan één patch en kapt de patch af: exact de LAR-479-val.
  // Op 4,5 blijft dit gewoon C.maxTiles (96); plafond 600 — met de midden-naar-
  // buiten-vulling kost aftoppen alleen de hoeken, geen band.
  function maxTilesEff() {
    const r = tilesAcrossEff() / C.tilesAcross;
    return Math.min(600, Math.ceil(C.maxTiles * r * r));
  }

  function shellZoomVoor(detailZ) {
    return Math.max(C.shellMinZ, Math.min(C.shellMaxZ, detailZ - C.shellZBelowDetail));
  }

  // ------------------------------------------------------------------- shell
  function updateShell(shellZ) {
    const key = `${bron}/${shellZ}`;
    if (key === shellKey) return;
    shellKey = key;

    const n = Math.pow(2, shellZ);
    const y0 = Math.max(0, Math.floor(mercYOfLat(85) * n));
    const y1 = Math.min(n - 1, Math.floor(mercYOfLat(-85) * n));

    const gewenst = new Set();
    for (let y = y0; y <= y1; y++) {
      for (let x = 0; x < n; x++) {
        gewenst.add(`${shellZ}/${x}/${y}`);
        zorgVoorTegel(shellGroup, shellLive, shellZ, x, y, C.shellLift, 1, C.shellMeshDetail);
      }
    }
    snoei(shellGroup, shellLive, gewenst);
  }

  // ------------------------------------------------------------------ detail
  function updateDetail(span, lat, lon, detailZ, shellZ) {
    if (detailZ <= shellZ) {
      if (detailLive.size) { leeg(detailGroup, detailLive); detailKey = ""; }
      return;
    }

    const n = Math.pow(2, detailZ);
    const xMid = Math.floor(((lon + 180) / 360) * n);
    const yMid = Math.floor(mercYOfLat(lat) * n);

    // Hoeveel tegels naast het midden hebben we nodig? De radius-kap moet
    // BOVEN wat het budget aankan liggen (budget 600 midden-naar-buiten is een
    // schijf met straal ~14): een kap van 12 hield op een groot scherm de
    // scherpe patch ver vóór de schermrand op — dát was "aan de buitenkant al
    // helemaal niet scherp". Het échte plafond is het budget, niet de radius.
    const spanX = Math.max(1, Math.ceil((span / 360) * n / Math.max(0.15, Math.cos(lat * D2R))));
    const spanY = Math.max(1, Math.ceil((span / 180) * n * 0.5));
    const rx = Math.min(spanX, 24);
    const ry = Math.min(spanY, 24);

    const key = `${bron}/${detailZ}/${xMid}/${yMid}/${rx}/${ry}`;
    if (key === detailKey) return;
    detailKey = key;

    // VALKUIL 2: van het midden naar buiten. Bij een vol budget verlies je dan
    // de rand van beeld, niet structureel de onderste rijen.
    const kandidaten = [];
    for (let dy = -ry; dy <= ry; dy++) {
      for (let dx = -rx; dx <= rx; dx++) {
        kandidaten.push([dx, dy, dx * dx + dy * dy]);
      }
    }
    kandidaten.sort((a, b) => a[2] - b[2]);

    const gewenst = new Set();
    let budget = maxTilesEff();
    for (const [dx, dy] of kandidaten) {
      if (budget <= 0) break;
      const y = yMid + dy;
      if (y < 0 || y >= n) continue;
      const x = ((xMid + dx) % n + n) % n;   // lengtegraad loopt rond
      gewenst.add(`${detailZ}/${x}/${y}`);
      zorgVoorTegel(detailGroup, detailLive, detailZ, x, y, C.detailLift, 2, C.meshDetail);
      budget--;
    }
    snoei(detailGroup, detailLive, gewenst);
  }

  // -------------------------------------------------------------------- tick
  let sinds = 0;
  let laatsteDetailZ = 0;

  // Laat binnengekomen tegels opkomen. Los van updateInterval: dit moet ELKE
  // frame, anders zie je de tegels in stapjes van 0,2 s aan/uit knipperen.
  function vaadTegelsIn(dt) {
    const stap = dt / 0.25;   // volledig zichtbaar in een kwart seconde
    for (const live of [shellLive, detailLive]) {
      live.forEach((mesh) => {
        if (!mesh.userData.vaadIn) return;
        const m = mesh.material;
        m.opacity = Math.min(1, m.opacity + stap);
        if (m.opacity >= 1) mesh.userData.vaadIn = false;
      });
    }
  }

  function tick(dt) {
    if (!aan) return;
    vaadTegelsIn(dt);
    sinds += dt;
    if (sinds < C.updateInterval) return;
    sinds = 0;

    const span = halveSpanDeg();
    const { lat, lon } = kijkMidden();
    const detailZ = detailZoomVoor(span, lat);
    const shellZ = shellZoomVoor(detailZ);
    laatsteDetailZ = detailZ;

    updateShell(shellZ);
    updateDetail(span, lat, lon, detailZ, shellZ);
  }

  function zetAan(waarde) {
    aan = !!waarde;
    group.visible = aan;
    // Bol laten zakken zodra er tegels overheen liggen, en weer terug in
    // "egaal" — daar IS de bol het oppervlak.
    GLOBE.setSphereSink(aan);
    if (!aan) { leeg(detailGroup, detailLive); detailKey = ""; }
  }

  function zetBron(naam) {
    if (!C.bronnen[naam] || naam === bron) return;
    bron = naam;
    leeg(shellGroup, shellLive); shellKey = "";
    leeg(detailGroup, detailLive); detailKey = "";
  }

  // De laag start aan, dus de bol moet meteen zakken (anders prikt hij door de
  // eerste tegelronde heen tot iemand voor het eerst een knop indrukt).
  GLOBE.setSphereSink(true);

  return {
    tick,
    zetAan,
    zetBron,
    isAan: () => aan,
    attributie: () => C.bronnen[bron].attributie,
    stats: () => ({
      detailZ: laatsteDetailZ,
      tegelsInBeeld: shellLive.size + detailLive.size,
      geladen,
      mislukt,
      cache: cache.size,
    }),
  };
}
