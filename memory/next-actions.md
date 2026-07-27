# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-27 (M28 fase 1-3 af: vijf bronnen, track-graaf, MARNET, live ?v=090)*

## 🔴 START HIER — de visuele check, en daarna de losse eindjes

**M28 fase 1-3 is af en staat live op `?v=090`** (gepusht `c0c2b73..ed24837`). De
track-graaf staat (`bouw_trackgraaf.py`), MARNET hecht erop (`hecht_marnet.py`), en de
bol draagt vijf bronnen. Wat nu openstaat:

1. ~~**Visuele check van Lars op `?v=090`**~~ — **GEDAAN, go binnen** (2026-07-27):
   *"ziet er goed uit zo, we hebben veel kustgebieden, goeie haven-aansluitingen nu."*
   Geen fixes uit voortgekomen. De twee bekende schoonheidspunten blijven staan en zijn
   geen bug: in de Deense straten en de Mississippi-delta verzadigt de bundel naar
   crème-wit (prijs van 0,55 opacity bij die dichtheid), en Australië oogt grover door
   AMSA's eigen korrel van 21 km per stap.
2. **De New Orleans-coördinaat is een stadscentroïde, geen kade** — daardoor faalt de
   snap-eis (0,726 tegen ≤0,5 km) terwijl geen enkele van 510.752 tracks daar binnen
   0,5 km komt. De echte loskade van het Balama-vlok opzoeken en `gr-port-neworleans` in
   `data/graphite.js` vervangen. Zelfde klasse als de eerdere `data/*.js`-datafouten.
3. **Terminal-nodes (LAR-531)** uit de track-eindpunten — het dok-bewijs ligt er al:
   119 tracks eindigen en 133 beginnen binnen 3 km van de Syrah-kade, en elke
   track-uiteinde-cel is al een knoop in de graaf.
4. **GFW uitwerken voor de nul-dekking-corridors** (Chili/koperbeen, Hormuz, Lobito,
   Suez, Constanța). Token staat in `~/.claude/grondstoffen-atlas.env` en is getoetst
   (rooktest 200; presence-rapport Patache–Antofagasta 3.577 rijen / 27.741
   aanwezigheidsuren). ⚠️ Korrel is 1 positie/uur → corridorlaag, geen geul; en gebruik
   `datasets%5B0%5D=` in de URL, want bash leest `[0]` als glob.
5. **De EuRIS-vaarweglaag verwerken** — 7.122 secties met CEMT **én max diepgang** van de
   beheerder zelf, al anoniem binnengehaald in `build-cache/ais/euris/`. Dat is de echte
   diepgang-meting die LAR-514 eiste. De Donau valt in 8 componenten uiteen met gaten van
   3 m tot 2 km = de bekende LAR-520-klasse; de bestaande twee-traps heal volstaat.
6. **Overweeg een VPS-endpoint voor de tracks-laag** — `aistracks-pilot.json` ging van
   21,4 naar 39,5 MB en groeit met elke bron. Voor de pings-laag is die keuze al gemaakt
   (*"geen databestanden in de git-history"*); hier komt hetzelfde punt in zicht.
7. **De graaf op de andere corridors draaien** — nu bewezen op Mississippi en Rijn.
   Let op: connectors zijn corridor-gebonden, dus elke nieuwe corridor vraagt een eigen
   `hecht`-run. Globale bovengrens al gemeten: 1.211 van 9.633 MARNET-zeeknopen hebben
   over alle bronnen een trackpunt binnen 0,5 km.
8. **Collector blijft aandikken** — wekelijks `haal_ais_data.py` + `bouw_tracks.py --bron`.
   VPS-schijf: 21 GB vrij, ~844 MB/dag = ~24 dagen marge.

## Ouder (deels vervallen) — het oorspronkelijke LAR-530-plan

**Het plan staat in Linear** (milestone *"M28 · AIS-tracknet"*, LAR-528 t/m LAR-535) —
niet in de oude gloed/density-notities hieronder. De collector draait al op **13 vensters**
en verzamelt; er is dus dagelijks meer materiaal, en wachten kost niets.

