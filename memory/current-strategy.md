# Current strategy — Grondstoffen Atlas
*Last updated: 2026-07-28 (laat: de anker-check — de corridors kloppen, de uiteinden niet)*

## Stand 2026-07-28 (laat) — de fout zit stelselmatig in kop en staart

**De werkwijze is aangescherpt op de plek waar hij lekte.** De routebrief vroeg het
detail al (elke splitsing, elk dorp, kop en staart op ~50 m) en leverde dat ook — maar
de fouten die Lars ving zaten niet in de corridor, ze zaten in de **uiteinden**. Daarom
staat er nu in `v2/design/routebrief-werkwijze.md`: **§2 status `satelliet-gelegd`**
(elk laadplek-/overslag-/losplek-punt eerst op een gestitchte Esri-overlay op z16,
vóórdat het anker heet), **§3.4 de last mile als eigen been** aan beide uiteinden, en
**§7 de stippellijn-conventie** — waar geen havenspoor of kade-aansluiting ligt wordt
het been gestippeld **mét reden** getekend, en voor Chili/Patache, Lobito, Hormuz, Suez
en Constanța is dat de **eindvorm**, geen tussenstand.

**De uitslag rechtvaardigt de regel: 10 van 16 ankers over vier stromen stond fout**,
van 42 m tot 4,5 km. Escondida stond ín de open put, de Waalhaven op de dijk bij een
woonwijk. **Het net bleek intussen beter dan gedacht:** het spoorbeen Beilun→Guixi, dat
ik eerst als corridor-fout meldde, meet hermeten 550,5 km en slaagt volledig voor de
tweezijdige toets van §4.

**Het scherpste gereedschap is een vraag, geen tool** (Lars): *"welk product is dat, dan
kun je toch checken waar ze dat verwerken of overslaan"*. Kathode is LME-leverbaar →
LME-erkend entrepot → RHB aan Waalhaven Noordzijde 4. Die vraag hoort bij élke kade.

**Gevolg voor de aanpak:** de satellietcheck per hand schaalt niet naar honderden
punten. De volgende stap is een **verdachtenlijst** die mechanisch scoort (kade op
water of land, afstand tot een OSM-pier, laadplek binnen het industrievlak,
snap-afstand tot het eigen net) zodat het oog alleen naar de kop van die lijst gaat.

## Stand 2026-07-28 — de routebrief-werkwijze werkt intercontinentaal

**Werkwijze bevestigd door Lars:** vóór het uitwerken van een grondstofstroom eerst
een **routebrief** (de echte corridor uit bronnen, punt voor punt met status), dan de
kaart daartegen afwerken. De tweede brief (grafiet Balama→Vidalia, kerndocument
DOE/EA-2181) corrigeerde in één klap vier kaartfouten én een dataverhaal: de overslag
lag niet bij Leeville maar in New Orleans/Port Allen, de losplek is de Port of
Vidalia (mijl 359), en **het spoorbeen bestond helemaal niet** — uitgaand AAM gaat
per truck, de "omdraaiende trein" bij Jackson was een artefact op een been dat er
niet hoort. De verklikker-toets ving bovendien live dat MARNET's delta-geometrie via
South Pass binnenkomt; gefixt met een Southwest Pass-via-punt over echte tracks.

**De stroom-machinerie is nu been-gestuurd:** `hecht_marnet.py route` routeert per
been (--been/--stippel/--marker), de laag tekent kleur-per-modaliteit inclusief
gestippelde eigen verbindingen. Live `?v=092`.

## Stand 2026-07-27 (late avond) — de eerste end-to-end stroomtests

**De architectuur is gevalideerd met echte stromen.** Grafiet Nacala→Vidalia routeert
als 16.936 km MARNET-zee (Kaap-route, zoals de echte stroom) + **één** connector van
0,154 km + 435 km echte Mississippi-trackgeometrie — alle track-routepunten letterlijk
uit de brontracks. Newcastle (AU)→Vidalia werkt idem (start snapt op een MARNET-zeeknoop;
de Australische binnenkant heeft bewust geen graaf). New Orleans→Baton Rouge is vóór en
ná de aanhechting byte-identiek. En het spoor draagt de VS-benen: Vidalia→battery belt
1.036 km, Long Beach→Fort Worth 2.312 km (nieuw: `toets_spoorroute.mjs`, snap op
hoofdnet-component ≥ 1.000 km). **Daarmee is de grafietketen Balama→battery belt voor
het eerst meetbaar over drie netten: zee → binnenvaart → spoor.**

**En het beeld is er nu ook (zelfde avond, `?v=091`):** de HUD-laag *"Stroom: grafiet
Balama → VS (preview)"* tekent de geroutete keten kleur-per-modaliteit (zee #5aa7ff ·
barge #35e0c0 · spoor #ffb04d) met witte overslagmarkers, standaard aan. De data komt
uit het nieuwe `hecht_marnet.py route`-subcommando (`v2/data/stroomroute-pilot.json`).
Twee CDP-lessen zitten in de file-kop van `stroomroute.js`: renderOrder 7,5 **bóven het
landnet** (het spoorbeen volgt per definitie een landnet-lijn en was er anders precies
onder onzichtbaar) en **toneMapped uit** (ACES bleekte de legenda-kleuren naar wit).

## Stand 2026-07-27 (avond) — vijf bronnen, de track-graaf, en MARNET erop

**Het natte net wordt nu gebouwd uit vijf AIS-bronnen** (768k tracks / 55 mln km):
MarineCadastre (VS) · DMA (DK) · Kystdatahuset (NO) · AMSA (AU) · eigen collector.
De eerste vier bronnen leveren edge-geometrie; AMSA niet.

**De maat die alles stuurt is de punt-tot-punt-afstand binnen de tracks**, niet het
ping-interval: DK 0,249 km · NO 0,265 · VS 0,269 · collector 0,453 · **AMSA 20,43**.
Alleen een bron met een korrel van honderden meters beschrijft de gevaren geul; een
bron van 20 km beschrijft een corridor. Daarom is AMSA een dekkingslaag en zijn de
knip-waarden van `bouw_tracks.py` CLI-parameters geworden (`--knip-min` / `--stil-max`
/ `--gat-max-km`): **de bron bepaalt de korrel, niet het recept**.

**De graaf, in twee lagen** (`bouw_trackgraaf.py`):
1. **hele-track-match** — bestaat er één track die zelf van A naar B loopt, dan ís die
   track de route. Geen graaf, geen middeling. Dit is de mooiste uitkomst, maar dun
   voor lange reizen: 119 tracks eindigen bij de Syrah-kade en 133 beginnen er, en
   tóch dekken er maar **5** de hele reis New Orleans→Vidalia — een meerdaagse
   duwvaart wordt geknipt zodra het schip echt aanlegt.
2. **graaf op raakpunten (~200 m)** voor de rest. Een route is dan een keten van
   track-*segmenten*.

**Geen bundeling, nergens** — en dat is structureel afgedwongen, niet alleen verboden:
een edge is een **verwijzing** `(set, regelnummer, i0, i1)` + knoop-ids + echte km. De
geometrie staat exact één keer, in de trackset. Daardoor kost niet-bundelen geen
opslag en is er geen plek waar een gemiddelde of celcentrum in een edge kán sluipen.
Routeren gaat over **haltes**, niet over knoop-cellen: met cellen is overstappen gratis
en telt niemand de naad (gemeten 78,6 km onverantwoord).

**Open zee blijft MARNET, en hecht via een RAAKPUNT** (`hecht_marnet.py`): een
MARNET-zeeknoop wordt opgenomen als er een graafknoop binnen 0,5 km ligt, met één
connector-edge tussen twee échte coördinaten. **Geen terugval** naar "de
dichtstbijzijnde, hoe ver ook" — dat is de schuine snap die eerder Whitby/Rostock 58 km
wegteleporteerde. Verlengen, niet verplaatsen. MARNET zelf komt van tag `pre-ais-net`
en gaat niet terug in `v2/data/`.

**Wat de bol toont** (`?v=090`): dekkingsgedreven selectie over alle vijf bronnen,
33.147 lijnen / 1,85 mln punten, kleur = richting (amber op / ijsblauw af), per bron
een eigen subgroep zodat een bron los uit te zetten is zonder rebake.

## Stand 2026-07-27 (nacht) — twee bronnen, één recept, en de tracks zíjn het net

**MarineCadastre (NOAA/USACE) is de tweede tracknet-bron.** Dagelijkse heel-VS-dumps
(CSV.zst ~285 MB/dag, publiek domein, `curl` zonder registratie, 2009-heden, mét de
binnenrivieren): mississippi **768/min waar aisstream 0 heeft**, duwboten dominant.
Kerninzicht: **de graaf heeft geen líve data nodig, alleen tracks** — een historisch
archief is even goed als een stream. 28 dagen (29 jun–26 jul 2025) verwerkt:
**259,4 mln pings → 510.510 tracks / 27,4 mln km** in 20,5 min
(`bouw_tracks.py` herbouwd: CSV direct = 5-10× sneller dan de JSONL-omweg, twee passes
via 64 bucket-bestanden, venster optioneel — de pilot-vensters gaven op de bol een
"afgekapte rivier" bij lat 35,6 en zijn weg).

**Live `?v=089`: HUD-laag "AIS-tracks VS (pilot)"** — 18.609 doorvaarten via een
**dekkingsgedreven selectie** (track gaat mee als hij genoeg onbezette ~1 km-cellen
dekt; op/af als eigen celruimtes), amber = opvaart / ijsblauw = afvaart.

**⚠️ DE DRIE BESLUITEN VAN LARS die de graaf-stap herdefiniëren:**
1. **Geen centerline-bundeling — de tracks zelf zijn het net.** LAR-530 wordt een
   **track-graaf**: knopen waar tracks elkaar raken (~200 m gekwantiseerd),
   edge-geometrie = de échte gevaren lijn. Bewijs dat dat moet: de Vidalia-toets gaf
   op een celgraaf −7,4% en "onrealistisch hoekig" (Lars), op de echte gevaren lijn
   **−0,1%** (430,6 vs ~431 km).
2. **Open zee blijft definitief MARNET** — aisstream levert daar niets (walbereik
   40-80 km), satelliet-AIS is betaald. Stitchen in de overlapzone waar tracks de zee
   op lopen.
3. **Track-venster 4 weken** — langere doorvaarten (langste nu 1.010 km), dokken vol.

**Europa = de eigen collector, zelfde recept.** Geen Europees MarineCadastre; 2 dagen
VPS-data → 23.766 tracks (Rijnmond→Duisburg al **3.195**; het Wesel-gat is
**dichtgelopen** — momentopname, zoals de Starlink-werkregel voorspelde). Wekelijks
meebakken. Vier research-agents zoeken open archieven voor de rest (rapport volgt).

---

## Stand 2026-07-26 (middag) — geen vensters meer, en we zagen de helft van de schepen niet

**De collector staat sinds 14:08 UTC op een WERELDABONNEMENT** met vijf berichtsoorten en
**live gzip**. Twee metingen dwongen dat af.

**1 · `PositionReport` is uitsluitend Class A.** Class B-transponders komen binnen als
`StandardClassB-`/`ExtendedClassBPositionReport` en hun naam/type als `StaticDataReport`
(msg 24) — die vielen buiten zowel de dekkingsscan als de draaiende collector. Gemeten in een
wereldabonnement: **9.655 ber/min en 8.089 unieke MMSI mét** tegen **4.465 en 4.269 zonder**.
In onze eigen vensters: meren-seaway **+77%**, schelde-antw **+42%**, noord-dld +21%, Rijn
+12–15% (daar vaart de vracht Class A). Geen codewijziging nodig — de collector bint al op
`MetaData`, dus het was puur de abonnementslijst.

