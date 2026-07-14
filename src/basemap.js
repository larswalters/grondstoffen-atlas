// basemap.js — Het oppervlak van de aarde. Volledig los van de data.
//
// Drie lagen boven op elkaar:
//   1. TEXTUUR   — echte satellietkaart (4096×2048), incl. reliëf (bump map)
//                  en een watermasker zodat alleen de zee glimt.
//   2. VECTOR    — kust- en grenslijnen als échte 3D-lijnen. Die blijven
//                  haarscherp, hoe ver je ook inzoomt (een textuur wordt wazig).
//   3. GRATICULE — optioneel lat/lon-raster.
//
// Valt automatisch terug op de oude, zelfgetekende vectorkaart als de
// textuur niet geladen kan worden (bv. offline of file:// zonder server).

const Basemap = (function () {
  const C = CONFIG.basemap;
  const R = GLOBE.RADIUS;
  const mat = GLOBE.sphereMat;

  const overlay = new THREE.Group();
  GLOBE.globeGroup.add(overlay);

  const loader = new THREE.TextureLoader();
  loader.setCrossOrigin("anonymous");
  const cache = {};

  function url(file) {
    return (C.source === "cdn" ? C.cdnPath : C.localPath) + file;
  }

  function load(file, onOk, onFail) {
    if (cache[file]) { onOk(cache[file]); return; }
    loader.load(
      url(file),
      (tex) => {
        tex.encoding = THREE.sRGBEncoding;
        tex.anisotropy = GLOBE.renderer.capabilities.getMaxAnisotropy();
        cache[file] = tex;
        onOk(tex);
      },
      undefined,
      () => { if (onFail) onFail(); }
    );
  }

  // ---------------------------------------------------------------- FALLBACK
  // De oude aanpak: kaart tekenen op een canvas vanuit geo-data.js.
  // Werkt altijd, ook zonder internet en zonder webserver.
  function vectorTexture() {
    const W = 4096, H = 2048;
    const cv = document.createElement("canvas");
    cv.width = W; cv.height = H;
    const ctx = cv.getContext("2d");
    const X = (lon) => ((lon + 180) / 360) * W;
    const Y = (lat) => ((90 - lat) / 180) * H;

    const og = ctx.createLinearGradient(0, 0, 0, H);
    og.addColorStop(0.0, "#0a2036");
    og.addColorStop(0.5, "#0e3350");
    og.addColorStop(1.0, "#0a2036");
    ctx.fillStyle = og;
    ctx.fillRect(0, 0, W, H);

    ctx.fillStyle = "#2c5738";
    ctx.strokeStyle = "#6ba078";
    ctx.lineWidth = 1;
    ctx.lineJoin = "round";
    LAND_POLYS.forEach((poly) => {
      ctx.beginPath();
      poly.forEach((ring) => {
        ring.forEach((p, i) => (i ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1]))));
        ctx.closePath();
      });
      ctx.fill("evenodd");
      ctx.stroke();
    });

    ctx.fillStyle = "#12405f";
    LAKE_POLYS.forEach((ring) => {
      ctx.beginPath();
      ring.forEach((p, i) => (i ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1]))));
      ctx.closePath();
      ctx.fill();
    });

    const tex = new THREE.CanvasTexture(cv);
    tex.encoding = THREE.sRGBEncoding;
    tex.anisotropy = GLOBE.renderer.capabilities.getMaxAnisotropy();
    return tex;
  }

  // -------------------------------------------------------- VECTOR-OVERLAY
  // Lijnen uit geo-data.js als 3D-geometrie net boven het oppervlak.
  // Alle lijnstukken in ÉÉN geometrie (LineSegments): 1 draw call in plaats
  // van ~1400. Scheelt enorm veel; met losse THREE.Line-objecten zakt de fps in.
  function polylines(list, color, opacity, liftFactor, closed) {
    const verts = [];
    list.forEach((line) => {
      const n = line.length;
      for (let i = 0; i < n - 1; i++) {
        const a = latLonToVec3(line[i][1], line[i][0], R * liftFactor);
        const b = latLonToVec3(line[i + 1][1], line[i + 1][0], R * liftFactor);
        verts.push(a.x, a.y, a.z, b.x, b.y, b.z);
      }
      if (closed && n > 2) {
        const a = latLonToVec3(line[n - 1][1], line[n - 1][0], R * liftFactor);
        const b = latLonToVec3(line[0][1], line[0][0], R * liftFactor);
        verts.push(a.x, a.y, a.z, b.x, b.y, b.z);
      }
    });
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.Float32BufferAttribute(verts, 3));
    return new THREE.LineSegments(
      geo,
      new THREE.LineBasicMaterial({ color, transparent: true, opacity })
    );
  }

  function buildOverlay() {
    clearGroup(overlay);
    overlay.children.length = 0;

    if (C.showCoastlines) {
      // buitenste ring van elk landpolygoon = kustlijn
      const rings = [];
      LAND_POLYS.forEach((poly) => poly.forEach((ring) => { if (ring.length > 3) rings.push(ring); }));
      overlay.add(polylines(rings, C.coastColor, C.coastOpacity, 1.001, true));
    }
    if (C.showBorders) {
      overlay.add(polylines(BORDER_LINES, C.borderColor, C.borderOpacity, 1.002, false));
    }
    if (C.showGraticule) {
      const g = new THREE.Group();
      const m = new THREE.LineBasicMaterial({ color: 0xbcd4e6, transparent: true, opacity: 0.12 });
      for (let lat = -60; lat <= 60; lat += 30) {
        const pts = [];
        for (let lon = -180; lon <= 180; lon += 4) pts.push(latLonToVec3(lat, lon, R * 1.003));
        g.add(new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints(pts), m));
      }
      for (let lon = -180; lon < 180; lon += 30) {
        const pts = [];
        for (let lat = -90; lat <= 90; lat += 4) pts.push(latLonToVec3(lat, lon, R * 1.003));
        g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), m));
      }
      overlay.add(g);
    }
  }

  // --------------------------------------------------------------- STIJLEN
  let current = null;

  function setStyle(name) {
    current = name;

    if (name === "vector") {
      mat.map = vectorTexture();
      mat.bumpMap = null;
      mat.specularMap = null;
      mat.emissiveMap = null;
      mat.emissive.set(0x000000);
      mat.color.set(0xffffff);
      mat.shininess = 6;
      mat.needsUpdate = true;
      buildOverlay();
      return;
    }

    const file = C.files[name] || C.files.satelliet;

    load(file, (tex) => {
      mat.map = tex;
      mat.color.set(0xffffff);

      if (name === "nacht") {
        // stadslichten: laten oplichten in plaats van belicht worden
        mat.emissiveMap = tex;
        mat.emissive.set(0xffffff);
        mat.emissiveIntensity = 1.0;
        mat.shininess = 2;
      } else {
        mat.emissiveMap = null;
        mat.emissive.set(0x000000);
        mat.shininess = 18;
      }

      // reliëf + glimmend water
      load(C.files.relief, (bump) => {
        mat.bumpMap = bump;
        mat.bumpScale = CONFIG.basemap.reliefStrength;
        mat.needsUpdate = true;
      });
      load(C.files.water, (spec) => {
        mat.specularMap = spec;
        mat.specular = new THREE.Color(0x33556b);
        mat.needsUpdate = true;
      });

      mat.needsUpdate = true;
      buildOverlay();
    }, () => {
      console.warn(
        "Textuur kon niet geladen worden (" + url(file) + "). " +
        "Terugval op de vectorkaart. Zie README: draai een lokale server of zet CONFIG.basemap.source op 'cdn'."
      );
      setStyle("vector");
    });
  }

  return { setStyle, current: () => current, rebuildOverlay: buildOverlay,
    // De vectorkust/-grenzen zijn een grove benadering. Zodra de scherpe
    // tegellaag verschijnt kloppen ze niet meer op de kilometer, dus dan
    // verbergen we ze (tiles.js regelt dat).
    setOverlayVisible: (v) => { overlay.visible = !!v; } };
})();