**Eerst even dit, kost vijf minuten:**

* **Schijfritme is nu routine, geen luxe.** De collector staat op een wereldabonnement met
  live gzip: ~1 GB/dag gegzipt tegen ~22 GB vrij = **~20 dagen marge**. Loop
  `df -h /` + `ls -la /var/lib/ais-collector/ais/` na en draai
  `python v2/tools/haal_ais_data.py --opruimen` als er afgesloten dagen liggen.
  ⚠️ De harde ondergrens (2 GB) stopt alleen het schrijven, niet de stream — dat valt pas op
  in `journalctl`.
* **~~Wesel hermeten~~ — GEDAAN (2026-07-26):** op 12,5 uur is lon 6,5 nog steeds **0** en
  6,6 slechts 5 berichten in één uurvak, tegen 509 op 6,3 en 14.118 op 6,7. **Structureel**,
  zie `bugs-and-risks.md`. De pilot-corridor krijgt dus een gedocumenteerd gat.
* **Optioneel: tweede wereldscan op een ander tijdstip.** `python v2/tools/ais_wereldscan.py
  --minuten 60` (op de VPS) + `analyseer_wereldscan.py`. Scheidt de twijfelgevallen: "0 in dit
  uur" bewijst geen afwezigheid van dekking, terwijl wat binnenkwam wél hard bewijs van
  aanwezigheid is. Vooral zinnig voor havens met weinig bewegingen per dag.
* **Aanbod dat openstaat** (Lars nog niet op geantwoord): een dekkingsrapport per
  corridor-segment dat toont wélk aandeel van de uren dekking had — dan zie je in één blik
  welke gaten dichtlopen en welke echt leeg blijven. Volgt uit Lars' Starlink-punt: dekking
  is statistisch, niet binair. **Nu goedkoper dan eerst**, want het wereldabonnement levert
  elke corridor al aan.

* **LAR-530 · track-naar-graaf**, de kern. Stappen uit het issue:
  1. tracks per MMSI (sorteren op tijd, splitsen bij tijdsprong > X min of onrealistische
     sprongafstand — vangt meteen stream-uitval van de collector af);
  2. varend/stilliggend knippen (SOG < ~0,5 kn → apart, dat is LAR-531-materiaal);
  3. opschonen per track (max plausibele snelheid tussen punten, Douglas-Peucker + lichte
     smoothing);
  4. **track-bundeling** — meerdere doorvaarten middelen tot één centerline per vaarbaan.
     ⚠️ Bundel-afstand **kleiner dan de eiland-schaal**, anders smelten twee geulen om een
     eiland samen tot één lijn (de Tongling-les, ook al is Tongling zelf nu ongedekt);
     **⚠️ VERVALLEN MÉT stap 4 — sleep deze waarschuwing NIET mee naar de track-graaf.**
     Hij ging over *middelen tot één middellijn* over de héle lengte. In de track-graaf is de
     eis het omgekeerde: twee geulen om een eiland zijn twee eigen edges die **boven en onder
     het eiland juist wél in één gedeelde knoop samenkomen** — precies de vorm die Lars bij
     Tongling goedkeurde (zuid-junctie → kade → noord-junctie op exacte vertices). Zonder die
     samenkomst heb je twee losse parallelle netwerken en kan er niets langs routeren.
     (Correctie Lars, 2026-07-27, nadat deze zin ten onrechte als ontwerpeis was doorgegeven.)
  5. naar graafformaat: nodes op splitsingen/samenkomsten, edges met lengte.
* **Pilot = Rotterdam-Rijnmonding** (Tongling valt af wegens dekking). Eerst één corridor
  end-to-end vóór het generiek maken.
* **Integriteits-metrics per run loggen**, geen screenshot-vergelijking als primaire check:
  aantal losse componenten · edges/nodes · bereikbaarheid van havens/terminal-nodes vanuit
  de hoofdcomponent · verdeling snap-afstanden.
