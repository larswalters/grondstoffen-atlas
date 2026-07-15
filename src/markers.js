// markers.js — Tekent de locaties (nodes) van de actieve grondstoffen.
//   mine      -> bol, grootte = share (alleen ACTIEVE productie), pulserende ring
//   refinery  -> ruit (octaëder)
//   port      -> kubusje
//   market    -> platte ring/schijf
// Projecten (status: "project"/"gepland") worden halftransparant getekend.
//
// TIERS: node.tier bepaalt vanaf welk zoomniveau een locatie (en zijn label)
// zichtbaar is. Tier 1 altijd, tier 2/3 pas bij inzoomen — zie CONFIG.markers.
// ZOOM: markers schalen mee met de camera zodat ze op het scherm ongeveer
// even groot blijven in plaats van uit te groeien tot klodders.
// FOCUS: setFocus(Set(nodeIds)|null) dimt alle niet-betrokken markers.

const MarkerLayer = (function () {
  const C = CONFIG.markers;
  const R = GLOBE.RADIUS;

  const group = new THREE.Group();
  GLOBE.globeGroup.add(group);

  const labelGroup = new THREE.Group();
  GLOBE.globeGroup.add(labelGroup);

  const items = [];       // {mesh, ring?, label, node, res, tier, baseOpacity, labelBase}
  let focusSet = null;    // Set(nodeIds) | null

  function defaultTier(node) {
    if (node.tier) return node.tier;
    if (node.type === "port" || node.type === "airport" || node.type === "recycler") return 2;
    if (node.type === "exchange" || node.type === "reserve" || node.type === "military") return 2;
    if (node.type === "hub" || node.type === "cb") return 1;
    if (node.type === "mine") return (node.share || 0) >= 10 ? 1 : 2;
    return 1;
  }

  // Een naambordje: GÉÉN kader (dat dekte de kaart af), maar lichte letters met
  // een donkere rand — leesbaar op zee én op woestijn. Links onderaan zit een
  // kort stokje dat naar de exacte plek wijst, zodat de naam ernáást kan staan
  // in plaats van bovenop de marker.
  //
  // Het anker (sprite.center) ligt linksonder, precies waar het stokje begint.
  // Daardoor "hangt" het label rechtsboven zijn locatie.
  function makeLabel(text, pos, color) {
    const L = C.label;
    const fs = L.fontSize;

    const meas = document.createElement("canvas").getContext("2d");
    meas.font = `600 ${fs}px system-ui, sans-serif`;
    const tw = meas.measureText(text).width;

    const cv = document.createElement("canvas");
    cv.width = Math.ceil(L.leader + tw + 14);
    cv.height = Math.ceil(fs * 2.1);

    const c = cv.getContext("2d");
    c.font = `600 ${fs}px system-ui, sans-serif`;
    c.textBaseline = "middle";

    // het stokje: van linksonder (de locatie) schuin omhoog naar de tekst
    c.strokeStyle = "rgba(255,255,255,0.5)";
    c.lineWidth = 2;
    c.beginPath();
    c.moveTo(2, cv.height - 2);
    c.lineTo(L.leader - 4, cv.height * 0.42);
    c.stroke();

    const tx = L.leader + 2;
    const ty = cv.height * 0.40;

    // donkere rand rondom de letters: dat vervangt het kader
    c.lineJoin = "round";
    c.strokeStyle = "rgba(3,7,14,0.9)";
    c.lineWidth = 6;
    c.strokeText(text, tx, ty);
    c.fillStyle = "#" + color.getHexString();
    c.fillText(text, tx, ty);

    const tex = new THREE.CanvasTexture(cv);
    tex.minFilter = THREE.LinearFilter;
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({
      map: tex, transparent: true, depthTest: false,
    }));
    sprite.center.set(0, 0);          // anker linksonder = op de locatie
    const scale = C.labelSize;
    const labelBase = new THREE.Vector2(cv.width * scale, cv.height * scale);
    sprite.scale.set(labelBase.x, labelBase.y, 1);
    sprite.position.copy(pos.clone().multiplyScalar(1.004));
    sprite.visible = false;
    sprite.renderOrder = 10;
    return { sprite, labelBase };
  }

  function build(resources, filters, usedIds) {
    clearGroup(group);
    clearGroup(labelGroup);
    items.length = 0;

    const showProjects = !filters || filters.showProjects !== false;

    resources.forEach((res) => {
      const color = new THREE.Color(res.color);
      const flowColor = flowColorOf(res);
      const maxShare = Math.max(1, ...res.nodes.filter((n) => n.share).map((n) => n.share));
      // centrale banken schalen op voorraad (goud); sqrt zodat de VS niet álles verplettert
      const maxReserve = Math.max(1,
        ...res.nodes.filter((n) => n.type === "cb" && n.reserve).map((n) => n.reserve));
      // beursmagazijnen (koper) schalen op voorraad, √ zodat het grootste niet álles verplettert
      const maxStock = Math.max(1,
        ...res.nodes.filter((n) => n.type === "exchange" && n.stock).map((n) => n.stock));
      // strategische reserves (olie/SPR) schalen op voorraad, √ zoals de beursmagazijnen
      const maxReserveStock = Math.max(1,
        ...res.nodes.filter((n) => n.type === "reserve" && n.stock).map((n) => n.stock));
      // militaire kringloop (uranium) schaalt op secundaire voorraad, √ zoals de reserves
      const maxMilitaryStock = Math.max(1,
        ...res.nodes.filter((n) => n.type === "military" && n.stock).map((n) => n.stock));

      res.nodes.forEach((node) => {
        const planned = node.status === "project" || node.status === "gepland";
        if (planned && !showProjects) return;
        // centrale-bank-nodes alleen tonen als de CB-laag aanstaat
        if (node.type === "cb" && !(filters && filters.showCentralBanks)) return;
        // beursmagazijn-nodes alleen tonen als de beursvoorraden-laag aanstaat
        if (node.type === "exchange" && !(filters && filters.showExchangeStocks)) return;
        // strategische-reserve-nodes (olie/SPR) alleen tonen als de voorraden-laag aanstaat
        if (node.type === "reserve" && !(filters && filters.showReserves)) return;
        // militaire-kringloop-nodes (uranium) alleen tonen als de militaire-laag aanstaat
        if (node.type === "military" && !(filters && filters.showMilitary)) return;
        // recycling-nodes met een recycle-laag (REE) alleen tonen met de toggle aan.
        // (Koper-recyclers hebben géén `layer` en blijven dus altijd zichtbaar.)
        if (node.layer === "recycle" && !(filters && filters.showRecycle)) return;

        const pos = latLonToVec3(node.lat, node.lon, R + C.lift);
        let mesh, ring = null;
        const baseOpacity = planned ? 0.45 : 1;

        if (node.type === "mine") {
          // Grootte alléén op basis van échte productie (share).
          // Projecten (potential, geen share) krijgen de minimummaat.
          const size = node.share
            ? C.mine.minSize + (C.mine.maxSize - C.mine.minSize) * normalize(node.share, maxShare)
            : C.mine.minSize;
          mesh = new THREE.Mesh(
            new THREE.SphereGeometry(size, 18, 18),
            new THREE.MeshBasicMaterial({ color, transparent: true, opacity: baseOpacity })
          );
          ring = new THREE.Mesh(
            new THREE.RingGeometry(size * 1.7, size * 2.2, 28),
            new THREE.MeshBasicMaterial({
              color: flowColor, transparent: true,
              opacity: planned ? 0.15 : 0.4, side: THREE.DoubleSide,
            })
          );
          ring.position.copy(pos);
          ring.lookAt(pos.clone().multiplyScalar(2));
          group.add(ring);
        } else if (node.type === "refinery") {
          mesh = new THREE.Mesh(
            new THREE.OctahedronGeometry(C.refinery.size, 0),
            new THREE.MeshBasicMaterial({ color: 0xf3ede0, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "port") {
          mesh = new THREE.Mesh(
            new THREE.BoxGeometry(C.port.size, C.port.size, C.port.size),
            new THREE.MeshBasicMaterial({ color: 0x9fd8ff, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "airport") {
          // klein pyramidetje — subtiel, want gateways zijn passagepunten
          mesh = new THREE.Mesh(
            new THREE.TetrahedronGeometry(C.airport.size * 1.25, 0),
            new THREE.MeshBasicMaterial({ color: 0xbcd3e8, transparent: true, opacity: baseOpacity * 0.9 })
          );
        } else if (node.type === "hub") {
          // handels-/kluishub: opvallende gouden ring (Londen/NY/Zürich/Shanghai…)
          mesh = new THREE.Mesh(
            new THREE.TorusGeometry(C.hub.size, C.hub.size * 0.34, 10, 28),
            new THREE.MeshBasicMaterial({ color: 0xffd257, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "cb") {
          // centrale bank: goudstaaf-blokje, grootte ∝ √voorraad
          const s = node.reserve
            ? C.cb.minSize + (C.cb.maxSize - C.cb.minSize) *
                normalize(Math.sqrt(node.reserve), Math.sqrt(maxReserve))
            : C.cb.minSize;
          mesh = new THREE.Mesh(
            new THREE.BoxGeometry(s * 1.6, s * 0.7, s),
            new THREE.MeshBasicMaterial({ color: 0xe9c85a, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "exchange") {
          // beursmagazijn: koperkleurige spoel/schijf, grootte ∝ √voorraad
          const s = node.stock
            ? C.exchange.minSize + (C.exchange.maxSize - C.exchange.minSize) *
                normalize(Math.sqrt(node.stock), Math.sqrt(maxStock))
            : C.exchange.minSize;
          mesh = new THREE.Mesh(
            new THREE.CylinderGeometry(s, s, s * 0.55, 18),
            new THREE.MeshBasicMaterial({ color: 0xd98e5a, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "reserve") {
          // strategische reserve (SPR): olie-amber opslagtank (platte cilinder), grootte ∝ √voorraad
          const s = node.stock
            ? C.reserve.minSize + (C.reserve.maxSize - C.reserve.minSize) *
                normalize(Math.sqrt(node.stock), Math.sqrt(maxReserveStock))
            : C.reserve.minSize;
          mesh = new THREE.Mesh(
            new THREE.CylinderGeometry(s, s, s * 0.42, 22),
            new THREE.MeshBasicMaterial({ color: 0xE8A838, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "military") {
          // militaire kringloop (uranium): rode octaëder (waarschuwingskleur), grootte ∝ √voorraad
          const s = node.stock
            ? C.military.minSize + (C.military.maxSize - C.military.minSize) *
                normalize(Math.sqrt(node.stock), Math.sqrt(maxMilitaryStock))
            : C.military.minSize;
          mesh = new THREE.Mesh(
            new THREE.OctahedronGeometry(s, 0),
            new THREE.MeshBasicMaterial({ color: 0xE0554F, transparent: true, opacity: baseOpacity })
          );
        } else if (node.type === "recycler") {
          // recycling: gedempte groene ring (schroot terug de keten in)
          mesh = new THREE.Mesh(
            new THREE.TorusGeometry(C.recycler.size, C.recycler.size * 0.3, 8, 18),
            new THREE.MeshBasicMaterial({ color: 0x7fc9a6, transparent: true, opacity: baseOpacity })
          );
        } else {
          // market
          mesh = new THREE.Mesh(
            new THREE.TorusGeometry(C.market.size, C.market.size * 0.32, 8, 20),
            new THREE.MeshBasicMaterial({ color: flowColor, transparent: true, opacity: baseOpacity })
          );
        }

        // eerst plaatsen, dán richten (lookAt rekent vanaf de huidige positie)
        mesh.position.copy(pos);
        mesh.lookAt(pos.clone().multiplyScalar(2));
        mesh.userData = { kind: "node", resource: res, node };
        group.add(mesh);
        GLOBE.registerPickable(mesh);

        const { sprite, labelBase } = makeLabel(
          node.name, pos, node.type === "mine" ? color : new THREE.Color(0xf0ece2)
        );
        labelGroup.add(sprite);

        items.push({
          mesh, ring, label: sprite, labelBase, node, res,
          tier: defaultTier(node), baseOpacity,
          // Een locatie die aan een zichtbare stroom hangt, mag NOOIT door de
          // tier-regel verdwijnen — anders lopen er lijnen naar een leeg punt.
          forced: !!(usedIds && usedIds.has(node.id)),
          ringBaseOpacity: ring ? ring.material.opacity : 0,
          pulse: node.type === "mine" && C.mine.pulse && !planned,
          // wie wint er bij botsende labels? lage waarde = belangrijker
          prio: (node.tier || 3) * 100 - (node.share || 0),
        });
      });
    });
    applyFocus();
  }

  function applyFocus() {
    const F = CONFIG.focus;
    items.forEach((it) => {
      const active = !focusSet || focusSet.has(it.node.id);
      it.mesh.material.opacity = active ? it.baseOpacity : F.markerDim;
      if (it.ring) it.ring.material.opacity = active ? it.ringBaseOpacity : F.markerDim * 0.6;
      it.dimmed = !active;
    });
  }

  function setFocus(nodeIds) {
    focusSet = nodeIds || null;
    applyFocus();
  }

  // Hoe groot moet iets zijn, gegeven de camerastand?
  // Doorslaggevend is de afstand tot het OPPERVLAK, niet de camerastand zelf.
  // Die zakt van 3.2 naar 0.6 als je van z=5.6 naar z=3.0 gaat — een factor 5,
  // terwijl de camerastand maar halveert. Op de camerastand delen (wat het
  // eerst deed) liet markers klodders blijven en labels uitgroeien tot
  // reuzenletters dwars over het continent.
  //   exp 1.0 = precies even groot op het scherm
  //   exp < 1 = groeit een beetje mee bij inzoomen (prettiger voor de vormen)
  function scaleFor(z, s) {
    const d = Math.max(0.25, z - R);
    const dref = Math.max(0.25, s.ref - R);
    return Math.min(s.max, Math.max(s.min, Math.pow(d / dref, s.exp)));
  }

  // pulse + zoom-schaling + tier-zichtbaarheid + labels
  //
  // LABELS ZONDER BOTSINGEN: we projecteren elk kandidaat-label naar het scherm,
  // rekenen uit hoeveel pixels het beslaat, en plaatsen ze op volgorde van
  // belang. Overlapt een label met een al geplaatst label? Dan valt het af.
  // Greenbushes wint dus van Bunbury, en "Salar de Atacama" staat niet meer
  // dwars door "Salar del Hombre Muerto" heen.
  const boxes = [];
  const wp = new THREE.Vector3();
  const ndc = new THREE.Vector3();

  GLOBE.onTick((t, camera) => {
    const z = camera.position.z;
    const zoomK = scaleFor(z, C.zoomScale);
    const labelK = scaleFor(z, C.labelScale);
    const eye = camera.position.clone().normalize();

    const canvas = GLOBE.renderer.domElement;
    const vw = canvas.clientWidth;
    const vh = canvas.clientHeight;
    // hoeveel pixels is één wereld-eenheid, op afstand d van de camera?
    const focal = vh / (2 * Math.tan((camera.fov * Math.PI / 180) / 2));

    // eerst zichtbaarheid en schaal, en verzamel de labelkandidaten
    const candidates = [];

    items.forEach((it, i) => {
      const visible = it.forced || it.tier <= 1 || z < (C.tierZoom[it.tier] || Infinity);
      it.mesh.visible = visible;
      if (it.ring) it.ring.visible = visible;

      if (visible) {
        it.mesh.scale.setScalar(zoomK);
        if (it.ring) {
          const pulse = it.pulse ? 1 + 0.18 * Math.sin(t * 2 + i * 0.7) : 1;
          it.ring.scale.setScalar(zoomK * pulse);
        }
      }

      it.label.visible = false;

      const labelZ = C.labelZoomByTier[it.tier] || C.labelZoomByTier[1];
      if (!visible || z >= labelZ) return;
      if (it.dimmed && CONFIG.focus.labelHideDimmed) return;

      it.label.getWorldPosition(wp);
      if (wp.clone().normalize().dot(eye) <= 0.2) return;   // achterkant van de bol

      it.label.scale.set(it.labelBase.x * labelK, it.labelBase.y * labelK, 1);
      candidates.push(it);
    });

    if (!C.label.collide) {
      candidates.forEach((it) => { it.label.visible = true; });
      return;
    }

    // belangrijkste eerst
    candidates.sort((a, b) => a.prio - b.prio);

    boxes.length = 0;
    const pad = C.label.padPx;

    candidates.forEach((it) => {
      it.label.getWorldPosition(wp);
      const d = camera.position.distanceTo(wp);
      const pxPerUnit = focal / Math.max(0.001, d);

      ndc.copy(wp).project(camera);
      const sx = (ndc.x * 0.5 + 0.5) * vw;
      const sy = (-ndc.y * 0.5 + 0.5) * vh;

      // anker linksonder -> het label loopt naar rechts en naar boven
      const w = it.labelBase.x * labelK * pxPerUnit;
      const h = it.labelBase.y * labelK * pxPerUnit;
      const box = { x0: sx - pad, y0: sy - h - pad, x1: sx + w + pad, y1: sy + pad };

      const clash = boxes.some((b) =>
        box.x0 < b.x1 && box.x1 > b.x0 && box.y0 < b.y1 && box.y1 > b.y0);
      if (clash) return;

      boxes.push(box);
      it.label.visible = true;
    });
  });

  return { build, group, setFocus };
})();
