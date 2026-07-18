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

  minZoom: 2.75,
  maxZoom: 11,
  startZoom: 5.6,

  // Slepen schaalt mee met de zoom: ver weg draai je de halve wereld,
  // ingezoomd wil je fijn kunnen sturen. (Overgenomen uit v1 — LAR-479.)
  dragSpeed: 28.65,   // graden wereld per 100px bij dragRefZoom
  dragRefZoom: 5.6,

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
  const renderer = new THREE.WebGLRenderer({ antialias: true });
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
  camera.position.set(0, 0, CONFIG.startZoom);

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

  el.addEventListener("pointerdown", (e) => {
    dragging = true;
    lastX = e.clientX;
    lastY = e.clientY;
    el.setPointerCapture(e.pointerId);
  });

  el.addEventListener("pointermove", (e) => {
    if (!dragging) return;
    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;
    lastX = e.clientX;
    lastY = e.clientY;

    // Draaisnelheid evenredig met de zoom (v1-fix LAR-479).
    const perPixel = (CONFIG.dragSpeed / 100) * (camera.position.z / CONFIG.dragRefZoom);
    lon -= dx * perPixel;
    lat += dy * perPixel;
    lat = Math.max(-89, Math.min(89, lat));
  });

  const endDrag = (e) => {
    dragging = false;
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

  function zoomBy(factor) {
    camera.position.z = Math.max(
      CONFIG.minZoom, Math.min(CONFIG.maxZoom, camera.position.z * factor)
    );
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

  function frame() {
    requestAnimationFrame(frame);

    globeGroup.rotation.y = THREE.MathUtils.degToRad(lon);
    globeGroup.rotation.x = THREE.MathUtils.degToRad(lat);

    for (const fn of tickFns) fn();
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
    onTick, setToneMapping, setSun, setBasemap, zoomBy,
    getStats: () => ({
      fps,
      zoom: camera.position.z,
      calls: renderer.info.render.calls,
      tris: renderer.info.render.triangles,
    }),
  };
}
