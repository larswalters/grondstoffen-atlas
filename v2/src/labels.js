// labels.js — LABELS PER ZOOMBAND voor de gloedknopen (golf 2 van de visuele
// fase, 2026-10-27, LAR-618; ontwerp: de semantische zoom van
// v2/design/lod-ontwerpbrief.md, besluit 1 en de alinea "het hiërarchische
// nodemodel blijft nodig voor labels").
//
// Waarom dit bestaat: de gloed laat zien WAAR iets gebeurt, maar niet WAT het
// is. Op wereldhoogte wil je een handvol namen (de Copperbelt, de Atacama, de
// Yangtze-delta), op continenthoogte de grote sites, regionaal elke fabriek en
// lokaal ook de kades en laadplekken van de stromen. Inzoomen levert zo NIEUWE
// INFORMATIE op, geen grotere pixels.
//
// HET MECHANISME — geen vaste lijst per band maar één regel die op elke hoogte
// hetzelfde doet:
//   1. Elke knoop is een kandidaat met een PRIORITEIT: zijn q (√(gewicht/gmax),
//      dezelfde maat als de gloed). Een stroomknoop (mijn, kade, fabriek van een
//      stroom) telt lichter dan een registersite met capaciteit, want zijn q is
//      een heuristiek en geen meting (zie stroombundel.js).
//   2. Per frame worden de kandidaten in beeld gesorteerd op prioriteit en
//      GULZIG geplaatst: een label komt er alleen als zijn tekstvak niet over een
//      al geplaatst vak valt ÉN zijn anker niet binnen `sepPx` van een al
//      geplaatst anker ligt. Die tweede regel is de semantische zoom: op
//      wereldhoogte is sepPx groot, dus een cluster (Tongling: twaalf sites op
//      een paar pixels) krijgt precies ÉÉN label — dat van zijn zwaarste lid.
//      Ingezoomd zakt sepPx en vallen de leden uiteen in eigen labels. Er is
//      geen regio-object en geen lijst "dit is de Copperbelt": het label van
//      het zwaarste lid ÍS het label van de cluster, precies zoals de hotspot
//      zelf uit de optelling ontstaat.
//   3. Het aantal labels, de ondergrens op q en sepPx lopen CONTINU met de
//      kijkhoogte (lineair in log₁₀ km tussen ankerpunten in BANDEN) — geen
//      zoomdrempel, dus geen moment waarop alles tegelijk omklapt.
//   4. Een label dat vorig frame stond krijgt een kleine bonus (HYSTERESE), zodat
//      twee bijna even zware buren niet per frame van plaats wisselen; en labels
//      vervagen in en uit (CSS-opacity) in plaats van te knipperen.
//
// WAT HET NIET IS: geen 3D-tekst in de scene. Labels zijn HTML (één div per
// zichtbaar label, uit een pool) boven het canvas, in css-px, met de lettertype-
// en kleurtokens van de HUD. Dat is scherp op elke pixelRatio, kost geen draw
// call, en de tekstmaat komt uit een echte meting (canvas measureText) in plaats
// van een gok.
//
// ⚠️ EEN STROOMKNOOP DIE OP EEN SITE LIGT KRIJGT GEEN EIGEN LABEL — dezelfde
// regel als (a) in gloed.js: binnen `samenvalKm` van een site (of van een
// eerdere stroomknoop) gaat hij op in dat label. Anders stond "Jinguan" naast
// "Tongling Nonferrous — kade" op dezelfde pixel. Een samengevallen label brandt
// zolang één lid aan staat (de aan/uit per stroom en per grondstof werkt dus
// gewoon door). Via-punten van een corridorkeuze ("via-punt corridorkeuze") zijn
// geen plek om te benoemen en doen niet mee.
//
// ⚠️ DE NAAM IS DE KORTE VORM. Registersites heten vaak "Sabine Pass LNG
// Terminal (Cheniere)" en stroomknopen "dia-orapa-mine — Orapa-mijn, Debswana
// (hoofdput + fabriek) — mijn, vertrekpunt, bron-gelegd": een id, de naam, een
// adres en de rol. Op de bol hoort alleen de naam: alles vóór het eerste
// " — " na een eventueel id, en vóór " (" of ", ". De volledige naam blijft in
// de data en in `title` van het label.