**2 · De hele aisstream-feed is maar ~9.800 ber/min** en onze 13 vensters trokken daar al
~1.600 van. Bij die verhouding zijn vensters voortijdige zuinigheid: ze kosten later een
corridor die je niet meer kunt terughalen. **De vensters blijven bestaan als health-banen**,
zodat uitval per corridor zichtbaar blijft in `journalctl` in plaats van te verdrinken in één
wereldtotaal. **Live gzip is daarbij een voorwaarde, geen optimalisatie**: ruw ~8,5 GB/dag
tegen ~1 GB gegzipt bij ~22 GB vrij — de code weigert `--wereld` zonder `--live-gz`.

**De gemeten dekkingskaart (1 uur, alles, 588.627 berichten / 41.812 schepen).** Hun
walstations zenden zichzelf uit als `BaseStationReport`, dus de stationskaart is nu gemeten:
**641 stations** — Europa 397 · Noord-Amerika 171 · Oost-Azië 22 · Afrika/MO 20 · Oceanië 20 ·
Zuid-Amerika 11. Posities: Europa **73,9%**, Noord-Amerika 16,7%, en **Zuid-Azië + de Golf
samen 163 berichten = 0,0%**.

**Wat dat betekent voor de graaf.** Van de 3.963 havens heeft **1.169 (29,5%) varend
verkeer** — alleen dáár valt een spoor náár de kade te bouwen; stilliggers geven een
ligplaats, geen route. **Nul havens met varend verkeer** in Chili (47), Peru (28), de VAE
(22), Egypte (18), Nigeria (18), Roemenië (16), Angola (12), Iran (12), de Filipijnen (58) en
Vietnam (21) — dus het koperbeen, Hormuz, Lobito, Constanța en Suez **blijven op MARNET + het
density-raster**. Wél uit tracks te bouwen: NW-Europa, Noord-Amerika (Meren + Seaway +
kusten), Japan/Korea, Australië/NZ, Singapore/Malakka.

**Werkwijze die dit vastlegt:** de scan bewaart naast het raster het volledige ruwe uur, en
`ais_wereldscan.py --herbereken` bouwt het raster daaruit opnieuw op. De Class A/B-uitsplitsing
per cel kostte zo **geen nieuwe meettijd** — hetzelfde principe waarom de collector dom is.

## Stand 2026-07-26 (nacht) — de debuglaag staat, de dekkingskaart is gemeten

