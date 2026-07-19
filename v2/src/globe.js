// globe.js — de scene zelf voor v2: renderer, camera, licht, sterren,
// slepen/zoomen en de renderloop. Weet NIETS van grondstoffen of routes.
// Latere lagen (vectorwereld, zeeroutes, markers) hangen zich hieraan op via
// GLOBE.globeGroup en GLOBE.onTick().
//
// VERSCHIL MET v1 (src/globe-core.js): Three r185 i.p.v. r128, ES-modules
// i.p.v. globals, en een moderne beeldpijplijn (zie setToneMapping hieronder).

import * as THREE from "three";

export const CONFIG = {
  radius: 2.4,
  segments: 128,

  // ZOOM WERKT IN HOOGTE BOVEN HET OPPERVLAK, niet in afstand tot het
  // middelpunt. Dat is het verschil tussen "tot 930 km" en "tot straatniveau":
  // 1 eenheid = 2.655 km (want 2,4 eenheden = 6.371 km aardstraal).
  minAltitude: 0.00038,   // ~1 km hoogte
  maxAltitude: 8.6,       // ~22.800 km — de hele bol in beeld
  startAltitude: 3.2,     // ~8.500 km

  // Slepen heeft géén snelheids-instelling meer: het punt dat je vastpakt
  // blijft onder je cursor, en daarmee volgt de snelheid uit de meetkunde.
  // Zie het blok "slepen" hieronder voor waarom de oude graden-per-pixel weg is.

  stars: 1800,
};

// Belichting van de scene. Eén plek, want zon en belichting zijn samen ingemeten.
const SUN_INTENSITY = 6.0;
const EXPOSURE = 1.6;

