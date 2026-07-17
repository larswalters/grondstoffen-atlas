// globe-core.js — De scene zelf: camera, licht, sterren, slepen/zoomen,
// de renderloop en het aanwijzen (raycasting) van objecten.
// Weet NIETS van grondstoffen. Andere modules hangen zich hieraan op via
// GLOBE.globeGroup, GLOBE.registerPickable() en GLOBE.onTick().

const GLOBE = (function () {
  const C = CONFIG;
  const mount = document.getElementById("canvasWrap");
  const RADIUS = C.globe.radius;

  let width = mount.clientWidth;
  let height = mount.clientHeight;

  // --- scene ---------------------------------------------------------------
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(C.scene.background);
  scene.fog = new THREE.FogExp2(C.scene.background, 0.035);

  const camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 200);
  camera.position.set(0, 0, 5.6);

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputEncoding = THREE.sRGBEncoding;
  mount.appendChild(renderer.domElement);

  // --- sterren -------------------------------------------------------------
  const starGeo = new THREE.BufferGeometry();
  const starPos = new Float32Array(C.scene.stars * 3);
  for (let i = 0; i < C.scene.stars; i++) {
    const r = 40 + Math.random() * 60;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    starPos[i * 3] = r * Math.sin(phi) * Math.cos(theta);
    starPos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
    starPos[i * 3 + 2] = r * Math.cos(phi);
  }
  starGeo.setAttribute("position", new THREE.BufferAttribute(starPos, 3));
  scene.add(new THREE.Points(starGeo, new THREE.PointsMaterial({
    color: 0x9aa5bb, size: 0.06, sizeAttenuation: true, transparent: true, opacity: 0.85,
  })));

  // --- de bol zelf (leeg; basemap.js vult de materialen) -------------------
  const globeGroup = new THREE.Group();
  scene.add(globeGroup);

  const sphereGeo = new THREE.SphereGeometry(RADIUS, C.globe.segments, C.globe.segments);
  const sphereMat = new THREE.MeshPhongMaterial({ color: 0x14273a, shininess: 12 });
  const globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
  globeGroup.add(globeMesh);

  // --- atmosfeer -----------------------------------------------------------
  const atmo = new THREE.Mesh(
    new THREE.SphereGeometry(RADIUS * 1.05, 64, 64),
    new THREE.MeshBasicMaterial({
      color: C.scene.atmosphereColor,
      transparent: true,
      opacity: C.scene.atmosphereOpacity,
      side: THREE.BackSide,
    })
  );
  scene.add(atmo);

  // --- licht ---------------------------------------------------------------
  scene.add(new THREE.AmbientLight(0x8899aa, C.scene.ambientLight));
  const sun = new THREE.DirectionalLight(0xffffff, C.scene.sunLight);
  sun.position.set(5, 3, 4);
  scene.add(sun);

  // --- interactie ----------------------------------------------------------
  let isDragging = false;
  let autoRotate = C.globe.autoRotate;
  let autoRotateTimer = null;
  let prev = { x: 0, y: 0 };
  let downAt = { x: 0, y: 0 };

  const raycaster = new THREE.Raycaster();
  const ndc = new THREE.Vector2();
  const pickables = [];
  const tickers = [];
  const hoverHandlers = [];
  const clickHandlers = [];

  function pickAt(e) {
    const rect = renderer.domElement.getBoundingClientRect();
    ndc.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    ndc.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
    raycaster.setFromCamera(ndc, camera);
    // onzichtbare objecten (uitgefilterde tiers) niet aanklikbaar maken
    const hits = raycaster.intersectObjects(pickables.filter((m) => m.visible), false);
    return hits.length ? hits[0].object.userData : null;
  }

  function pauseAutoRotate() {
    autoRotate = false;
    clearTimeout(autoRotateTimer);
    // 0 = niet meer hervatten. Niets is zo irritant als een bol die onder je
    // handen vandaan draait terwijl je naar Lombok zit te kijken.
    const resume = C.globe.autoRotateResumeMs;
    if (resume > 0) {
      autoRotateTimer = setTimeout(() => { autoRotate = C.globe.autoRotate; }, resume);
    }
  }

  renderer.domElement.addEventListener("pointerdown", (e) => {
    isDragging = true;
    prev = { x: e.clientX, y: e.clientY };
    downAt = { x: e.clientX, y: e.clientY };
    pauseAutoRotate();
    renderer.domElement.style.cursor = "grabbing";
    try { renderer.domElement.setPointerCapture(e.pointerId); } catch (err) {}
  });

  // Radialen bolrotatie per gesleepte pixel, evenredig met de afstand van de
  // camera tot het booloppervlak: ingezoomd zie je minder wereld, dus moet een
  // veeg ook minder graden draaien. Zonder dit voelt de bol bij volle zoom alsof
  // hij onder je vinger wegschiet.
  function dragRadPerPixel() {
    const d = Math.max(0.05, camera.position.z - RADIUS);
    const dRef = Math.max(0.05, C.globe.dragRefZoom - RADIUS);
    return C.globe.dragSpeed * (d / dRef);
  }

  window.addEventListener("pointermove", (e) => {
    if (isDragging) {
      const k = dragRadPerPixel();
      const dx = e.clientX - prev.x;
      const dy = e.clientY - prev.y;
      globeGroup.rotation.y += dx * k;
      globeGroup.rotation.x = Math.max(-1.15, Math.min(1.15, globeGroup.rotation.x + dy * k));
      prev = { x: e.clientX, y: e.clientY };
      return;
    }
    const data = pickAt(e);
    renderer.domElement.style.cursor = data ? "pointer" : "grab";
    hoverHandlers.forEach((fn) => fn(data));
  });

  window.addEventListener("pointerup", (e) => {
    if (!isDragging) return;
    isDragging = false;
    renderer.domElement.style.cursor = "grab";
    const moved = Math.abs(e.clientX - downAt.x) + Math.abs(e.clientY - downAt.y);
    if (moved < 5) clickHandlers.forEach((fn) => fn(pickAt(e)));
    pauseAutoRotate();
  });

  function zoomTo(z) {
    camera.position.z = Math.max(C.globe.minZoom, Math.min(C.globe.maxZoom, z));
  }
  renderer.domElement.addEventListener("wheel", (e) => {
    e.preventDefault();
    pauseAutoRotate();
    zoomTo(camera.position.z + e.deltaY * 0.003);
  }, { passive: false });

  // pinch-to-zoom
  const pointers = new Map();
  let pinchDist = 0, pinchZoom = 0;
  const dist = () => {
    const p = [...pointers.values()];
    return Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y);
  };
  renderer.domElement.addEventListener("pointerdown", (e) => {
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size === 2) { pinchDist = dist(); pinchZoom = camera.position.z; isDragging = false; }
  });
  renderer.domElement.addEventListener("pointermove", (e) => {
    if (!pointers.has(e.pointerId)) return;
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size === 2 && pinchDist > 0) zoomTo(pinchZoom * (pinchDist / dist()));
  });
  const dropPointer = (e) => { pointers.delete(e.pointerId); if (pointers.size < 2) pinchDist = 0; };
  renderer.domElement.addEventListener("pointerup", dropPointer);
  renderer.domElement.addEventListener("pointercancel", dropPointer);

  window.addEventListener("resize", () => {
    width = mount.clientWidth;
    height = mount.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });

  // --- renderloop ----------------------------------------------------------
  let t = 0;
  function animate() {
    requestAnimationFrame(animate);
    t += 0.016;
    if (autoRotate && !isDragging) globeGroup.rotation.y += C.globe.autoRotateSpeed;
    tickers.forEach((fn) => fn(t, camera));
    renderer.render(scene, camera);
  }

  return {
    RADIUS, scene, camera, renderer, globeGroup, globeMesh, sphereMat, mount,
    start: animate,
    registerPickable: (mesh) => pickables.push(mesh),
    clearPickables: () => { pickables.length = 0; },
    onTick: (fn) => tickers.push(fn),
    onHover: (fn) => hoverHandlers.push(fn),
    onClick: (fn) => clickHandlers.push(fn),
    zoomBy: (f) => zoomTo(camera.position.z * f),
    // Draai de bol zo dat een coördinaat naar de camera kijkt (voor "vlieg naar")
    flyTo(lat, lon) {
      pauseAutoRotate();
      const targetY = Math.PI / 2 - (lon + 180) * (Math.PI / 180);
      const targetX = lat * (Math.PI / 180);
      const from = { x: globeGroup.rotation.x, y: globeGroup.rotation.y };
      const start = performance.now();
      const step = () => {
        const k = Math.min(1, (performance.now() - start) / 900);
        const e = 1 - Math.pow(1 - k, 3);
        globeGroup.rotation.x = from.x + (targetX - from.x) * e;
        globeGroup.rotation.y = from.y + (targetY - from.y) * e;
        if (k < 1) requestAnimationFrame(step);
      };
      step();
    },
  };
})();