const AARDSTRAAL_KM = 6371;
const D2R = Math.PI / 180;
const CJK = /[㐀-鿿]/;

/** Ankerpunten van de banden, van hoog naar laag. Tussen twee ankers wordt
 *  lineair in log₁₀(km) geïnterpoleerd. Richtwaarden uit de ontwerpbrief
 *  (>20.000 wereld · 3.000–20.000 continent · 300–3.000 regionaal · <300
 *  lokaal) — de getallen zijn in de lokale atlas afgestemd, zie de bak-noot
 *  in memory/session-summaries.md. */
export const BANDEN = [
  //  km      max  minQ  sepPx  knoopMinQ
  [22000,     7,  0.55,  120,   9],   // wereld: één naam per werelddeel-cluster
  [6000,     11,  0.42,   95,   9],   // continent: de grote sites
  [1500,     18,  0.26,   64,   9],   // regionaal, grof
  [300,      30,  0.06,   40,   0.5], // regionaal, fijn: + de uiteinden van stromen
  [40,       48,  0,      24,   0.25],// lokaal: elke site, + overslagpunten
  [1,        64,  0,      16,   0],   // ultra-lokaal: alles wat er staat
];

export const AFSTEMMING = {
  /** stroomknoop-prioriteit = q × knoopFactor (heuristiek, geen meting) */
  knoopFactor: 0.6,
  /** bonus op de prioriteit van een label dat vorig frame stond */
  hysterese: 0.15,
  /** een stroomknoop binnen deze afstand van een site of eerdere knoop gaat op in dat label */
  samenvalKm: 1.0,
  /** marge tussen twee tekstvakken, css-px */
  vakMarge: 3,
  /** twee labels met DEZELFDE naam (de site "Rotterdam" en de kade "Rotterdam"
   *  van een stroom, 92 px uiteen op 300 km) staan niet binnen deze afstand allebei */
  naamSepPx: 220,
  /** afstand van het anker tot de linkerrand van de tekst, css-px */
  offsetPx: 10,
  /** op een telefoon: minder labels (het scherm is kleiner, de letters niet) */
  telefoonFactor: 0.7,
  /** hoe lang een uitgedoofd label zijn div vasthoudt (de CSS-fade), ms */
  fadeMs: 260,
  /** maximale lengte van de korte naam, tekens */
  maxTekens: 30,
};

