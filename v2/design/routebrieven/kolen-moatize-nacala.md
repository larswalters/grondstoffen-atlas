# Routebrief (licht) · kolen — Moatize (Tete) → Nacala-a-Velha (Mozambique, via Malawi)

**stroom-id:** `kolen-moatize-nacala` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** cokeskool/thermische kolen van de Moatize-mijn (Vulcan Mozambique SA, ex-Vale)
gaat per **spoor** over de Nacala Logistics Corridor — dwars door Malawi (Nkaya, Sena-spoorkruising)
en terug Mozambique in (Nayuchi, Cuamba) — naar de Nacala-a-Velha-kolenterminal (Vale-infrastructuur,
westoever Baai van Nacala), de eerste Afrikaanse kolenas op de bol. Geen zeebeen: geen bron noemt een
specifieke koper op ladingniveau, dus de brief stopt bewust bij de kade.
**Welke as van het verhaal:** Mozambique — het "grootste geïntegreerde pit-to-port cokeskoolbedrijf
ter wereld" volgens eigen opgave, 16,3 Mt (2024, gerealiseerd) → 19 Mt (2025, prognose), ROM-capaciteit
>42 Mt/j [4][web]; Vulcan zelf meldt de verscheping van mijn tot haven over "nearly 1.000 kilometers"
spoor [web].