* **LAR-531 · terminal-nodes** uit de ligplaats-clusters (DBSCAN ε ~50–100 m), verrijkt met
  scheepstype uit `ShipStaticData` — dat komt al binnen, dus dit kan zodra stap 2 draait.
  Let op het onderscheid ankerplaats vs kade (afstand tot land / laad-context).
* **Collector-hygiëne:** af en toe `journalctl -u ais-collector | grep health` — blijft een
  venster op 0/min staan terwijl de verbinding er is, dan is dat dekking, geen storing.
  Schijf: dagbestanden gzippen automatisch, ondergrens 2 GB (VPS had 22,8 GB vrij).
* **Kandidaat-vensters zodra het recept staat:** de VS-binnenwateren (Mississippi/Ohio/
  Illinois/Seaway — Memphis, Cincinnati, Baton Rouge uit de routebrieven) zijn volgens de
  stationskaart gedekt, en dat zijn precies de corridors met de meeste OSM-topologiegaten.
* **Open, meeliften bij gelegenheid:** de reboot-overleving van `ais-collector.service` is
  mechanisch geborgd (`enabled` + `Restart=always`) maar niet live bevestigd — bevestigen
  bij de eerstvolgende geplande VPS-reboot (Hermes/Traefik/form4app draaien mee).
* *Herinnering:* de water-toetsen (`toets_routes.mjs`, `toets_stromen_14.mjs`) heffen hun
  parkering zelf op zodra er weer een waternet-bake ligt — verwachtingen dan herijken op het
  AIS-net (de oude 30/30-stand leeft op tag `pre-ais-net`).

## ⏸️ INGEHAALD DOOR M28 — de graaf-stap op de rug-lijnen

De onderstaande M27-acties (gloed-check, graaf-stap op de rug-lijnen, convergentie-filter)
zijn **geen route meer**. De gloed blijft als visuele laag, `bake_aisnet.py` als fallback
voor ongedekte corridors. Bewaard als context, niet als werklijst.

## ✅ AFGEROND 2026-07-25 (laat) — RUG-RECEPT VERVANGT DREMPEL+VERDUNNEN (live `?v=085`, commit `9576dea`)

Lars keurde v084 af (hoekig, gaten in oostgeul + Rijn, te dun) → tweede recept i.p.v.
fix. `bake_aisnet.py` herschreven: Steger-rug-NMS op het continue log-veld (2 schalen,
σ²-genormaliseerd) + hysteresis (zwak-maar-aaneengesloten loopt door → gaten dicht) +
geijkte bezettingstoets (oostgeul ≥0,53 vs drijfzone ≤0,40 + groot-component) +
kruimel-snoei + gladstrijken. 2.369 lijnen / 245 KB (was 9.631 / 770). Beide
Tongling-geulen doorlopend · NL glad tot de grens · Patache één corridor. Gemeten en
verworpen in de file-header: NMS-tolerantie, vlak-bezetting, max-filter-bezetting.
Het aparte "open-zee-recept" is hiermee opgegaan in de grove σ 3,5-schaal.

## ✅ AFGEROND 2026-07-25 — AIS-PILOT OP DE BOL (live `?v=084`, commit `9ddd96f`)

`verken_ais.py` (kijk-eerst: density-PNG's bewezen de bron) + `bake_aisnet.py` (drempel
100k → adaptief verdunnen → glad log-veld → confetti-filter → skelet + spur-snoei) +
`aisnet.js` (één LineSegments, HUD-knop). Tongling's beide geulen komen rechtstreeks uit
de data; binnenvaart-NL compleet. Les: heel NL-water is één verbonden component —
per-component herdrempelen sloopte de rivieren; brede vlakken lokaal uitsnijden.

## ✅ AFGEROND 2026-07-24 — SCHONE BOL: WATERNET ERUIT (live `?v=083`, commit `960ad15`)

