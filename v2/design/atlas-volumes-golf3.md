# Visuele fase · golf 3 — hoeveelheden bij de stromen (LAR-642, 2026-10-29)

**Wens Lars (2026-10-29):** *"daarna zou ik iets met hoeveelheden ± bij de stromen willen kunnen zien zoals bij v1 was."*
v1 deed (`src/flows.js`, `src/ui.js`, `index.html`): lijndikte = relatief volume t.o.v. de grootste stroom van die grondstof
(wortel), deeltjes ∝ relatief volume, tooltip "volume ≈ X eenheid", legenda "dikte = volume". Dit is besluit 4 van
`lod-ontwerpbrief.md` ("dikte flow = volume") en de golf 3-kandidaat uit `atlas-product-golf1.md` §13.

## 1 · Waar de cijfers vandaan komen — en wat "±" betekent

- **Bron = de routebrieven.** Per grondstof las een leesagent alle brieven en noteerde per stroom het jaarvolume van de
  lading over DÉZE route: `v2/design/volumes/<grondstof>.json` (tekst = citaat, waarde, eenheid, per, productvorm,
  peiljaar, bron, status, toelichting). Een regex over de brieven is bewust geen bron: hij pakte fabriekscapaciteiten
  (Kibali "7,2 Mt/j" is de ertsfabriek, niet het goud).
- **Drie statussen, eerlijk in de HUD:** `bron` (de brief geeft het stroomvolume met bron, 64 stromen) · `indicatie`
  (mijn-/fabriekstotaal, capaciteit, natte vinger, v1-checklist, of een volume van nul terwijl de weg bestaat — 252) ·
  `onbekend` (niets bruikbaars — de bol tekent de dunste lijn, de HUD zegt "volume onbekend"). Dat is de "±": de dikte is
  relatief en indicatief, de tekst is de waarheid, en de toelichting zegt wat het cijfer wél is.
- **Los metadatabestand, geen herbak** (besluit 2026-08-06): `v2/tools/maak_stroomvolumes.py` → `v2/data/stroomvolumes.json`
  (+ `stroomvolumes-handmatig.json` voor correcties, die winnen). Een nieuwe golf = een leesagent over de nieuwe brieven
  en het script opnieuw; het verslag noemt stromen die in geen bronlijst staan.

## 2 · Normalisatie — alleen voor de dikte, nooit voor de tekst

Per grondstof één basis-eenheid (koper/nikkel/kobalt/lithium/grafiet/ree kt · goud/zilver/pgm/uranium t · kolen/olie Mt ·
gas bcm · diamant Mct). Eenduidige omrekeningen wél (Mt → kt, koz/Moz → t, kb/d → Mt/j bij 7,3 vaten/t, Mtpa LNG → bcm
bij 1,36, Mlb U3O8 → tU, PJ → bcm, mln m3/d → bcm); product ≠ metaal (erts, concentraat, matte, MHP) NIET — de dikte is
indicatief. `rel` = positie op een log-schaal tussen het 15e en 90e percentiel van de grondstof (0..1, robuust tegen
uitschieters zoals één Alrosa-totaal of één leidingcapaciteit).

## 3 · Wat de bol ermee doet

| element | regel | waar |
|---|---|---|
| lijndikte | breedtefactor = 0,65 + (2,1 − 0,65)·√rel; onbekend = 0,65 (de dunste, zoals v1 `value \|\| 1`); alle benen van één stroom delen de factor, de stijl per modaliteit blijft de basis | `stroombundel.js` `AFSTEMMING_VOLUME` → `BeenInfo.zetBreedteF` (kanaal B van de informatietextuur, de haak uit golf 1) |
| kometen | per been 1–3 (desktop) of 1–2 (telefoon) = min + round(√rel·(max − min)); onbekend = min | `stroomkometen.js` `AFSTEMMING.kometenMin/Max…`, slots per drager i.p.v. een vaste K |
| HUD | onder elke stroomknop "≈ 411 kt Cu/j" (of "volume onbekend", dimmer en cursief); tooltip = het citaat + (indicatie) + productvorm | `main.js` `toonVolumes()`, `.srVol` in `style.css` |
| legenda | "dikte = hoeveelheid" in de kopregel; legNoot "dikte en aantal kometen = jaarvolume (± relatief per grondstof; dunste lijn = onbekend)" | `index.html`, `main.js` |
| bundel | `stromen.json` per stroom `volume {kort, tekst, status, productvorm, rel}`; `stroomvolumes.json` in `bron` → `bundel-check` ziet drift; `totalen.metVolume` | `bak_stroombundel.py` |

Geen shaderwijziging, geen nieuw verzoek (het volume reist mee in `stromen.json`), geen herbak van stromen.

## 4 · Gemeten (2026-10-29, `?v=143`)

352 stromen · 304 met dikte (36 onbekend, 12 met een tekst maar zonder omrekenbare eenheid) · desktop 1.905 kometen (K 1–3),
telefoon 1.465 (K 1–2) · 0 consolefouten · 375 px zonder horizontale scroll. Telefoontest Lars = de poort.

## 5 · Open

- De 36 onbekenden (o.a. koper-escondida-guixi, koper-collahuasi-tongling, koper-lobito-duisburg, vijf ree-, vijf zilver-,
  drie uranium-stromen): alleen te vullen met nieuw bronwerk, niet met een schatting.
- Grafiet: 14 stromen met volume 0 (project-assen) — de dunste lijn is daar het eerlijke beeld.
- Mengeenheden binnen één grondstof (kt LCE naast kt SC6, kt Ni naast Mt erts): de log-schaal dempt het, maar de
  toelichting in `stroomvolumes.json` blijft de plek om het na te lezen.
- Een klik op een lijn met het volume erbij (v1 had dat): de bundel heeft geen picking; labels per zoomband zouden het
  cijfer kunnen dragen als Lars dat wil.