## 1 · Ketenkaart
```
Moatize-mijn `kolen-moatize-mijn` (Tete, Vulcan Mozambique SA)
  ──(b1 spoor · Nacala Logistics Corridor via Nkaya-Moatize-tak (Vale, 2017) + de Nacala-hoofdlijn
      via Malawi (Mwanza-grens → Nkaya-splitsing → Nayuchi-grens → Cuamba → Monapo) · 912–931 km)──►
Nacala-a-Velha kolenterminal `kolen-nacala-velha-terminal` (Vale-infrastructuur, westoever Baai van
Nacala, kolenkade sinds jan. 2016) ── STOPPUNT
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-moatize-mijn` → `kolen-nacala-velha-terminal` | Nacala Logistics Corridor: Moatize → Mwanza (grens MZ/MW) → Nkaya (Malawi, splitsing met de Sena-lijn naar Beira/Chipata) → Nayuchi (grens MW/MZ) → Cuamba (splitsing met de Cuamba–Lichinga-tak) → Monapo (splitsing met de Lumbo-tak) → Nacala-a-Velha-tak | 912 [4][web] tot 931 [3] — twee licht uiteenlopende gepubliceerde lengtes voor dezelfde corridor, als bandbreedte | toets_spoorroute (`BAKE_SUFFIX=-raw`; extracts `mozambique` + `malawi`, beide in raw1op1; corridorkeuze op elke via-punt hieronder, meerdere runs kop→via→via→staart) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-moatize-mijn` | mijn / laadplek | Moatize-mijn (Vulcan Mozambique SA, ex-Vale, verkocht dec. 2021), open-pit-complex Tete | -16.1537, 33.7207 | [6][sat] | bron-gelegd (z15 gezien: open-pit-excavaties met haldes, toegangswegen en een waterbekken direct ten noorden van het punt — het punt zelf ligt op de toegangsweg binnen het mijnconcessiegebied, ~0,4 km van de dichtstbijzijnde zichtbare put; GEM geeft deze coördinaat zelf als "exact") |
| `kolen-nacala-velha-terminal` | overslag / losplek (stoppunt) | Nacala-a-Velha kolenterminal (Vale/CLIN-infrastructuur, westoever Baai van Nacala, in bedrijf sinds jan. 2016) | -14.533, 40.624 | [1][3][grafiet-brief] | **hergebruikt, letterlijk** uit `v2/design/routebrieven/grafiet-balama-vidalia.md` (regel 235, daar expliciet als NEGATIEF anker "hoort NIET bij de grafietstroom" — de grafietketen gebruikt de containerkade oostoever, deze kolenketen juist wél deze westoever-kolenkade; Nominatim-reverse op deze coördinaat gaf "Nacala Coal Terminal, Nacala-a-Velha" terug, dus het hergebruik is bevestigd) |

## 4 · Via-punten (b1 — vijf corridorkeuzes: twee landsgrenzen + drie sporen splitsingen)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Mwanza (Malawi, spoorstation/grensplaats) | -15.6092, 34.5234 | grensovergang Mozambique→Malawi op de Nacala-lijn (tussen Cana-Cana/Moatize-zijde en de Malawische kant); sluit een andere grensroute uit |
| b1 | 2 | Nkaya (Malawi, spoorwegknooppunt) | -15.1173, 35.0230 | splitsing met de Sena-spoorlijn (west naar Mchinji/Chipata, Zambia); de kolenroute gaat hier NIET die tak op maar blijft op de Nacala-lijn richting Nayuchi/Cuamba |
| b1 | 3 | Nayuchi (Malawi, grensstation) | -14.9793, 35.8731 | grensovergang Malawi→Mozambique terug, exacte OSM-spoorstation-node |
| b1 | 4 | Cuamba (Mozambique, spoorwegknooppunt) | -14.8033, 36.5358 | splitsing met de Cuamba–Lichinga-tak (262 km); de kolenroute gaat hier NIET die tak op maar blijft op de hoofdlijn richting Nampula/Monapo |
| b1 | 5 | Monapo (Mozambique, spoorwegknooppunt) | -14.9155, 40.2972 | splitsing met de Lumbo-tak (naar Monapo-Lumbo) en het punt waar de Nacala-a-Velha-tak (via Andre Mossuril) van de hoofdlijn aftakt naar de kolenkade |

## 5 · Verwerkingsknopen
Geen — de brief stopt bij de laadkade; er is geen verwerkingsstap tussen mijn en exportterminal
(kolen gaat ongewassen/gewassen bij de mijn direct de trein op, geen tussenliggende knoop gebrond).

## 6 · Stoppunt
De brief stopt hard bij de Nacala-a-Velha-kolenterminal: dat is het bewezen einde van de spoorkorrel
(exportterminal, in bedrijf sinds januari 2016, gebouwd door Vale specifiek voor Moatize-kolen [3]).
Geen bron noemt een specifieke koper of bestemmingshaven op ladingniveau — de Jindal-eigenaarschapshint
(Vulcan International, voorgezeten door Naveen Jindal, met een mogelijke band naar JSPL's Indiase
staalfabrieken) is een opvallende aanwijzing maar **niet bevestigd op ladingniveau** [5], dus er wordt
bewust geen zeebeen getekend. Fase D/E vervallen.

## 7 · Open punten
- **Geen ladingniveau-bron voor een specifieke koper.** Vulcan International (moederbedrijf) wordt
  mede voorgezeten door Naveen Jindal (Jindal Steel & Power); een apart, ANDER Jindal-bedrijf (JSW
  Steel, Sajjan Jindal, Naveens broer) ontwikkelt een NIEUW, ongerelateerd project (Minas de Revuboè,
  ~2,4 Mt/j eerste fase) op een aangrenzende maar andere concessie — bevestigd via [5]: die twee
  projecten worden in de bron expliciet los van elkaar behandeld. Geen van beide levert een
  ladingniveau-koppeling voor déze kolenstroom.
- **Twee licht uiteenlopende gepubliceerde spoorlengtes** (912 km [4] vs 931 km [3]) voor dezelfde
  corridor — als bandbreedte gebruikt, geen aparte meting binnen het webbudget.
- **Via-punten zijn corridor-stations, niet zelf OSM-wegvertex/spoorvertex-geverifieerd** binnen het
  webbudget — de bak-agent routeert over het 1-op-1-spoornet, dus de exacte ligging volgt uit die
  routering; de coördinaten komen uit OSM `railway=station`-nodes (Nkaya, Nayuchi, Cuamba) resp.
  OSM-plaatsnodes (Mwanza, Monapo).
- **`kolen-moatize-mijn` ligt op de toegangsweg van het mijnconcessiegebied**, niet exact op de
  laadlus/het spoorpunt zelf — GEM noemt de coördinaat "exact" en het punt ligt satelliet-bevestigd
  binnen het mijnterrein; het precieze laadpunt (spoorkop van de Nkaya-Moatize-tak) kan bij het
  bakken een paar honderd meter afwijken.
- **Grensspoor-status ongewijzigd sinds 2017** (Nkaya-Moatize-tak door Vale/CLIN gebouwd, voltooid
  2017) — geen aanwijzing gevonden dat de lijn sindsdien is uitgebreid of verlegd.

## 8 · Bronnen
[1] Wikipedia, "Nacala railway" — 912 km, hoofdstations incl. Nkaya/Nayuchi/Cuamba/Monapo, Nacala-a-Velha-tak, Nkaya-Moatize-uitbreiding door Vale voltooid 2017. https://en.wikipedia.org/wiki/Nacala_railway
[2] Wikipedia, "Sena railway" — Nkaya als kruispunt met de Nacala-lijn; Dona Ana–Moatize-tak (1949, andere corridor, niet gebruikt door deze keten). https://en.wikipedia.org/wiki/Sena_railway
[3] Wikipedia, "Port of Nacala" — 931 km, kolenterminal Nacala-a-Velha voltooid januari 2016 voor export van Moatize-kolen, corridorbeschrijving Cuamba→Nayuchi→Malawi→Nkaya→Moatize. https://en.wikipedia.org/wiki/Port_of_Nacala
[4] Ecofin Agency, "Mozambique's Largest Coal Mine Begins $155 Million Shift Away From Diesel" (2026-07-28) — "dedicated 912-kilometre rail corridor linking the mine to the deep-water Port of Nacala"; Moatize 300 km², 2–3 miljard t reserves; productiecapaciteit 22→45 Mt/j sinds Vulcan-overname dec. 2021 (CEO Mukesh Kumar). https://www.ecofinagency.com/news-industry/2807-57769-mozambiques-largest-coal-mine-begins-155-million-shift-away-from-diesel
[5] Mining.com (Bloomberg News), "Indian steel tycoon's pathway to Mozambique coal deal reopens" (2025-05-26) — bevestigt Naveen Jindal als voorzitter van Vulcan International (eigenaar Moatize); JSW Steel/Sajjan Jindal's Minas de Revuboè is een apart, ongerelateerd project op een aangrenzende concessie. https://www.mining.com/web/indian-steel-tycoons-pathway-to-mozambique-coal-deal-reopens/
[6] Global Energy Monitor, Global Coal Mine Tracker — Moatize-coördinaat -16,1537/33,7207, opgegeven als "exact" (via het ketenontwerp; niet apart binnen het webbudget herbevraagd).
[web] Wikipedia-zoek-API (en.wikipedia.org/w/api.php, list=search) — gebruikt om "Nacala railway"/"Sena railway"/"Port of Nacala" te vinden.
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15, 2026-09-28) — `v2/build-cache/satcheck/sat-kolen-moatize-nacala-moatize.png`.
[grafiet-brief] `v2/design/routebrieven/grafiet-balama-vidalia.md` (regel 235) — bron van het letterlijk hergebruikte anker `kolen-nacala-velha-terminal`.
[osm] OpenStreetMap (ODbL) via Nominatim — Mwanza (town) -15,6092/34,5234 · Nkaya (railway=station) -15,1173/35,0230 · Nayuchi (railway=station) -14,9793/35,8731 · Cuamba (railway=station) -14,8033/36,5358 · Monapo (town) -14,9155/40,2972 · Nacala-a-Velha (town) -14,5481/40,6255 (bevestigt de ligging van het hergebruikte anker). https://www.openstreetmap.org

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Één been (b1, fase A, spoor), zes router-runs.** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs`
op het 1-op-1-spoornet (console bevestigt `3260717 spoor-edges`); extracts `mozambique` + `malawi`
beide al aanwezig in `v2/build-cache/raw1op1/`, geen download nodig. Kop→via→via→…→staart in
reisvolgorde als zes aparte `--been-geojson`-regels (het `kolen-tavantolgoi-baotou`-patroon).

