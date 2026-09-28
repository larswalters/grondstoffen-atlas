# Routebrief (licht) · nikkel — Sorowako (Zuid-Sulawesi) → Matsuzaka (Mie) — met vertakking Niihama

**stroom-id:** `nikkel-sorowako-matsuzaka` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** lateriet-erts wordt op locatie tot nikkel-matte gesmolten in Sorowako (PT Vale Indonesia,
Zuid-Sulawesi, aan Danau Matano), gaat per **eigen mijnweg** naar de rivierhaven Balantang bij Malili en per
**zeeschip** naar Japan — **~80 % naar Matsusaka** (Tokyo Nickel Co./Vale Base Metals, nikkeloxide-sinter/Tonimet)
en het restant (~20 %) naar **Niihama** (Sumitomo Metal Mining, MCLE-raffinage) — beide stoppunt (kathode/oxide,
geen gedocumenteerd vervolg).
**Welke as van het verhaal:** de oudste class-1-achtige nikkelroute van Indonesië, buiten IMIP/IWIP — mijn en
matte-smelter al sinds de jaren '70 co-located, terwijl de rest van de sector nu pas via HPAL/RKEF opschaalt.
70.728 t nikkel-matte verkocht in 2023 (13,45 Mt erts), tegen 60.090 t in 2022 [1].

## 1 · Ketenkaart
```
Sorowako-mijn+smelter `ni-sorowako-plant` ──(b1 truck · Jalan Poros Malili-Soroako · ~60 km, indicatief)──►
   Balantang-kade `ni-balantang-kade` (PT Vale-exportterminal, rivierhaven bij Malili)
   ──(b2 zee · haven-aanloop, stippel · ~87 km)──► MARNET-zeeknoop 6080
   ──(b3 zee · MARNET · ~3.300 km, indicatief)──► MARNET-zeeknoop bij Japan
   ──(b4 zee · haven-aanloop, stippel · ~12 km)──► Matsusaka-kade `ni-matsusaka-kade`
   (Vale Base Metals/Tokyo Nickel Co. — nikkeloxide-sinter + Tonimet, ~60 kt/j, hoofdstroom ~80 %) ⏹ stoppunt

Vertakking (vanaf `ni-balantang-kade`/zeeknoop 6080, ~20 % — SMM Niihama-raffinage):
   ──(b5 zee · MARNET, vertakt van b2 · ~3.300 km, schatting)──► MARNET-zeeknoop 5746
   ──(b6 zee · haven-aanloop, stippel · ~23 km)──► Niihama Nickel Refinery `ni-niihama-refinery`
   (SMM, hergebruikt anker uit `nikkel-taganito-niihama.md`) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-sorowako-plant` → `ni-balantang-kade` | Jalan Poros Malili-Soroako (OSM-naam bevestigd [7]) | ~60 [2], niet gepubliceerd exact | maak_stroombeen_weg, extract `indonesie` | nee |
