// stamp_assets.js — zet een inhouds-hash achter elke lokale asset-URL in
// index.html:  src="src/util.js"  ->  src="src/util.js?v=a1b2c3d4"
//
// Waarom: GitHub Pages serveert met `Cache-Control: max-age=600` en zonder
// versie in de URL houdt een browser die bestanden veel langer vast. Gevolg
// (2026-07-18, hele sessie): elke fix stond wél live, maar Lars kreeg steeds de
// vorige versie te zien — drie keer achter elkaar "ik zie geen verschil".
// Een hash per bestand lost dat deterministisch op: verandert de inhoud, dan
// verandert de URL en moet de browser wel opnieuw ophalen. Ongewijzigde
// bestanden houden hun hash en blijven dus gewoon gecachet.
//
// Idempotent: een bestaande ?v=... wordt vervangen.
// Draaien vóór elke commit die assets aanraakt (zie README / sectie I).
//
// Gebruik:  node tools/stamp_assets.js

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const ROOT = path.join(__dirname, "..");
const INDEX = path.join(ROOT, "index.html");

function hash(file) {
  const abs = path.join(ROOT, file);
  if (!fs.existsSync(abs)) return null;
  return crypto.createHash("sha1").update(fs.readFileSync(abs)).digest("hex").slice(0, 8);
}

let html = fs.readFileSync(INDEX, "utf8");
let stamped = 0, missing = [];

// src="..." en href="..." die lokaal zijn (geen http(s):// en geen //)
html = html.replace(/(\s(?:src|href)=")(?!https?:|\/\/|#)([^"?]+)(?:\?v=[a-f0-9]+)?(")/g,
  (m, pre, file, post) => {
    const h = hash(file);
    if (!h) { missing.push(file); return m; }
    stamped++;
    return `${pre}${file}?v=${h}${post}`;
  });

fs.writeFileSync(INDEX, html);
console.log(`${stamped} assets gestempeld in index.html`);
if (missing.length) {
  console.error(`  ! niet gevonden (ongestempeld): ${missing.join(", ")}`);
  process.exit(1);
}