| # | segment | km | punten |
|---|---|---|---|
| 1 | Moatize-mijn → Mwanza | 131,8 | 370 |
| 2 | Mwanza → Nkaya | 88,2 | 237 |
| 3 | Nkaya → Nayuchi | 99,5 | 284 |
| 4 | Nayuchi → Cuamba | 79,6 | 71 |
| 5 | Cuamba → Monapo | 463,2 | 778 |
| 6 | Monapo → Nacala-a-Velha-kolenterminal | 71,9 | 133 |
| **totaal** | | **934,2** | **1.873** |

**2 markers** (de twee ankers uit §3 — geen extra marker op de via-punten, want alle zes segmenten
zijn dezelfde modaliteit zonder drager-wissel). **Bestand:** `v2/data/stroomroute-kolen-moatize-nacala.json`,
versie 2, `punt_formaat: lonlat`, 35,7 KB.

**Km-toets:** 934,2 km tegen de bandbreedte 912 (Ecofin/Vulcan) – 931 (Wikipedia/Port of Nacala) km —
0,6% boven de bovenkant van de brief-bandbreedte, ruim binnen de ±15%-norm (775–1.071 km). De brief
zei zelf al dat de twee bronnen niet met elkaar overeenkomen voor dezelfde corridor; dit is geen
afwijking maar bevestigt de bandbreedte.

