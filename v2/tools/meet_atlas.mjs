// meet_atlas.mjs — de atlas-bol METEN in een echte headless Chrome via CDP.
//
// Waarom dit bestaat (2026-10-08, LAR-490 visuele fase): de Browser-pane van
// Claude Code composit geen frames (document.hidden = true, canvas 1×1, rAF
// staat stil) — de bekende M22-valkuil. Per-frame maatregelen (fps, draw calls,
// kometen) leveren daar dus nul op. Deze harness praat via de ingebouwde
// WebSocket van node met een EXTERN gestarte headless Chrome en levert één
// rapport.json + PNG's per kijkstand, voor desktop én telefoon-emulatie.
//
// Het is de generalisatie van build-cache/verificatie-fase3/capture.mjs (de
// AIS-tracks-harness van 2026-07-27); dat bestand blijft staan als voorbeeld.
//
// ⚠️ Chrome wordt NIET hier gestart: de Bash-sandbox laat het proces wel
// starten maar meteen hangen (geen output, geen CDP-poort). Vanuit PowerShell
// komt hij wél op. Start hem dus eerst zelf, bv.:
//
//   Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList `
//     '--headless=new','--remote-debugging-port=9333','--window-size=1600,1000', `
//     '--ignore-gpu-blocklist','--enable-unsafe-swiftshader', `
//     '--user-data-dir=C:\Users\lars\AppData\Local\Temp\atlas-cdp-profiel','about:blank'
//
// Gebruik:
//   node v2/tools/meet_atlas.mjs --url http://localhost:8732/v2/ --out <map> \
//        [--profiel desktop|telefoon|beide] [--kleur modaliteit|grondstof] \
//        [--poort 9333] [--wacht 120] [--label v131]
//
// ⚠️ Wat de fps hier betekent: headless Chrome rendert via ANGLE/SwiftShader
// (software) of via de GPU van deze pc — géén van beide is een telefoon-GPU.
// De absolute fps is dus niet de fps op Lars' telefoon; de VERHOUDING tussen
// twee versies, de draw calls, de puntenaantallen, het geheugen en de laadtijd
// zijn wél betekenisvol. De telefoon-stand voegt een CPU-vertraging ×4 toe
// (Emulation.setCPUThrottlingRate), wat de laad- en per-frame-JS-kant wél
// realistisch zwaarder maakt.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

// --- argumenten ------------------------------------------------------------
const arg = (naam, standaard) => {
  const i = process.argv.indexOf(`--${naam}`);
  return i >= 0 && process.argv[i + 1] !== undefined ? process.argv[i + 1] : standaard;
};
const URL_BASIS = arg("url", "http://localhost:8732/v2/");
const OUT = arg("out", "./meting");
const PROFIEL = arg("profiel", "beide");           // desktop | telefoon | beide
const KLEUR = arg("kleur", null);                  // null = de default van de pagina
const MODUS = arg("modus", null);                  // atlas | bouw → ?modus= op de url (golf 1)
const POORT = +arg("poort", "9333");
const WACHT_S = +arg("wacht", "150");              // max wachten op alle stromen
const LABEL = arg("label", "meting");
// ?modus= aan de url hangen zonder een bestaande querystring te slopen
const URL_ = MODUS ? URL_BASIS + (URL_BASIS.includes("?") ? "&" : "?") + `modus=${MODUS}` : URL_BASIS;

mkdirSync(OUT, { recursive: true });
const slaap = (ms) => new Promise((r) => setTimeout(r, ms));

// De vier kijkstanden van de ontwerpbrief (wereld · continent · regionaal ·
// lokaal). Lon/lat/hoogte in km, zoals GLOBE.vliegNaar ze wil.
const KIJKSTANDEN = [
  ["wereld",    110,    28,   9000],   // de "wereld"-knop uit de HUD
  ["continent", 10,     50,   3500],   // Europa, van de Noordzee tot de Zwarte Zee
  ["regionaal", 4.3,    51.9,  300],   // Rijnmond → Ruhr
  ["lokaal",    117.80, 30.98,  14],   // Tongling-complex (de gloed-toets)
];

