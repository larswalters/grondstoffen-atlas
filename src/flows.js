// flows.js — Tekent de handelsstromen tussen nodes.
//
// Dikte   = relatief volume (t.o.v. de grootste stroom van die grondstof)
// Kleur   = KETENSTAP (flow.stage): erts is dof/donker, raffinaat de
//           grondstofkleur, eindproduct licht (zie stageColorOf in util.js)
// Hoogte  = ook ketenstap: erts kruipt over het oppervlak, product het hoogst
// Streep  = transportmodus: schip doorgetrokken, pijp/spoor/weg gestreept
// via     = optionele waypoints: havens (nodes) en zeestraten (wp-* uit
//           data/_chokepoints.js). De boog volgt dan een echte route en
//           bundelt zich vanzelf in knelpunten.
//
// ZOOM: dikte en hoogte hebben drie banden (ver / midden / dichtbij). Bij
// het passeren van een grens vraagt deze laag ATLAS om een rebuild, zodat
// je ingezoomd routes ziet in plaats van dikke slierten.
//
// FOCUS: setFocus({nodeIds, flowKeys}) dimt alles wat niet betrokken is.
// Aanklikbaar: userData.kind === "flow" | "waypoint".

const FlowLayer = (function () {
  const C = CONFIG.flows;
  const R = GLOBE.RADIUS;

  const group = new THREE.Group();
  GLOBE.globeGroup.add(group);

  const particles = [];
  const records = [];        // per flow: meshes, materialen, betrokken node-ids
  const wpMarkers = [];      // getekende knelpunt-markers
  const routes = [];         // curves per flow, voor de tijd-/schepenlaag
  let shipsActive = false;   // staat de tijdmodus aan? -> schip-deeltjes uit

  let lastResources = null;  // voor rebuild bij band-wissel
  let lastFilters = null;
  let currentBand = null;
  let focusSel = null;       // {nodeIds:Set, flowKeys:Set} | null
  let needRebuild = null;    // callback, gezet door main.js

  const TUBE_SEGMENTS = 96;

  function bandFor(z) {
    const t = C.zoomBands.thresholds;
    if (z > t[0]) return "far";
    if (z > t[1]) return "mid";
    return "near";
  }

  function tubeFor(curve, width, dashed, material, totalAngle) {
    if (!dashed) {
      const geo = new THREE.TubeGeometry(curve, TUBE_SEGMENTS, width, 6, false);
      return [new THREE.Mesh(geo, material)];
    }
    // gestreept: knip de curve in stukjes en sla er om en om één over.
    // Aantal streepjes schaalt met de routelengte, anders worden korte
    // routes één klodder en lange routes onleesbaar grof.
    const meshes = [];
    const DASHES = Math.max(10, Math.min(60, Math.round(10 + totalAngle * 16)));
    for (let i = 0; i < DASHES; i++) {
      if (i % 2) continue;
      const t0 = i / DASHES, t1 = (i + 0.75) / DASHES;
      const pts = [];
      for (let k = 0; k <= 6; k++) pts.push(curve.getPoint(t0 + (t1 - t0) * (k / 6)));
      const sub = new THREE.CatmullRomCurve3(pts);
      meshes.push(new THREE.Mesh(new THREE.TubeGeometry(sub, 6, width, 5, false), material));
    }
    return meshes;
  }

  // Zoek een routepunt: eerst in de nodes van de grondstof, dan in de
  // universele knelpuntenlijst (data/_chokepoints.js).
  function getRoutePoint(res, id) {
    return getNode(res, id) ||
      (typeof WAYPOINTS !== "undefined" ? WAYPOINTS[id] : null);
  }

  // Ligt dit punt aan zee? Havens en knelpunten sowieso — maar ook fabrieken
  // die pál aan de kade staan (`coastal: true` in de data), zoals Gwangyang en
  // Kwinana. Zonder die vlag kregen die geen zeeroute en trok de atlas een
  // rechte lijn: dwars over Japan, dwars over Australië.
  function isSeaPoint(p) {
    if (p.kind === "grensovergang") return false; // grenspost = landpunt
    return p.type === "port" || p.coastal === true ||
      (p.id && String(p.id).startsWith("wp-"));
  }

  function flowKey(flow) { return flow.from + ">" + flow.to; }

  function build(resources, filters) {
    lastResources = resources;
    lastFilters = filters;
    currentBand = bandFor(GLOBE.camera.position.z);
    const band = C.zoomBands[currentBand];

    // WEERGAVE: "route" = varen over het oppervlak langs via-punten,
    //           "hemelsbreed" = rechtstreekse hoge boog, via-punten genegeerd.
    const routeView = (filters && filters.viewMode ? filters.viewMode : C.viewMode) === "route";
    const vs = routeView ? C.routeStyle : C.arcStyle;

    // routering klaarzetten (eenmalig: bouwt het land/zee-raster)
    const useRouting = CONFIG.searoute.enabled && typeof Routing !== "undefined";
    const useLand = useRouting && CONFIG.searoute.landEnabled;
    if (useRouting && routeView) Routing.init();

    clearGroup(group);
    particles.length = 0;
    records.length = 0;
    wpMarkers.length = 0;
    routes.length = 0;

    const stages = filters && filters.stages;
    const showProjects = !filters || filters.showProjects !== false;
    const usedWaypoints = new Map(); // wp-id -> waypoint

    resources.forEach((res) => {
      const flows = res.flows || [];
      if (!flows.length) return;
      const maxValue = Math.max(1, ...flows.map((f) => f.value || 1));

      flows.forEach((flow, flowIdx) => {
        const stage = flow.stage || "raffinaat";
        if (stages && !stages.has(stage)) return;

        // Centrale-bank-laag (goud): alleen tonen als de toggle aanstaat.
        if (flow.layer === "cb" && !(filters && filters.showCentralBanks)) return;
        // Beursvoorraden-laag (koper): alleen tonen als de toggle aanstaat.
        if (flow.layer === "exchange" && !(filters && filters.showExchangeStocks)) return;

        const from = getNode(res, flow.from);
        const to = getNode(res, flow.to);
        if (!from || !to) return;

        const planned = flow.status === "gepland" ||
          from.status === "project" || from.status === "gepland" ||
          to.status === "project" || to.status === "gepland";
        if (planned && !showProjects) return;

        // route: from -> via[] -> to   (hemelsbreed: rechtstreeks from -> to)
        const viaIds = routeView ? (flow.via || []) : [];
        const stops = [from];
        viaIds.forEach((id) => {
          const p = getRoutePoint(res, id);
          if (!p) { console.warn(`[${res.id}] onbekend via-punt: ${id}`); return; }
          stops.push(p);
          if (typeof WAYPOINTS !== "undefined" && WAYPOINTS[id]) usedWaypoints.set(id, WAYPOINTS[id]);
        });
        stops.push(to);

        // ROUTERING PER STUK. Een stroom bestaat uit meerdere legs (mijn → haven
        // → zeestraat → haven → fabriek), en elk stuk kiest zelf zijn kaart:
        //
        //   zee → zee, per schip     -> ZEEroute (buigt om Java, door Lombok)
        //   land → zee of zee → land -> LANDroute (de aanvoer naar de kade, de
        //                               laatste mijl van haven naar fabriek)
        //   trein / weg / pijp       -> LANDroute
        //   schip tussen twee punten die géén van beide een haven zijn
        //                            -> rechte lijn. Dat is een grondstof die
        //                               nog geen havens in zijn data heeft (olie,
        //                               nikkel). Die door de landrouter sturen is
        //                               zinloos: er lóópt geen weg van Nigeria
        //                               naar Amerika.
        const shipMode = (flow.mode || "ship") === "ship";
        // LUCHTVRACHT (goud): geen A* over land/zee — goud vliegt de great-circle.
        // De via-luchthavens buigen alleen de grondbaan; makeRouteCurve tilt de
        // boog op (hoogte ∝ afstand). De korte EU-hops blijven `road`/`rail` (land-A*).
        const airMode = flow.mode === "air";
        const routePts = [stops[0]];
        const anchors = [];

        for (let i = 0; i < stops.length - 1; i++) {
          const a = stops[i];
          const b = stops[i + 1];
          const seaA = isSeaPoint(a);
          const seaB = isSeaPoint(b);
          let leg = null;

          if (routeView && useRouting && !airMode) {
            if (shipMode && seaA && seaB) {
              leg = Routing.sea(a, b);
            } else if (useLand && (!shipMode || seaA !== seaB)) {
              leg = Routing.land(a, b);
            }
            // anders: rechte lijn (zeetransport zonder havens in de data)
          }

          if (leg && leg.length > 2) {
            for (let k = 1; k < leg.length - 1; k++) routePts.push(leg[k]);
          }
          routePts.push(b);
          // dit knooppunt is een anker: híer knijpen de vaarbanen samen
          if (i < stops.length - 2) anchors.push(routePts.length - 1);
        }

        const k = normalize(flow.value || 1, maxValue);
        const width = (C.minWidth + (C.maxWidth - C.minWidth) * Math.sqrt(k))
          * band.width * vs.widthScale;
        const style = C.modeStyle[flow.mode || "ship"] || C.modeStyle.ship;

        // hoogte: route = dunne laag per ketenstap, boog = sinusprofiel.
        // Lucht is ALTIJD een boog (ook in route-view): hoogte ∝ afstand, want
        // goud vliegt écht die boog — voor lithium was diezelfde boog juist fout.
        const as = C.arcStyle;
        const lift = airMode
          ? as.lift * (as.stageLift[stage] || 1) * band.lift
          : routeView
            ? (vs.lift + (vs.stageOffset[stage] || 0)) * band.lift
            : vs.lift * (vs.stageLift[stage] || 1) * band.lift;

        // VAARBAAN: elke stroom een eigen baan, maar samenknijpend bij elk anker
        const L = C.lanes;
        const laneIdx = (flowIdx % L.count) - (L.count - 1) / 2;
        const lane = laneIdx * L.spacing;

        const { curve, totalAngle } = makeRouteCurve(routePts, R, lift, {
          flat: routeView && !airMode, lane, anchors,
        });

        const color = stageColorOf(res, stage);
        const baseOpacity = (C.opacity + 0.35 * k) * (planned ? 0.45 : 1);
        const material = new THREE.MeshBasicMaterial({
          color, transparent: true, opacity: baseOpacity,
        });

        const meshes = tubeFor(curve, width, style.dash, material, totalAngle);
        meshes.forEach((mesh) => {
          mesh.userData = { kind: "flow", resource: res, flow, from, to };
          group.add(mesh);
          GLOBE.registerPickable(mesh);
        });

        // deeltjes: méér volume = méér deeltjes
        const flowParticles = [];
        const count = Math.max(1, Math.round(C.particlesPerFlow * (0.4 + k)));
        const mode = flow.mode || "ship";
        for (let p = 0; p < count; p++) {
          const dot = new THREE.Mesh(
            new THREE.SphereGeometry(width * 1.9 + 0.006, 8, 8),
            new THREE.MeshBasicMaterial({ color, transparent: true })
          );
          group.add(dot);
          const rec = { curve, dot, offset: p / count, mode, dimmed: false };
          particles.push(rec);
          flowParticles.push(rec);
        }

        const key = flowKey(flow);
        const nodeIds = new Set([from.id, to.id, ...viaIds]);
        records.push({
          key, nodeIds, material, meshes,
          particles: flowParticles, baseOpacity,
        });

        // voor de tijdlijn-laag: echte zeeroutes (schip) én luchtroutes (goud),
        // en alleen in de route-weergave (in hemelsbreed reist er niemand).
        if (routeView && (mode === "ship" || mode === "air")) {
          routes.push({
            key, curve, totalAngle, color, res, flow, mode,
            value: flow.value || 1, planned,
          });
        }
      });
    });

    // knelpunt-markers voor alle gebruikte waypoints: gouden ringetjes.
    // Vaarpunten (marker: false) krijgen er géén — dat zijn geen knelpunten,
    // die houden de route alleen op het water.
    usedWaypoints.forEach((wp) => {
      if (wp.marker === false) return;
      const pos = latLonToVec3(wp.lat, wp.lon, R + CONFIG.markers.lift);
      const size = CONFIG.markers.waypoint.size;
      const ring = new THREE.Mesh(
        new THREE.TorusGeometry(size, size * 0.28, 8, 24),
        new THREE.MeshBasicMaterial({ color: 0xc9a227, transparent: true, opacity: 0.95 })
      );
      ring.position.copy(pos);
      ring.lookAt(pos.clone().multiplyScalar(2));
      ring.userData = { kind: "waypoint", wp };
      group.add(ring);
      GLOBE.registerPickable(ring);
      wpMarkers.push({ mesh: ring, wp });
    });

    applyFocus();
  }

  // ------------------------------------------------------------------ FOCUS
  function recordActive(rec, sel) {
    if (!sel) return true;
    if (sel.flowKeys && sel.flowKeys.has(rec.key)) return true;
    if (sel.nodeIds) {
      for (const id of sel.nodeIds) if (rec.nodeIds.has(id)) return true;
    }
    return false;
  }

  function applyFocus() {
    const F = CONFIG.focus;
    records.forEach((rec) => {
      const active = recordActive(rec, focusSel);
      rec.material.opacity = active ? rec.baseOpacity : F.flowDim;
      rec.particles.forEach((p) => { p.dimmed = !active; });
    });
    wpMarkers.forEach((m) => {
      const active = !focusSel ||
        (focusSel.nodeIds && focusSel.nodeIds.has(m.wp.id)) ||
        records.some((rec) => rec.nodeIds.has(m.wp.id) && recordActive(rec, focusSel));
      m.mesh.material.opacity = active ? 0.95 : F.markerDim;
    });
  }

  // Zet de focus en geef de verzameling BETROKKEN node-ids terug, zodat
  // main.js de MarkerLayer dezelfde selectie kan laten dimmen.
  function setFocus(sel) {
    focusSel = sel;
    applyFocus();
    if (!sel) return null;
    const involved = new Set(sel.nodeIds || []);
    records.forEach((rec) => {
      if (recordActive(rec, sel)) rec.nodeIds.forEach((id) => involved.add(id));
    });
    return involved;
  }

  // ------------------------------------------------------------------- TICK
  GLOBE.onTick((t, camera) => {
    // deeltjes animeren. Staan de schepen aan, dan verdwijnen de abstracte
    // deeltjes op de zeeroutes — daar varen nu echte schepen.
    particles.forEach((p) => {
      if (shipsActive && (p.mode === "ship" || p.mode === "air")) { p.dot.visible = false; return; }
      p.dot.visible = true;
      const u = (t * C.particleSpeed + p.offset) % 1;
      p.dot.position.copy(p.curve.getPoint(u));
      const fade = Math.sin(u * Math.PI);
      p.dot.material.opacity = p.dimmed
        ? CONFIG.focus.particleDim
        : 0.25 + 0.75 * fade;
      const s = 0.6 + 0.7 * fade;
      p.dot.scale.set(s, s, s);
    });

    // knelpunt-ringen meeschalen met de camera (zelfde formule als de markers:
    // afstand tot het oppervlak, niet de camerastand)
    const zs = CONFIG.markers.zoomScale;
    const d = Math.max(0.25, camera.position.z - R);
    const dref = Math.max(0.25, zs.ref - R);
    const zoomK = Math.min(zs.max, Math.max(zs.min, Math.pow(d / dref, zs.exp)));
    wpMarkers.forEach((m) => m.mesh.scale.setScalar(zoomK));

    // band gewisseld? -> geometrie opnieuw opbouwen (via main, zodat de
    // pickables van markers en flows samen kloppen)
    if (lastResources && bandFor(camera.position.z) !== currentBand && needRebuild) {
      needRebuild();
    }
  });

  // Is deze stroom op dit moment "actief" (niet weggedimd door de focus)?
  // De schepen-laag gebruikt dit om mee te dimmen.
  function isFlowActive(key) {
    if (!focusSel) return true;
    const rec = records.find((r) => r.key === key);
    return rec ? recordActive(rec, focusSel) : true;
  }

  return {
    build, group, setFocus, isFlowActive,
    getRoutes: () => routes,
    setShipsActive: (v) => { shipsActive = !!v; },
    onNeedRebuild: (fn) => { needRebuild = fn; },
  };
})();