Besluit Lars: alles nat weg (zee + binnenvaart), clean slate voor de AIS-graaf. Backup tag
`pre-ais-net` + branch `backup/pre-ais-net` (`?v=082`, 30/30). Bol = tegels + vectorwereld +
landnet + havens-als-ankers; marnet.bin/json verwijderd; HUD-secties Zeeroutes/route-test/
stromen weg; water-toetsen geparkeerd (zelfopheffende guard), land-toets draait door.
AIS-bron gedownload (Commercial 458 MB, gratis/CC-BY) + rasterio/scikit-image geïnstalleerd.
* **Optioneel: de 22 grove AFGEKNIPT-sites breder uitrollen.** De last-mile-pass draait nu op de
  15 aangewezen aansluitingen; de brede detector (`toets_spoor_aansluiting.mjs`) vond nog **22
  AFGEKNIPT** industriële nodes (Fresnillo, Kalgoorlie, Norilsk, Hunan-Ag…) — dat zijn de grove
  `data/*.js`-coördinaten, niet de aansluitingen. Uitrollen = per site een precieze coördinaat
  opzoeken (veel zijn stad-centroïdes) en `PUNT_EXTRACT` in `fetch_service_lastmile.py` uitbreiden;
  de heal + drop + wees-opruiming werken dan generiek mee.

## ✅ AFGEROND 2026-07-24 — ROUTEBRIEF-WERKWIJZE + EERSTE BRIEF (commit `a595095`, gepusht)

Besluit Lars: per stroom een **routebrief** die de échte corridor vastlegt — elk dorp/
splitsing/sluis in volgorde, per punt bron + status (bevestigd/aannemelijk/onzeker),
negatieve ankers, tweezijdige toets (dekking + verklikker), routeren via-punt→via-punt,
**simulator alleen op zee**. Spec: `v2/design/routebrief-werkwijze.md`. Eerste brief kolen
Cerrejón→Ruhr: spoorbeen 37 punten (laadlus→Muelle Carbonífero) + Rijnbeen 93 punten mét
operator-bron (thyssenkrupp Veerhaven: Hartelkanaal→Oude Maas→Merwede→Waal→Rijn, 240 km,
sluisvrij) — de toets ving meteen de **Beerkanaal-fout** en bevestigde de Oude Maas-keuze.
AIS-richting: corridor-first met World Bank-density als geul-bewijs (idee Lars, geverifieerd).

## ✅ AFGEROND 2026-07-24 — TONGLING: BEIDE GEULEN ALS GRAAF (live `?v=077`, Lars' go, commits `6327707`→`5428001`)

