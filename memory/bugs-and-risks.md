# Bugs & risks — Grondstoffen Atlas
*Last updated: 2026-07-14*

## M5-bugs — OPGELOST + geverifieerd (2026-07-14, aparte CC-sessie) → LAR-393/394/395/396 Done
**Aanpak 395/396** (kobaltroutes Cuba→Canada + Europa→Amerika): Straat van Dover + St. Lawrence als knelpunt
open geforceerd (zelfde patroon als Lombok/Malakka); regressiecheck 0 kapotte routes over alle stromen.
**Aanpak 393/394** (tegelnaad + drempel): shell-laag (hele bol grove tegels) + scherpe detailpatch; blue-marble
prikt nergens meer door. ⚠️ Visueel **niet met screenshot** bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.
Referentie-symptomen hieronder:
- **LAR-393 (High)** — bol toont **twee verschillende kaarten naast elkaar** bij vaste zoom: de ene helft
  tegellaag (Esri, scherp), de andere basemap-satelliettextuur, met zichtbare naad/overhang. Beeld springt
  vaak van view. Vermoedelijke oorzaak: tegellaag (`tiles.js`, z=6.2) en basemap (`basemap.js`) te
  gescheiden. (Waargenomen op mobiel, 14 juli 2026.)
- **LAR-394 (Medium)** — tegellaag (mooier dan basemap) eerder tonen: drempel `z=6.2` omhoog (~7.5–8),
  evt. standaard actief zodra bol interactief wordt. **Afweging:** eerder tegels = meer tegelverzoeken =
  zwaarder op mobiel.
- **LAR-395 (High)** — kobaltroute **Zuid-Amerika → Noord-Amerika** loopt niet plausibel (knik bij Great
  Lakes/Nova Scotia). Checken: lat/lon omgedraaid of verkeerd teken, haven aan verkeerde kust,
  raster/waypoint. Bestanden: `data/kobalt.js`, `searoute.js`.
- **LAR-396 (High)** — kobaltroute **Europa → Amerika** klopt niet. Transatlantisch is de simpelste route;
  als díé eruitziet als een omweg wijst dat op iets structureels (great-circle vs. rasterpad). Bestand:
  `data/kobalt.js`, `searoute.js`.

## Risico's / aandachtspunten
- **Coördinaatfouten** (lat/lon-swap, verkeerd teken west/oost) zijn een terugkerende bron van verkeerde
  routes. Bij elke nieuwe grondstof checken.
- **Rasterresolutie 0,25°** verliest smalle doorgangen; nieuwe knelpunten moeten expliciet in
  `_chokepoints.js` als water geforceerd worden.
- **Gewogen A\* is niet gegarandeerd optimaal** — bewust ingeruild voor "wel een route vinden". Bij vreemde
  paden eerst hier kijken.
- **Goud-specifiek risico:** goud reist grotendeels per **luchtvracht**, terwijl de hele route-engine op
  zee/land-A\* is gebouwd. Zonder ontwerpbeslissing over luchtroutes wordt een goudketen ofwel onjuist
  (alles over zee) ofwel visueel inconsistent. Los dit op vóór implementatie.
- **Mobiele performance:** tegellaag + veel stromen + voyages kunnen zwaar worden; bewaken bij uitbreiding.
- **Modulair vs single-file (open):** huidige werkende versie is single-file `atlas-lithium-kobalt.html`; modulair
  staat in `globe-oud`. Beslissen vóór goud. Risico: doorgaan in single-file = geen per-grondstof `data/<x>.js`-scheiding;
  terug naar modulair = de M5-fixes moeten worden overgezet.
- **Visuele M5-bevestiging ontbreekt** (screenshot). Bevestig op Netlify/mobiel voordat `globe-oud` definitief weg mag.

## Verholpen (referentie)
- Schaalbug (delen door camerastand i.p.v. afstand tot oppervlak) — opgelost in M2 (`scaleFor()`).
- Lange oceaanroutes vielen terug op rechte lijnen — opgelost met gewogen A\* (M3).
- Zeven Australische stromen als één dikke worm over Lombok — opgelost met vaarbanen (`laneShape`, M3).