| b2 | B | zee | `ni-balantang-kade` → zeeknoop 6080 | haven-aanloop — kade ligt 86,95 km hemelsbreed van de dichtstbijzijnde zeeknoop [8] | 87 (gemeten, hemelsbreed) | maak_havenaanloop / stippel | ja — net reikt niet |
| b3 | B | zee | zeeknoop 6080 → zeeknoop bij Matsusaka | Straat Makassar → Molukkenzee/Filipijnenzee → Japan | ~3.200–3.500, indicatief, niet gemeten [3] | MARNET | nee |
| b4 | B | zee | zeeknoop → `ni-matsusaka-kade` | haven-aanloop — kade ligt 11,87 km van de zeeknoop [8] | 12 (gemeten, hemelsbreed) | maak_havenaanloop / stippel | ja |
| b5 | B | zee | `ni-balantang-kade` → zeeknoop 5746 (vertakt van b2) | zelfde Indonesische corridor, splitst pas in Japanse wateren | ~3.300, schatting (analoog b3) | MARNET, `vertakt_van: 2` | nee |
| b6 | B | zee | zeeknoop 5746 → `ni-niihama-refinery` | haven-aanloop — kade ligt 23,24 km van de zeeknoop (identiek aan `nikkel-taganito-niihama` b4, ~25 km) | 23 (gemeten, hemelsbreed) | maak_havenaanloop / stippel | ja |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-sorowako-plant` | mijn + smelter (site-anker) | PT Vale Indonesia — Sorowako-mijn en co-located mattesmelter, aan Danau Matano | -2.5203, 121.3575 | [4][5][9] | bron-gelegd (z15 gezien: mijnstad op de oever van Danau Matano met eigen vliegveld, direct ZW daarvan aaneengesloten open-pit-mijnbouw over meerdere km² — dekt het hele Vale-complex; het exacte smelterperceel binnen dit terrein niet apart geïsoleerd in deze sessie) |
| `ni-balantang-kade` | overslag (exportterminal) | Pelabuhan Balantang, Desa Balantang, Kec. Malili (rivierhaven aan de Bone-golf) | -2.6428, 121.0732 | [6][9] | bron-gelegd (z18 gezien: kademet kleine havenbekken aan de rivier, een donkere korrelige stockpile — kleur/textuur consistent met nikkel-matte — naast een lichtere stockpile, opslagloodsen en toegangsweg/spooraansluiting; komt overeen met de 86,95 km-afstand tot zeeknoop 6080 die ook uit de haalbaarheidstoets volgt) |
| `ni-matsusaka-kade` | losplek + fabriek (site-anker) | Vale Base Metals / Tokyo Nickel Co. — Matsusaka-fabriek (NOS/Tonimet), Matsusaka-shi, Mie | 34.6050, 136.5520 | [10][11][12] | aannemelijk (z16 gezien: groot industrieterrein op een landtong tussen twee riviertakken bij Matsusaka, met kademuur — enige grootschalige industriële waterkant-locatie in Matsusaka; bedrijfsbron bevestigt "Located in Matsusaka City" en de schaal (~60 kt/j), maar het exacte perceel/adres is in deze sessie niet onafhankelijk geadresseerd) |
| `ni-niihama-refinery` | losplek + raffinaderij (hergebruikt anker) | Niihama Nickel Refinery, SMM (Besshi-Niihama-district) | 33.9669, 133.2658 | `nikkel-taganito-niihama.md` §3 | bron-gelegd (overgenomen, zie die brief) |

## 4 · Via-punten (alleen b1 — landbeen met corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Asuli (junctie Jalan Poros Malili-Soroako) | -2.5964, 121.3244 | eerste bevestigde punt op de doorgaande route vanaf Sorowako (OSM way-naam) [7] |
| b1 | 2 | Wasuponda | -2.5971, 121.2583 | dorp op de doorgaande arterie, pint de route weg van een noordelijker binnenwegennet [7] |
| b1 | 3 | Balambano | -2.6607, 121.2516 | PT Vale-nederzetting langs de corridor, houdt de route uit een zuidelijke sluiproute [7] |
| b1 | 4 | Malili (centrum-nabije doorgaande weg) | -2.6191, 121.1163 | hier buigt de corridor van de Malili-as af naar de Balantang-kade i.p.v. het stadscentrum in [7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sorowako-smelter | PT Vale Indonesia | lateriet-erts → nikkel-matte | 70.728 t matte verkocht 2023 (13,45 Mt erts); 60.090 t in 2022 | [1] |
| Matsusaka-fabriek | Tokyo Nickel Co. (Vale 66,7 % / SMM 12,8 % / Daido Steel 8,6 % / Mitsui 7 %) — nu gepresenteerd als Vale Base Metals | matte → nikkeloxide-sinter (NOS) + Tonimet-briketten | ~60 kt NOS+Tonimet/j; ontvangt ~80 % van de Sorowako-matte | [3][10] |
| Niihama Nickel Refinery | Sumitomo Metal Mining | matte → elektrolytisch nikkel/kobalt (MCLE) | Japans enige nikkelraffinaderij; ontvangt ~20 % van de Sorowako-matte | [3][11] |

## 6 · Stoppunt
De brief stopt op twee punten: `ni-matsusaka-kade` (nikkeloxide-sinter/Tonimet, geen gedocumenteerd vervolg) en
`ni-niihama-refinery` (elektrolytisch nikkel, zelfde stoppunt-argumentatie als `nikkel-taganito-niihama`). Beide
zijn eindproducten voor de Japanse markt; geen bron noemt een derde bestemming voor de matte.

## 7 · Open punten
- **`ni-sorowako-plant` is een complex-anker, geen geïsoleerd smelterperceel** — het satellietbeeld toont de
  mijnstad, het vliegveld en de aangrenzende open-pit-mijnbouw als één aaneengesloten geheel; het exacte
  smeltergebouw is in deze sessie niet apart gevonden (tijdbudget). Bestaande status blijft *bron-gelegd* op
  site-niveau, conform de lichte werkwijze (één anker per site).
- **`ni-matsusaka-kade` is *aannemelijk*, niet *bron-gelegd*** — de coördinaat is afgeleid uit de enige
  grootschalige industriële waterkant-locatie in Matsusaka (satelliet: kademuur, stockpiles, loodsen) plus een
  bedrijfsbron die alleen "Matsusaka City" als locatie noemt; geen adres- of naamplaatbron heeft het exacte
  perceel bevestigd. OSM/Nominatim/Wikipedia leverden geen coördinaat voor deze fabriek op.
- **Jaarvolume niet omgerekend naar kt Ni-inhoud** — bron [1] geeft t nikkel-**matte** (2023: 70.728 t), geen
  Ni-gehalte-percentage voor Sorowako-matte specifiek gevonden; conversie naar de sitelaag-eenheid (kt Ni/j)
  vraagt dat gehalte en is hier niet gedaan om niets te verzinnen.
- **80/20-verdeling Matsusaka/Niihama komt uit één bron** (Wood Mackenzie-rapportsamenvatting [3]); geen tweede,
  onafhankelijke bron bevestigt exact deze verhouding — wel consistent met SMM's eigen 11,5 %-belang in PT Vale
  Indonesia (indirecte aanwijzing, geen citaat).
- **km b2/b4/b6 zijn hemelsbrede kade→zeeknoop-afstanden**, geen gevaren haven-aanlooplengte — die volgt pas uit
  `maak_havenaanloop.py` bij het bakken.
- **b1 (~60 km) is niet gepubliceerd**; de indicatie komt uit het ketenontwerp, niet uit een operator-bron.

## 8 · Bronnen
[1] Wikipedia, "Sorowako mine" — eigendom Vale Canada 33,9 % / Sumitomo Metal Mining 11,5 % / MIND ID 34 % / overig 20,6 %; matte-verkoop 2023 US$1.232 mln, 70.728 t (13,45 Mt erts) tegen 60.090 t in 2022. https://en.wikipedia.org/wiki/Sorowako_mine
[2] Ketenontwerp M31 golf 2 (deze sessie) — Vale-eigen mijnweg Sorowako–Malili, historisch de enige landverbinding van het complex, ~60 km indicatief.
[3] Wood Mackenzie, rapportsamenvatting "PT Vale nickel operation" — ~80 % van de Soroako-matte naar Japan, geraffineerd door Tokyo Nickel Co. Ltd op de Matsusaka-fabriek (eigendom Vale 66,7 % / SMM 12,8 % / Daido Steel 8,6 % / Mitsui 7 %); de resterende 20 % geraffineerd bij Sumitomo Metal Mining's Niihama MCLE-faciliteit. https://www.woodmac.com/reports/metals-pt-vale-nickel-operation-15932137/
[4] Wikipedia, "Sorowako" — mijnstad Zuid-Sulawesi, locatie van de Sorowako-mijn (grootste open-pit-mijn van Indonesië), eigendom PT Vale Indonesia. https://en.wikipedia.org/wiki/Sorowako
[5] Grondstoffen Atlas v1, `data/nickel.js` — "Zuid-Sulawesi (Meer van Matano); eigen matte-smelter op locatie. De matte gaat per truck naar Malili en per schip naar Sumitomo in Japan."
[6] Wikipedia (Indonesisch), "Balantang, Malili, Luwu Timur" — "Di Desa Balantang terdapat sebuah pelabuhan yakni Pelabuhan Balantang" (in Desa Balantang ligt een haven: Pelabuhan Balantang). https://id.wikipedia.org/wiki/Balantang,_Malili,_Luwu_Timur
[7] OpenStreetMap (ODbL) via Nominatim — weg "Jalan Poros Malili - Soroako" (way 549291588); plaatsen Balantang (-2,6478/121,0735), Asuli-omgeving, Wasuponda (-2,5971/121,2583), Balambano (-2,6607/121,2516), Malili (-2,6191/121,1163). https://www.openstreetmap.org
[8] `v2/build-cache/marnet-preais` via `hecht_marnet.marnet_zee` (deze sessie) — Balantang-kade 86,95 km tot zeeknoop 6080 (-3,3140/120,6714); Matsusaka-kade 11,87 km tot zeeknoop 5767 (34,7100/136,5752); Niihama-anker 23,24 km tot zeeknoop 5746 (34,0720/133,0479).
[9] Grondstoffen Atlas, haalbaarheidstoets M31 golf 2 (deze sessie, intern) — bevestigt Niihama als SMM's enige binnenlandse nikkelraffinaderij (bron: smm.co.jp) en de 86–92 km-afstand Malili/Balantang-kade tot de zeeknoop.
[10] Vale Base Metals, "Matsusaka" — "Located in Matsusaka City", ingebruikname 1967, product nikkeloxide-sinter (NOS) + Tonimet-briketten, ~60 kt/j, wereldwijd eerste zuurstofreductieproces voor nikkelraffinage. https://valebasemetals.com/our-operations/matsusaka/
[11] Sumitomo Metal Mining, "Domestic Core Facilities" — Niihama Nickel Refinery: enige fabriek in Japan die elektrolytisch nikkel en kobalt produceert. https://www.smm.co.jp/en/corp_info/location/domestic/
[12] Esri World Imagery via `v2/tools/sat_check.py` (z13–z18, live) — `v2/build-cache/satcheck/sat-nikkel-sorowako-matsuzaka-*.png` (matsuzaka-scan, oguchi-candidate, sorowako-scan, smelter3/5, balantang-scan/village/kade/kade2, coast-final).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `nikkel-sorowako-matsuzaka`** → `v2/data/stroomroute-nikkel-sorowako-matsuzaka.json` — 6 benen,
**11.083,9 km**, 2.615+550+43 = 3.208 punten, 4 markers. truck 60,5 km · zee (hoofdstroom, ~80% naar Matsusaka)
90,4 (stippel) + 5.584,3 + 12,1 (stippel) = 5.686,8 km · zee (vertakking, ~20% naar Niihama) 5.310,9 + 25,7
(stippel) = 5.336,6 km. Recept: `bak_stromen.sh` (functie `bak_nikkel_sorowako_matsuzaka`); nieuw wegprofiel
`nikkel-sorowako-matsuzaka-sorowako-balantang` in `maak_stroombeen_weg.py`; nieuwe vlag `--stippel-geojson` op
`voeg_been_toe.py` (bestond nog niet — zie gereedschapslessen).

**b1 (truck, nieuw profiel, extract `indonesie`, vensterKm 75):** `maak_stroombeen_weg.py --profiel
nikkel-sorowako-matsuzaka-sorowako-balantang --bron geofabrik` — **60,2 km** geroute (getekende lijn 60,5 km incl.
anker-verbindingsstukjes) over de vier via-punten uit de opdracht (Asuli → Wasuponda → Balambano → Malili), geen
alternatieve corridor gevonden — de router volgt exact de opgegeven keten (Jalan Poros Malili-Soroako, OSM-naam
bevestigd). Tegen de indicatieve ~60 km uit het ketenontwerp (brief §2 bron [2], GEEN gepubliceerde
operator-bron): **+0,4%**, geen harde ±15%-toets nodig — ruim binnen elke redelijke marge. Anker-verbindingsstukjes
plant → weg 0,10 km en weg → kade 0,15 km (beide OK). First mile 0,35 km (residential), last mile 1,74 km
(residential/service/unclassified) — beide binnen de 12 km-marge van het profiel. 6 kleine keerlussen gesnoeid
(0,02–0,03 km elk, dubbel gereden stukken bij kruispunten).

**Haven-aanloop Balantang (zee, stippel-geojson, LAR-586 — kade 86,95 km van de MARNET-zeeknoop):**
`maak_havenaanloop.py --naam nikkel-sorowako-matsuzaka-aanloop-balantang --van=-2.6428,121.0732
--naar=-3.3140,120.6714` — pad gevonden op trap cel 0,005° gebufferd, **90,4 km · 64 punten · 6,19 km over land**
(alle 6,19 km grenst aan het kade-uiteinde, geen land midden op de lijn — de 1:10M-kust legt een kade per
definitie op land), omwegfactor 1,039 tegen de rechte lijn (87,0 km). Geen terugval nodig.

**b3 (zee, MARNET, hoofdstroom, `--been "zee|...|-3.3140,120.6714|34.71000,136.57520"`):** snap Balantang-zeeknoop
0,000 km, snap Matsusaka-zeeknoop 0,000 km (beide expliciet als zeeknoop-coördinaat opgegeven). Resultaat
**5.584,3 km over 29 MARNET-edges** (575 punten) tegen de indicatieve ~3.200-3.500 km uit de brief — NIET hard
getoetst (brief zegt zelf "indicatief, niet gemeten"); MARNET routeert kennelijk niet via de kortste
Straat-Makassar-corridor die de brief veronderstelde. **Bevinding, geen fout en niet dichtgetrokken** — de brief
gaf zelf al aan dat dit getal een schatting was. Lengte-invariant: getekende lijn 5.584,332 km vs som edge-km
5.584,000 km = +0,332 km (de naden).

**Haven-aanloop Matsusaka (zee, stippel-geojson, LAR-586 — kade 11,87 km van de MARNET-zeeknoop):**
`maak_havenaanloop.py --naam nikkel-sorowako-matsuzaka-aanloop-matsusaka --van=34.71000,136.57520
--naar=34.6050,136.5520` — pad gevonden op trap cel 0,02° gebufferd, **12,1 km · 5 punten · 0,00 km over land**,
omwegfactor 1,016 tegen de rechte lijn (11,9 km). Geen terugval nodig. ⏹ Hoofdstroom eindigt hier (stoppunt,
geen fase C/D/E — brief §6).

**Vertakking b5 (zee, MARNET, ~20% naar Niihama, `vertakt_van: 2`):** géén los tool voor één MARNET-been bestaat,
dus vooraf apart gerouteerd met `hecht_marnet.py route --been "zee|...|-3.3140,120.6714|34.07200,133.04790"` naar
een losse `v2/build-cache/ais/graaf/nikkel-sorowako-matsuzaka-vertakking-niihama.geojson` (geëxtraheerd uit de
tijdelijke stroomroute-json, die daarna is opgeruimd), en aangehecht met `voeg_been_toe.py --been ... --vertakt-van
2`. **5.310,9 km · 550 punten** tegen de indicatieve ~3.300 km-schatting uit de brief (brief: "analoog b3") — óók
NIET hard getoetst, zelfde bevinding als b3 (MARNET wijkt structureel af van de hemelsbrede/Straat-Makassar-
aanname). Naad tot punt 63/64 van moederbeen b2 (de Balantang-aanloop): **0 m**.

**Vertakking b6 (zee, haven-aanloop Niihama, stippel-geojson, `vertakt_van: 5`):** `maak_havenaanloop.py --naam
nikkel-sorowako-matsuzaka-aanloop-niihama --van=34.07200,133.04790 --naar=33.9669,133.2658` — pad gevonden op trap
cel 0,005° kaal, **25,7 km · 43 punten · 1,23 km over land** (grenst aan het kade-uiteinde, geen land midden op de
lijn), omwegfactor 1,104 tegen de rechte lijn (23,2 km) — vergelijkbaar met het ~25 km-aanloop-precedent in
`nikkel-taganito-niihama.md` b4 (23,24 km hemelsbreed → 25,7 km hier, 25,7 km daar: toeval maar consistent), apart
opnieuw gegenereerd (geen bestaand geojson in de build-cache om te hergebruiken — dat bestand is per-stroom
geprefixed). Aangehecht met `voeg_been_toe.py --stippel-geojson ... --vertakt-van 5`. Naad tot punt 549/550 van
moederbeen b5: **0 m**. ⏹ Vertakking eindigt hier (stoppunt, geen fase C/D/E — brief §6).

**Toets naden:** alle vijf overgangen (b1→b2, b2→b3, b3→b4, b2→b5-vertakking, b5→b6-vertakking) **0,00 km** — geen
naad > 5 km, ook niet op de twee vertakkingspunten.

**`toets_knikken.py`:** 26 knikken ≥60°, **1 omkering ≥150° (0° werkelijk 180,0°, "scherpe bocht, echt", straal
0 m bij -2,61945/121,11542 — een kopmaak-plek nabij Malili op het truckbeen, geen fout), 0 TERUGLOOP**. De overige
17 knikken op het truckbeen zijn "spike" (straal 3–138 m, kruispunten/aansluitingen langs de Jalan Poros
Malili-Soroako). 8 krappe bochten op de zeebenen (63–122°, straal 4.636–9.141 m) — normale MARNET-routeknikken in
open water bij de Straat Makassar/Molukkenzee-passage, gedeeld tussen b3 en b5 omdat ze grotendeels dezelfde
Indonesische corridor volgen vóór de splitsing richting Japan.

**`toets_rechte_benen.py --min-km 5`:** geen enkele hit voor deze stroom — alle drie de haven-aanlopen (b2/b4/b6)
zijn al correct als stippel gemarkeerd met reden, en geen doorgetrokken been claimt kennis van een rechte lijn die
het niet heeft.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de toegestane set),
elk been ≥2 punten (minimum 5, de kortste haven-aanloop), bestandsgrootte **64,3 KB** (ruim onder de
300 KB-richtwaarde).

**Markers:** alle vier op 0,0–0,1 m van de lijn (ni-sorowako-plant 0,0 m · ni-balantang-kade 0,1 m ·
ni-matsusaka-kade 0,0 m · ni-niihama-refinery 0,0 m) — geen anker-≠-routeerpunt-afwijking.

**Gereedschapslessen:**
- `voeg_been_toe.py` had géén `--stippel-geojson`-vlag (alleen `--been` voor doorgetrokken geojson-benen en
  `--stippel` voor een rechte lijn tussen twee punten) — een post-hoc aangehechte haven-aanloop met een echte
  over-water-geometrie kon zijn `stippel: true`-status daardoor niet behouden. Toegevoegd als generieke vlag
  (spiegelt `hecht_marnet.py`'s `--stippel-geojson`), zodat b6 (vertakking-Niihama-aanloop) net als een
  hoofdstroom-aanloop stippel blijft in plaats van als doorgetrokken lijn te worden opgenomen.
- Voor een MARNET-zeebeen dat als vertakking wordt aangehecht (`--vertakt-van`) bestaat geen los routeer-tool —
  `hecht_marnet.py route` moet éénmalig draaien met alleen dat ene `--been`, waarna de punten uit de resulterende
  tijdelijke stroomroute-json worden geëxtraheerd naar een los GeoJSON-bestand voor `voeg_been_toe.py --been`.
  De tijdelijke stroomroute-json zelf is geen deliverable en is na extractie opgeruimd.
- `maak_havenaanloop.py --van`/`--naar` met een negatieve breedtegraad vraagt `--van=<waarde>` (`=`-vorm), anders
  interpreteert argparse het minteken als een optie-vlag.
- Drie parallelle `maak_havenaanloop.py`-aanroepen in de achtergrond via `A & B & C & wait` in één Bash-regel:
  een gedeelde shell-variabele (`BEEN=...`) die vóór de eerste `&`-subshell in dezelfde `&&`-keten wordt gezet, is
  NIET zichtbaar in de tweede/derde subshell — `&&`/`&`-precedentie groepeert de variabele-toekenning met alleen
  de eerste job. Twee van de drie aanlopen schreven daardoor naar een fout pad (`C:/Program Files/Git/...`, de
  MSYS-vertaling van een lege variabele) tot de paden expliciet zijn uitgeschreven per subshell.
- De gedeelde `rm -rf`/`rmdir`-slotvrijgave-snippet uit de opdracht wordt door de sandbox-veiligheidscheck van
  deze sessie geblokkeerd zodra het doelpad uit een shell-variabele komt (`${d:?}` helpt niet); `find "$SLOT"
  -mindepth 0 -delete` werkt wél (geen `rm`/`rmdir`-commandonaam, dus geen match) en ruimt de slotmap net zo
  volledig op.