De oostgeul (waar de schepen echt varen) als échte graaf-tak **naast de hoofdgeul**: 18
punten, zuid-junctie → kade → noord-junctie, beide uiteinden op exacte vertices van
hoofdgeul-way 226556520 → gedeelde knopen. **Werkwijze-doorbraak:** OSM's watervlak bleek
geen waarheid (elke afleiding gaf de 27 km-lus) → Esri-tegels lokaal gestitcht (z14,
0,01°-grid) en elk punt visueel in het geul-midden gelegd — voortaan de standaard voor
handmatige vaarweglijnen. Onderweg het `knipWayId`-mechanisme gebouwd
(`bake_marnet.bulklaag`, extra-vaarwegen-feature = knip-instructie, guard ≤1 km); de
v076-knip van de west-arm was een **misinterpretatie** en is in v077 teruggedraaid — het
mechanisme blijft voor echt foute armen. Kleur = grondstof: bevestigd besloten. Toets
30/30 elke ronde; zee-invarianten exact. Lars: *"top helemaal goed — zo lang beide geulen
een simpele graaf, dat was alles."*
* **Realiteitsronde** (Lars' eigen volgorde: "eerst de rail beter verbinden, dan de realiteit"):
  per dragende site checken of het product écht per trein/truck vertrekt (bedrijfsrapporten) —
  nu is er een stuk minder te vullen omdat de last-mile-sidings al hechten.
* **Echte OSM-gaten** (blijven `onbekend`): EU-spoor rond Krefeld/Kempen (daar ligt écht niets)
  en de Escondida-slurryleiding (geen `substance=slurry` richting Coloso).

## ✅ AFGEROND 2026-07-24 — INDUSTRIEEL LAST-MILE-SPOOR GEHEELD (live `?v=072`, commit `6266aba`)

Vervolg op de heal-ronde: is er meer spoor/riviergraaf dat we missen? Twee detectoren
(`toets_stromen_14.mjs` → riviernet solide, 0 gaten; `toets_spoor_aansluiting.mjs` → 22 AFGEKNIPT).
Wortel: het M25-filter dropt álle `service=`-rail — juist het last-mile-spoor. Fix:
`fetch_service_lastmile.py` (service=spur/siding/yard binnen 7 km van de aansluitingen) +
transitieve vertex-op-vertex heal in `bake_landnet` (smelter→tussennet→hoofdnet ≤200 m) +
`drop_onverbonden` (weg + wees-knoop-opruiming, anti-regressie). Tongling/Beilun/Guixi/Duisburg
aan het hoofdnet; toets_routes 30/30; marnet/ports byte-identiek; Lars' visuele go.

## ✅ AFGEROND 2026-07-24 — DE HEAL-RONDE (de spoor+riviernet-heal van hieronder)

Live `?v=071` (commit `0eaff4b`). De diagnose draaide de opdracht om: niet het net healen,
maar de pijplijn laten ophouden met knippen — de bron was op elk breukpunt al verbonden
(raw-experiment, ook onder het service-filter).

- **Heal verlengt i.p.v. verplaatst** → EMO-flip-flop weg; Cerrejón→Ruhr **0 gaten**.
- **Riviersnap relatief naar doorgaand component** → Manaus→Amazone; Saldanha→Manaus routeert.
- **Dedup-connectiviteitsguard** → spoor 3.140 → **638 componenten**, grootste 402.845 →
  **664.313 km**; Beilun↔Guixi trein 883 km; Antwerpen↔Duisburg één component (EU 96%).
- toets_routes 30/30; zee-invarianten exact. Gemeten en verworpen: snipper verlagen alléén.

## ✅ AFGEROND 2026-07-23 (avond) — GROENE STROOM (COLLAHUASI→TONGLING) VERFIJND

Live `?v=066` → `070` (commits `8d2842e` · `7afc0e1` · `5e6fcd5` · `d14c602` · `a0b5959`).

- **Yangtze-heal in de bake:** `snij_bulk()` neemt nu alleen kop/staart weg, nooit een gat in
  het midden → de rivier blijft in de graaf één stuk. Been 616 → 540 km; 59 lijnen / ~282 km
  wereldwijd heel gehouden.
- **Overslag-markers:** `transparent:true` op het merk (zat in de opaque pass, tegels
  schilderden eroverheen) + maat gehalveerd.
- **Tongling-kade** naar de nieuwe TNMG-kopersmelter (`117,7718/30,98656`); oostgeul afgeleid
  met `middellijn_uit_vlakken.py` op 167 m, water-constrained, **alleen noordaanvaart** (met
  óók de zuidkant maakte de router een lus om het eiland).
- **Nieuw:** bake-optie `--extra-vaarwegen` + gecommit `data/vaarwegen-handmatig.geojson`
  (reproduceerbaar via `tools/maak_tongling_oostgeul.py`); `BAKE_SUFFIX` in `laad_headless.mjs`.

## ⚪ AANSLUITINGEN VERFIJNEN (Lars: "we laten het hierbij, verfijnen kan later")

* **Puerto Patache — de espesadores.** Collahuasi's eigen video geeft de keten ná de leiding:
  espesadores → planta de molibdeno → planta de filtro → stockpile → embarque. De leiding
  mondt uit bij de **indikkers**, niet bij de pier. Nu doet `cu-patache-kade` twee dingen
  tegelijk (eind van de leiding én begin van het zeebeen) terwijl dat twee plekken zijn met
  vier verwerkingsstappen ertussen. Eerlijke opzet: leiding → espesadores · terminalverwerking
  als *eigen verbinding* · zeebeen vanaf de pier. **Blokkade:** de espesadores staan niet in
  OSM (binnen 1,8 km kent de kaart vijf objecten, geen tank) → één coördinaat van Lars nodig.
* **Shanghai/Luojing** — nu de Baogang-bulkpier; concentraat voor de Yangtze-smelters lost in
  werkelijkheid vaak verder stroomopwaarts (Zhangjiagang/Jiangyin) of aan de eigen kade van
  de smelter.
* **Tongling** — de pier ligt 1,5 km van het smelterterrein; de smelter zelf heeft geen
  kade-tag in OSM.
* **Rotterdam/Duisburg** — OSM tagt bij géén van de gekozen kades wát er wordt overgeslagen;
  de toewijzing leunt op de buren binnen 1 km (ArcelorMittal Staalhandel / Metaalhandel
  Ketting bij de Waalhaven; Kokerei + Erzlager bij Schwelgern). Staat per aansluiting in de
  `noot`.

## ⚪ OPENSTAAND ONTWERPBESLUIT

* **Blijft "kleur = grondstof"?** De LOD-ontwerpbrief zegt van wel, maar de koperkleur
  (#E0965A) is op de Atacama en de Chinese kust onleesbaar — zandkleur op zandkleur. De pilot
  draait nu op vier contrastkleuren (Lars' eigen schets). Of de regel grondstof-gebonden
  blijft of per stroom mag verschillen hoort bij de rest van M26. Staat als `kleurnoot` in
  `v2/data/stromen-pilot.json`.
* **Pijpleidingen ooit tóch een net?** Voor slurry: nee (Lars' criterium — één product, twee
  punten, nooit een keuze). Voor **olie en gas ligt het anders**: Droezjba of Power of Siberia
  ís gedeelde infrastructuur waar een blokkade een echte herrouteringsvraag oplevert, en
  `data/*.js` heeft 36 pijpleidingstromen. Dán een eigen milestone, niet nu.

## ✅ AFGEROND 2026-07-23 — M26.1 · DE STROMEN OP STRAATNIVEAU

Live `?v=065` (commits `d5b2204` · `d8e86fd` · `0f4ba0b` · `5bc5997` · `4d1581e` · `17b5ac2` ·
`34f7a3a`). Vier werkelijke stromen, twee grondstoffen, been voor been over de gekoppelde netten.

- **`v2/data/aansluitingen.json`** — 15 aansluitingen per grondstof, coördinaten uit OSM (ODbL)
  via de nieuwe scout **`v2/tools/verken_terminals.py`**, gemeten door
  **`v2/tools/maak_aansluitingen.py`**.
- **`v2/src/stromen.js`** (three-vrij) + **`v2/src/stroomlaag.js`** (tekenen) — zelfde splitsing
  als `router.js`, zodat het routeren headless narekenbaar blijft.
- **`v2/data/pijpleidingen.json`** + **`v2/tools/fetch_pijpleidingen.py`** — de slurryleiding
  Collahuasi→Patache als tekengeometrie, 1.363 punten, 192,4 km (−3,8%).
- **`v2/design/stroom-aansluiting.md`** — het ontwerp, incl. §4a met Lars' net-criterium.
- `globe.js` kreeg **`vliegNaar(lon, lat, hoogteKm)`**; `keten.js` meet nu ook de componenten
  van land- én waternet zodat "geen pad" op elk net zijn reden draagt.
- **`toets_routes.mjs` 15/15 → 30/30 groen**; zee-invarianten onveranderd (19.610 / 89).

## ⚪ OUDER OPEN GELATEN

* **Drie wegcorridors zonder pad:** `bx-boke-katougouma`, `li-atacama-lanegra`,
  `ree-mountweld-leonora`.
* **89 atlas-plaatsen op een spoorcomponent <1.000 km** (New York op 0 km, Amsterdam op 87).
* **In "egaal" (tegellaag uit) blijft de vectorlaag onzichtbaar** — daar ís de bol het
  oppervlak, dus hij schrijft diepte en wint opnieuw.
* **Manaus→Rotterdam = "geen pad"** — Amazone-fragment raakt Macapá niet.
* **Drie datafouten in `data/*.js`** (zie `bugs-and-risks.md`), plus de nieuwe bevinding dat
  de via-havens daar te grofkorrelig zijn voor straatniveau.
