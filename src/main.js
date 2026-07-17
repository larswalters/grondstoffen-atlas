// main.js — Knoopt de losse onderdelen aan elkaar. Hier staat de state:
// actieve grondstoffen, filters (ketenstap/projecten) en de focus-selectie.

const ATLAS = (function () {
  let activeIds = ["lithium"];

  const filters = {
    viewMode: CONFIG.flows.viewMode,   // "route" | "hemelsbreed"
    ships: false,                      // tijdmodus: schepen/vluchten met lichtspoor
    stages: new Set(["erts", "raffinaat", "product"]),
    showProjects: true,
    showCentralBanks: false,           // goud: optionele centrale-bank-laag
    showExchangeStocks: false,         // koper: optionele beursvoorraden-laag
    showRecycle: false,                // zeldzame aardmetalen: optionele recycling-laag
    showReserves: false,               // olie: optionele strategische-voorraden-laag (SPR)
    showMilitary: false,               // uranium: optionele militaire-kringloop-laag
    showLabGrown: false,               // diamant: optionele lab-grown/synthetische-laag
  };

  function activeResources() { return RESOURCES.filter((r) => activeIds.includes(r.id)); }
  function hasCentralBanks() { return activeResources().some((r) => r.nodes.some((n) => n.type === "cb")); }
  function hasExchangeStocks() { return activeResources().some((r) => r.nodes.some((n) => n.type === "exchange")); }
  // strategische-voorraden-toggle: alleen bij grondstoffen met `type:"reserve"`-nodes (olie/SPR).
  function hasReserves() { return activeResources().some((r) => r.nodes.some((n) => n.type === "reserve")); }
  // militaire-kringloop-toggle: alleen bij grondstoffen met `type:"military"`-nodes (uranium).
  function hasMilitary() { return activeResources().some((r) => r.nodes.some((n) => n.type === "military")); }
  // recycling-toggle: alleen bij grondstoffen die de kringloop achter een `layer:"recycle"`-
  // laag zetten (REE) — koper heeft recycling always-on (geen layer) en krijgt dus geen chip.
  function hasRecycle() { return activeResources().some((r) => (r.flows || []).some((f) => f.layer === "recycle")); }
  // lab-grown-toggle: alleen bij grondstoffen die een `layer:"labgrown"`-schaduwlaag hebben (diamant).
  function hasLabGrown() { return activeResources().some((r) => (r.flows || []).some((f) => f.layer === "labgrown")); }
  // recycling-tooltip is grondstof-specifiek (REE <5% magneetschroot ≠ PGM ~25% autokat ≠ grafiet nascent):
  // pak de `recycleHint` van de actieve grondstof met een recycle-laag (fallback = generiek in ui.js).
  function recycleHint() {
    const r = activeResources().find((r) => (r.flows || []).some((f) => f.layer === "recycle"));
    return r && r.recycleHint ? r.recycleHint : null;
  }
  function activeHasAir() { return activeResources().some((r) => (r.flows || []).some((f) => f.mode === "air")); }

  // Chrome die van de ACTIEVE grondstoffen afhangt: de CB-chip (alleen bij goud)
  // en de tijdlijn-woordkeus (schepen ↔ vluchten). syncVoyageNoun eerst, want
  // renderViewModes zet daar de knoptekst op.
  function refreshChrome() {
    UI.setVoyageNoun(activeHasAir()
      ? { one: "vlucht", many: "vluchten", btn: "✈ vluchten" }
      : { one: "schip", many: "schepen", btn: "⚓ schepen" });
    UI.renderViewModes(filters, onFilterChange);
    UI.renderFilters(filters, onFilterChange,
      { hasCB: hasCentralBanks(), hasExchange: hasExchangeStocks(), hasRecycle: hasRecycle(), hasReserves: hasReserves(), hasMilitary: hasMilitary(), hasLabGrown: hasLabGrown(), recycleHint: recycleHint() });
  }

  // focus: null | {type:"node", id} | {type:"flow", key, nodeIds}
  //             | {type:"waypoint", id} | {type:"tension", tension}
  let focus = null;

  function focusSelection() {
    if (!focus) return null;
    if (focus.type === "node" || focus.type === "waypoint") {
      return { nodeIds: new Set([focus.id]), flowKeys: null };
    }
    if (focus.type === "flow") {
      return { nodeIds: new Set(focus.nodeIds), flowKeys: new Set([focus.key]) };
    }
    if (focus.type === "tension") {
      const t = focus.tension;
      return {
        nodeIds: new Set(t.nodes || []),
        flowKeys: new Set(t.flows || []),
      };
    }
    return null;
  }

  function applyFocus() {
    const sel = focusSelection();
    const involved = FlowLayer.setFocus(sel);
    MarkerLayer.setFocus(involved); // null = niets dimmen
  }

  // NB (LAR-481): hier stond `usedNodeIds()` — de set locaties aan een zichtbare
  // stroom, die MarkerLayer gebruikte om ze ondanks hun tier te blijven tonen
  // ("een lijn mag niet in het niets eindigen"). Nu markers niet meer op tier
  // verdwijnen is die uitzondering overbodig: het gevaar dat hij afdekte kan
  // niet meer optreden.

  function rebuild() {
    const active = RESOURCES.filter((r) => activeIds.includes(r.id));
    GLOBE.clearPickables();
    MarkerLayer.build(active, filters);
    FlowLayer.build(active, filters);

    // schepen varen alleen in de route-weergave
    const sailing = filters.ships && filters.viewMode === "route";
    Voyages.setActive(sailing);
    UI.showTimeBar(sailing);
    if (sailing) {
      UI.paintPlayBtn();
      UI.paintTime(Voyages.getDay());
    }

    applyFocus();
  }

  function clearFocus() {
    focus = null;
    UI.clearSelection();
    UI.clearTensionPick();
    applyFocus();
  }

  function toggle(id) {
    clearFocus();
    activeIds = activeIds.includes(id)
      ? activeIds.filter((x) => x !== id)
      : activeIds.concat([id]);
    UI.renderPills(activeIds, toggle);
    UI.renderTensions(activeIds, pickTension);
    refreshChrome();   // CB-chip + schepen/vluchten hangen van de actieve set af
    rebuild();
  }

  function pickTension(res, t) {
    focus = { type: "tension", tension: t };
    UI.setSelected({ kind: "tension", resource: res, tension: t });
    applyFocus();
    if (t.lat != null && t.lon != null) GLOBE.flyTo(t.lat, t.lon);
  }

  // --- opstarten -----------------------------------------------------------
  Basemap.setStyle(CONFIG.basemap.default);
  UI.renderStyles((s) => Basemap.setStyle(s));
  UI.renderPills(activeIds, toggle);
  function onFilterChange() {
    refreshChrome();
    rebuild();
  }
  refreshChrome();
  UI.renderTensions(activeIds, pickTension);
  UI.renderTileStyles();
  UI.paintAttrib();
  UI.wireTimeBar();
  rebuild();

  // band-wissel bij zoomen -> flows opnieuw opbouwen (dunner/platter)
  FlowLayer.onNeedRebuild(rebuild);

  GLOBE.onHover((d) => UI.setHover(d));
  GLOBE.onClick((d) => {
    if (!d) { clearFocus(); return; }
    UI.clearTensionPick();
    UI.setSelected(d);
    if (d.kind === "node") {
      focus = { type: "node", id: d.node.id };
      applyFocus();
      GLOBE.flyTo(d.node.lat, d.node.lon);
    } else if (d.kind === "waypoint") {
      focus = { type: "waypoint", id: d.wp.id };
      applyFocus();
    } else if (d.kind === "flow") {
      focus = {
        type: "flow",
        key: d.flow.from + ">" + d.flow.to,
        nodeIds: [d.from.id, d.to.id, ...(d.flow.via || [])],
      };
      applyFocus();
    }
  });

  document.getElementById("zoomIn").addEventListener("click", () => GLOBE.zoomBy(0.82));
  document.getElementById("zoomOut").addEventListener("click", () => GLOBE.zoomBy(1.22));

  GLOBE.start();

  return { rebuild, toggle, get activeIds() { return activeIds; }, filters };
})();