De **pings-debuglaag** (LAR-535) staat live op `?v=087`: HUD-toggle *"AIS-pings (debug)"*
gevoed door een eigen HTTPS-endpoint op de VPS (publisher-timer elk kwartier → nginx op
`localhost:8088` → Traefik met Let's Encrypt + CORS via de file-provider). Besluit Lars:
endpoint boven meeliften met het repo; en de **PC trekt** de ruwe data via de bestaande
SSH-sleutel (`haal_ais_data.py`), geen mail of cloud.

**De laag verdiende zich in een uur terug.** Lars zag een gat op de Rijn: Emmerich 215
pings · **Wesel 0** · Duisburg 637 in hetzelfde venster = ~55 km zonder ontvanger, precies
op het Rijnbeen van de kolen-routebrief. En zijn voorstel om de Chinese kust erbij te nemen
is met een **positieve controle** weerlegd: in dezelfde subscriptie Busan 220 en Tokio-baai
71 berichten tegen Shanghai 0 en Ningbo 0 — dus geen box-limiet, het Chinese vasteland is
ook aan de kust donker.

**De collector staat nu op 13 vensters** (9 met data, besluit Lars: nu al breder, want
verzamelen en het recept bouwen lopen parallel). ~1.480 berichten/min ≈ 1,2 GB/dag ruw,
~120 MB gegzipt; 22 GB vrij. Gemeten dekking per corridor staat in
`v2/design/ais-collector-vps.md`; de structurele conclusie is dat dekking sterk is waar
walstations dicht bij druk vaarwater staan en zwak op open zee — wat **langs een
onafhankelijke weg** de M28-taakverdeling bevestigt (open zee = MARNET).

**Werkregel die hieruit volgt** (uit Lars' Starlink-punt): dekking kan opportunistisch
aangroeien, dus een gat is een momentopname en geen eigenschap van de kaart. Stille vensters
blijven staan, een gat wordt **niet** gerepareerd met geleende geometrie zolang het nog kan
dichtlopen, en de zinnige maat is *welk aandeel van de uren dekking had* — niet "0 pings".

## Stand 2026-07-25 (nacht) — M28: de graaf komt uit TRACKS, niet uit dichtheid

**Het plan is omgedraaid** (besluit Lars, buiten de sessie om vastgelegd als Linear-
milestone *"M28 · AIS-tracknet"*, LAR-528 t/m LAR-535). Niet het 500 m-dichtheidsraster
maar de **tracks van individuele schepen** — geordende ping-reeksen per MMSI via
[aisstream.io](https://aisstream.io) — zijn de bron van de vaargraaf. Eén doorvaart =
één vloeiende edge op GPS-precisie, tot áán de kade. Geen threshold, geen skeleton, dus
per constructie geen driehoek-uitschieters, lussen of spurs; terminal-nodes vallen er
gratis uit via ligplaats-clusters (SOG < 0,5 kn).

**Taakverdeling per laag:** open zee = MARNET blijft · kust/riviermonding/binnenwater/
havens = eigen AIS-tracks · overgang = overlap-stitching · offshore olie/gas = World Bank
platformlaag als node-bron · fallback = het density-raster voor corridors zonder tracks.

**⚠️ De beperking is geografisch, niet technisch.** De aisstream-stationskaart is dicht op
Europa (incl. Duits binnenland/Rijn), de VS-kust **plus** Grote Meren en Mississippi/Ohio-
binnenland, Japan/Korea/Zuidoost-Azië en de Australische kust — maar China heeft **alleen
kustpunten**. Gemeten in 3 minuten: Rotterdam 884 berichten / 293 per min / 572 unieke
MMSI, **Tongling 0**. Een station reikt 40–80 km en Tongling ligt ±400 km landinwaarts.
Besluit Lars: doorgaan voor de gedekte corridors; de Yangtze houdt het density-raster.

**De collector draait** (`ais-collector.service`, VPS `root@187.124.169.172`, enabled) en
is **bewust dom**: ruwe berichten erin, ruwe JSONL per UTC-dag eruit, géén track-logica.
Die zit in de aparte verwerkingsstap (LAR-530), zodat een verbeterd recept nooit nieuwe
verzameltijd kost. Vensters `rijnmond` · `rijn-corridor` (tot Duisburg — het Rijnbeen uit
de kolen-routebrief) · `tongling` (doorlopende controle). Opzet + bediening:
`v2/design/ais-collector-vps.md`.

**Verwachting, expliciet:** de eerste week oogt de graaf dunner dan de density-screenshots.
Corridors vullen zich één doorvaart tegelijk — dat is by design, geen tegenvaller.
Verzamelen en bouwen overlappen.

De gloed (`bake_aisgloed.py` + `aisgloed.js`) blijft als **visuele laag**; `bake_aisnet.py`
blijft werkend als **fallback**. Beide zijn geen routeringsbron meer — dat staat nu ook in
hun bestandskop.

## Stand 2026-07-25 (avond) — de gloed is het beeld, de lijnen zijn het zaad *(ingehaald door M28)*

Lars keurde ook het rug-lijnenbeeld af op de bol (*"waarom is de omzetting zo mager?"*).
Diagnose: het mooie op de dichtheids-PNG's is het **veld zelf** — breedte, drukte,
parallelle banen — en dat gaat bij elke middellijn-extractie op een 500 m-raster
verloren; bovendien kijkt de bol op meters-scherp satelliet en heeft breed water geen
eenduidige middellijn. **Keuze Lars: de gloed als laag** (boven de hybride met
OSM-geometrie en boven verder verfijnen). Live `?v=086` (commit `af55a8d`):
`bake_aisgloed.py` (gloed-textuur per venster: artefact-gaten dichten →
vierdemachtswortel-schaal → blauw→cyaan→wit op zwart → ×3 + blur → randvervaging) +
`aisgloed.js` (gebogen quad, AdditiveBlending, klemOpHorizon, renderOrder 6,3). HUD:
gloed standaard aan, lijnen standaard uit. **Wacht op Lars' check op `?v=086`**;
inhoudelijk volgende stap blijft de graaf-stap op de rug-lijnen.

## Stand 2026-07-25 (laat) — het rug-recept vervangt drempel+verdunnen

Lars keurde `?v=084` af (hoekig, gaten in de Tongling-oostgeul én de Rijn, dunner dan de
dichtheidsfoto's beloven) → `bake_aisnet.py` volledig herschreven naar het **rug-recept**
(live `?v=085`, commit `9576dea`): Steger-rug-NMS op het **continue** log-veld (twee
schalen σ 1,5/3,5, σ²-genormaliseerd; ankervlekken zijn blobs en vallen er per
constructie uit) → hysteresis 0,35/1,1 (zwak maar aaneengesloten loopt door → de gaten
dicht, geen harde 100k-drempel meer) → bezettingstoets per lijn, **geijkt** op de
oostgeul-draad (≥0,53) vs de Patache-drijfzone (≤0,40) + groot-component-eis →
kruimel-/spur-snoei → gladstrijken (1-2-1, uiteinden vast). 2.369 lijnen / 245 KB (was
9.631 fragmenten / 770 KB); beide Tongling-geulen doorlopend, NL glad tot de grens,
Patache één corridor, Shanghai-aanloop strak. Gemeten rasterfeit: geulen = 1-cels draden
mét artefact-nullen; drijfzones = corridor-waarden als speckle → alleen geometrie
onderscheidt. **Wacht op Lars' check op `?v=085`**, dan de graaf-stap.

## Stand 2026-07-25 — de eerste AIS-geulen liggen erop (v084, vervangen)

Pilot live (`?v=084`): vaargeulen uit de AIS-density als zichtbare laag in vier vensters —
Tongling (**beide geulen om het eiland rechtstreeks uit de data**, het satelliet-handwerk
van 24 juli is daarmee overbodig aan het worden), Nederland (compleet binnenvaartnet),
Shanghai-mond (scherp), Patache (snipperig — open zee vraagt een eigen recept). Pijplijn
`bake_aisnet.py`: drempel 100k berichten → **adaptief verdunnen** (brede vlakken lokaal
uitsnijden en per gebied tot de vaarrug drempelen; les: heel NL-water is één component,
per-component drempelen sloopte de rivieren) → glad log-veld σ=1 → confetti-filter →
skelet → polylijnen + spur-snoei. Ankervlek-filter beslist als **convergentiegedrag**
(corridor dunt naar een rug, ankervlek convergeert nooit) — uitvoering in de graaf-stap.
**Wacht op Lars' visuele check**; daarna de graaf-stap (knopen/edges, healen, havens
aanhechten) of eerst het recept aanscherpen.

## Stand 2026-07-24 (laat) — schone bol, de AIS-graaf komt

**Besluit Lars: alles nat weg** — het volledige waternet (marnet zee + binnenvaart) is van de
bol en uit de bake verwijderd zodat het natte net clean uit AIS-density opgebouwd wordt
("dan is het net ook veel dichter"). Backup: tag `pre-ais-net` + branch `backup/pre-ais-net`
(`?v=082`, toets 30/30). Live `?v=083`: bol = tegels + vectorwereld + landnet + havens
(ankers). Water-toetsen geparkeerd via zelfopheffende guard (heffen zichzelf op zodra er
weer een waternet-bake ligt); keten/router/stromen-code blijft in de repo, ongebruikt.
Bron binnen: World Bank "Global Shipping Traffic Density" **Commercial** (458 MB,
gratis/CC-BY, 0,005°≈500 m, jan 2015–feb 2021; incl. BULK CARRIER/ORE CARRIER/PUSHER
TUG/INLAND TANKER → óók binnenvaart) in `v2/build-cache/ais/`. Volgende: raster verkennen
(Rijn/Maasvlakte) → eerste zelfgelegde knopen (pilot Maasvlakte, brief = ankers, AIS = geul).

## Stand 2026-07-24 (avond) — de routebrief stuurt, het net volgt

Nieuwe werkwijze (besluit Lars): per stroom een **routebrief** — de werkelijke corridor als
geordende, gesourcete puntenlijst (`v2/design/routebrief-werkwijze.md`) — en de lijn wordt
ertegen getoetst: **dekking** (alle bevestigde punten in volgorde) + **verklikker** (geraakte
plaats niet in de brief = vlag). Spoor/leiding/binnenvaart zijn **brief-gestuurd** (routeren
via-punt→via-punt); **simulator alleen op zee**. Voor het natte net gaan we **corridor-first**:
brief = ankers, AIS-density (World Bank Global Shipping Traffic Density, ~500 m, gratis,
wereldwijd) = waar de geul ligt; knopen zelf leggen en verbinden i.p.v. datasets verzoenen
(nuance op LAR-482: AIS = geul-bewijs, geen stromen-bron; open-zeenet blijft zolang het
werkt). Eerste brief (kolen Cerrejón→Ruhr, spoor 37 + Rijn 93 punten) bewees de methode:
Beerkanaal-fout gevangen, Oude Maas bevestigd, Schwelgern = Rijn-km 790,20.

> **Stand na ?v=072 — het last-mile-spoor hecht.** Het M25-filter dropt álle `service=`-rail;
> een additieve pass (`fetch_service_lastmile.py`) sluit `service=spur/siding/yard` bij de
> aangewezen aansluitingen in en `bake_landnet` heelt die clusters transitief vertex-op-vertex aan
> het net (drop-onverbonden + wees-opruiming = anti-regressie). Tongling/Beilun/Guixi/Duisburg
> hangen nu aan het hoofdnet. Detectoren: `toets_spoor_aansluiting.mjs` (breed) + `toets_stromen_14.mjs`
> (riviernet solide). Volgende: optioneel de 22 grove AFGEKNIPT-sites, dan de realiteitsronde.


## Stand 2026-07-24 — de netten zijn heel waar de bron heel is

De heal-ronde (aangekondigd als "spoor+riviernet-heal") bleek een pijplijn-fix: een
raw-experiment bewees dat de bron op elk breukpunt al verbonden was, dus repareren we niet het
net maar de stappen die knipten. **De regel die nu op alle drie de knip-plekken staat: een stap
mag geen verbinding verbreken die de bron had** — snij_bulk (kop/staart, 2026-07-23), de heal
(verlengen i.p.v. verplaatsen) en de dedup (connectiviteitsguard, kortste stukkenpad terug).
Spoor wereldwijd: 638 componenten met de grootste op 664.313 km; alle vier de M26.1-netgaten
dicht op de Escondida-leiding na (echt OSM-gat). Wat overblijft is brongrofheid (Tongling-vlecht)
en echte OSM-gaten — geen pipeline-schade meer.

## Stand 2026-07-23 — de stromen liggen erop, en ze wijzen de gaten aan

De vier netten zijn gekoppeld (LAR-518) en er lopen nu **vier werkelijke stromen** overheen (M26.1).
Daarmee is de fase "fundament" voorbij: de atlas toont niet meer alleen infrastructuur maar echte
ketens, been voor been, van laadplek tot fabriek.

**De drie lagen onder een stroom, van grof naar fijn:**

| laag | wat het is | bestand |
| -- | -- | -- |
| de netten | zee, binnenwater, spoor, weg — gedeelde infrastructuur | `marnet.bin` / `landnet.bin` |
| het register | welke plaatsen mogen overslaan, per modaliteit | `knooppunten.json` |
| de aansluitingen | de kade of het laadspoor van **deze grondstof**, ~50 m | `aansluitingen.json` |

**De werkregel die dit stuurt** (Lars): *"we moeten het vooral meemaken waar iets ontbreekt; dat
zien we zodra we de routes voor stromen hebben bekeken."* Precies wat gebeurde — vier netgaten
kwamen boven die geen enkele meting vooraf had opgeleverd, en de router meldt ze nu zelf mét getal
in plaats van stil "geen pad" te zeggen.

**Wat wel en niet een net wordt** (besluit Lars, 2026-07-23): alleen GEDEELDE infrastructuur. Een
slurryleiding vervoert één product tussen twee punten en levert als graaf niets op; die wordt
tekengeometrie ("eigen verbinding") en telt niet als gat. Voor olie en gas ligt dat anders — daar
is een pijpleiding wél gedeeld, en dan pas is een pijpleidingnet een eigen milestone waard.

**Niet de simulator.** De keten van een stroom komt uit `data/*.js` (`via:` + `mode:` per been); de
router zoekt alleen BÍNNEN een been, op precies één net. Vervoerskeuzes verzinnen is de simulator,
en die komt later.

## Stand 2026-07-22 avond — VIER netten liggen er, het koppelen is het enige dat rest

| net | omvang | bestand |
| -- | -- | -- |
| zeenet (MARNET) | 15.933 edges | `marnet.bin` |
| riviernet | 407.626 km | `marnet.bin` |
| landnet (spoor) | 1.154.092 km | `landnet.bin` |
| **landnet (weg)** | **17 corridors · 17.635 km** | **`landnet.bin`, soort 3** |

De wegkant is bewust **geen net maar een handvol verhalende lijnen**: weg is de enige modus
zónder onafhankelijke scheidsrechter, dus de acceptatietoets is **topologisch** (loopt de lijn
aantoonbaar via Kasumbalesa, Chirundu, Beitbridge?) met de gepubliceerde lengte als tweede toets
waar die bestaat. Negen van de zeventien hebben er een en vallen allemaal binnen de tolerantie.

⚠️ **De vectorlagen liggen boven de tegels met een horizonklem** (`klemOpHorizon` in `globe.js`).
Zonder dat is de hele vectorlaag onzichtbaar zodra de tegels laden — dat was maandenlang zo en
niemand kon het zien. Raak `depthTest` op die lagen niet aan zonder de meting opnieuw te doen,
en meet **niet boven open water**.

## ⚠️ 2026-07-22 later — het spoornet was structureel gebroken, en dat is hersteld

De landnet-pijplijn eindigt op `schrijf_geojson()`, en die draait een **Douglas-Peucker-simplify
met tolerantie 100 m** die 96% van de vertices weggooit. Dat gebeurde **ná** de heal, en brak
daarmee een deel van de naden weer open. Polen met de bake-regel: 77 componenten / grootste
15.341 km (79%) → 91 / 8.673 km (45%); de twee helften raakten elkaar op 75 plekken, waarvan één
op **0,7 meter**.

Hersteld met `heel_na_simplify()`, die **uitsluitend terugzet wat de simplify brak** — een naad mag
alleen tussen ketens die vóór in hetzelfde component zaten en er ná in verschillende. Daarmee is
"geen kruisingen, viaducten of tunnels verbinden" een eigenschap van de constructie in plaats van
een guard die je moet vertrouwen. Grootste component **356.682 → 402.845 km**; de vijver voor de
overslagknooppunten (roze havens op het wereldnet) **23 → 45** van de 200. Live `?v=046`.

⚠️ **Meet componenten voortaan tegen de LIJNGEOMETRIE, niet tegen `landnet-aanhecht.json`.** Dat
bestand meet plaats → dichtstbijzijnde **knoop**, en knopen liggen elke 10 km, dus een stub van 1 km
lijkt er altijd dichterbij dan een doorgaande hoofdlijn. Die vertekening kostte in deze sessie een
halve diagnose voor 11 van de 497 plaatsen.

## De wegkant — machinerie staat, lijst wacht op de redactieronde

`CORRIDORS` is **bewust leeg**: welke corridors bestaan is een redactiebesluit, geen afleiding. Wat
er wel staat in `fetch_landnet.py`: `weg_houden()` + `WEG_HOUD` (`motorway` t/m `secondary` — ruim,
want `highway=motorway` geeft gemeten **0 km in Zambia én DR Congo**; de scope komt van het venster,
niet van de tag), het **corridorvenster** om de lijn *anker → tussenpunten → anker*,
`corridor_keten()` met Dijkstra per been, en `--modus weg` als eigen pijplijn (geen vouwen/dedup/
heal/snoei — dat is gereedschap voor een net, en dit zijn losse verhalende lijnen).

⚠️ **Het venster ligt niet om de grootcirkel.** De echte truckroute Kolwezi→Durban loopt via Lusaka
(155 km van de rechte lijn) en Harare (362 km); een buffer van 50 km om de rechte lijn mist de hele
corridor. De tussenpunten — grensposten en tussensteden — zijn wat een corridor tot een corridor
maakt, én sinds 2026-07-22 ook de **acceptatietoets** (voor weg bestaat geen scheidsrechter).

## Stand 2026-07-22 — VIER netten liggen er, koppelen komt als laatste

**Lars' volgorde (omgedraaid op 2026-07-22):** riviernet heel ✅ → havens op de juiste plek ✅ →
**landnet neerleggen ✅ (spoor; wegcorridors volgen)** → **koppelen in één keer over álle netten**.

| net | omvang | bestand | knoopruimte |
| -- | -- | -- | -- |
| zeenet (MARNET) | 15.933 edges | `marnet.bin` | 0 … 9.685 |
| riviernet | 407.626 km · 60.131 edges | `marnet.bin` | 9.686 … 71.264 |
| **landnet (spoor)** | **1.154.092 km · 236.784 edges** | **`landnet.bin` (4,4 MB)** | **lokaal 0 … 237.879** |
| *(volgt)* wegcorridors | ~20-40 verhalende corridors | `landnet.bin` (soort 3) | idem |

⚠️ **Het landnet leeft bewust in een EIGEN bestand met LOKALE knoop-ids.** `bak_havens()` slicet de
knopenlijst op `zee_knopen` en telt élke knoop daarboven als water; spoor ligt in élke haven
dichterbij dan de dichtstbijzijnde zeeknoop, dus landknopen in dezelfde lijst = elke haven snapt op
een spoorknoop en de WPI-positieschoning verplaatst havens naar het spoor. Een gebakken offset zou
bovendien stil verlopen bij een marnet-rebake (varints lezen altijd "iets" → plausibele onzin i.p.v.
een exception). De offset wordt pas bij het **laden** berekend uit `marnet.json`.

**De landnet-pijplijn** (`fetch_landnet.py` → `bake_landnet.py`): parallelle osmium-scan met
per-extract cache → **ketenvouwen** (OSM knipt spoor op elke tagwissel; zonder deze stap bepaalt
het aantal way-uiteinden het aantal knopen) → **dedup van dubbelspoor** per monster met gauge in de
sleutel → **heal** (cross-component ≤150 m; anders blijven de snijranden van de dedup los) →
component-snoei die op land ómgekeerd werkt aan water (houden wat een atlas-plaats raakt óf ≥25 km
is — Pilbara, Carajás en Sishen–Saldanha zijn geïsoleerd én het onderwerp) → simplify die **knipt
op aanhechtpunten** (een kale DP sneed juist de aftakkingen weg).

**Landbrug (beslist):** het standaardprofiel sluit `land`; de modus per been komt uit de
flows-data, niet uit de router. Zonder die regel wint een spoorroute lexicografisch van zee
(0 overslagen, ~11.000 km) en kantelen 7 van de 11 invarianten naar een trein.


## Stand 2026-07-21 (avond) — riviernet geknoopt; werkwijze: bouwen boven meten

**Lars' volgorde is nu leidend: (1) net heel ✅ → (2) havens op de juiste plek ⬅️ NU → (3)
aansluiten via overslag → (4) wegen/spoor.** De route-test als gap-detector is geschrapt (een
kortste-pad-router rijdt om een gat heen en verbergt het); werkregel: **bij twijfel bouwen, meten
alleen als diagnose bij iets dat aantoonbaar kapot is** — het bestaande regressie-vangnet blijft.

**Het net:** componenten 10.669 → **1.772** via drie mechanismen die alle drie "het water volgen":
de twee-traps heal (`?v=040`), **1.828 bruggen** over ongetagde OSM-riviergeometrie (`?v=041`,
`v2/tools/knoop_riviernet.py`) en **75 meer-oversteken** dwars door `natural=water`-vlakken met
`covers`-toets (`?v=042`, `--meren`). **Ohio-Cairo en de Waal-tak dicht via échte geometrie**;
zeenet in élke stap byte-ongemoeid (0 zee↔rivier, -t == live, bake zonder vlaggen byte-identiek).
Signalen `"brug"`/`"meer"` dragen géén maat (onbekend = geen grens) en zijn gericht verwijderbaar.

## Stand 2026-07-21 — de architectuur: drie netten, verbonden door aangewezen overslag
Zeenet (MARNET, knoop 0–9.685) + riviernet (9.686+, bewust losse component) + straks land (M25).
Havens dragen sinds LAR-518 twee aanhechtingen (zee + rivier) en een watermaat; de kaart toont
alleen wat aan water ligt. De overslag wordt een gelaagde keten-router over een aangewezen
`knooppunten.json` (ontwerp: `v2/design/overslag-ontwerp.md`).

**✅ Het riviernet is nu gestitcht** ([LAR-520], live `?v=040`): een twee-traps over-water heal in
`binnenwaternet()` (achter `--heal-km 0.25 --corridor-km 2.0`, geïtereerd tot convergentie) bracht de
componenten van **10.669 → 3.490**. **tier-1** cross-component confluentie-heal (uiteinde → op de lijn
van een ander component, over water per constructie — cross-component sluit de meander-sluipweg per
constructie uit); **tier-2** collineaire corridor-heal (uiteinde↔uiteinde ≤2 km mét richtingsguard).
Mississippi en Rijn-mainstem verenigd; zeenet byte-identiek; 0 edges zee↔rivier. Meetgereedschap
`v2/tools/diagnose_riviernet.py`. **Nog open:** de router (`zoekKeten` + `toets_routes.py`) en twee
angled confluenties (Ohio-Cairo, Waal-tak) via de lengtetoets. Bronnen-rolverdeling voor de
overslaghavens: `v2/design/havenbron-keuze.md` (WPI/EMODnet/UNECE/LOCODE).

## 🌊 De architectuur: drie netten, verbonden door overslag (2026-07-20)

Sinds deze sessie bestaat de kaart uit **losse netten die elkaar niet raken**, en dat is bewust:

| net | wat | verbonden met |
| -- | -- | -- |
| **zeenet** (MARNET) | 15.840 edges, verzoend met de vectorwereld | — |
| **binnenwaternet** | 374.342 km, 53.922 edges, maten per lijn | — |
| *(later)* landnet | M25, spoor + weg | — |

**De verbinding tussen die netten is een OVERSLAGHAVEN, geen edge.** Lars: *"van binnenvaart naar
zee naar binnenvaart gebeurt altijd met 3 schepen, niet 1."* Een route is dus een **keten van
legs** met een overstap, niet één doorlopend pad.

**Dat lost twee dingen op die eerder veel werk kostten.**
1. Het **ankerwerk vervalt**: elk riviersysteem met de hand aan een zeeknoop hangen kostte ~30 min
   × 375 systemen, en dát maakte de wereldwijde uitrol onhaalbaar.
2. **De Donau-ring-fout verdwijnt structureel.** De `zeevaart`-vlag en het groepslabel
   `binnenvaart` bestaan alleen om te voorkomen dat een zeeschip door sluizen vaart. Zijn zee en
   rivier losse componenten, dan kán dat niet meer — geen filter nodig, het volgt uit de vorm.

⚠️ **Zolang de overslag er niet is:** havens snappen alleen op het zeenet
(`bak_havens(max_knoop=...)`), het riviernet draagt nul routes, en binnenhavens snappen slecht
(Nijmegen 79,1 km). Dat is de verwachte tussenstand, geen defect.

## 🗺️ Eén binnenwaternet, niet twee lagen (2026-07-20)

Het binnenwater wordt **één keer gemapt**, met de eigenschappen op de lijn:

* **de vier maten** (diepgang · breedte · lengte · hoogte, decimeter, 0 = onbekend)
* **getoetst of mechanisch** — een *veld*, geen aparte laag; de kleur leest het uit

**Knopen en geometrie zijn los van elkaar.** Knopen liggen op kruisingen en uiteinden plus elke
10 km; daartussen zit de volledige lijn met alle meanders, en `edgeKm` is de echte vaarafstand.
Een haven wordt met `hecht_aan_keten()` aangehaakt, dat de edge op een bestaande vertex openknipt —
dus de knoopafstand begrenst de nauwkeurigheid van een haven niet.

De artisanale pijplijn (`extra_vaarwegen()` + `SYSTEMEN`) blijft bestaan als **promotiepad** voor
een rivier die een eigen `vermijd`-knop of een gevalideerde lengtetoets verdient.

## 📐 Gabariet: de graaf weet welk schip past (2026-07-20, [LAR-514])

Elke edge draagt **vier maten** — diepgang · breedte · lengte · doorvaarthoogte — in **decimeter**,
waarbij **0 = onbekend**. De router filtert erop via `opties.schip = {diepgang, breedte, lengte,
hoogte}`; een edge valt weg **vóór de relaxatie**, op exact dezelfde plek en van dezelfde soort als
`vermijd`. Daardoor blijft de A*-heuristiek toelaatbaar en is het gevonden pad nog steeds precies
het kortste over wat overblijft. Zonder `schip` gaat er **geen enkele** edge dicht.

**Het draagprincipe: bekende maat = harde grens, onbekende maat = géén grens.** Een lege maat mag
nooit stilzwijgend een route afsluiten — dat effect is onvindbaar, want je ziet alleen dát een
route niet bestaat, niet waaróm. Liever zeven systemen leeg dan één systeem verzonnen.

**De regel die bepaalt wat een maat mág zijn** (twee keer duur geleerd, zie `decisions.md`):
*een getal dat de VAARWEG beschrijft is geen getal dat het SCHIP begrenst.*

| soort getal | de graaf in? |
| -- | -- |
| gepubliceerde max scheepsdiepgang / LOA | ✅ |
| sluiskolkmaat als lengte/breedte (bovengrens, hooguit te ruim = veilige kant) | ✅ |
| brugklaring mét bekend referentievlak | ✅ |
| vaargeul-projectdiepte / 维护水深 als diepgang | ❌ garantie, geen maximum |
| CEMT-diepgangkolom | ❌ beschrijft het referentieschip (niet-monotoon: VIb 4,50 → VIc 4,00) |
| CEMT-hoogtekolom | ❌ de tabel geeft alternatieven, de beheerder kiest |

**Waar de tabellen staan:** `CEMT_PRESETS` (klasse → lengte + breedte) en `GABARIET_PER_SYSTEEM`
(de gemeten maten) leven in **`bake_marnet.py`**, niet in de fetcher — ze komen niet uit OSM, dus
een correctie hoeft geen re-fetch af te dwingen. `cemt` blijft wél bij `SYSTEMEN`, want de
CEMT-clause selecteert er OSM-ways mee.

**Een edge mag pas een gabariet dragen als hij uniform is.** Zes edges wachten daarom op een split
of een gepinde node (zie `next-actions.md`): één gabariet kan geen factor anderhalf in
doorvaarthoogte of een kolkmaat die maar over 10 van 1.728 km geldt eerlijk beschrijven.

## 🌍 De bulklaag: twee lagen naast elkaar (2026-07-20, [LAR-515])

Sinds deze sessie bestaan er TWEE soorten binnenwater-geometrie op de bol, met een principieel
verschil in wat ze mogen kosten en wat ze moeten bewijzen:

| | **verhalend** (`EXTRA_VAARWEGEN`, `fetch_waterways.SYSTEMEN`) | **bulk** (`vaarwegen_bulk.geojson`) |
|---|---|---|
| selectie | naam-whitelist per systeem | mechanisch filter (laag C: elk bevaarbaarheidssignaal) |
| topologie | ankers, `kortste_waterpad`, knopen/edges in de graaf | **geen** — elke OSM-way is zijn eigen polyline |
| routeerbaar | ja, eigen passage-label = `vermijd`-knop | **nee**, bewust — puur tekengeometrie |
| lengtetoets | tegen de officiële vaarafstand, 6-14 punten | steekproefsgewijs (nog te doen) |
| omvang | 36 systemen, ~17.400 km | 349.312 km, 8 regio's |
| bakt in | `nodes`/`edge_lijst`/`status` (muteert de graaf) | apart bestand `marnet-bulk.json` (muteert niets) |

**Waarom de bulklaag geen topologie heeft — dit is de kernbeslissing van de sessie.** Het voor de
hand liggende ontwerp (stitch de bulklaag tot een graaf zoals de 36 verhalende systemen) bleek bij
een risicoanalyse VOOR het bouwen fataal: op Nederland alleen al (5,5% van laag C) gaf dat
**23.189 knopen — meer dan het hele huidige netwerk (10.773)**, want bulkketens zijn extreem kort
(mediaan 52 m in NL) en de baker zet een knoop op elk ketenuiteinde. Zonder topologie bestaat dat
risico niet. Bijkomend voordeel, niet vooraf voorzien: de bouw werd ook **drastisch sneller** —
wereldwijde scan + bake in ~16 minuten in plaats van de geschatte uren.

**Bewijs dat de graaf onaangeroerd blijft:** `git diff` op `marnet.bin`/`marnet.json`/`ports.json`
is **leeg**, zowel op de China-proefbake als de wereldwijde run. Dit is het sterkste soort bewijs in
dit project (zelfde patroon als LAR-504's byte-identieke bake) — geen aanname, een meting.

**Promotie bulk → verhalend gebeurt later, systeem voor systeem** (de Promotie-milestone). Een
systeem promoveren = het een eigen label geven in `SYSTEMEN`, wat het routeerbaar maakt en een
`vermijd`-knop oplevert voor M21. Tot die tijd draagt de bulklaag geen enkele route.

**Ondergrens verbreed: "alles wat bevaarbaar is", niet meer CEMT ≥ IV.** Lars: *"liever een kanaal
mappen dat niet gebruikt wordt dan dat we straks nog extra moeten maken omdat er spoorwegen uitkomen
op plekken waar nu geen binnenwater aansluit."* Concreet: laag C uit `v2/tools/meet_vaarwegen.py` —
een expliciet bevaarbaarheidssignaal (`CEMT`, `ship=yes`, `boat=yes`, `motorboat=yes`, `draft`),
bewust ongeacht `waterway=`-type (de Poses-les veralgemeniseerd). Gemeten: 428.428 km wereldwijd; het
oude criterium ving daarvan maar 7,7%.

**Kleur: fel rood (`0xff1a1a` @ opaciteit 0,85), niet gedempt amber.** Eerste keuze (`0xa8814a` @
0,35) was bedoeld om de getoetste ketens visueel te laten winnen, maar bleek in de praktijk vrijwel
onzichtbaar. Zichtbaarheid gaat voor; niet-routeerbaarheid blijft geborgd doordat de laag buiten de
graaf staat, niet doordat hij onopvallend is.

Zie `v2/design/binnenwater-scope.md` voor het volledige scope-onderzoek (375 systemen / regio) en
de LAR-515-comments in Linear voor de gemeten cijfers per stap.

## 🚢 M24-uitrol: de vaarwegen vormen een NET (2026-07-19, [LAR-504])

Sinds [LAR-504] is `EXTRA_VAARWEGEN` geen verzameling losse lijnen meer. Een systeem met `volgtOp`
hecht aan het **dichtstbijzijnde punt** van zijn voorganger; ligt dat middenin een edge, dan wordt
die daar doorgeknipt — altijd op een **bestaande geometrie-vertex**, zodat er geen coördinaat
verschuift en de corridor-toets van de moeder per constructie geldig blijft.

Gevolg voor de rest van de uitrol: **rivieren hoeven niet meer vooraf opgeknipt te worden** op
plekken waar later iets aantakt. Splits alleen waar het iets betekent — bij een **verstoring**, want
elk segment is een eigen passage-label = een eigen `vermijd`-knop voor M21. De Rijn is daarom bij
**Bingen** geknipt (Kaub-laagwater), niet bij de zeevaart/binnenvaart-grens: die vlag is puur
metadata en stuurt geen routering.

### Sinds [LAR-505]: een keten mag aan BEIDE kanten hechten

`volgtOp` hecht het **begin** van een keten, `sluitAan` het **eind**. Dat is het verschil tussen een
boom en een net: een verbindingskanaal (Amsterdam-Rijnkanaal, straks het Schelde-Rijnkanaal) verbindt
twee bestaande ketens en is zonder tweede hechting een **doodlopende tak die nul routes draagt** —
gemeten, niet vermoed: Amsterdam→Nijmegen bleef 263 km mét én zonder het kanaal, en werd 105 km zodra
de sluiting erin zat.

**Vuistregel voor de rest van de uitrol:** takt een systeem aan één kant aan (zijrivier), dan volstaat
`volgtOp`. Verbindt het twee bestaande systemen (kanaal), dan **hoort er een `sluit_aan` bij** —
controleer dat door een route te zoeken die er logisch overheen moet en hem één keer mét en één keer
zónder het label in `vermijd` te meten. Verandert er niets, dan draagt de keten niets.

**Vaste volgorde per systeem** (nu vier stappen, want stap 1 is gereedschap geworden):
1. `v2/tools/survey_vaarwegen.py` over de extracts → namen **op lengte, mét lon/lat-strekking**.
   Aan die strekking zie je of de whitelist een doorlopend traject dekt; een gat = een ontbrekende
   naam of een ontbrekende extract.
2. Ankers verifiëren tegen waar MARNET (of de moederketen) wérkelijk ophoudt.
3. `fetch_waterways.py geofabrik --alleen <labels>` → stitch, dan **lengte tegen de officiële
   vaarafstand** (de beslissende toets) + de haventoets uit [LAR-488].
4. Bakken, regressie (6818→9654 **19.610**, 6391→6818 **8.031**), `?v=` bumpen, pushen.

## 🛤️ M25-aanpak (2026-07-19, [LAR-491]) — bronnenplan staat, nog niet gebouwd

**Afbakening gekozen: het complete hoofdspoornet, géén corridor-scope** (Lars: *"complete spoor is wel
beter zeker voor de simulator"*). Zelfde argument als M23: een netwerk beantwoordt vragen die je niet
vooraf hebt uitgerekend. Blokkeer `grens-kasumbalesa` en met een compleet net **ís** Lobito de uitkomst;
met corridor-scope kan M21 alleen verstoringen tonen die we vooraf bedachten.

**Gelaagd zoals water:** compleet spoor = de MARNET-rol (mechanisch verzoend, niet edge-voor-edge
nagelopen) · de verhalende corridors (Kasumbalesa, Lobito, Gashuunsukhait, Ruili) = de
`EXTRA_VAARWEGEN`-rol — apart gebakken, op lengte gecontroleerd, mét passage-label = de M21-knop.

| modus | geometrie | meetlat |
|---|---|---|
| spoor | OSM via Geofabrik-pbf | NARN (VS) · RINF-lengtes (EU) · gepubliceerde lijnlengtes elders |
| pijpleiding | OSM waar goed + GEM's openbare GitHub-repo | operator-lengtes (CNPC, ADNOC) |
| weg | Overture of Overpass per corridor | **geen** |

**Wat op land anders is dan op water — drie dingen die de aanpak sturen:**
1. **De corridor-toets verliest z'n kracht.** "≤250 m van een middellijn" was op water sterk bewijs omdat
   water schaars is; op land ligt élke verkeerde route ook dicht bij een weg. **Lengte is de enige echte
   controle** — de LAR-487-les is hier geen verfijning maar het hele fundament.
2. **Filteren gebeurt door UITSLUITING.** `usage=main` eisen sloopt precies de regio's waar de atlas z'n
   corridors heeft (40–43% van de spoor-ways draagt geen `usage`-tag). Houden: `railway` in
   (`rail`, `narrow_gauge`); weg: alles met `service=`, `usage` in (`tourism`, `military`), en
   abandoned/disused/razed/construction/proposed. Gereedschap: `v2/tools/meet_spoor.py`.
3. **Vorm ≠ routering.** Bij water deed één `LineSegments` allebei; bij spoor niet meer. Routeergraaf
   190–240k knopen bij 10 km bemonstering past; ruwe tekengeometrie ~11M punten ≈ 36 MB past niet.
   Kandidaat-oplossing bestaat al: M24's `strak_trekken()` (simplify mét bewijslast).

**⚠️ De stap die M24 niet had: parallelle sporen samenvouwen.** Dubbelspoor is meestal als twéé losse
lijnen gemapt (`tracks=2` staat in China op maar 5.406 ways) → de lengtetoets meet er 2,4× te veel én de
graaf verdubbelt gratis mee. Rivieren komen niet in paren. Bouw dit vóór pilot 1, anders "faalt" een
bake die klopt.

**Open bij de start:** pilotkeuze · GEM-licentie · dedup vóór/tijdens pilot 1 · knoopafstand 5 of 10 km.
**Volgorde:** eerst M24's uitrol (M24.0–M24.5), dán M25, dán [LAR-490].

## ✅ M24-pilotreeks compleet (2026-07-19) — alle drie controle-situaties bewezen

De pilots per regio zijn af (op Lars' visuele go na). Elk bewees een manier om te controleren
zonder de bron zelf te vertrouwen:

| pilot | controle-situatie | uitkomst |
|---|---|---|
| NL (LAR-486) | twee onafhankelijke bronnen | OSM vs UNECE mediaal ~80 m → OSM gekozen |
| VS (LAR-487) | officiele meetlat | USACE mediaan 76 m; **lengte 0,3% van de officiele vaarafstand** |
| China (LAR-488) | geen scheidsrechter | 9 searoute-havens vallen vanzelf op de keten (Wuhan 0,7 km) |

**De pijplijn zoals hij nu staat:** `fetch_waterways.py` (OSM via Overpass, exacte naam-match,
schijf-cache) → `bake_marnet.py --vaarwegen` (`EXTRA_VAARWEGEN` + `volgtOp`-ketening, corridor-toets,
verzoening-cache ~1 min) → `toets_usace.py` (meetlat) → browser-acceptatie via
`window.MARNET`/`HAVENS`/`zoekRoute`. Zes systemen, 126 vaarweg-edges.

**Werkwijze die zich bewees en die de uitrol moet aanhouden:** meet de **lengte** tegen de officiele
vaarafstand, niet alleen punt-tot-net-afstanden — een fout gevolgde zijarm of oxbow ligt overal dicht
bij iets, maar verraadt zich meteen in de totale kilometers.

## 🔭 M26-richting (2026-07-19) — LOD-systeem, spec in `v2/design/lod-ontwerpbrief.md`

- **Semantische zoom:** ~4–5 banden op `getAltitude()`; hotspots vallen build-time-geaggregeerd
  uiteen in echte sites; flows aggregeren mee (bundeling gratis via het M23-netwerk). Ultra-lokaal
  = Esri z17–19 + onze markers/labels (coördinaten ~100 m nauwkeurig).
- **Look:** combinatie referentiebeelden + v1; glow-bollen + selective bloom; lijndikte in meters
  met pixel-minimum; night-side/stadslichten als kandidaat-default — go/no-go én night-side-test
  bij de **koper-pilot** (data-ambitie C: koper eerst volledig, rest per grondstof).
- **Volgorde hard:** M24 (bezig) → M25 (weg/spoor — vereiste voor kloppende regionale/lokale views)
  → LAR-490. Tot die tijd niets aan bouwen.

## 🧭 M24-aanpak (2026-07-19) — GEBOUWD in LAR-486; hieronder de architectuur zoals hij nu draait

- **Pipeline:** `v2/tools/fetch_waterways.py` (middellijnen per systeem, cache in `v2/build-cache/` naast
  `ne_10m_*`) → `EXTRA_VAARWEGEN`-stap in `bake_marnet.py` (edges `soort=1` + systeemlabel + zeevaart-vlag,
  zeezijde gesnapt aan een MARNET-knoop in NE-water, lon-normalisatie zoals de M23-les) → `ports.json`
  her-snappen → **corridor-toets** (elk ~2 km-monster ≤ ε van de bron-middellijn; kruis-vergelijking met
  UNECE/USACE waar die bestaan) → acceptatie-routes als regressietests (Amsterdam via IJmuiden;
  Duluth→R'dam 8.031 / R'dam→Shanghai 19.610 onveranderd).
- **Bron:** de bake-off in LAR-486 (OSM vs UNECE op NZK + Waal) beslist de definitieve rolverdeling;
  kandidaat = OSM-geometrie overal + officiële netten als meetlat (het M23-model doorgetrokken).
- **Volgorde:** NL-pilot (LAR-486) → VS-pilot (LAR-487, USACE-meetlat) → China-pilot (LAR-488, zónder
  scheidsrechter) → wereldwijde uitrol (EU CEMT ≥ IV, VS USACE-net, elders de commerciële systemen) +
  restpunten uit LAR-485 (Yangon-stubs, 2 restedges, Wolga-Don-dekking).

## ⚓ Sinds M23 (2026-07-18) — het netwerk is de router, de baker is de verzoening

- **`v2/tools/bake_marnet.py`** repareert MARNET **één keer** tegen de 1:10M-vectorwereld (dezelfde bron
  als wat op het scherm staat) en bakt `v2/data/marnet.bin/json` + `ports.json`. Deterministisch; opnieuw
  draaien vereist `ne_10m_land/minor_islands/lakes.geojson` in `v2/build-cache/` (gitignored) + shapely/numpy/searoute.
- **Drie klassen** in de verzoening: *aanloop* (treffer ≤5 km van een knoop — dokbekken/riviermond, ok) ·
  *binnenwater* (29 zones: kanalen + rivieren die NE-land niet als water kent; als-is bewaard, soort=1) ·
  *kapot* (koorde snijdt kaap/eiland → lokale A* 0,02°→0,01°, mét én zonder kustbuffer, simplify met
  land-bewijs, eindtolerantie per uiteinde gemeten op de oorspronkelijke koorde).
- **`v2/src/marnet.js`** = laag + graaf + router: één LineSegments (vertex colors), CSR-adjacency, A* met
  grootcirkel-heuristiek (~3 ms), **passage-restricties** (default `northwest` dicht — searoute's eigen
  default; "Suez dicht" voor M21 = label toevoegen aan `opties.vermijd`).
- **Cache-discipline geldt óók voor data:** `marnet.bin`/`ports.json` dragen `?v=` mee (nu 011); bump bij
  elke nieuwe bake, anders test je tegen de vorige.
- **Valkuil vastgelegd:** MARNET had 15 knopen dubbel op lon ±180 → altijd lon-normaliseren in graafbouw.

## 🌍 Sinds 2026-07-18 — er zijn TWEE codebases, en `v2/` is de actieve

- **Root van de repo = de bevroren v1-atlas.** Blijft live, wordt niet meer aangeraakt. Vanilla JS + globals
  + Three **r128** via script-tags.
- **`v2/` = de nieuwe bouwplaats.** Three **r185**, **ES-modules met importmap**, geen bundler en geen
  build-stap. Draait mee op Pages onder `…/grondstoffen-atlas/v2/`. **Harde regel: buiten `v2/` niets.**

### De lagenordening in v2 (belangrijker dan de bestandsindeling)
1. **De vectorwereld is de WAARHEID** — waar land ophoudt en water begint. Natural Earth 1:10M, één
   `LineSegments`. Hiertegen wordt geverifieerd en straks gerouteerd.
2. **De tegels zijn een SKIN** — Esri World Imagery (of OSM) op het detailniveau dat bij de kijkhoogte past.
   Mooi en handig om plekken te herkennen, maar geen bewijs: de shell is ~9,8 km/pixel en de bron verschilt
   van Natural Earth.
3. **De weergave staat los van beide** — ondergrond (satelliet/kaart/egaal) en kustlijn (aan/uit) zijn
   onafhankelijke schakelaars.

Dit is de directe voortzetting van het ontkoppelingsprincipe hieronder: **één ding = één verantwoordelijkheid.**
Waar v1 één puntenlijst drie taken liet dragen, laat v2 niet één laag tegelijk "mooi" én "waar" zijn.

### Twee dingen die je moet weten vóór je code schrijft in v2
- **lat/lon → 3D volgt EXACT v1's `latLonToVec3`** (`x = cos(lat)·cos(lon)`, `z = −cos(lat)·sin(lon)`). Het
  moet tegelijk kloppen met de UV-afbeelding van `THREE.SphereGeometry` én met wat in M26 uit v1 komt.
- **Zoom rekent in hoogte boven het oppervlak**, niet in afstand tot het middelpunt. Alles wat met zoom
  schaalt (sleepsnelheid, tegelniveau, de opheffing van de kustlijn) hangt aan `getAltitude()`.

## 🏗️ Het leidende architectuurprincipe sinds 2026-07-18 — ONTKOPPELEN

De atlas zat vast in een patch-spiraal: elke fix brak iets anders. Oorzaak was geen reeks bugs maar **één
gekoppelde structuur** — dezelfde puntenlijst bediende drie taken met tegenstrijdige eisen:

| taak | wil | krijgt sinds 18 juli |
|---|---|---|
| **vorm** van de lijn | weinig punten, alleen echte bochten | eigen geometrie (817 punten) |
| **vaarsnelheid** van de schepen | punten gelijkmatig over afstand | `getPointAt` (booglengte) |
| **baan-klem** (vaarbanen) | juist veel punten in nauw water | eigen profiel `wp`, per 20 km |

**Toets bij elke nieuwe wijziging: raakt dit meer dan één van die drie?** Zo ja, ontkoppel eerst. Het bewijs dat
dit klopt: na de ontkoppeling verbeterde *alles tegelijk* — snelheidsvariatie 15,9× → 1,27× (slechtste 47× → 2,3×),
landtreffers 406 → 108, Japan 8 → 0, Baja 21 → 0, Malakka 9 → 0 — terwijl élke eerdere ronde winst op het ene
inruilde tegen verlies op het andere.

**Vaste pipeline (volgorde telt):**
`bake_searoutes.py` (vorm) → `lane_widths.js` (klem-profiel) → `check_corridors.js` (validatie) →
`stamp_assets.js` (**cache-busting — anders ziet Lars niets veranderen**) → `build-standalone.py` (55 checks).

## 🧩 De volgende structurele stap: één gedeeld netwerk (LAR-483)

Corridors worden nu **per haven-paar** gebakken. Daardoor: routes naar dezelfde bestemming bundelen niet
(Lars: *"lijnen gaan uit elkaar terwijl ze dezelfde bestemming hebben naar China"*), dezelfde kapotte edge wordt
steeds opnieuw gerepareerd (7 corridors deelden hetzelfde Baja-trapje), en antipodale paren kiezen willekeurig
een halfrond. **MARNET gemeten:** 15.840 segmenten / 9.646 knopen, segment mediaan 83 km maar **max 3.611 km** →
een **grove graaf, geen waterkaart**; kaal over de bol leggen voorkomt land-treffers níet. De aanpak is het
netwerk **één keer** verzoenen met onze landpolygonen en daarover routeren — dan erven alle 14 grondstoffen die
waterschoonheid, bundelen routes vanzelf, en werkt M21 native (knelpunt = edge eruit).

## 🖥️ Weergave-laag (2026-07-17, bevestigd) — de ondergrond staat nu
Drie fixes live en door Lars bevestigd; hij pauzeerde de pilot er bewust voor. **Wat dit betekent voor de manier
waarop we verder werken:**
- **De kaart is scherp op élke zoomstand en breedtegraad** (LAR-479: `cos(lat)` + budget 96 + midden-naar-buiten).
  Route-beoordeling op mobiel is daardoor betrouwbaarder dan tijdens de vorige pilot-test — een wazige onderhelft
  kon eerder een routefout maskeren.
- **De bol is bestuurbaar ingezoomd** (draaien schaalt met de camera-afstand). Van dichtbij een corridor volgen is nu
  praktisch mogelijk; dat is precies wat de M18-verificatie vraagt.
- **Markers verdwijnen niet meer op tier; `tier` = alleen labels** (LAR-481). De tier-LOD is dus de facto uit voor
  markers — hou daar rekening mee bij nieuwe nodes: **een node krijgt geen zichtbaarheid meer "gratis" van een flow**
  (de `forced`/`usedNodeIds`-uitzondering bestaat niet meer), maar hij verdwijnt ook nooit meer.
- **Vaste knoppen:** `CONFIG.tiles.maxTiles` (noodrem, 96) · `CONFIG.markers.labelZoomByTier` (het échte declutter-
  mechanisme) · `CONFIG.globe.dragSpeed`/`dragRefZoom` (draaigevoel, geankerd op de startzoom).

## ⚡ Stand van de pilot (2026-07-17, avond) — MIDDEN IN DE TEST
Koper vaart volledig op gebakken MARNET-corridors (22 stuks, 26 KB, `data/_searoutes.js`), 3× live op Pages
(t/m `3c801a0`). **Nog geen go:** Lars ziet op mobiel nog routes over Japan (stale-cache-hypothese, morgen
verifiëren) én wil de wereldbal-weergave duidelijker vóór de uitrol. **Principe aangescherpt: "MARNET beslist"** —
corridors kaal haven→haven, óók echte knelpunten niet meer afgedwongen; knelpunt-ringen + laneShape-ankers worden
**afgeleid uit de geometrie** (≤150 km). De milestone-diagnose is onderweg gecorrigeerd: niet "1.090 km omweg"
(antipodaal → 231 km echt) maar **verkeerd geplaatste via-punten** (`wp-taiwan` +1.497 km) en **trapjes** waren het
probleem; winst nu gemeten: zeereizen −9,3%, ratio 1,203→1,091. Twee diepe render-lessen: corridor-reparaties horen
in de **baker** (de-zigzag + landomleiding met kustbuffer, checker `tools/check_corridors.js`) en de **curve-
bemonstering** mag nooit invoerpunten overslaan (adaptief gemaakt in `util.js` — verifieer op de gétekende curve,
niet alleen op de data).

## 🧭 Nu (2026-07-17) — eerst de routes, dan de features

De atlas is **inhoudelijk compleet** (14 grondstoffen, backlog leeg). De volgende stap is bewust **géén 15e
grondstof** maar **route-kwaliteit** — want de drie geplande features **staan erop**: M19-stress telt verkeerd als een
boot "toevallig" langs Hormuz scheert, en M21-simulator liegt als de routes niet écht door Malakka gaan. *Een
impact-teller op verkeerde routes is erger dan geen teller.*

**De routing is aantoonbaar onrealistisch** (audit 2026-07-17). Antofagasta→Shanghai: grote-cirkel 18.526 km ·
searoute (echte lanen) 18.880 km (+2%) · **onze bol 19.970 km (+8%)** — het handgeplaatste vaarpunt **`wp-pac-zuid`**
(26°Z) dwingt **~1.090 km omweg** af. Drie oorzaken in `searoute.js`: **`openRadiusDeg: 1.2`** (~130 km geforceerd
water rond élk knelpunt → A\* vaart dwars over land) · **8-richtingen-A\*** (trapjes) · **grof raster + gretige
heuristiek + géén echte vaarlanen**. De `via`-ketens blijken grotendeels **handmatige compensatie voor een slechte
router**.

**→ M18 · Realistische zeeroutes (searoute)** = routeren over een **echt scheepvaart-lanen-netwerk** (Eurostat
MARNET via het Python-pakket `searoute` 1.6.0): **precompute at build-time, gededupliceerd per haven-paar** (één
gedeelde corridor-cache over alle 14 → je routeert unieke corridors, niet elke flow), polylines in
`data/_searoutes.js`, atlas rendert direct; **netwerk bewaren** zodat M21 een knelpunt blokkeert als *edge eruit →
herrouteren*; **raakt alleen zee-legs** (land/lucht ongemoeid); runtime blijft pure JS, `searoute` = build-dependency.
Bonus: A\* uit de runtime = lichter op mobiel. **Pilot-first: koper** (LAR-474) → go/no-go Lars → dan de andere 13.

**Volgorde:** M18 → M19 (knelpunt-stress) → M20 (China-meta-view) → M21 (disruptie-simulator).
**Open besluit (Lars, bij de pilot):** via-punten op zee-legs opruimen of behouden als hint.
**Harde regel:** vergelijk nooit tegen een kale origin→dest A\*-run — altijd tegen wat `flows.js` werkelijk rendert.

---

*Eerder (2026-07-16 — M17 · Kolen uitgevoerd; richting 14 uitgewerkt, gas M15/diamant M16 parallel):*

## Architectuur (hoe we bouwen)

> ✅ **Modulair = bron van waarheid, in gebruik.** Onderstaande beschrijft de **modulaire** opzet, die nu als
> git-repo in déze projectmap staat (`Projects\General\grondstoffen-atlas`, 2 commits). De M5-fixes zijn erin
> geport. De single-file `atlas-lithium-kobalt.html` op het bureaublad is nog slechts referentie/deploy-build.

- **Vanilla JS + Three.js, geen bundler.** Losse globals-bestanden, vaste laadvolgorde via
  `<script>`-tags in `index.html`.
- **Scheiding:** `config.js` (instellingen) · `geo-data.js` (`LAND_POLYS`) · `src/` (rendering-modules)
  · `data/` (`_registry.js`, `_chokepoints.js` + één bestand per grondstof).
- **Routering:** A\*-algoritme over een **1440×720 land/zee-raster** (0,25°/cel, opgebouwd uit
  `LAND_POLYS` in ~35 ms). Zeeroutes = zee begaanbaar; landroutes = gespiegeld raster.
  - Knelpunten (`_chokepoints.js`) worden als **water geforceerd** (`openRadiusDeg: 1.2`) zodat smalle
    straten (Lombok, Makassar) begaanbaar blijven.
  - **Gewogen A\*** (`heuristicWeight: 1.35`, `maxExpansions: 1500000`) voor lange oceaanroutes.
  - `LAND_LINKS` (Øresund, Storebælt, Fehmarn, Kanaaltunnel, Bosporus) worden als land geforceerd.
  - **Vaarbanen** (`laneShape(t)` in `util.js`): parallelle stromen waaieren onderweg uit maar knijpen
    bij een knelpunt samen tot één punt — precies het beeld waar de atlas om draait.
- **Rendering-details:** schaal op basis van afstand tot boloppervlak (`scaleFor()` in `markers.js`,
  `Math.pow(d/dref, exp)` met `d = camera.z - R`), kaderloze labels met botsingsdetectie
  (prioriteit `tier × 100 − share`), tegellaag (`tiles.js`, Esri/OSM) onder z=6.2, autorotate uit na
  eerste interactie.
- **Tijd:** `voyages.js` + afspeelbalk — schepen/vluchten bewegen over de tijd langs hun gerouteerde pad.
- **Luchtroute-modus (sinds M6):** een **3e route-type** naast zee-A\*/land-A\*. In `flows.js` krijgt
  `mode:"air"` een `&& !airMode`-uitzondering op de A\*-routering en wordt het een **opgetilde great-circle-boog**
  (`flat:false` + `arcStyle`-lift, hoogte ∝ afstand) — óók in de `routes`-weergave. Korte hops blijven
  `road`/`rail` (land-A\*). `makeRouteCurve` schaalde de booghoogte al met de routelengte. Voyages pusht nu
  ship+air; de tijdlijn-teller is resource-bewust ("✈ vluchten" ↔ "⚓ schepen", via `UI.setVoyageNoun`).
- **Optionele lagen via filter (herbruikbaar patroon, nu 5×):** goud-CB, koper-exchange, REE-recycle, olie-reserve, en sinds
  LAR-414 **uranium-`military`** (`type:"military"`/`layer:"secondary"`/`showMilitary`, de militaire kringloop = down-blend/tails/reserves).
  `layer:"cb"`-flows + `type:"cb"`-nodes op
  `filters.showCentralBanks` (goud); `layer:"exchange"` + `type:"exchange"` op `filters.showExchangeStocks` (koper —
  beursvoorraden); sinds M8 `layer:"recycle"` op `filters.showRecycle` (REE — recycling); sinds M11 `layer:"reserve"` +
  `type:"reserve"` op `filters.showReserves` (olie — strategische voorraden/SPR). Alle default uit, in
  `flows.js`/`markers.js`/`main.js` + `ui.js`-chip + `config.js`-marker; de chip verschijnt alleen als een actieve grondstof
  die data heeft. **Nuance bij recycling (M8):** de node-gate zit op `node.layer==="recycle"` (niet op `type==="recycler"`)
  en `hasRecycle()` detecteert op `f.layer==="recycle"` — zo blijft **koper's always-on recycling** (recyclers zónder `layer`)
  ongemoeid en krijgt alleen REE de toggle/chip. De **olie-reserve-laag (M11)** volgt daarentegen exact het `exchange`-patroon
  (eigen `type:"reserve"`, `hasReserves()` op `n.type==="reserve"`) — een dedicated type dat geen andere grondstof gebruikt.
  Kopieer de vier filterplekken + config + ui-chip + marker-vorm voor elke nieuwe laag.
- **Marker-types:** `mine`/`refinery`/`port`/`market` + (M6) `airport`/`hub`/`cb`/`recycler` + (M7) `exchange`
  (koperkleurige CylinderGeometry-spoel, grootte ∝ √`stock`) + (M11) `reserve` (olie-amber tank-cilinder, grootte ∝ √`stock`) in `markers.js`.
- **Single-file build:** `build-standalone.py` genereert `atlas-standalone.html` uit `index.html` (lijnt CSS +
  lokale scripts inline, houdt three.js-CDN extern). Modulair = bron van waarheid; draai het script na wijzigingen.

## Aanpak per grondstof (het sjabloon)

1. **Ontwerp eerst** (op papier/in de sessie): de belangrijkste knopen (mijnen, havens, raffinaderijen,
   fabrieken) en de stromen ertussen, met operators, capaciteiten, transportmodi.
2. **Dan implementeren** in `data/<grondstof>.js` volgens het **lithium-schema** (`data/lithium.js` =
   referentie: 34 knopen, 31 stromen, NL-annotaties, verhaallijn incl. Chinese-raffinage-afhankelijkheid).
3. Registreren in `data/_registry.js`.

**Brief-template:** gebruik `design/_brief-template.md` als vast invulschema voor stap 1 — kopieer naar
`data/<grondstof>.md` en vul alle nodes/stromen in vóór je de `.js` schrijft. De template sluit 1-op-1 aan
op het node/flow-schema (`lithium.md` = het volledig ingevulde voorbeeld).

## Detailniveaus

- **Volledig:** lithium (template), kobalt, **goud** (M6 — 73 nodes/48 flows, luchtroutes + CB-laag),
  **koper** (M7 — 69 nodes/50 flows, China-smelttrechter + Copperbelt-kathode over land + beursvoorraden-laag),
  **uranium** (M9 — 38 nodes/36 flows, 4-staps kernbrandstofketen met verrijking als flessenhals + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering),
  **zeldzame aardmetalen** (M8 — 41 nodes/38 flows, magneet-REE NdPr+Dy/Tb: Ganzhou-scheidingstrechter + Dy/Tb-landstroom Myanmar→China over `grens-ruili` + Mountain-Pass-rondreis + NdFeB-waaier + recycling-toggle),
  **nikkel** (M10 — 50 nodes/46 flows, Indonesië-onshoring-trechter: mijn+raffinage in tien jaar via de exportban + class-1/class-2-splitsing + prijscrash-shakeout + LME-nuance; beursvoorraden-toggle hergebruikt met 0 engine-wijziging),
  **olie** (M11 — 45 nodes/46 flows, het knelpunten-netwerk dat tegelijk oplicht: Hormuz #1 + Malakka + Suez/Bab + Bosporus + Panama + Kaap; géén nieuw chokepoint = eigen aha; Hormuz-bypass-pijpleidingen + Rusland-omleiding 2022→ + VS-schalie-ommekeer; 3 stages erts/raffinaat/petrochemie),
  **zilver** (M13 — 42 nodes/37 flows, de **eerste écht nieuwe grondstof**: géén winnings-trechter — ~70-75% bijproduct van zink/lood/koper/goud (aanbod inelastisch) — terwijl de concentratie downstream zit (Chinese zonnepanelen/PV) → structureel tekort dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt; schip+land, géén nieuw chokepoint; exchange-toggle hergebruikt met 0 engine-wijziging),
  **PGM** (M12 — 38 nodes/41 flows, de scherpste twee-landen/twee-metalen-concentratie: Zuid-Afrika/Bushveld = Pt/Rh + Rusland/Norilsk = Pd; **luchtvracht** (hergebruik goud-air-mode, JNB-gateway) — concentraat/matte over land; géén nieuw chokepoint; recycling-toggle hergebruikt van REE met 0 engine-wijziging; 6 tensions incl. autokat-leiband + Pt↔Pd-substitutie, rodium-spof, waterstof-hedge, Eskom-stroomcrisis),
  **grafiet** (M14 — 31 nodes/26 flows, een REE-achtige **verwerkingstrechter met TWEE feedstocks**: natuurlijk vlokgrafiet + synthetische naaldcokes convergeren op de anode-verwerking die ~90%+ in China zit (Shandong natuurlijk, Binnen-Mongolië synthetisch); zelfs ex-China vlok vaart naar China; dec-2023 China-exportvergunningen; dunne ex-China buildout Syrah Vidalia/Talga/Novonix/NMG/POSCO; schip+land, géén nieuw chokepoint (4e na nikkel/olie/zilver); recycling-toggle hergebruikt REE/PGM-patroon met 0 engine-wijziging, bewust bescheiden),
  **diamant** (M16 — 25 nodes/35 flows, de **scherpste downstream-trechter**: winning verspreid maar ~90-95% geslepen in **één stad (Surat)**; Antwerpen = G7-certificeringsknooppunt met Alrosa-herrouting via Dubai/India; De Beers/Alrosa-duopolie + lab-grown-ontwrichting + waarde-vs-volume; diamant **vliegt** = hergebruik goud/PGM air-mode, 0 engine-wijziging, géén nieuw chokepoint/marker-types; lab-grown-toggle bewust apart in backlog LAR-471),
  **gas** (M15 — 42 nodes/51 flows, aardgas/LNG: **gas is nauwelijks te verplaatsen** → twee gescheiden leversystemen (captive **pijpleiding**-arcs Rusland↔EU/Power of Siberia/Turkmenistan/Noorwegen náást heldere **LNG-oceaan**-arcs), met de **liquefactie-stap als trechter** (VS-Golfkust/Qatar/Australië); Qatar via Hormuz (géén bypass, scherper dan olie); Europa-pivot 2022 + Russische oost-pivot + drie prijszones + Panama-LNG-knelpunt; Iran = reserves≠export; schip+pipeline, géén nieuw chokepoint/render-modus/marker-types; opslag-laag hergebruikt de olie-`reserve`-toggle met 0 engine-wijziging).
- Ook nieuw op "uitgewerkt": **kolen** (M17) uit een parallelle sessie → de atlas telt nu **14 grondstoffen** (basis-10 + zilver + gas + diamant + kolen).
- **Basis:** — **geen** meer. Alle basis-10-grondstoffen staan op "uitgewerkt"; de nieuwe grondstoffen (zilver/gas/diamant/kolen) zijn losse toevoegingen.
- **Volgende kandidaat:** géén basis-grondstof meer. Verder grondstof-werk = alleen nog een *nieuwe 12e+* grondstof (nieuw bestand + script-tag + build-check, zoals zilver).

## Nu (2026-07-15 — M14 · Grafiet uitgevoerd — atlas inhoudelijk COMPLEET)

- **Grafiet volledig gebouwd + geverifieerd — het laatste basis-10-bestand.** `data/graphite.js` van "basis" (10/3) →
  **uitgewerkt** (31 nodes / 26 flows / 6 tensions) + brief `design/grafiet.md` + 5 grafiet-checks in `build-standalone.py`.
  Na M14 staat **geen enkele grondstof meer op "basis"** — alle 11 zijn uitgewerkt.
- **De vorm = een REE-achtige verwerkingstrechter met TWEE feedstocks.** Grafiet is HET anodemateriaal in Li-ionbatterijen
  (~1 kg/kWh). **Natuurlijk vlokgrafiet** (China #1, Balama/Mozambique, Madagascar, Brazilië, Tanzania, +Europa/Sri Lanka) én
  **synthetisch grafiet** (uit petroleum-**naaldcokes**, gegrafitiseerd bij ~3000 °C) convergeren op de anode-verwerking die
  **~90%+ in China** zit (Shandong natuurlijk, Binnen-Mongolië synthetisch). **Zelfs ex-China vlok vaart naar China.** Levende
  geopolitiek: de **China-exportvergunningen op grafiet (dec 2023)**. Dunne ex-China buildout: Syrah Vidalia (Louisiana, uit
  Balama-vlok, IRA-FEOC) + Talga/Novonix/NMG/POSCO.
- **Schip+land, géén nieuwe render-modus, géén nieuw chokepoint** (4e na nikkel/olie/zilver). **Recycling-toggle**
  (`layer:"recycle"`, default uit) = hergebruik van het REE/PGM-patroon met **0 engine-wijziging**, bewust bescheiden
  (batterijgrafiet-recycling nog nascent).
- **Verificatie (headless, poort 8735 — eigen `-4`-server):** grafiet **77 legs (57 zee + 20 land) / 0 kapot / 0 straight /
  0 warnings**; toggle aan = 80 legs (+3 recycle); regressie schoon (0 kapot over álle grondstoffen). Route-bug gefixt
  (`gr-ref-japan→gr-mkt-korea-japan` road→ship). Browser-pane cachete de oude data hardnekkig → verse schijf-data via synchrone
  fetch + `REGISTER`-capture geverifieerd. `atlas-standalone.html` geregenereerd (5 grafiet-checks OK). **Code-commit `34b1ed4`**,
  **gepusht** naar GitHub → live op Pages. **Linear M14 · LAR-449..454** (449–453 Done, 454 In Progress).
- **Repo-correctie:** de repo is **niet** lokaal-only — hij staat op GitHub (`larswalters/grondstoffen-atlas`) en draait live op
  **GitHub Pages** (https://larswalters.github.io/grondstoffen-atlas/); elke `git push origin main` deployt. De "lokaal-only"-
  notities in oudere milestones zijn achterhaald.
- **Rest:** alleen visuele bevestiging op de live URL (LAR-454, Lars). **Geen grondstoffen meer op "basis".**

## Eerder (2026-07-15 — M13 · Zilver uitgevoerd)

- **Zilver volledig gebouwd + geverifieerd — de eerste écht nieuwe grondstof.** Anders dan M6–M12 (die een bestaand
  "basis"-bestand naar "uitgewerkt" brachten) bestond zilver nog niet: nieuw `data/silver.js` (42 nodes / 37 flows /
  6 tensions) + brief `design/zilver.md` + `<script src="data/silver.js">` in `index.html` + 5 zilver-checks in
  `build-standalone.py`. De vorm is **fundamenteel anders**: **géén winnings-trechter** — ~70-75% is **bijproduct** van
  zink/lood/koper/goud (aanbod inelastisch; mijn-nodes = eigenlijk andermans mijnen), terwijl de concentratie **downstream
  aan de vraagkant** zit: de energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie** (PV = grootste + snelst
  groeiende toepassing) → een **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt.
- **Schip+land, géén nieuwe render-modus, géén nieuw chokepoint** (derde na nikkel/olie op de bestaande routekaart). Keten
  op de 3 stages: erts=mijn(bijproduct)→doré/concentraat → raffinaat=good-delivery baar → product=industrieel (solar/
  elektronica/sieraad). Mexico als winning+raffinage-anker (Fresnillo + Peñoles/Torreón). **Kluis-/beursvoorraden-laag** =
  hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (nikkel-patroon, 2e datagedreven hergebruik):
  3 exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows; recycling always-on.
- **Verificatie (headless, poort 8734 — eigen server naast de parallelle uranium-toggle-sessie):** zilver **85 legs / 0 kapot /
  0 straight / 0 warnings**; regressie schoon (andere uitgewerkte grondstoffen 0/0). 2 route-bugs empirisch gefixt (VS-raffinage
  Tacoma→Astoria; China-solar Suzhou→Jiangsu-kust). Exchange-chip "beursvoorraden" + blurb + 6 tensions renderen.
  `atlas-standalone.html` geregenereerd (5 zilver-checks OK). **Code-commit `e091848`** (repo lokaal-only, Claude-trailer;
  alléén eigen bestanden gestaged — de parallelle sessie's engine-files ongemoeid, sectie J). **Linear M13 · LAR-434..438 Done, 439 In Progress.**
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-439, Lars).
- **Volgende grondstof:** grafiet (het laatste van de basis-10; PGM/M12 loopt parallel) — zelfde brief→bouw-flow.

## Eerder (2026-07-15 — M11 · Olie uitgevoerd)

- **Olie volledig gebouwd + geverifieerd.** `data/oil.js` van "basis" (18/15) → **uitgewerkt** (45 nodes / 46 flows /
  6 tensions) + brief `design/olie.md`. Olie's "aha" is bewust **anders dan alle eerdere**: geen enkele trechter maar het
  **hele knelpunten-netwerk dat tegelijk oplicht** — Hormuz #1 (15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama,
  Kaap. Daarom **géén nieuw chokepoint** (olie hergebruikt het volledige bestaande net = het eigen aha); wel 3 olie-only
  navigatie-vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`.
- **Drie levende verhalen bovenop de straten:** de **Hormuz-bypass-pijpleidingen** (Saoedi Oost-West → Yanbu; UAE Habshan →
  Fujairah, `mode:"pipeline"`), de **Rusland-omleiding 2022→** (Europese crude → India/China via Primorsk/Novorossiysk/
  ESPO-Kozmino/Druzhba), en de **Amerikaanse schalie-ommekeer** (Corpus Christi → Atlantische Oceaan). Keten op 3 stages:
  erts=ruwe olie (knelpunten-verhaal) → raffinaat=producten (diesel/benzine) → product=petrochemie (nafta→kraker→kunststof).
  Schip+pijpleiding, **géén nieuwe render-modus**. Kust-raffinaderijen `coastal:true`.
- **Verificatie (headless, poort 8734 — eigen server naast de parallelle nikkel-sessie):** olie **210 legs / 0 kapot /
  0 straight**; regressie schoon (globale baseline 5 = lithium 4 + goud 1, olie voegt 0 toe). `atlas-standalone.html`
  geregenereerd (4 olie-checks OK) + zelf geverifieerd (210/0/0). **Code-commit `1d4ece5`** (repo lokaal-only, Claude-trailer;
  alleen eigen bestanden gestaged). **Linear M11 · LAR-428..433 (4 Done, 432 Backlog, 433 In Progress).**
- **Toegevoegd (na de nikkel-sessie):** de optionele **SPR-voorraden-toggle** (`layer:"reserve"`, LAR-432 **Done**, commit
  `86c8c1f`) — gebouwd zodra de engine-bestanden vrij waren. Het **vierde** optionele-laag-patroon (goud-CB/koper-beurs/
  REE-recycling/olie-reserve), exact het koper-`exchange`-patroon + olie-amber tank-marker. 5 SPR-nodes (US Gulf/China Dalian/
  Japan Kiire/India Mangalore/IEA-EU Le Havre, `stock` in mln vaten) + 5 vul-flows + tension `oil-t-spr`. Headless: olie 232 legs
  / 0 kapot / 0 straight; toggle uit=45/46, aan=50/51; chip "voorraden" alleen bij olie; regressievrij. **Olie is nu volledig
  compleet** (data + optionele laag), gelijk aan goud/koper/REE.
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-433, Lars).
- **Volgende grondstof:** grafiet, PGM — zelfde brief→bouw-flow.

## Eerder (2026-07-15 — M10 · Nikkel uitgevoerd)

- **Nikkel volledig gebouwd + geverifieerd.** `data/nickel.js` van "basis" (13/4) → **uitgewerkt** (50 nodes / 46 flows /
  6 tensions) + brief `design/nikkel.md`. De nikkel-"aha": de **trechter staat op z'n kop** t.o.v. koper — **Indonesië heeft
  in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban op ruw erts** (IMIP Morowali / IWIP Weda
  Bay, Chinees kapitaal Tsingshan/Huayou); het erts blíjft in het land (korte mijn→smelter-hops), pas als NPI/matte/MHP de
  zee op. Plus **twee nikkels** (class-1 batterij/sulfaat vs class-2 roestvrij/NPI, HPAL→MHP/matte als brug), de **prijscrash-
  shakeout** (BHP Nickel West stilgelegd 2024, Nieuw-Caledonië in crisis), de **LME-nuance** (alleen class-1 leverbaar + de
  2022-squeeze) en het **Filipijnse ruw-erts-contrast** (geen ban).
- **Schip+land, géén nieuwe render-modus, géén nieuw chokepoint** (tweede grondstof na koper die volledig op de bestaande
  routekaart draait: Makassar/Lombok/SCS/Taiwan/Deense-Straten/Panama/Saint-Laurent). **Beursvoorraden-laag (LME)** hergebruikt
  de bestaande exchange-toggle van koper met **0 engine-wijziging** (eerste keer dat een optionele laag puur via de data-laag
  wordt hergebruikt); recycling always-on (koper-patroon).
- **Verificatie (headless, poort 8733 — eigen server want een parallelle olie-sessie bezette 8732):** nikkel **91 legs
  (63 zee + 18 land + 10 korte hops) / 0 kapot / 0 straight**; regressie schoon (0 kapot over álle grondstoffen).
  `atlas-standalone.html` geregenereerd (nikkel-checks OK). **Code-commit `08aa4f5`** (repo lokaal-only, Claude-trailer).
  **Linear M10 · LAR-422..426 Done, 427 In Progress.**
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-427, Lars).
- **Volgende grondstof:** grafiet, PGM (olie loopt in een parallelle sessie) — zelfde brief→bouw-flow.

### Eerder (2026-07-15 — M8 · Zeldzame aardmetalen uitgevoerd)

- **Zeldzame aardmetalen volledig gebouwd + geverifieerd.** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt**
  (41 nodes/38 flows/6 tensions), **magneet-REE-framing** (NdPr licht + Dy/Tb zwaar; `symbol: NdPr`, `unit: kt magneet-REO/jaar`).
  De extreemste trechter van de atlas: winning breed verspreid, **scheiding ~85–90% Zuid-China** (Ganzhou/Baotou/Sichuan).
  Vier kern-aha's renderen: Ganzhou-scheidingstrechter, **Dy/Tb-landstroom Myanmar→China** over de nieuwe grenscorridor
  **`grens-ruili`** (`_chokepoints.js`, Kasumbalesa-patroon), **Mountain-Pass-rondreis** (concentraat heen over de Stille
  Oceaan, oxide terug), **NdFeB-magneet-waaier** vanuit China. Plus het dunne Lynas-draadje (Mount Weld→Kuantan→Japan/EU).
  Nieuwe **recycling-toggle** (`layer:"recycle"`, default uit) = het derde optionele-laag-patroon.
- **Headless:** rare-earths **90 legs (39 land + 51 zee) / 0 kapot / 0 straight**; regressievrij (5 kapot = bekende
  lithium/goud-baseline). `atlas-standalone.html` geregenereerd (REE-checks OK). **Linear M8 · LAR-416..420 Done, 421 In Progress.**
- **Rest:** **visuele bevestiging op Netlify/mobiel** (WebGL-screenshot lukt niet headless — LAR-421, Lars).
- **Ook open (uranium, M9):** alleen nog de visuele bevestiging (LAR-415, Lars). De militaire-kringloop-toggle (LAR-414) is nu **Done** (commit `6a6d062`, 5e optionele laag `type:"military"`/`layer:"secondary"`; headless 60 legs/0 kapot/0 straight).
- **Volgende grondstof:** nikkel (runner-up), grafiet, PGM, olie — volgens dezelfde brief→bouw-flow.
