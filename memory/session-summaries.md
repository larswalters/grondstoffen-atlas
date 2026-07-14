# Session summaries — Grondstoffen Atlas
*Newest first.*

## 2026-07-14 (addendum) — M5 bevestigd + single-file-situatie ontdekt
- **M5 af + geverifieerd** door de aparte CC-sessie: LAR-393/394/395/396 → Done, milestone 100%.
  Aanpak: Dover + St. Lawrence als knelpunt open geforceerd (kobaltroutes Cuba→Canada + Europa→Amerika);
  shell-laag + detailpatch (tegelnaad/blue-marble-doorprik). Regressie 0 kapotte routes. Visueel niet met
  screenshot bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.
- **Ontdekt bij het checken van het bureaublad:** de code is **niet meer modulair** — de huidige werkende versie
  is de single-file `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html`. De modulaire opzet staat als backup
  in `globe-oud\grondstoffen-atlas-v2\atlas\`. → nieuwe open beslissing **modulair vs single-file** (vóór goud),
  en `globe-oud` mag pas weg na visuele bevestiging. Projectmemory + vault gecorrigeerd (locatie was fout).

## 2026-07-14 — Brain-scaffold opgezet + goud verkend
- **Context:** Lars werkte de atlas eerder als losse bureaublad-map + Claude-project. Besloten dat het
  bestaande systeem (vault + Pinecone + Linear) sterker is; project moet daarin ingebed worden.
- **Gedaan (deze sessie, Claude Code):**
  - Linear-project "Grondstoffen Atlas" (LAR, LAR-378 t/m LAR-396) doorgenomen; M0–M4 done, M5 open.
  - **Projectmap-scaffold** aangemaakt: `C:\automation\Projects\General\grondstoffen-atlas\` met
    folder-`CLAUDE.md` (A–H) + `memory/` (de 6 standaardfiles), gevuld met de stand uit Linear.
  - Code en vault **bewust niet aangeraakt**: aparte CC-sessie maakt M5 af; vault-onboarding + git-init
    + goud-werk komen daarná.
- **Belangrijkste inzicht voor goud:** goud past niet 1-op-1 op het lithium/kobalt-verhaal. Geen Chinese-
  raffinage-monopolie; het verhaal draait om mijnbouw wereldwijd → raffinage (o.a. Zwitserland) → LBMA/
  Londen + COMEX/Shanghai als handels-/kluiscentra → centrale banken + juwelen. En: goud reist vooral per
  **luchtvracht**, wat botst met de zee/land-route-engine. **Eerste goud-beslissing = hoe luchtroutes weer te geven.**
- **Status einde sessie:** scaffold klaar; wachten op afronding M5 door de andere sessie, dan onboarden
  in vault/Pinecone en goud oppakken (ontwerp eerst, dan `data/goud.js`).
- **Niet gedaan / bewust uitgesteld:** git init, code-migratie, vault-wiki-pagina, Pinecone-gist — allemaal
  na M5 (zie `next-actions.md`).
