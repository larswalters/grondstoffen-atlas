# Project brief — Grondstoffen Atlas
*Last updated: 2026-07-14*

## Summary

Een interactieve **3D-grondstoffenatlas**: een Three.js-wereldbol waarop je per kritieke grondstof de
volledige handelsketen ziet — mijn → raffinage → fabriek → eindproduct — met de **echte** zee- en
landroutes ertussen en de **knelpunten** (Malakka, Lombok, Suez, Chinese raffinage) als kern van het
verhaal. Vanilla JS, geen bundler; gedeployed via Netlify.

## Current stable baseline

- **State:** M0–M5 compleet (M5 gemeld afgerond 2026-07-14 door de aparte CC-sessie; niet apart door mij geverifieerd).
  - M0 modulaire herbouw + satelliettextuur (4096×2048) + standalone single-file
  - M1 lithium als volledig sjabloon (34 knopen, 31 stromen); 8 overige grondstoffen op niveau "basis"
  - M2 rendering-fundament (schaal-fix, kaderloze labels + botsingsdetectie, tegellaag, autorotate uit)
  - M3 echte routes: A\* over 1440×720 land/zee-raster, knelpunten als water, LAND_LINKS, vaarbanen
  - M4 kobalt volledig uitgewerkt + scheepvaart-tijdlijn (`voyages.js` + afspeelbalk)
- **Code:** single-file `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html` (M5 hierin gedaan); modulaire
  backup in `C:\Users\lars\Desktop\globe-oud\...`. Nog niet in `Projects/`, nog geen git-repo. ⚠️ modulair-vs-single-file open.
- **Deploy:** Netlify (drag-and-drop `atlas`-map). Live-URL: door Lars beheerd (Netlify).
- **Volledig uitgewerkt:** lithium ✅, kobalt ✅. Overige 8: niveau "basis".

## Next product direction

1. **Goud** als volgende volledig uitgewerkte grondstof — ontwerp op papier klaar (`design/goud.md`);
   volgende sessie: research (coördinaten/volumes) → `data/goud.js` + air-route-modus.
2. **Nieuwe grondstofketens uitwerken** volgens het lithium-sjabloon. Roadmap noemt koper; Lars' huidige
   focus is **goud**.
3. **Brain-onboarding:** dit project inbedden in vault + Pinecone + Linear (dit is de reden dat deze
   projectmap is aangemaakt).

## Hard boundaries

- **Geen bundler/framework** introduceren — de losse-globals-opzet met vaste script-laadvolgorde is bewust.
- **Eerst ontwerpen, dan bouwen:** per grondstof eerst knopen+stromen op een rij, pas daarna code.
- UI-teksten/annotaties **Nederlandstalig**.
- Coördinaten `lat`/`lon`, west = negatief — nauwkeurig houden (routefouten komen hier vaak vandaan).