// --- minimale CDP-client ---------------------------------------------------
class CDP {
  constructor(ws) {
    this.ws = ws; this.id = 0; this.wacht = new Map(); this.luister = [];
    ws.addEventListener("message", (ev) => {
      const m = JSON.parse(ev.data);
      if (m.id && this.wacht.has(m.id)) {
        const { res, rej } = this.wacht.get(m.id);
        this.wacht.delete(m.id);
        m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result);
      } else if (m.method) {
        for (const f of this.luister) f(m);
      }
    });
  }
  send(method, params = {}) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((res, rej) => {
      this.wacht.set(id, { res, rej });
      setTimeout(() => {
        if (this.wacht.has(id)) { this.wacht.delete(id); rej(new Error(`timeout ${method}`)); }
      }, 240000);
    });
  }
  on(f) { this.luister.push(f); }
}

async function wachtOpChrome() {
  for (let i = 0; i < 40; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${POORT}/json/version`);
      if (r.ok) return await r.json();
    } catch {}
    await slaap(500);
  }
  throw new Error(`geen Chrome op poort ${POORT} — start hem eerst (zie de kop van dit bestand)`);
}

async function verbind(url) {
  const ws = new WebSocket(url);
  await new Promise((res, rej) => {
    ws.addEventListener("open", res, { once: true });
    ws.addEventListener("error", (e) => rej(new Error("ws fout: " + (e.message || e.type))), { once: true });
  });
  return new CDP(ws);
}

// --- de meting per profiel --------------------------------------------------
let laatsteRapport = null;     // voor de foutafhandeling: toon wat de pagina zei
async function meetProfiel(profiel) {
  const telefoon = profiel === "telefoon";
  const nieuw = await fetch(`http://127.0.0.1:${POORT}/json/new?about:blank`, { method: "PUT" });
  const doel = await nieuw.json();
  const cdp = await verbind(doel.webSocketDebuggerUrl);

  const rapport = {
    profiel, url: URL_, label: LABEL,
    console: [], excepties: [], netwerk: { verzoeken: 0, bytes: 0, data: [] },
    laden: {}, kijkstanden: [], scene: null,
  };
  laatsteRapport = rapport;
  const verzoeken = new Map();
  cdp.on((m) => {
    if (m.method === "Runtime.consoleAPICalled") {
      if (m.params.type === "warning" || m.params.type === "error") {
        rapport.console.push({
          type: m.params.type,
          tekst: m.params.args.map((a) => a.value ?? a.description ?? "").join(" ").slice(0, 300),
        });
      }
    } else if (m.method === "Runtime.exceptionThrown") {
      const d = m.params.exceptionDetails;
      rapport.excepties.push({ tekst: (d.exception?.description || d.text || "").slice(0, 400), url: d.url, regel: d.lineNumber });
    } else if (m.method === "Network.requestWillBeSent") {
      verzoeken.set(m.params.requestId, { url: m.params.request.url, t0: m.params.timestamp });
    } else if (m.method === "Network.loadingFinished") {
      const v = verzoeken.get(m.params.requestId);
      if (v) { v.bytes = m.params.encodedDataLength; v.ms = Math.round((m.params.timestamp - v.t0) * 1000); v.klaar = true; }
    } else if (m.method === "Network.loadingFailed") {
      const v = verzoeken.get(m.params.requestId);
      if (v) v.mislukt = m.params.errorText;
    }
  });

  await cdp.send("Page.enable");
  await cdp.send("Runtime.enable");
  await cdp.send("Log.enable");
  await cdp.send("Network.enable");
  await cdp.send("Network.setCacheDisabled", { cacheDisabled: true });   // koud meten
  if (telefoon) {
    await cdp.send("Emulation.setDeviceMetricsOverride",
      { width: 390, height: 844, deviceScaleFactor: 3, mobile: true });
    await cdp.send("Emulation.setCPUThrottlingRate", { rate: 4 });
    await cdp.send("Emulation.setTouchEmulationEnabled", { enabled: true });
  } else {
    await cdp.send("Emulation.setDeviceMetricsOverride",
      { width: 1600, height: 1000, deviceScaleFactor: 1, mobile: false });
  }

  const evalueer = async (expr, wachtOpBelofte = false) => {
    const r = await cdp.send("Runtime.evaluate",
      { expression: expr, returnByValue: true, awaitPromise: wachtOpBelofte });
    if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text);
    return r.result.value;
  };
  const schiet = async (naam) => {
    const r = await cdp.send("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
    const pad = join(OUT, `${LABEL}-${profiel}-${naam}.png`);
    writeFileSync(pad, Buffer.from(r.data, "base64"));
    return pad;
  };

  // 1) laden — tot álle stromen uit de HUD geladen (of mislukt) zijn
  const t0 = Date.now();
  const geladen = new Promise((res) => cdp.on((m) => { if (m.method === "Page.loadEventFired") res(); }));
  await cdp.send("Page.navigate", { url: URL_ });
  await geladen;
  rapport.laden.msPaginaLoad = Date.now() - t0;

  // Wachten tot alle stromen er zijn: sinds golf 1 via window.ATLAS (de bundel,
  // één laag); de oude per-stroom-lagen (?laag=los of ?v≤131) via de drie Maps.
  const klaar = await evalueer(`new Promise((res) => {
    const t0 = performance.now();
    const p = setInterval(() => {
      const n = document.querySelectorAll('.srBtn').length;
      const A = window.ATLAS;
      const bundel = !!(A && A.stats && A.stats.geladen === A.stats.stromen && A.stats.stromen > 0);
      const ok = window.STROOMROUTES ? window.STROOMROUTES.size : 0;
      const lv = window.STROOMLEVEN ? window.STROOMLEVEN.size : 0;
      const gl = window.GLOEDNODES ? window.GLOEDNODES.size : 0;
      const los = n > 0 && ok >= n && lv >= n;
      const stromenKlaar = bundel || los;
      if (stromenKlaar || performance.now() - t0 > ${WACHT_S * 1000}) {
        clearInterval(p);
        res({ stromenInHud: n, stroomroutes: bundel ? A.stats.stromen : ok, stroomleven: lv, gloedlagen: gl,
              bundel, atlasStats: bundel ? A.stats : null,
              msTotAlleStromen: Math.round(performance.now()), compleet: stromenKlaar });
      }
    }, 250);
  })`, true);
  Object.assign(rapport.laden, klaar);

  // Netwerk-telling van de data-laag (geen tegels: die hangen aan de kijkstand)
  const data = [...verzoeken.values()].filter((v) => /\/data\//.test(v.url) && !/arcgis|tile/.test(v.url));
  rapport.netwerk.verzoeken = data.length;
  rapport.netwerk.bytes = data.reduce((s, v) => s + (v.bytes || 0), 0);
  rapport.netwerk.mislukt = data.filter((v) => v.mislukt).map((v) => v.url.split("/").pop());
  rapport.netwerk.data = data
    .sort((a, b) => (b.bytes || 0) - (a.bytes || 0))
    .slice(0, 8)
    .map((v) => ({ bestand: v.url.split("/").pop().split("?")[0], kb: Math.round((v.bytes || 0) / 1024), ms: v.ms }));
  rapport.netwerk.alleVerzoeken = verzoeken.size;
  rapport.netwerk.alleBytes = [...verzoeken.values()].reduce((s, v) => s + (v.bytes || 0), 0);

  // 2) kleurmodus zetten als gevraagd (de atlasmodus zet ook de ondergrond op donker)
  if (KLEUR) {
    await evalueer(`(()=>{const b=document.querySelector('.skBtn[data-sk="${KLEUR}"]'); if(b) b.click(); return !!b;})()`);
    await slaap(1500);
  }

  // 3) de scene tellen: wat staat er, en hoeveel draw calls levert dat op
  rapport.scene = JSON.parse(await evalueer(`(()=>{
    const G = window.GLOBE; if (!G) return "null";
    const telling = { LineSegments: 0, Line: 0, Line2: 0, Points: 0, Mesh: 0, overig: 0, vertices: 0, zichtbaar: 0 };
    G.scene.traverse((o) => {
      if (!o.isObject3D || o.isGroup || o.isScene || o.isCamera || o.isLight) return;
      // alleen renderbare objecten tellen
      if (!o.geometry) return;
      let zichtbaar = o.visible; let p = o.parent;
      while (zichtbaar && p) { zichtbaar = p.visible; p = p.parent; }
      if (!zichtbaar) return;
      telling.zichtbaar++;
      const t = o.isLine2 ? "Line2" : (o.isLineSegments ? "LineSegments" : (o.isLine ? "Line" : (o.isPoints ? "Points" : (o.isMesh ? "Mesh" : "overig"))));
      telling[t]++;
      const pos = o.geometry.getAttribute && (o.geometry.getAttribute("position") || o.geometry.getAttribute("instanceStart"));
      if (pos) telling.vertices += pos.count;
    });
    const gl = G.renderer.getContext();
    const dbg = gl.getExtension("WEBGL_debug_renderer_info");
    return JSON.stringify({
      objecten: telling,
      geheugenGpu: G.renderer.info.memory,
      programmas: G.renderer.info.programs ? G.renderer.info.programs.length : null,
      webgl: dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : "onbekend",
      pixelRatio: G.renderer.getPixelRatio(),
      canvas: [G.renderer.domElement.width, G.renderer.domElement.height],
      jsHeapMb: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : null,
      kleurModus: document.querySelector('.skBtn.is-on')?.dataset.sk,
      lijnModus: document.querySelector('.slBtn.is-on')?.dataset.sl,
      ondergrond: document.querySelector('.sdBtn.is-on')?.dataset.sd,
    });
  })()`));

  // 4) per kijkstand: vliegen, wachten tot de tegels er zijn, dan 3 s fps middelen
  for (const [naam, lon, lat, km] of KIJKSTANDEN) {
    await evalueer(`window.GLOBE.vliegNaar(${lon}, ${lat}, ${km}, 800); true`);
    await slaap(telefoon ? 7000 : 5000);
    const meting = JSON.parse(await evalueer(`new Promise((res) => {
      const fps = [], calls = [], tris = [];
      let n = 0;
      const p = setInterval(() => {
        const s = window.GLOBE.getStats();
        fps.push(s.fps); calls.push(s.calls); tris.push(s.tris);
        if (++n >= 6) {
          clearInterval(p);
          const mid = (a) => a.slice().sort((x, y) => x - y)[Math.floor(a.length / 2)];
          res(JSON.stringify({
            fpsMediaan: mid(fps), fpsMin: Math.min(...fps), fpsMax: Math.max(...fps),
            drawCalls: mid(calls), driehoeken: mid(tris),
            hoogteKm: Math.round(window.GLOBE.getAltitudeKm()),
            tegels: window.TEGELS ? window.TEGELS.stats() : null,
            jsHeapMb: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : null,
          }));
        }
      }, 500);
    })`, true));
    meting.kijkstand = naam;
    meting.screenshot = await schiet(naam);
    rapport.kijkstanden.push(meting);
  }

  rapport.fouten = { console: rapport.console.length, excepties: rapport.excepties.length };
  await cdp.send("Page.close").catch(() => {});
  return rapport;
}

// --- hoofdprogramma ---------------------------------------------------------
async function main() {
  const versie = await wachtOpChrome();
  const profielen = PROFIEL === "beide" ? ["desktop", "telefoon"] : [PROFIEL];
  const uit = { label: LABEL, url: URL_, chrome: versie.Browser, profielen: {} };
  for (const p of profielen) {
    console.log(`[meet_atlas] ${LABEL} · ${p} …`);
    uit.profielen[p] = await meetProfiel(p);
  }
  const pad = join(OUT, `${LABEL}-rapport.json`);
  writeFileSync(pad, JSON.stringify(uit, null, 2));

  // compacte samenvatting op stdout
  for (const [p, r] of Object.entries(uit.profielen)) {
    console.log(`\n== ${LABEL} · ${p} · ${r.scene?.webgl ?? "?"} · ${r.scene?.kleurModus}/${r.scene?.ondergrond} ==`);
    console.log(`laden: pagina ${r.laden.msPaginaLoad} ms · alle stromen ${r.laden.msTotAlleStromen} ms · ` +
      `${r.laden.stroomroutes}/${r.laden.stromenInHud} stromen · ${r.laden.bundel ? "bundel" : r.laden.gloedlagen + " gloedlagen"} · compleet=${r.laden.compleet}`);
    if (r.laden.atlasStats) {
      const a = r.laden.atlasStats;
      console.log(`bundel ${a.bundelVersie}: ${a.benen} benen · L0 ${a.segmentenL0} / L1 ${a.segmentenL1} / lucht ${a.segmentenLucht} seg · ` +
        `${a.kometen.kometen} kometen · ${a.gloedKnopen} gloedknopen · laden ${a.msLaden} ms, decoderen ${a.msDecoderen} ms · ${a.kleurModus}/${a.lijnModus}`);
    }
    console.log(`netwerk data/: ${r.netwerk.verzoeken} verzoeken · ${(r.netwerk.bytes / 1048576).toFixed(1)} MB` +
      ` (alles incl. tegels: ${r.netwerk.alleVerzoeken} · ${(r.netwerk.alleBytes / 1048576).toFixed(1)} MB)`);
    const o = r.scene?.objecten || {};
    console.log(`scene: ${o.zichtbaar} zichtbare objecten (LineSegments ${o.LineSegments} · Line ${o.Line} · Line2 ${o.Line2} · ` +
      `Points ${o.Points} · Mesh ${o.Mesh}) · ${(o.vertices / 1000).toFixed(0)}k vertices · ` +
      `GPU geometries ${r.scene?.geheugenGpu?.geometries} textures ${r.scene?.geheugenGpu?.textures} · heap ${r.scene?.jsHeapMb} MB`);
    for (const k of r.kijkstanden) {
      console.log(`  ${k.kijkstand.padEnd(10)} ${String(k.hoogteKm).padStart(5)} km · fps ${k.fpsMediaan} (${k.fpsMin}–${k.fpsMax}) · ` +
        `${k.drawCalls} draw calls · ${(k.driehoeken / 1000).toFixed(0)}k tris · heap ${k.jsHeapMb} MB`);
    }
    console.log(`fouten: ${r.fouten.console} console-warn/err · ${r.fouten.excepties} excepties`);
    for (const c of r.console.slice(0, 5)) console.log(`   · ${c.type}: ${c.tekst}`);
    for (const e of r.excepties.slice(0, 5)) console.log(`   · EXC: ${e.tekst}`);
  }
  console.log(`\nrapport: ${pad}`);
}

main().catch((e) => {
  console.error("FOUT:", e.message);
  // Een meting die strandt is meestal een pagina die strandt: toon wat die zei.
  if (laatsteRapport) {
    for (const x of laatsteRapport.excepties.slice(0, 10)) console.error("  EXC:", x.tekst, "@", x.url, x.regel);
    for (const c of laatsteRapport.console.slice(0, 10)) console.error(`  ${c.type}:`, c.tekst);
  }
  process.exitCode = 1;
}).finally(() => process.exit(process.exitCode || 0));