/** De korte naam voor op de bol. */
export function kortNaam(naam, soort) {
  let n = String(naam || "").trim();
  if (soort === "knoop") n = n.replace(/^[a-z]{1,4}-[a-z0-9-]+\s+—\s+/i, "");   // id-prefix "dia-orapa-mine — "
  n = n.split(" — ")[0];
  n = n.replace(/\s*\(.*$/, "");          // "(Cheniere)", "(hoofdput + fabriek)"
  n = n.replace(/,\s.*$/, "");             // ", Debswana" — adres en operator
  // Chinese registernamen dragen de rechtsvorm in de naam (有限公司, 分公司 …);
  // dat is geen plaatsnaam. De gedeelde concernprefix (铜陵有色金属集团…) gaat
  // er in bouwLabels() af, want die is pas te zien naast de buren.
  if (CJK.test(n)) n = n.replace(/(股份有限公司|有限责任公司|有限公司|集团公司|分公司|公司)/g, "");
  n = n.trim();
  if (n.length > AFSTEMMING.maxTekens) n = n.slice(0, AFSTEMMING.maxTekens - 1).replace(/\s+\S*$/, "") + "…";
  return n;
}

function hexCss(hex) {
  return "#" + (hex >>> 0).toString(16).padStart(6, "0").slice(-6);
}

function opBol(lonDeg, latDeg, r) {
  const lat = latDeg * D2R, lon = lonDeg * D2R;
  const c = Math.cos(lat);
  return [r * c * Math.cos(lon), r * Math.sin(lat), -r * c * Math.sin(lon)];
}

function kmTussen(lon1, lat1, lon2, lat2) {
  const dLat = (lat2 - lat1) * D2R, dLon = (lon2 - lon1) * D2R;
  const a = Math.sin(dLat / 2) ** 2 + Math.cos(lat1 * D2R) * Math.cos(lat2 * D2R) * Math.sin(dLon / 2) ** 2;
  return 2 * AARDSTRAAL_KM * Math.asin(Math.min(1, Math.sqrt(a)));
}

/** Bandwaarden op een kijkhoogte: lineair in log₁₀(km) tussen de ankers. */
export function bandOp(hoogteKm) {
  const x = Math.log10(Math.max(1, hoogteKm));
  const B = BANDEN;
  if (x >= Math.log10(B[0][0])) return B[0].slice(1);
  if (x <= Math.log10(B[B.length - 1][0])) return B[B.length - 1].slice(1);
  for (let i = 0; i < B.length - 1; i++) {
    const x0 = Math.log10(B[i][0]), x1 = Math.log10(B[i + 1][0]);
    if (x <= x0 && x >= x1) {
      const t = (x0 - x) / (x0 - x1);
      return B[i].slice(1).map((v, k) => v + (B[i + 1][k + 1] - v) * t);
    }
  }
  return B[B.length - 1].slice(1);
}

/**
 * @param opts.mount      het HTML-element boven het canvas (position: absolute, inset 0)
 * @param opts.knopen     dezelfde lijst als bouwGloed krijgt, met `naam` en `soort`
 *                        ("site" | "knoop") erbij; `q`, `kleur`, `lon`, `lat`
 * @param opts.radius     bolstraal in scene-eenheden
 * @param opts.camera     THREE.PerspectiveCamera (staat vast; de bol draait)
 * @param opts.globeGroup de draaiende groep (zijn `matrix` wordt per frame gelezen)
 * @param opts.telefoon   minder labels op een klein scherm
 * @param opts.vermijd    HTML-elementen waar geen label onder mag vallen (de HUD,
 *                        de zoomknoppen, de bronvermelding); per frame gemeten
 */
export function bouwLabels(opts) {
  const { mount, knopen, radius, camera, globeGroup } = opts;
  const telefoon = !!opts.telefoon;
  const vermijd = (opts.vermijd || []).filter(Boolean);
  const n = knopen.length;
  const A = AFSTEMMING;

  // ── samenvallen: invoerknoop i → label p ────────────────────────────────
  // Sites eerst (elk een eigen label), dan de stroomknopen: binnen samenvalKm
  // van een site of een eerdere stroomknoop → lid van dat label.
  const lidVan = new Int32Array(n).fill(-1);
  const labels = [];                      // {lon, lat, naam, vol, kleur, q, soort, leden:[i], xyz}
  const sitesVolgorde = [];
  for (let i = 0; i < n; i++) if (knopen[i].soort !== "knoop") sitesVolgorde.push(i);
  for (const i of sitesVolgorde) {
    const k = knopen[i];
    lidVan[i] = labels.length;
    labels.push({ lon: k.lon, lat: k.lat, naam: kortNaam(k.naam, "site"), vol: k.naam || "", kleur: k.kleur,
                  q: Math.max(0, Math.min(1, +k.q || 0)), soort: "site", leden: [i] });
  }
  const nSites = labels.length;
  for (let i = 0; i < n; i++) {
    const k = knopen[i];
    if (k.soort !== "knoop") continue;
    const naam = String(k.naam || "");
    if (/via-punt/i.test(naam)) { lidVan[i] = -1; continue; }   // geen plek om te benoemen
    // dichtstbijzijnde bestaand label binnen samenvalKm (sites én eerdere knopen)
    let beste = -1, besteKm = A.samenvalKm;
    for (let p = 0; p < labels.length; p++) {
      const L = labels[p];
      if (Math.abs(L.lat - k.lat) > 0.02 || Math.abs(L.lon - k.lon) > 0.03) continue;
      const d = kmTussen(L.lon, L.lat, k.lon, k.lat);
      if (d < besteKm) { besteKm = d; beste = p; }
    }
    if (beste >= 0) {
      lidVan[i] = beste;
      labels[beste].leden.push(i);
      // een site houdt zijn eigen naam en q; een knoop-label neemt de hoogste q
      if (labels[beste].soort === "knoop") labels[beste].q = Math.max(labels[beste].q, (+k.q || 0) * A.knoopFactor);
      continue;
    }
    lidVan[i] = labels.length;
    labels.push({ lon: k.lon, lat: k.lat, naam: kortNaam(naam, "knoop"), vol: naam, kleur: k.kleur,
                  q: Math.max(0, Math.min(1, (+k.q || 0) * A.knoopFactor)), soort: "knoop", leden: [i] });
  }
  // Chinese registernamen delen vaak de concernprefix (铜陵有色金属集团 + 金冠铜业 /
  // 铜冠冶化 / 动力厂): naast elkaar op de bol is alleen het verschil informatie.
  // Een prefix van ≥ 4 tekens die een ANDER label ook draagt gaat eraf, zolang
  // er ≥ 2 tekens overblijven ("铜陵有色" zelf blijft dus staan).
  {
    const cjk = [];
    for (let p = 0; p < labels.length; p++) if (CJK.test(labels[p].naam)) cjk.push(p);
    const ruw = cjk.map((p) => labels[p].naam);
    for (let a = 0; a < cjk.length; a++) {
      let beste = 0;
      for (let b = 0; b < cjk.length; b++) {
        if (a === b) continue;
        let k = 0;
        while (k < ruw[a].length && k < ruw[b].length && ruw[a][k] === ruw[b][k]) k++;
        if (k > beste) beste = k;
      }
      if (beste >= 4 && ruw[a].length - beste >= 2) labels[cjk[a]].naam = ruw[a].slice(beste);
    }
  }
  const m = labels.length;
  const pos = new Float32Array(m * 3);
  for (let p = 0; p < m; p++) {
    const [x, y, z] = opBol(labels[p].lon, labels[p].lat, radius);
    pos[p * 3] = x; pos[p * 3 + 1] = y; pos[p * 3 + 2] = z;
  }

  // ── aan/uit per invoerknoop → per label ─────────────────────────────────
  const aanI = new Uint8Array(n).fill(1);
  const aanP = new Uint8Array(m).fill(1);
  function herleidAan(p) {
    let a = 0;
    for (const i of labels[p].leden) if (aanI[i]) { a = 1; break; }
    aanP[p] = a;
  }
  function zetAan(i, waarde) {
    if (i < 0 || i >= n) return;
    const v = waarde ? 1 : 0;
    if (aanI[i] === v) return;
    aanI[i] = v;
    if (lidVan[i] >= 0) herleidAan(lidVan[i]);
  }

  // ── tekstmaat, één keer per label ───────────────────────────────────────
  const meetCanvas = document.createElement("canvas");
  const ctx = meetCanvas.getContext("2d");
  // Hetzelfde lettertype als #labelLaag in style.css — uit de losse
  // eigenschappen, want de `font`-shorthand komt niet uit elke browser terug.
  const cs = getComputedStyle(mount);
  ctx.font = `${cs.fontWeight || 400} ${cs.fontSize || "11px"} ${cs.fontFamily || "system-ui, sans-serif"}`;
  const breedte = new Float32Array(m);
  const HOOGTE = 18;                      // tekstvak-hoogte in css-px (regel + padding)
  for (let p = 0; p < m; p++) breedte[p] = Math.ceil(ctx.measureText(labels[p].naam).width) + 12;

  // ── de pool van divs ────────────────────────────────────────────────────
  const divVan = new Int32Array(m).fill(-1);       // label → pool-index
  const pool = [];                                 // {el, label, vrijOp}
  let atlasKleur = true;
  function neemDiv(p) {
    let idx = -1;
    const nu = performance.now();
    for (let j = 0; j < pool.length; j++) if (pool[j].label < 0 && pool[j].vrijOp <= nu) { idx = j; break; }
    if (idx < 0) {
      const el = document.createElement("div");
      el.className = "lbl";
      mount.appendChild(el);
      pool.push({ el, label: -1, vrijOp: 0 });
      idx = pool.length - 1;
    }
    const d = pool[idx];
    d.label = p; divVan[p] = idx;
    const L = labels[p];
    d.el.textContent = L.naam;
    d.el.title = L.vol;
    d.el.dataset.soort = L.soort;
    d.el.style.color = atlasKleur ? hexCss(L.kleur) : "";
    return d;
  }
  function laatDiv(p) {
    const idx = divVan[p];
    if (idx < 0) return;
    const d = pool[idx];
    d.el.classList.remove("is-zichtbaar");
    d.label = -1; d.vrijOp = performance.now() + A.fadeMs;
    divVan[p] = -1;
  }

  // ── per frame ───────────────────────────────────────────────────────────
  const getoond = new Uint8Array(m);              // vorig frame
  const kand = [];                                // indices van kandidaten in beeld
  const sx = new Float32Array(m), sy = new Float32Array(m), prio = new Float32Array(m);
  const geplaatstVak = [];                        // [x0,y0,x1,y1]
  const geplaatstAnker = [];                      // [x,y]
  const geplaatstNaam = [];                       // de korte naam, voor de naam-dedupe
  let zichtbaar = true;
  let nGetoond = 0;
  const v = { x: 0, y: 0, z: 0 };
  const M = new Float64Array(16);
  const VP = new Float64Array(16);

  function update(camLocaal, scherm, hoogteKm) {
    if (!zichtbaar || !scherm || !(scherm.breedte > 0) || !(scherm.hoogte > 0)) { if (nGetoond) wisAlles(); return; }
    const W = scherm.breedte, H = scherm.hoogte;
    const d = camLocaal.length();
    if (d <= radius) return;
    const horizon = radius / d;
    const rx = camLocaal.x / d, ry = camLocaal.y / d, rz = camLocaal.z / d;

    // view-projectie × de groepsmatrix, één keer per frame (de bol draait, de camera staat vast)
    const g = globeGroup.matrix.elements, pv = camera.projectionMatrix.elements, vw = camera.matrixWorldInverse.elements;
    // VP = P × V
    for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) {
      VP[c * 4 + r] = pv[r] * vw[c * 4] + pv[4 + r] * vw[c * 4 + 1] + pv[8 + r] * vw[c * 4 + 2] + pv[12 + r] * vw[c * 4 + 3];
    }
    // M = VP × G
    for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) {
      M[c * 4 + r] = VP[r] * g[c * 4] + VP[4 + r] * g[c * 4 + 1] + VP[8 + r] * g[c * 4 + 2] + VP[12 + r] * g[c * 4 + 3];
    }

    const [maxRuw, minQ, sepPx, knoopMinQ] = bandOp(hoogteKm);
    // minder labels op een klein scherm — het scherm is kleiner, de letters niet
    const schermFactor = Math.min(1, (W * H) / (1200 * 800));
    const max = Math.max(3, Math.round(maxRuw * (telefoon ? A.telefoonFactor : 1) * Math.max(0.45, schermFactor)));

    kand.length = 0;
    for (let p = 0; p < m; p++) {
      if (!aanP[p]) continue;
      const L = labels[p];
      const drempel = L.soort === "knoop" ? knoopMinQ : minQ;
      const pr = L.q + (getoond[p] ? A.hysterese : 0);
      if (L.q < drempel && !(getoond[p] && L.q + A.hysterese >= drempel)) continue;
      const o = p * 3, px = pos[o], py = pos[o + 1], pz = pos[o + 2];
      if ((px * rx + py * ry + pz * rz) / radius <= horizon) continue;     // achter de bolrand
      const cx = M[0] * px + M[4] * py + M[8] * pz + M[12];
      const cy = M[1] * px + M[5] * py + M[9] * pz + M[13];
      const cw = M[3] * px + M[7] * py + M[11] * pz + M[15];
      if (cw <= 0) continue;
      const nx = cx / cw, ny = cy / cw;
      if (nx < -1.05 || nx > 1.05 || ny < -1.05 || ny > 1.05) continue;
      sx[p] = (nx + 1) * 0.5 * W;
      sy[p] = (1 - ny) * 0.5 * H;
      prio[p] = pr;
      kand.push(p);
    }
    kand.sort((a, b) => prio[b] - prio[a]);

    geplaatstVak.length = 0; geplaatstAnker.length = 0; geplaatstNaam.length = 0;
    // De HUD, de zoomknoppen en de bronvermelding zijn bezet gebied: als vak
    // vooraf "geplaatst", dan houdt de gewone overlaptoets ze vrij.
    if (vermijd.length) {
      const mr = mount.getBoundingClientRect();
      for (const el of vermijd) {
        if (el.hidden || el.offsetParent === null) continue;
        const r = el.getBoundingClientRect();
        if (r.width > 0 && r.height > 0) geplaatstVak.push([r.left - mr.left, r.top - mr.top, r.right - mr.left, r.bottom - mr.top]);
      }
    }
    const nieuw = new Uint8Array(m);
    let geteld = 0;
    const marge = A.vakMarge;
    for (const p of kand) {
      if (geteld >= max) break;
      const x = sx[p], y = sy[p];
      let botst = false;
      const naam = labels[p].naam;
      for (let k = 0; k < geplaatstAnker.length; k++) {
        const a = geplaatstAnker[k];
        const afst = Math.hypot(a[0] - x, a[1] - y);
        if (afst < sepPx || (afst < A.naamSepPx && geplaatstNaam[k] === naam)) { botst = true; break; }
      }
      if (botst) continue;
      const x0 = x + A.offsetPx, y0 = y - HOOGTE / 2, x1 = x0 + breedte[p], y1 = y0 + HOOGTE;
      if (x0 < 0 || y0 < 0 || x1 > W || y1 > H) continue;             // half buiten beeld: niet tonen
      for (let k = 0; k < geplaatstVak.length; k++) {
        const b = geplaatstVak[k];
        if (x0 < b[2] + marge && x1 > b[0] - marge && y0 < b[3] + marge && y1 > b[1] - marge) { botst = true; break; }
      }
      if (botst) continue;
      geplaatstVak.push([x0, y0, x1, y1]);
      geplaatstAnker.push([x, y]);
      geplaatstNaam.push(naam);
      nieuw[p] = 1;
      geteld++;
      const dv = divVan[p] >= 0 ? pool[divVan[p]] : neemDiv(p);
      dv.el.style.transform = `translate3d(${Math.round(x0)}px,${Math.round(y0)}px,0)`;
      if (!getoond[p]) dv.el.classList.add("is-zichtbaar");
    }
    for (let p = 0; p < m; p++) if (getoond[p] && !nieuw[p]) laatDiv(p);
    getoond.set(nieuw);
    nGetoond = geteld;
  }

  function wisAlles() {
    for (let p = 0; p < m; p++) if (getoond[p]) { laatDiv(p); getoond[p] = 0; }
    nGetoond = 0;
  }

  return {
    update, zetAan,
    /** de hele laag aan/uit (de HUD-knop) */
    zetZichtbaar(aan) { zichtbaar = !!aan; if (!zichtbaar) wisAlles(); mount.hidden = !zichtbaar; },
    /** kleur = grondstof (atlas) of de HUD-inkt (routewerk) */
    zetKleurModus(atlas) {
      atlasKleur = !!atlas;
      for (const d of pool) if (d.label >= 0) d.el.style.color = atlasKleur ? hexCss(labels[d.label].kleur) : "";
    },
    afstemming: A, banden: BANDEN,
    get stats() {
      let aan = 0;
      for (let p = 0; p < m; p++) if (aanP[p]) aan++;
      return { knopen: n, labels: m, sites: nSites, aan, getoond: nGetoond, divs: pool.length };
    },
    /** voor diagnose: de labels die nu staan, met naam en schermpositie */
    getoondLijst() {
      const uit = [];
      for (let p = 0; p < m; p++) if (getoond[p]) uit.push({ naam: labels[p].naam, soort: labels[p].soort, q: +labels[p].q.toFixed(2), x: Math.round(sx[p]), y: Math.round(sy[p]) });
      return uit;
    },
  };
}
