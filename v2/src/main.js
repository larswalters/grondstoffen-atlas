// main.js — start v2 op en koppelt de HUD aan de bol.
// Bewust dun: alle logica hoort in de lagen, niet hier.

import { createGlobe, CONFIG } from "./globe.js?v=004";
import { laadVectorWereld } from "./world.js?v=004";

const GLOBE = createGlobe(document.getElementById("canvasWrap"));

// --- de vectorwereld -------------------------------------------------------
// Dit is de waarheid van v2. Laadt asynchroon; de bol is al bruikbaar terwijl
// dit binnenkomt.

let wereldStats = null;
let kustlijn = null;

laadVectorWereld(CONFIG.radius)
  .then(({ lijnen, stats }) => {
    GLOBE.globeGroup.add(lijnen);
    kustlijn = lijnen;
    wereldStats = stats;
    // Standaard: satelliet ALS ondergrond met de vectorkustlijn eroverheen.
    // De vectorwereld blijft de waarheid voor routering; de satelliet is puur
    // een skin. Lars kijkt het liefst naar deze combinatie.
    GLOBE.setBasemap("satelliet");
    console.log(
      `[atlas v2] vectorwereld: ${stats.punten.toLocaleString("nl")} punten · ` +
      `${stats.ringen.toLocaleString("nl")} vormen · ${stats.kbOverdracht} KB · ` +
      `laden ${stats.msLaden} ms, verwerken ${stats.msVerwerken} ms`
    );
  })
  .catch((e) => {
    console.error("[atlas v2] vectorwereld niet geladen:", e);
    // Zonder vectorwereld is de satelliet de enige zinnige weergave.
    GLOBE.setBasemap("satelliet");
  });

// --- HUD-knoppen -----------------------------------------------------------

function wireButtons(selector, attr, apply) {
  const btns = [...document.querySelectorAll(selector)];
  for (const btn of btns) {
    btn.addEventListener("click", () => {
      btns.forEach((b) => b.classList.remove("is-on"));
      btn.classList.add("is-on");
      apply(btn.dataset[attr]);
    });
  }
}

wireButtons(".tmBtn", "tm", (mode) => GLOBE.setToneMapping(mode));
wireButtons(".sunBtn", "sun", (mode) => GLOBE.setSun(mode));
wireButtons(".bmBtn", "bm", (mode) => GLOBE.setBasemap(mode));
wireButtons(".clBtn", "cl", (mode) => {
  if (kustlijn) kustlijn.visible = (mode === "aan");
});

document.getElementById("zoomIn").addEventListener("click", () => GLOBE.zoomBy(1 / 1.25));
document.getElementById("zoomOut").addEventListener("click", () => GLOBE.zoomBy(1.25));

// --- statusregel -----------------------------------------------------------
// Toont wat de bol kost. Zodra de vectorwereld erop komt is dit de plek waar
// we zien of we binnen budget blijven — op PC én op de telefoon.

const statsEl = document.getElementById("stats");

GLOBE.onTick(() => {
  const s = GLOBE.getStats();
  let tekst =
    `${s.fps} fps · zoom ${s.zoom.toFixed(2)}\n` +
    `${s.calls} draw calls · ${(s.tris / 1000).toFixed(0)}k driehoeken`;
  if (wereldStats) {
    tekst += `\n${(wereldStats.punten / 1000).toFixed(0)}k vectorpunten · ${wereldStats.kbOverdracht} KB`;
  }
  statsEl.textContent = tekst;
});

statsEl.style.whiteSpace = "pre-line";

// Handvat voor diagnose vanuit de console/devtools. Dit project wordt veel
// visueel geverifieerd; zonder globals is er anders geen enkele manier om de
// scene van buitenaf te bevragen (ES-modules hebben geen window-scope).
window.GLOBE = GLOBE;

console.log("[atlas v2] three r185 · ACES tone mapping actief");