**Naden:** alle vijf naden tussen de zes segmenten zijn **0,000 km** — elk run-uiteinde en het
volgende run-startpunt snappen op precies dezelfde hoofdnet-spoorknoop (1899443 bij Mwanza, 1899377
bij Nkaya, 1899439 bij Nayuchi, 1945906 bij Cuamba, 1945236 bij Monapo).

**`toets_knikken.py`: 2 knikken ≥60°, waarvan 2 omkeringen ≥150°, waarvan 1 terugloop.**
- Segment 1 (Moatize→Mwanza): 175,2° bij -16,13190/33,79690, boograal ~320 m, **TERUGLOOP**
  (v=3,0) — kopmaak-plek op het Moatize-mijnemplacement/laadterrein, zelfde klasse als de
  Chuqui-/Matarani-emplacementen in eerdere kolen-/koperstromen. Niet gerepareerd: een via-punt
  bijschuiven zou de reisvolgorde/km-toets verstoren zonder dat er een reële corridorkeuze is —
  het is de korrel van het eigen mijnspoor, geen wegkeuze. Blijft staan als bevinding.
- Segment 2 (Mwanza→Nkaya): 178,7° bij -15,12010/35,03650, boograal ~189 m, scherpe bocht (echt,
  v=2,2) — bij de Nkaya-spoorsplitsing met de Sena-lijn; een reële kopmaak/wisselconfiguratie op
  het splitsingsemplacement, geen via-punt nodig.

**`toets_rechte_benen.py --min-km 5`:** geen van de zes segmenten van deze stroom komt boven de
omwegfactor-drempel uit (geen stippel-verdachte rechte lijn).

**Snap-afstanden (bevindingen, geen fouten):**
- `kolen-moatize-mijn`: 3,62 km van de dichtstbijzijnde hoofdnet-spoorknoop. De brief (§7) noemt
  "een paar honderd meter" als verwachte afwijking van het precieze laadpunt (spoorkop van de
  Nkaya-Moatize-tak); gemeten is dat ruimer, 3,6 km. Het mijnanker blijft ongewijzigd op de
  satelliet-bevestigde toegangsweg binnen het concessiegebied (geen coördinaat verzonnen).
- `kolen-nacala-velha-terminal`: 0,61 km — ruim binnen de norm.

**Stippels:** geen. Dit is een doorgetrokken, gemeten been zoals de brief voorspelde (§2: "geen
stippel verwacht").

**Haven-aanloop / zee:** niet van toepassing — de keten stopt bewust bij de kolenkade, geen
MARNET-zeeknoop-check nodig (brief §6/§7: geen bron met een koper op ladingniveau).

**Luchtbeen:** niet van toepassing.

**Gedeeld anker:** `kolen-nacala-velha-terminal` (-14,533/40,624) is een letterlijk hergebruik uit
`v2/design/routebrieven/grafiet-balama-vidalia.md` (regel 235, daar een NEGATIEF anker voor de
grafietstroom) — hier voor het eerst hoofdanker van een echte kolenketen; geen nieuwe satellietpas.

**Lessen:** de zes-runs-aanpak (kop→via→via→…→staart, elke run apart geregistreerd als
`--been-geojson`) reproduceert exact het `kolen-tavantolgoi-baotou`-patroon en gaf op elke naad
0,000 km, omdat elke run-invoer letterlijk het uitvoerpunt van de vorige run hergebruikt — dat is
de reden waarom een multi-via-corridor zonder `--via`-optie op de spoorrouter toch naadloos aan
elkaar sluit.
