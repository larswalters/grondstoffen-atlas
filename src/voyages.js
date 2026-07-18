// voyages.js — TIJD: schepen als lichtjes met een spoor, over een periode
// van enkele maanden.
//
// Het punt van deze laag is dat de animatie GEEN sfeerplaatje is: hoe vaak er
// een schip vertrekt en hoe lang het onderweg is, volgt rechtstreeks uit de
// data.
//
//   afvaarten per jaar = volume (kt LCE) / ktPerShipment
//   reisduur (dagen)   = routelengte (km) / shipSpeedKmPerDay
//
// Greenbushes → Jiangxi (110 kt LCE) wordt daarmee ongeveer 27 afvaarten per
// jaar — grofweg elke twee weken een schip — en elke reis duurt ruim twee
// weken. Er is dus bijna altijd precies één schip onderweg. Dat is geen
// toevallige animatiesnelheid; dat is hoe die keten werkt.
//
// De vertrekmomenten liggen VAST (afgeleid van de route-id), zodat je bij het
// terugspoelen van de tijdlijn exact hetzelfde beeld terugkrijgt.

const Voyages = (function () {
  const T = CONFIG.time;
  const R = GLOBE.RADIUS;
  const EARTH_KM = 6371;

  const group = new THREE.Group();
  GLOBE.globeGroup.add(group);

  let ships = [];        // {routeIdx, light, trail, positions, colors}
  let plans = [];        // per route: reisduur, interval, aantal schepen
  let active = false;    // tijdmodus aan/uit
  let playing = false;
  let day = 0;           // simulatietijd in dagen sinds 1 januari
  let speed = 1;
  let lastT = null;
  let onTickCb = null;

  const totalDays = () => T.monthsSpan * 30.44;

  // Vaste "willekeurige" fase per route, zodat niet alle schepen tegelijk
  // vertrekken én de tijdlijn reproduceerbaar blijft bij terugspoelen.
  function phaseOf(key) {
    let h = 0;
    for (let i = 0; i < key.length; i++) h = (h * 31 + key.charCodeAt(i)) % 9973;
    return (h % 1000) / 1000;
  }

  // ------------------------------------------------------------------ OPBOUW
  // Wordt aangeroepen na elke FlowLayer.build (ook bij zoom-band-wissel,
  // want dan zijn de curves opnieuw gemaakt).
  function rebind() {
    clearGroup(group);
    ships = [];
    plans = [];
    if (!active) return;

    const routes = FlowLayer.getRoutes();

    routes.forEach((route, idx) => {
      const lengthKm = route.totalAngle * EARTH_KM;
      const durationDays = Math.max(1, lengthKm / T.shipSpeedKmPerDay);
      const perYear = Math.max(1, Math.round(route.value / T.ktPerShipment));
      const intervalDays = 365 / perYear;

      // hoeveel schepen kunnen er tegelijk onderweg zijn?
      const concurrent = Math.min(
        T.maxShipsPerRoute,
        Math.max(1, Math.ceil(durationDays / intervalDays) + 1)
      );

      plans.push({ route, durationDays, intervalDays, perYear, phase: phaseOf(route.key) });

      for (let s = 0; s < concurrent; s++) {
        // lichtje
        const light = new THREE.Mesh(
          new THREE.SphereGeometry(T.shipSize, 8, 8),
          new THREE.MeshBasicMaterial({
            color: 0xffffff, transparent: true, opacity: 0.95,
            blending: THREE.AdditiveBlending, depthWrite: false,
          })
        );
        light.visible = false;
        group.add(light);

        // spoor: een lijn die achter het schip aan sleept en uitdooft.
        // Additief blenden + kleur naar zwart = een lichtspoor dat vervaagt.
        const n = T.trailPoints;
        const geo = new THREE.BufferGeometry();
        geo.setAttribute("position", new THREE.BufferAttribute(new Float32Array(n * 3), 3));
        geo.setAttribute("color", new THREE.BufferAttribute(new Float32Array(n * 3), 3));
        const trail = new THREE.Line(geo, new THREE.LineBasicMaterial({
          vertexColors: true, transparent: true, opacity: 0.9,
          blending: THREE.AdditiveBlending, depthWrite: false,
        }));
        trail.visible = false;
        group.add(trail);

        ships.push({ planIdx: plans.length - 1, slot: s, light, trail });
      }
    });
  }

  // -------------------------------------------------------------------- TICK
  const tmp = new THREE.Vector3();

  GLOBE.onTick((t) => {
    if (lastT === null) lastT = t;
    const dt = Math.min(0.1, t - lastT); // sprongen (tabblad inactief) afvlakken
    lastT = t;
    if (!active) return;

    if (playing) {
      day += (dt / T.secondsPerMonth) * 30.44 * speed;
      if (day > totalDays()) day -= totalDays();
      if (onTickCb) onTickCb(day);
    }

    ships.forEach((ship) => {
      const plan = plans[ship.planIdx];
      const { route, durationDays, intervalDays, phase } = plan;

      // Welk vertrek hoort bij dit "slot"? We rekenen terug vanaf de huidige
      // dag: het n-de meest recente vertrek op deze route.
      const lastDep = Math.floor((day - phase * intervalDays) / intervalDays);
      const dep = (lastDep - ship.slot) * intervalDays + phase * intervalDays;
      const elapsed = day - dep;

      const dimmed = !FlowLayer.isFlowActive(route.key);
      const sailing = elapsed >= 0 && elapsed <= durationDays && !route.planned;

      if (!sailing) {
        ship.light.visible = false;
        ship.trail.visible = false;
        return;
      }

      const u = Math.min(1, elapsed / durationDays);

      // schip — getPointAt (BOOGLENGTE), niet getPoint (curve-parameter).
      // getPoint verdeelt u over de controlepunten, niet over de afgelegde
      // afstand: waar punten dicht opeen staan kroop het schip, waar ze ver uit
      // elkaar lagen schoot het weg. Gemeten op Antofagasta->Ningbo was de
      // snelste stap 7,3x de traagste — precies het "soms heel snel en dan
      // ineens afremmen" dat Lars zag. getPointAt gebruikt de booglengte-tabel
      // en loopt dus constant, ONGEACHT hoe dicht de punten liggen. Daarmee is
      // de vaarsnelheid losgekoppeld van de geometrie-resolutie.
      route.curve.getPointAt(u, tmp);
      ship.light.position.copy(tmp);
      ship.light.visible = true;
      ship.light.material.opacity = dimmed ? 0.10 : 0.95;

      // spoor: punten achter het schip, uitdovend
      const pos = ship.trail.geometry.attributes.position;
      const col = ship.trail.geometry.attributes.color;
      const n = T.trailPoints;
      for (let i = 0; i < n; i++) {
        const back = (i / (n - 1)) * T.trailSpan;
        const uu = Math.max(0, u - back);
        route.curve.getPointAt(uu, tmp);
        pos.setXYZ(i, tmp.x, tmp.y, tmp.z);

        // helder vlak achter het schip, zwart (= onzichtbaar) aan het eind
        const fade = (1 - i / (n - 1)) * (dimmed ? 0.10 : 1);
        col.setXYZ(i, route.color.r * fade, route.color.g * fade, route.color.b * fade);
      }
      pos.needsUpdate = true;
      col.needsUpdate = true;
      ship.trail.visible = true;
    });
  });

  // --------------------------------------------------------------------- API
  function setActive(v) {
    const was = active;
    active = !!v;
    // Alleen bij het áánzetten automatisch gaan spelen. Zonder deze check zou
    // elke rebuild (bv. zoomen) een pauze weer ongedaan maken.
    if (active && !was) playing = true;
    FlowLayer.setShipsActive(active);
    group.visible = active;
    if (active) {
      rebind();
    } else {
      clearGroup(group);
      ships = [];
      plans = [];
      playing = false;
    }
  }

  return {
    setActive,
    rebind,
    isActive: () => active,
    isPlaying: () => playing,
    play: () => { playing = true; },
    pause: () => { playing = false; },
    toggle: () => { playing = !playing; return playing; },
    getDay: () => day,
    setDay: (d) => { day = d; },
    setSpeed: (s) => { speed = s; },
    getSpeed: () => speed,
    totalDays,
    onTick: (fn) => { onTickCb = fn; },

    // "dag 47" -> "17 februari"
    dateLabel(d) {
      const MONTHS = ["januari", "februari", "maart", "april", "mei", "juni",
        "juli", "augustus", "september", "oktober", "november", "december"];
      const date = new Date(2025, 0, 1);
      date.setDate(date.getDate() + Math.floor(d));
      return date.getDate() + " " + MONTHS[date.getMonth()];
    },

    // aantal schepen dat op dit moment vaart — leuk cijfer voor de balk
    shipsAtSea() {
      return ships.filter((s) => s.light.visible).length;
    },
  };
})();
