# Golf-scripts (M31)

Gebruikt in golf 7 (2026-10-09), zie `v2/design/bakhandleiding-licht.md` §8.

- `golf7-script.mjs` — het draaiklare workflow-script (ontwerp, toets, brief, bake, keuring; reserve-assen en ontwerpronde naast elkaar). Starten als bestand: `Workflow({scriptPath, args: {datum, model: "sonnet"}})`, in LF zonder U+FE0F. De invoer (14 grondstoffen met bestaande ketens, afwijzingen en hints) zit ingebed; `maak_golf7.py` bouwt hem uit het register en de runbestanden van eerdere golven.
- `golf7c-script.mjs` — het herstelpatroon: een grondstof opnieuw plus een herbak van ketens met een opgeslagen brief.
- `centraal_check.py` · `sitelaag_check.py` · `registreer_golf.py` (+ `noten.json`) — de centrale nameting en registratie.

- `golf8-script.mjs` · `golf9-script.mjs` — de scripts van golf 8 en 9 (met `agentR`-retries, literale slots en `wegscan_puur.py`); `maak_golf8.py` en `maak_golf9.py` bouwen ze uit het vorige script en de resultaten van de vorige golf.

- `golf10-script.mjs` — golf 10 (2026-10-28): alleen de reserve-route (brief, bake, keuring) voor de 15 getoetste reserve-assen uit golf 9, geen ontwerpronde; `maak_golf10.py` bouwt hem uit `golf9-script.mjs` + `golf10-reserves.json` (de assen en toetsen uit het golf 9-journal). Les: een reserve zonder per-keten-toets wordt in de EERSTE pijplijnstap getoetst, niet vooraf in een lus — anders wachten alle ketens op die ene agent. `golf10-resultaat.json` is de invoer voor `registreer_golf.py`.

- `golf13-script.mjs` — golf 13 (2026-10-29): opnieuw een ontwerpronde zonder reserves (de 11 reserves van golf 11 waren in golf 12 op); `maak_golf13.py` bouwt hem uit `golf11-script.mjs` + `golf11-resultaat.json` (de 19 in de toets afgewezen assen van golf 11 met reden in de prompts) en een herschreven kobalt-hint. 100 agenten op Sonnet, 24/24 gebakken, kobalt opnieuw 0 (zie `golf13-resultaat.json`, toets kobalt). De 8 reserves staan in `golf14-reserves.json` (patroon golf 12: `maak_golf12.py`).

- `golf14-script.mjs` — golf 14 (2026-10-30): vierde ontwerpronde, zonder reserves en ZONDER KOBALT (golf 11 en 13: acht van acht afgewezen; bakhandleiding §13); `maak_golf14.py` bouwt hem uit `golf13-script.mjs` + `golf13-resultaat.json` (de 24 afgewezen assen met reden) en `golf14-reserves.json` (de 8 reserves als "niet opnieuw ontwerpen" in de hint — die liggen nog klaar voor een reserve-golf). 104 agenten op Sonnet, 26/26 gebakken over 13 grondstoffen (zie `golf14-resultaat.json`). De 9 reserves staan in `golf15-reserves.json` (patroon golf 12: `maak_golf12.py`).

- `golf15-script.mjs` — golf 15 (2026-10-30): alleen de reserve-route voor de 17 reserves uit golf 13 en 14 (`golf14-reserves.json` + `golf15-reserves.json`), geen ontwerpronde; `maak_golf15.py` bouwt hem uit `golf14-script.mjs` (patroon golf 12: de 2 reserves zonder toets in de eerste pijplijnstap). 50 agenten op Sonnet, 21 min, 16/17 gebakken (grafiet-teverola-heroya in de toets afgewezen; zie `golf15-resultaat.json`). Geen reserves meer over.

- `golf16-script.mjs` — golf 16 (2026-10-30): GROTE ontwerpronde, 3 nieuwe ketens per grondstof (max 39) over 13 grondstoffen (kobalt overgeslagen), geen reserves; `maak_golf16.py` bouwt hem uit `golf14-script.mjs` + `golf14-resultaat.json` + `golf15-resultaat.json` (18 afgewezen assen met reden). 120 agenten op Sonnet, 24,9 M tokens, 127 min, 31/32 gebakken (nikkel-kouaoua-laadkade door de briefagent afgebroken: weg al twee jaar onbruikbaar); zie `golf16-resultaat.json`. De 7 reserves staan in `golf17-reserves.json` (patroon golf 15: `maak_golf15.py`).

- `golf17-script.mjs` — golf 17 (2026-10-31): tweede grote ontwerpronde, 3 per grondstof over 13 grondstoffen (kobalt overgeslagen); `maak_golf17.py` bouwt hem uit `golf16-script.mjs` + `golf16-resultaat.json` (23 afgewezen of afgebroken assen met reden) + `golf17-reserves.json` (7 reserves als niet-opnieuw-ontwerpen); nieuw in de prompts: een stroom-id bevat uitsluitend [a-z0-9-]. 117 agenten op Sonnet, 67 min, 30/31 gebakken (goud-blanket-fidelity afgebroken: goud per helikopter); zie `golf17-resultaat.json`. De 7 reserves van golf 17 staan in `golf18-reserves.json` (met die van golf 16 in `golf17-reserves.json`: 14 klaar).

- `golf18-script.mjs` — golf 18 (2026-10-31): alleen de reserve-route voor de 14 reserves uit golf 16 en 17 (`golf17-reserves.json` + `golf18-reserves.json`, alle met toets), geen ontwerpronde; `maak_golf18.py` bouwt hem uit `golf17-script.mjs` (patroon golf 15). 42 agenten op Sonnet, 6,7 M tokens, 20 min, 14/14 gebakken en gekeurd (zie `golf18-resultaat.json`). Geen reserves meer over.
