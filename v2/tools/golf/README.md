# Golf-scripts (M31)

Gebruikt in golf 7 (2026-10-09), zie `v2/design/bakhandleiding-licht.md` §8.

- `golf7-script.mjs` — het draaiklare workflow-script (ontwerp, toets, brief, bake, keuring; reserve-assen en ontwerpronde naast elkaar). Starten als bestand: `Workflow({scriptPath, args: {datum, model: "sonnet"}})`, in LF zonder U+FE0F. De invoer (14 grondstoffen met bestaande ketens, afwijzingen en hints) zit ingebed; `maak_golf7.py` bouwt hem uit het register en de runbestanden van eerdere golven.
- `golf7c-script.mjs` — het herstelpatroon: een grondstof opnieuw plus een herbak van ketens met een opgeslagen brief.
- `centraal_check.py` · `sitelaag_check.py` · `registreer_golf.py` (+ `noten.json`) — de centrale nameting en registratie.

- `golf8-script.mjs` · `golf9-script.mjs` — de scripts van golf 8 en 9 (met `agentR`-retries, literale slots en `wegscan_puur.py`); `maak_golf8.py` en `maak_golf9.py` bouwen ze uit het vorige script en de resultaten van de vorige golf.