export function createGlobe(mount) {
  // Fallback op 1: een verborgen mount geeft 0 en dat maakt camera.aspect NaN
  // (0/0), waarna de bol ook na het bijschalen niet meer terugkomt.
  let width = mount.clientWidth || 1;
  let height = mount.clientHeight || 1;

  // --- renderer ------------------------------------------------------------
  // logarithmicDepthBuffer is VERPLICHT zodra je van 22.000 km tot 1 km hoogte
  // wilt kunnen zoomen. Met een gewone dieptebuffer moet het nabij-vlak heel
  // dicht bij de camera liggen om niet weg te knippen, en dan verliest de
  // buffer zoveel precisie dat tegels en kustlijnen door elkaar heen flikkeren.
  const renderer = new THREE.WebGLRenderer({
    antialias: true,
    logarithmicDepthBuffer: true,
  });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // In r185 is outputColorSpace standaard al sRGB — dat hoeven we niet meer
  // te zetten (in r128 heette dat outputEncoding en moest het handmatig).
  // Wat we WEL zetten is de tone mapping: van HDR-licht naar beeldscherm.
  // Belichting ingemeten op 2026-07-18 (zon 6.0 + belichting 1.6): dat geeft
  // een gemiddelde beeldhelderheid van ~46 met NUL uitgebrande pixels. Zet je
  // ACES aan zonder de belichting mee te verhogen, dan wordt het beeld juist
  // dónkerder dan v1 — ACES drukt middentonen. Deze twee horen bij elkaar.
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = EXPOSURE;

  mount.appendChild(renderer.domElement);

  // --- scene & camera ------------------------------------------------------
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x05070c);

  const camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 400);
  camera.position.set(0, 0, CONFIG.radius + CONFIG.startAltitude);

  // Hoogte boven het oppervlak — de maat waarin alles rekent.
  let altitude = CONFIG.startAltitude;

  // Het nabij-vlak schuift mee met de hoogte. Vast op 0,1 (= 265 km) zou vanaf
  // die hoogte alles wegknippen; vast op 1e-6 kost precisie als je ver weg bent.
  function updateNear() {
    camera.near = Math.max(1e-6, altitude * 0.05);
    camera.far = 400;
    camera.updateProjectionMatrix();
  }
  updateNear();

  // --- sterren -------------------------------------------------------------
  const starGeo = new THREE.BufferGeometry();
  const starPos = new Float32Array(CONFIG.stars * 3);
  for (let i = 0; i < CONFIG.stars; i++) {
    const r = 60 + Math.random() * 120;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    starPos[i * 3 + 0] = r * Math.sin(phi) * Math.cos(theta);
    starPos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
    starPos[i * 3 + 2] = r * Math.cos(phi);
  }
  starGeo.setAttribute("position", new THREE.BufferAttribute(starPos, 3));
  scene.add(new THREE.Points(starGeo, new THREE.PointsMaterial({
    color: 0x9aa5bb, size: 0.09, sizeAttenuation: true,
    transparent: true, opacity: 0.8, depthWrite: false,
  })));

  // --- licht ---------------------------------------------------------------
  // Sinds r155 rekent Three met fysiek geloofwaardige lichtsterktes. Eén
  // richtingslicht = de zon, plus een beetje omgevingslicht zodat de nachtzijde
  // niet pikzwart is (later vervangen door echte stadslichten).
  const sun = new THREE.DirectionalLight(0xfff4e6, SUN_INTENSITY);
  sun.position.set(5, 2, 4);
  scene.add(sun);

  const ambient = new THREE.AmbientLight(0x2a3a52, 0.6);
  scene.add(ambient);

  // --- de bol --------------------------------------------------------------
  const globeGroup = new THREE.Group();
  scene.add(globeGroup);

  const loader = new THREE.TextureLoader();

  // Kleurtexturen moeten als sRGB gemarkeerd worden, datatexturen (maskers,
  // hoogte) NIET — die zijn getallen, geen kleur. Dit verkeerd zetten is de
  // klassieke reden dat een bol er "afgewassen" uitziet.
  const dayMap = loader.load("../textures/earth-blue-marble.jpg");
  dayMap.colorSpace = THREE.SRGBColorSpace;
  dayMap.anisotropy = renderer.capabilities.getMaxAnisotropy();

  const waterMask = loader.load("../textures/earth-water.png"); // data, geen kleur
  const bumpMap = loader.load("../textures/earth-topology.png"); // data, geen kleur

  const sphereGeo = new THREE.SphereGeometry(
    CONFIG.radius, CONFIG.segments, CONFIG.segments
  );

  const globeMat = new THREE.MeshStandardMaterial({
    map: dayMap,
    bumpMap: bumpMap,
    bumpScale: 0.6,
    // Watermasker als ruwheidskaart: water glad (spiegelt de zon), land ruw.
    roughnessMap: waterMask,
    roughness: 1.0,
    metalness: 0.0,
  });

  const globeMesh = new THREE.Mesh(sphereGeo, globeMat);
  globeGroup.add(globeMesh);

  // --- atmosfeer (voorlopig nog de v1-truc: omgekeerde bol met vlakke kleur).
  // Dit wordt in de schoonheidsslag vervangen door echte Rayleigh/Mie-verstrooiing.
  const atmo = new THREE.Mesh(
    new THREE.SphereGeometry(CONFIG.radius * 1.055, 64, 64),
    new THREE.MeshBasicMaterial({
      color: 0x4a90e2, transparent: true, opacity: 0.14,
      side: THREE.BackSide, depthWrite: false,
    })
  );
  globeGroup.add(atmo);

  // --- slepen & zoomen -----------------------------------------------------
  let dragging = false;
  let lastX = 0, lastY = 0;
  let lat = 0, lon = 0; // in graden — waar we naar kijken

  const el = renderer.domElement;

  // Slepen = GRIJPEN EN MEENEMEN: het punt waar je de bol vastpakt blijft onder
  // de cursor. Dat is de enige variant die natuurlijk aanvoelt, en ze is meteen
  // zelfcorrigerend — de draaisnelheid volgt uit de meetkunde in plaats van uit
  // een ingestelde graden-per-pixel.
  //
  // Wat hier eerst stond (graden/pixel evenredig met de hoogte) klopte qua VORM
  // maar was gemeten **3,52x te snel op elke zoom**: 28,65 graden per 100 px
  // waar de meetkunde er 8,15 vraagt. Bovendien zat de vensterhoogte er niet in,
  // dus op een ander scherm liep hij verder uit de pas — en zelfs met de juiste
  // gain glijdt het gegrepen punt weg zodra je niet in het midden grijpt, want
  // aan de rand van de bol dekt een pixel veel meer graden dan in het midden.
  //
  // De wiskunde: gezocht zijn lat/lon zodat  Rx(lat)*Ry(lon)*p = t , met p het
  // gegrepen punt in bol-eigen coordinaten en t de richting onder de cursor nu.
  // Ry laat y ongemoeid, dus  p.y = cos(lat)*t.y + sin(lat)*t.z = R*cos(lat-F)
  // met R = hypot(t.y,t.z) en F = atan2(t.z,t.y) -> lat = F +- acos(p.y/R).
  // Daarna is lon gewoon het hoekverschil in het xz-vlak.
  const _straal = new THREE.Raycaster();
  const _bol = new THREE.Sphere(new THREE.Vector3(0, 0, 0), CONFIG.radius);
  const _ndc = new THREE.Vector2();
  const _tref = new THREE.Vector3();
  let grijpLokaal = null;   // null = naast de bol gepakt -> terugval op stappen

  /** Eenheidsrichting op de bol onder de cursor. */
  function bolRichting(clientX, clientY) {
    const r = el.getBoundingClientRect();
    // Een verborgen of nog niet gemeten mount geeft 0x0; delen daardoor maakt
    // de NDC NaN en dan verdwijnt de bol. Val dan terug op de stap-modus.
    if (!(r.width > 0) || !(r.height > 0)) return null;
    _ndc.x = ((clientX - r.left) / r.width) * 2 - 1;
    _ndc.y = -(((clientY - r.top) / r.height) * 2 - 1);
    _straal.setFromCamera(_ndc, camera);
    if (_straal.ray.intersectSphere(_bol, _tref)) return _tref.clone().normalize();
    // Naast de bol: pak het punt op de rand dat het dichtst bij de straal ligt.
    // Zo loopt slepen aan de rand netjes uit i.p.v. abrupt te blokkeren.
    _straal.ray.closestPointToPoint(_bol.center, _tref);
    return _tref.lengthSq() > 1e-12 ? _tref.clone().normalize() : null;
  }

  /** Wereldrichting -> bol-eigen coordinaten, bij de gegeven lat/lon (graden). */
  function naarLokaal(v, latDeg, lonDeg) {
    const a = THREE.MathUtils.degToRad(latDeg), b = THREE.MathUtils.degToRad(lonDeg);
    const ca = Math.cos(a), sa = Math.sin(a);
    const y1 = ca * v.y + sa * v.z;          // Rx(-lat)
    const z1 = -sa * v.y + ca * v.z;
    const cb = Math.cos(b), sb = Math.sin(b);
    return new THREE.Vector3(cb * v.x - sb * z1, y1, sb * v.x + cb * z1);  // Ry(-lon)
  }

  el.addEventListener("pointerdown", (e) => {
    dragging = true;
    lastX = e.clientX;
    lastY = e.clientY;
    const t = bolRichting(e.clientX, e.clientY);
    grijpLokaal = t ? naarLokaal(t, lat, lon) : null;
    el.setPointerCapture(e.pointerId);
  });

  el.addEventListener("pointermove", (e) => {
    if (!dragging) return;

    if (grijpLokaal) {
      const t = bolRichting(e.clientX, e.clientY);
      if (t) {
        const p = grijpLokaal;
        const rho = Math.hypot(t.y, t.z);
        if (rho > 1e-9) {
          const phi = Math.atan2(t.z, t.y);
          // Buiten bereik (de gegrepen breedtegraad kan de cursor niet halen)
          // klemmen we het argument: dan loopt het zo dicht mogelijk mee i.p.v.
          // te springen.
          const d = Math.acos(Math.max(-1, Math.min(1, p.y / rho)));
          const huidig = THREE.MathUtils.degToRad(lat);
          // twee oplossingen; neem de tak die het dichtst bij de huidige stand ligt
          const kandidaten = [phi + d, phi - d];
          let a = kandidaten[0];
          if (Math.abs(kandidaten[1] - huidig) < Math.abs(kandidaten[0] - huidig)) a = kandidaten[1];
          const ca = Math.cos(a), sa = Math.sin(a);
          const ux = t.x, uz = -sa * t.y + ca * t.z;   // u = Rx(-a)*t
          const b = Math.atan2(ux, uz) - Math.atan2(p.x, p.z);
          const nieuweLat = THREE.MathUtils.radToDeg(a);
          if (Number.isFinite(nieuweLat) && Math.abs(nieuweLat) <= 89.5) {
            lat = nieuweLat;
            lon = THREE.MathUtils.radToDeg(b);
          }
        }
      }
      lastX = e.clientX;
      lastY = e.clientY;
      return;
    }

    // Terugval: naast de bol gepakt, dus er is niets om onder de cursor te
    // houden. Draai dan met de hoek die op het MIDDEN van het scherm 1:1 zou
    // zijn — uit fov en vensterhoogte, dus schermonafhankelijk.
    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;
    lastX = e.clientX;
    lastY = e.clientY;
    const hoogtePx = el.clientHeight || 1;
    const perPixel = THREE.MathUtils.radToDeg(
      (2 * altitude * Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2)) /
      (CONFIG.radius * hoogtePx));
    lon -= dx * perPixel;
    lat += dy * perPixel;
    lat = Math.max(-89, Math.min(89, lat));
  });

  const endDrag = (e) => {
    dragging = false;
    grijpLokaal = null;
    if (e.pointerId !== undefined && el.hasPointerCapture?.(e.pointerId)) {
      el.releasePointerCapture(e.pointerId);
    }
  };
  el.addEventListener("pointerup", endDrag);
  el.addEventListener("pointercancel", endDrag);

  el.addEventListener("wheel", (e) => {
    e.preventDefault();
    zoomBy(e.deltaY > 0 ? 1.08 : 1 / 1.08);
  }, { passive: false });

  // Zoomen is VERMENIGVULDIGEN MET DE HOOGTE. Daardoor kost elke stap
  // hetzelfde gevoel, of je nu van 20.000 naar 18.000 km gaat of van 2 naar
  // 1,8 km. Zou je (zoals eerst) de afstand tot het middelpunt schalen, dan
  // staat de laatste 900 km in een handvol stappen en kom je nooit lager.
  function zoomBy(factor) {
    altitude = Math.max(CONFIG.minAltitude, Math.min(CONFIG.maxAltitude, altitude * factor));
    camera.position.z = CONFIG.radius + altitude;
    updateNear();
  }

  // --- knijpzoom op mobiel -------------------------------------------------
  let pinchDist = 0;
  el.addEventListener("touchmove", (e) => {
    if (e.touches.length !== 2) return;
    const dx = e.touches[0].clientX - e.touches[1].clientX;
    const dy = e.touches[0].clientY - e.touches[1].clientY;
    const d = Math.hypot(dx, dy);
    if (pinchDist) zoomBy(pinchDist / d);
    pinchDist = d;
  }, { passive: true });
  el.addEventListener("touchend", () => { pinchDist = 0; });

  // --- beeldverwerking omschakelen (de A/B die Lars kan checken) -----------
  // BELANGRIJK: de A/B wisselt ALLEEN de tone mapping, bij gelijk licht en
  // gelijke belichting. Zou ik ook de belichting meeschakelen, dan vergelijk je
  // helderheid i.p.v. beeldverwerking en zegt de test niets.
  // Gemeten verschil bij zon 6.0 / belichting 1.6: legacy 0,03% uitgebrande
  // pixels (puur wit, detail onherstelbaar weg) tegen 0% bij ACES, terwijl ACES
  // méér doortekening in de hooglichten houdt (0,23% vs 0,07%).
  function setToneMapping(mode) {
    renderer.toneMapping = (mode === "legacy")
      ? THREE.NoToneMapping
      : THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = EXPOSURE;
  }

  // Ondergrond wisselen. De satelliettextuur blijft beschikbaar (Lars: "die
  // satelliet is prima, maar nu gaat het om het vectormodel"), maar is niet
  // meer de waarheid — de vectorwereld is dat. Zonder textuur zie je een
  // egale oceaan waar de vectorkustlijn scherp op afsteekt, op elke zoom.
  function setBasemap(mode) {
    if (mode === "satelliet") {
      globeMat.map = dayMap;
      globeMat.color.set(0xffffff);
    } else {
      globeMat.map = null;
      globeMat.color.set(0x0e3a63); // diepe oceaan
    }
    globeMat.needsUpdate = true;
  }

  // De bol laten ZAKKEN als er tegels overheen liggen.
  //
  // Het probleem dat dit oplost: een tegel is een plat lapje. Zijn koorde duikt
  // tussen de hoekpunten ONDER het boloppervlak, en dan prikt de bol-textuur
  // door de tegels heen — horizontale banden langs de breedtegraden en een
  // ringpatroon op de pool (waar de Mercator-tegels het grootst zijn).
  // Gemeten voor de fix: 8,5% van de schermpixels veranderde als je de bol
  // verborg; 7,8% sterk.
  //
  // v1 loste dit op door de TEGELS op te tillen (`shellLift: 1.0016` = 3,8 km).
  // Dat kan hier niet: v2 zoomt tot ~1 km hoogte, dus dan zou de camera ONDER
  // de tegellaag uitkomen. Andersom werkt wel — de bol is toch alleen nog een
  // achtergrond terwijl de tegels laden.
  const SPHERE_SINK = 0.998;   // ~12,7 km onder het oppervlak; koordezakking is ~2 km
  function setSphereSink(aan) {
    globeMesh.scale.setScalar(aan ? SPHERE_SINK : 1);
  }

  function setSun(mode) {
    if (mode === "flat") {
      // Vlak licht: geen schaduwzijde. Handig om de kaart zelf te beoordelen
      // zonder dat de nachtzijde de helft van de wereld opslokt — straks bij
      // het inmeten van de vectorwereld wil je dat.
      sun.intensity = 1.2;
      ambient.intensity = 4.0;
    } else {
      sun.intensity = SUN_INTENSITY;
      ambient.intensity = 0.6;
    }
  }

  // --- renderloop ----------------------------------------------------------
  const tickFns = [];
  function onTick(fn) { tickFns.push(fn); }

  let frames = 0, fpsLast = performance.now(), fps = 0;
  let vorigeTijd = performance.now();

  function frame() {
    requestAnimationFrame(frame);

    const nu = performance.now();
    const dt = Math.min(0.25, (nu - vorigeTijd) / 1000);
    vorigeTijd = nu;

    globeGroup.rotation.y = THREE.MathUtils.degToRad(lon);
    globeGroup.rotation.x = THREE.MathUtils.degToRad(lat);

    for (const fn of tickFns) fn(dt);
    renderer.render(scene, camera);

    frames++;
    const now = performance.now();
    if (now - fpsLast >= 500) {
      fps = Math.round((frames * 1000) / (now - fpsLast));
      frames = 0;
      fpsLast = now;
    }
  }
  frame();

  // --- meeschalen ----------------------------------------------------------
  // Let op: een ResizeObserver i.p.v. alleen window.resize. Reden: als de pagina
  // opstart terwijl hij nog verborgen is (achtergrondtab, preview-pane die nog
  // niet zichtbaar is, telefoon die de tab pas later toont) is clientWidth 0 en
  // krijg je een canvas van 0×0 dat nooit meer bijtrekt — er komt dan immers
  // geen window-resize. De observer vangt óók die eerste maatwijziging.
  function applySize() {
    const w = mount.clientWidth;
    const h = mount.clientHeight;
    if (w === 0 || h === 0) return; // nog niet zichtbaar; observer meldt zich later
    if (w === width && h === height) return;
    width = w;
    height = h;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  }

  new ResizeObserver(applySize).observe(mount);
  window.addEventListener("resize", applySize);

  return {
    scene, camera, renderer, globeGroup,
    radius: CONFIG.radius,
    onTick, setToneMapping, setSun, setBasemap, setSphereSink, zoomBy,
    getAltitude: () => altitude,
    // hoogte in km, voor de statusregel: 2,4 eenheden = 6.371 km
    getAltitudeKm: () => (altitude / CONFIG.radius) * 6371,
    getStats: () => ({
      fps,
      zoom: camera.position.z,
      altitude,
      calls: renderer.info.render.calls,
      tris: renderer.info.render.triangles,
    }),
  };
}
