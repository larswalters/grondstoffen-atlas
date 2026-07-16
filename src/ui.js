// ui.js — Alles wat HTML is: grondstofknoppen, filterchips, kaartstijl-
// schakelaar, knelpuntenlijst en het infopaneel.
// Roept via callbacks ATLAS aan als er iets verandert.

const UI = (function () {
  const pillList = document.getElementById("pillList");
  const viewRow = document.getElementById("viewRow");
  const filterRow = document.getElementById("filterRow");
  const blurbEl = document.getElementById("blurb");
  const infoPanel = document.getElementById("infoPanel");
  const styleList = document.getElementById("styleList");
  const tensionBox = document.getElementById("tensionBox");
  const tensionList = document.getElementById("tensionList");

  let selected = null;
  let hovered = null;

  // Tijdlijn-woordkeus: schepen (zee) of vluchten (goud). main.js zet dit per
  // actieve grondstof, zodat de teller "3 vluchten onderweg" toont i.p.v. schepen.
  let voyageNoun = { one: "schip", many: "schepen", btn: "⚓ schepen" };

  // ------------------------------------------------------------- GRONDSTOFFEN
  function renderPills(activeIds, onToggle) {
    pillList.innerHTML = "";
    RESOURCES.forEach((r) => {
      const active = activeIds.includes(r.id);
      const c = r.flowColor || r.color;
      const btn = document.createElement("button");
      btn.className = "pill" + (active ? " active" : "");
      btn.style.borderColor = active ? c : "#25344a";
      btn.style.background = active ? c + "22" : "transparent";
      btn.innerHTML =
        '<span class="dot" style="background:' + c + '"></span>' + r.name +
        (r.detail === "uitgewerkt" ? '<span class="badge">detail</span>' : "");
      btn.onclick = () => onToggle(r.id);
      pillList.appendChild(btn);
    });

    if (activeIds.length === 1) {
      const res = getResource(activeIds[0]);
      blurbEl.textContent = res.blurb;
      blurbEl.style.display = "block";
    } else {
      blurbEl.style.display = "none";
    }
  }

  // ------------------------------------------------------------------ FILTERS
  // Chips voor ketenstap + projecten. 30+ stromen tegelijk is nooit leesbaar;
  // hiermee pel je de keten laag voor laag af.
  const STAGE_CHIP = { erts: "erts", raffinaat: "raffinaat", product: "product" };

  // WEERGAVE-SCHAKELAAR: routes over het oppervlak vs. hemelsbrede bogen.
  const VIEW_MODES = [
    { id: "route", label: "routes",
      title: "Zoals schepen echt varen: laag over het oppervlak, langs havens en zeestraten" },
    { id: "hemelsbreed", label: "hemelsbreed",
      title: "Rechtstreeks van A naar B in een hoge boog — wie handelt met wie" },
  ];

  function renderViewModes(filters, onChange) {
    viewRow.innerHTML = "";
    VIEW_MODES.forEach((m) => {
      const on = filters.viewMode === m.id;
      const btn = document.createElement("button");
      btn.className = "viewBtn" + (on ? " on" : "");
      btn.textContent = m.label;
      btn.title = m.title;
      btn.onclick = () => {
        if (filters.viewMode === m.id) return;
        filters.viewMode = m.id;
        onChange();
      };
      viewRow.appendChild(btn);
    });

    // schepen-schakelaar: alleen zinvol bij routes
    if (filters.viewMode === "route") {
      const sail = document.createElement("button");
      sail.className = "viewBtn sail" + (filters.ships ? " on" : "");
      sail.textContent = voyageNoun.btn;
      sail.title = "Speel enkele maanden af: elk lichtje is een lading onderweg";
      sail.onclick = () => { filters.ships = !filters.ships; onChange(); };
      viewRow.appendChild(sail);
    }
  }

  function renderFilters(filters, onChange, opts) {
    filterRow.innerHTML = "";

    Object.keys(STAGE_CHIP).forEach((stage) => {
      const on = filters.stages.has(stage);
      const chip = document.createElement("button");
      chip.className = "chip" + (on ? " on" : "");
      chip.textContent = STAGE_CHIP[stage];
      chip.title = CONFIG.flows.stageStyle[stage].label;
      chip.onclick = () => {
        if (on && filters.stages.size === 1) return; // minstens één stap aan
        on ? filters.stages.delete(stage) : filters.stages.add(stage);
        onChange();
      };
      filterRow.appendChild(chip);
    });

    const proj = document.createElement("button");
    proj.className = "chip" + (filters.showProjects ? " on" : "");
    proj.textContent = "projecten";
    proj.title = "Geplande mijnen, fabrieken en routes tonen";
    proj.onclick = () => { filters.showProjects = !filters.showProjects; onChange(); };
    filterRow.appendChild(proj);

    // Centrale-bank-laag: alleen aanbieden als een actieve grondstof CB-data heeft (goud).
    if (opts && opts.hasCB) {
      const cb = document.createElement("button");
      cb.className = "chip" + (filters.showCentralBanks ? " on" : "");
      cb.textContent = "centrale banken";
      cb.title = "Voorraden + de huidige inkoop-/repatriëringsstromen tonen";
      cb.onclick = () => { filters.showCentralBanks = !filters.showCentralBanks; onChange(); };
      filterRow.appendChild(cb);
    }

    // Beursvoorraden-laag: alleen aanbieden als een actieve grondstof beursdata heeft (koper).
    if (opts && opts.hasExchange) {
      const ex = document.createElement("button");
      ex.className = "chip" + (filters.showExchangeStocks ? " on" : "");
      ex.textContent = "beursvoorraden";
      ex.title = "LME/SHFE/COMEX-magazijnen + bufferstromen tonen (buffer, geen verbruik)";
      ex.onclick = () => { filters.showExchangeStocks = !filters.showExchangeStocks; onChange(); };
      filterRow.appendChild(ex);
    }

    // Recycling-laag: alleen aanbieden als een actieve grondstof een recycle-laag heeft (REE).
    if (opts && opts.hasRecycle) {
      const rc = document.createElement("button");
      rc.className = "chip" + (filters.showRecycle ? " on" : "");
      rc.textContent = "recycling";
      rc.title = opts.recycleHint || "Recyclingstromen (secundair aanbod) terug de keten in tonen";
      rc.onclick = () => { filters.showRecycle = !filters.showRecycle; onChange(); };
      filterRow.appendChild(rc);
    }

    // Strategische-voorraden-laag: alleen aanbieden als een actieve grondstof reserve-data heeft (olie/SPR).
    if (opts && opts.hasReserves) {
      const rv = document.createElement("button");
      rv.className = "chip" + (filters.showReserves ? " on" : "");
      rv.textContent = "voorraden";
      rv.title = "Strategische petroleumreserves (US SPR/China/Japan/India/IEA) tonen (buffer tegen aanbodschokken)";
      rv.onclick = () => { filters.showReserves = !filters.showReserves; onChange(); };
      filterRow.appendChild(rv);
    }

    // Militaire-kringloop-laag: alleen aanbieden als een actieve grondstof militaire data heeft (uranium).
    if (opts && opts.hasMilitary) {
      const ml = document.createElement("button");
      ml.className = "chip" + (filters.showMilitary ? " on" : "");
      ml.textContent = "militaire kringloop";
      ml.title = "Down-geblend wapen-HEU, tails-herverrijking en strategische reserves tonen (secundair aanbod)";
      ml.onclick = () => { filters.showMilitary = !filters.showMilitary; onChange(); };
      filterRow.appendChild(ml);
    }

    // Lab-grown-laag: alleen aanbieden als een actieve grondstof een lab-grown-laag heeft (diamant).
    if (opts && opts.hasLabGrown) {
      const lg = document.createElement("button");
      lg.className = "chip" + (filters.showLabGrown ? " on" : "");
      lg.textContent = "lab-grown";
      lg.title = "Synthetische kweekdiamant (China HPHT + India/VS CVD) tonen — schaduwaanbod dat de natuurlijke markt, vooral de VS-verlovingsring, ondergraaft";
      lg.onclick = () => { filters.showLabGrown = !filters.showLabGrown; onChange(); };
      filterRow.appendChild(lg);
    }
  }

  // --------------------------------------------------------------- KAARTSTIJL
  // De bol-textuur (ver uitgezoomd) én de tegellaag (ingezoomd).
  function renderStyles(onPick) {
    const styles = ["satelliet", "nacht", "donker", "vector"];
    styleList.innerHTML = "";
    styles.forEach((s) => {
      const btn = document.createElement("button");
      btn.className = "styleBtn" + (s === CONFIG.basemap.default ? " active" : "");
      btn.textContent = s;
      btn.onclick = () => {
        [...styleList.children].forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        onPick(s);
      };
      styleList.appendChild(btn);
    });
  }

  // Tegellaag: welke scherpe kaart komt er tevoorschijn als je inzoomt?
  const attribEl = document.getElementById("attrib");
  function renderTileStyles() {
    const row = document.getElementById("tileRow");
    row.innerHTML = "";

    const opts = [
      { id: "satelliet", label: "satelliet", title: "Esri World Imagery — scherp tot straatniveau" },
      { id: "kaart", label: "kaart", title: "OpenStreetMap — met plaatsnamen, havens en wegen" },
      { id: "uit", label: "uit", title: "Geen tegels; alleen de bol-textuur" },
    ];

    opts.forEach((o) => {
      const on = o.id === "uit" ? !TileLayer.isEnabled()
        : TileLayer.isEnabled() && TileLayer.currentSource() === o.id;
      const btn = document.createElement("button");
      btn.className = "tileBtn" + (on ? " on" : "");
      btn.textContent = o.label;
      btn.title = o.title;
      btn.onclick = () => {
        if (o.id === "uit") TileLayer.setEnabled(false);
        else { TileLayer.setEnabled(true); TileLayer.setSource(o.id); }
        renderTileStyles();
        paintAttrib();
      };
      row.appendChild(btn);
    });
  }

  function paintAttrib() {
    attribEl.textContent = TileLayer.isEnabled() ? TileLayer.attribution() : "";
  }

  // --------------------------------------------------------------- SPANNINGEN
  const TENSION_ICON = {
    knelpunt: "⌖", concentratie: "◍", beleid: "§", spof: "!",
  };

  function renderTensions(activeIds, onPick) {
    const res = activeIds.length === 1 ? getResource(activeIds[0]) : null;
    const tensions = res && res.tensions;
    if (!tensions || !tensions.length) { tensionBox.style.display = "none"; return; }

    tensionBox.style.display = "block";
    tensionList.innerHTML = "";
    tensions.forEach((t) => {
      const btn = document.createElement("button");
      btn.className = "tension";
      btn.innerHTML =
        '<span class="tIcon">' + (TENSION_ICON[t.type] || "•") + "</span>" +
        '<span class="tTitle">' + t.title + "</span>";
      btn.onclick = () => {
        [...tensionList.children].forEach((b) => b.classList.remove("picked"));
        btn.classList.add("picked");
        onPick(res, t);
      };
      tensionList.appendChild(btn);
    });
  }

  function clearTensionPick() {
    [...tensionList.children].forEach((b) => b.classList.remove("picked"));
  }

  // ------------------------------------------------------------- AFSPEELBALK
  // Alleen zichtbaar in de route-weergave: in hemelsbreed varen er geen schepen.
  const timeBar = document.getElementById("timeBar");
  const playBtn = document.getElementById("playBtn");
  const timeSlider = document.getElementById("timeSlider");
  const timeDate = document.getElementById("timeDate");
  const timeCount = document.getElementById("timeCount");
  const speedBtn = document.getElementById("speedBtn");

  function showTimeBar(on) {
    timeBar.style.display = on ? "flex" : "none";
  }

  function paintTime(day) {
    timeSlider.value = String(Math.round((day / Voyages.totalDays()) * 1000));
    timeDate.textContent = Voyages.dateLabel(day);
    const n = Voyages.shipsAtSea();
    timeCount.textContent = n + " " + (n === 1 ? voyageNoun.one : voyageNoun.many) + " onderweg";
  }

  function paintPlayBtn() {
    playBtn.textContent = Voyages.isPlaying() ? "❘❘" : "▶";
    playBtn.title = Voyages.isPlaying() ? "Pauzeer" : "Afspelen";
  }

  function wireTimeBar() {
    playBtn.onclick = () => { Voyages.toggle(); paintPlayBtn(); };

    timeSlider.oninput = () => {
      Voyages.pause();
      paintPlayBtn();
      Voyages.setDay((timeSlider.value / 1000) * Voyages.totalDays());
      paintTime(Voyages.getDay());
    };

    speedBtn.onclick = () => {
      const speeds = CONFIG.time.speeds;
      const next = speeds[(speeds.indexOf(Voyages.getSpeed()) + 1) % speeds.length];
      Voyages.setSpeed(next);
      speedBtn.textContent = next + "×";
    };
    speedBtn.textContent = Voyages.getSpeed() + "×";

    Voyages.onTick(paintTime);
    paintPlayBtn();
    paintTime(0);
  }

  // ---------------------------------------------------------------- INFOPANEEL
  const MODE_LABEL = {
    ship: "per schip", air: "luchtvracht", pipeline: "pijpleiding",
    rail: "per spoor", road: "over land",
  };
  const TYPE_LABEL = {
    mine: "Mijn / winning", refinery: "Raffinage / verwerking",
    port: "Haven / overslag", market: "Fabriek / afzetmarkt",
    airport: "Luchthaven / gateway", hub: "Handels- & kluishub",
    cb: "Centrale bank", recycler: "Recycling", exchange: "Beursmagazijn",
    reserve: "Strategische reserve", military: "Militaire kringloop",
    labgrown: "Lab-grown / synthetisch",
  };
  const WP_KIND_LABEL = { zeestraat: "Zeestraat", kanaal: "Kanaal", kaap: "Kaap",
    vaarpunt: "Vaarpunt", grensovergang: "Grenspost" };

  function paintInfo() {
    const d = selected || hovered;
    if (!d) { infoPanel.style.display = "none"; return; }
    infoPanel.style.display = "block";

    const dot = document.getElementById("infoDot");
    const resEl = document.getElementById("infoResource");
    const symEl = document.getElementById("infoSymbol");

    // gedeeld knelpunt (geen grondstof)
    if (d.kind === "waypoint") {
      const wp = d.wp;
      dot.style.background = "#C9A227";
      resEl.textContent = "Knelpunt";
      symEl.textContent = "";
      document.getElementById("infoTitle").textContent = wp.name;
      document.getElementById("infoSub").textContent = WP_KIND_LABEL[wp.kind] || wp.kind;
      document.getElementById("infoMeta").textContent = "";
      document.getElementById("infoNote").textContent = wp.note || "";
      return;
    }

    // spanning (aangeklikt in de lijst)
    if (d.kind === "tension") {
      const res = d.resource, t = d.tension;
      dot.style.background = res.flowColor || res.color;
      resEl.textContent = res.name;
      symEl.textContent = "(" + res.symbol + ")";
      document.getElementById("infoTitle").textContent = t.title;
      document.getElementById("infoSub").textContent = "spanning · " + t.type;
      document.getElementById("infoMeta").textContent = t.metric || "";
      document.getElementById("infoNote").textContent = t.note || "";
      return;
    }

    const res = d.resource;
    const c = res.flowColor || res.color;
    dot.style.background = c;
    resEl.textContent = res.name;
    symEl.textContent = "(" + res.symbol + ")";

    if (d.kind === "node") {
      const n = d.node;
      document.getElementById("infoTitle").textContent = n.name;
      document.getElementById("infoSub").textContent =
        n.country + " · " + (TYPE_LABEL[n.type] || n.type) +
        (n.status && n.status !== "actief" ? " · " + n.status : "");
      const meta = [];
      if (n.share) meta.push("aandeel wereldproductie ≈ " + n.share + "%");
      if (n.reserve) meta.push("goudvoorraad ≈ " + n.reserve + " t");
      if (n.stock && n.type === "reserve") meta.push("strategische voorraad ≈ " + n.stock + " mln vaten");
      if (n.stock && n.type === "military") meta.push("secundaire voorraad ≈ " + n.stock + " tU");
      else if (n.stock) meta.push("beursvoorraad ≈ " + n.stock + " kt");
      if (n.exchange) meta.push(n.exchange);
      if (n.potential) meta.push("potentie: " + n.potential);
      if (n.capacity) meta.push(n.capacity);
      if (n.operator) meta.push(n.operator);
      document.getElementById("infoMeta").textContent = meta.join(" · ");
      document.getElementById("infoNote").textContent = n.note || "";
    } else {
      const f = d.flow;
      const stage = f.stage || "raffinaat";
      const stageLabel = (CONFIG.flows.stageStyle[stage] || {}).label || stage;
      document.getElementById("infoTitle").textContent = d.from.name + " → " + d.to.name;
      document.getElementById("infoSub").textContent =
        d.from.country + " → " + d.to.country + " · " + (MODE_LABEL[f.mode] || "transport") +
        " · " + stageLabel + (f.status === "gepland" ? " · gepland" : "");
      document.getElementById("infoMeta").textContent =
        f.value ? "volume ≈ " + f.value + (res.unit ? " " + res.unit : "") : "";
      document.getElementById("infoNote").textContent = f.note || "";
    }
  }

  return {
    renderPills,
    renderViewModes,
    renderFilters,
    setVoyageNoun(n) { voyageNoun = n; },
    renderTileStyles,
    paintAttrib,
    showTimeBar,
    wireTimeBar,
    paintTime,
    paintPlayBtn,
    renderStyles,
    renderTensions,
    clearTensionPick,
    setHover(d) { hovered = d; paintInfo(); },
    setSelected(d) { selected = d; paintInfo(); },
    clearSelection() { selected = null; paintInfo(); },
  };
})();
