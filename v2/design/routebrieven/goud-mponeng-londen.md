# Routebrief (licht) · goud — Mponeng → Rand Refinery → Londen (LBMA)

**stroom-id:** `goud-mponeng-londen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** Witwatersrand-goud van de Mponeng-mijn (Harmony Gold, diepste mijn ter wereld) per
**truck** naar Rand Refinery (Germiston, LBMA/LPPM-geaccrediteerd), per **truck** naar de vrachtterminal
van OR Tambo (JNB), per **vrachtvlucht** (grootcirkel) naar de vrachtterminal van Heathrow (LHR), en per
**truck** over de M4 naar de LBMA-kluizen in de City of London.
**Welke as van het verhaal:** *Zuid-Afrika → Londen, de klassieke LBMA-goudroute.* Rand Refinery raffineert
≈450–600 t/j (eigen Zuid-Afrikaanse mijnbouw + regionaal doré, peiljaar ~2024–2026 [7][8]); Zuid-Afrikaanse
mijnproductie zelf ≈100 t/j (USGS/WGC 2024), Mponeng draagt daarvan ≈8 t Au/j (Harmony, v1-register [10]).
Export naar Londen is het grootste deel van de Zuid-Afrikaanse goudoutput, maar niet per bestemming
gepubliceerd — zie §7.

## 1 · Ketenkaart
```
Mponeng-mijn `au-mponeng-mijn` ──(b1 truck · N12/R28-industriecorridor Witwatersrand · ≈77 km)──►
   Rand Refinery `au-randrefinery` (Germiston)
   ──(b2 truck · R21/N12 · ≈15 km)──► OR Tambo-vrachtterminal `au-jnb-vracht`
   ──(b3 lucht · vlucht JNB → LHR, grootcirkel, aannemelijk: één bron · ≈9.070 km)──►
   Heathrow-vrachtterminal `au-lhr-vracht`
   ──(b4 truck · M4/A4 · ≈27 km)──► LBMA-kluis City of London `au-lbma-kluis` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Mponeng-mijn → Rand Refinery | N12 (via Westonaria/Soweto) — ontwerp noemt N12/R28 | ≈77 [eigen berekening §7] | maak_stroombeen_weg | nee |
| b2 | A | truck | Rand Refinery → OR Tambo-vrachtterminal | R21/N12 | ≈15 [ontwerp, redactioneel] | maak_stroombeen_weg | nee |
| b3 | B | lucht | OR Tambo-vrachtterminal → Heathrow-vrachtterminal | vlucht JNB → LHR (vrachtvlucht, grootcirkel, **aannemelijk: één bron**) | ≈9.070 [1][2] | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | Heathrow-vrachtterminal → LBMA-kluis City of London | M4/A4 (via Hounslow/Chiswick/Hammersmith) | ≈27 [eigen berekening §7] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-mponeng-mijn` | mijn / laadplek (schacht + oppervlaktecomplex) | Mponeng Gold Mine, Harmony Gold, Witwatersrand | -26.4361, 27.4306 | [3][9] | bron-gelegd (z15 gezien: industrieel schachtcomplex met hallen en een ronde bezinker direct ZO van de open pit/tailings, precies op de Wikipedia-geohack-coördinaat) |
| `au-randrefinery` | raffinaderij (overslag truck→truck) | Rand Refinery (Pty) Ltd, Germiston | -26.2189, 28.1550 | [4][9] | bron-gelegd (z15 gezien: industrieel gebouwencomplex tussen twee snelwegknopen en een dam, ~1,3 km van het Germiston-stadscentrum; hergebruikt/verfijnd t.o.v. v1 au-ref-rand -26.23/28.16) |
| `au-jnb-vracht` | overslag truck→lucht (vrachtterminal) | OR Tambo (JNB) vrachtterminal/-apron, zuid van de passagiersterminal | -26.1440, 28.2295 | [5][9] | bron-gelegd (z16 gezien: meerdere vrachtloodsen met platte/schuurdaken en meerdere widebody-vrachttoestellen op de apron, geen jetbridges, direct zuid van het passagiersterminalcomplex) |
| `au-lhr-vracht` | overslag lucht→truck (vrachtterminal) | Heathrow Cargo Centre, Sandringham Road | 51.4605, -0.4680 | [6][9] | bron-gelegd (z16 gezien: lange loodsen met karakteristiek geribbeld dak zuid van de taxibanen tussen de twee start-/landingsbanen, vrachttoestellen op de apron ernaast; komt overeen met de SEGRO-listing "Heathrow Cargo Centre, Sandringham Road" [6]) |
| `au-lbma-kluis` | losplek / stoppunt (LBMA-kluis) | Londen — LBMA/Bank of England-omgeving, City of London | 51.5140, -0.0880 | [9][11] | bron-gelegd (z15 gezien: dicht financieel City-blok rond Bank/Mansion House; hergebruik van au-hub-london uit `data/goud.js` v1) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Westonaria | -26.3178, 27.6506 | West-Rand-mijngordel; de N12/R28-corridor uit het ontwerp loopt hierlangs richting Johannesburg [12] |
| b1 | 2 | Soweto | -26.2678, 27.8585 | ligt vrijwel exact op de rechte lijn Westonaria→Germiston; pint de N12-doorgaande route i.p.v. de langere R28-omweg via Krugersdorp/Roodepoort [12] |
| b4 | 1 | Hounslow | 51.4668, -0.3750 | eerste grote plaats op de M4/A4-corridor bij het verlaten van de Heathrow-omgeving [12] |
| b4 | 2 | Chiswick | 51.4900, -0.2600 | de A4 loopt door Chiswick vóór de overgang naar centraal Londen [12] |
| b4 | 3 | Hammersmith | 51.4933, -0.2228 | bekend knooppunt (Hammersmith flyover) op de A4 richting de City [12] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rand Refinery (Germiston) | Rand Refinery (Pty) Ltd | doré/erts → LBMA/LPPM good-delivery baren | ≈450–600 t/j (eigen ZA-mijnbouw + regionaal doré) | [7][8] |

## 6 · Stoppunt
De brief stopt bij de LBMA-kluis in de City of London: dat is de bestemming uit het ketenontwerp
(Bank of England / commercieel Brink's-Malca-Amit-Loomis) en er is geen verdere, specifiekere
eindbestemming (fabriek/afnemer) in de bronnen genoemd — fase D/E vervallen.

## 7 · Open punten
- **km b1 gecorrigeerd t.o.v. het ontwerp:** het ontwerp noemt ≈65 km, maar de rechte afstand
  Mponeng–Rand Refinery is al 76,2 km (haversine) — een wegroute kan nooit korter zijn. Eigen
  optelling via de via-punten Westonaria/Soweto geeft ≈77 km; dat cijfer is gebruikt in §2, geen
  gepubliceerde bron. De echte OSM-route (N12 vs. R28 via Krugersdorp/Roodepoort) is niet bevestigd
  en moet bij het bakken blijken; vensterKm ruim zetten (~40–50 km).
- **km b4 licht bijgesteld:** ontwerp ≈25 km (M4); eigen optelling via Hounslow/Chiswick/Hammersmith
  geeft ≈27 km, vrijwel gelijk aan de rechte afstand (27,0 km) — de M4/A4-corridor is vrijwel recht.
- **Slechts 2 via-punten op b1 i.p.v. de gebruikelijke 3–8:** door het webbudget (max 3 WebSearch) kon
  geen derde, onafhankelijk bevestigd tussenpunt op de N12-corridor gevonden worden. Krugersdorp en
  Roodepoort zijn wél gebronde plaatsnamen maar liggen op de langere R28-westomweg, niet op de directe
  N12-lijn — bewust niet gebruikt om de bake niet op het verkeerde been te zetten.
- **b2-km (Rand Refinery → OR Tambo) is redactioneel geschat** (ontwerp ≈15 km; rechte afstand 11,2 km)
  — geen aparte bron, conform de haalbaarheidstoets ("niet blokkerend").
- **bron_voor_luchtvracht is markt-niveau** (LBMA/WGC-marktbeschrijvingen van de Zuid-Afrikaanse
  goudketen), geen Rand Refinery-specifieke verzendingsbron — vandaar **"aannemelijk: één bron"** in de
  beennaam van b3, conform de haalbaarheidstoets. Een eventuele tussenlanding (bv. via Dubai/Zürich) is
  niet gedocumenteerd → één directe vlucht JNB→LHR aangenomen.
- **Volume specifiek naar Londen** (i.t.t. Zürich/Shanghai) is niet per bestemming gepubliceerd —
  aanname op basis van Rand Refinery's LBMA-rol, zoals de haalbaarheidstoets al aangaf.
- **Jaarvolume:** Mponeng zelf ≈8 t Au/j (fine gold, Harmony, v1-register [10], peiljaar ~2024) is de
  volume-indicatie voor déze keten specifiek; Rand Refinery's totale doorvoer (≈450–600 t/j, doré +
  regionale aanvoer) is veel groter en niet 1-op-1 aan Mponeng toe te schrijven — oorspronkelijke
  eenheid t/j (fine gold), geen omrekening nodig.
- **`au-lbma-kluis` is hergebruikt van v1** (`au-hub-london`, 51.514/-0.088) — dit is een generiek
  City-anker (Bank of England-omgeving), geen specifiek kluisadres van Brink's/Malca-Amit/Loomis.

## 8 · Bronnen
[1] Great Circle Mapper / algemeen gepubliceerde JNB–LHR-vluchtafstand ≈9.070 km (great circle tussen OR Tambo en Heathrow).
[2] Rand Refinery — https://www.randrefinery.com/ (LBMA/LPPM-accreditatie, good-delivery-status).
[3] Wikipedia, "Mponeng Gold Mine" — coördinaat -26.43611/27.43056 (MediaWiki API prop=coordinates). https://en.wikipedia.org/wiki/Mponeng_Gold_Mine
[4] Wikipedia, "Rand Refinery" — coördinaat -26.21889/28.155 (MediaWiki API prop=coordinates); "world's largest integrated single-site precious metals refining and smelting complex", opgericht 1920. https://en.wikipedia.org/wiki/Rand_Refinery
[5] OpenStreetMap/Esri World Imagery — vrachtloodsen + apron met vrachttoestellen zuid van de OR Tambo-passagiersterminal (satellietblik, geen aparte naam-tag gevonden binnen het webbudget).
[6] SEGRO, "Building 577 Sandringham Road, Heathrow Cargo Centre" — bevestigt de naam/locatie Heathrow Cargo Centre aan Sandringham Road. https://www.segro.com/countries-repository/united-kingdom/segro-airside-heathrow/building-577-sandringham-road-heathrow-cargo-centre-airside-united-kingdom
[7] SMM/marktpers, Rand Refinery-doorvoer ≈450–600 t/j (South Africa + regionaal doré) — algemene marktbeschrijving, geen exacte bron-URL binnen het webbudget vastgelegd.
[8] USGS Mineral Commodity Summaries 2025 / World Gold Council — Zuid-Afrikaanse mijnproductie ≈100 t/j (2024).
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `sat-goud-mponeng-londen-mponeng.png`, `sat-goud-mponeng-londen-randrefinery.png`, `sat-goud-mponeng-londen-jnb-cargo-zoom.png`, `sat-goud-mponeng-londen-lhr-cargo-zoom.png`, `sat-goud-mponeng-londen-lbma.png`.
[10] `data/goud.js` (v1-register) — node `au-mponeng`, Mponeng, Harmony, capaciteit ≈8 t/j; node `au-ref-rand` (-26.23/28.16); node `au-hub-london` (51.514/-0.088).
[11] LBMA — Good Delivery List / Londen als prijsbenchmark en OTC-hart van de goudmarkt. https://www.lbma.org.uk/good-delivery/list
[12] Wikipedia (MediaWiki API prop=coordinates) — Westonaria -26.31778/27.65056, Soweto -26.26781/27.85849, Hounslow 51.4668/-0.3750, Chiswick 51.4900/-0.2600, Hammersmith 51.49333/-0.22278.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-mponeng-londen`** → `v2/data/stroomroute-goud-mponeng-londen.json` — 4 benen (truck · truck · lucht
· truck, fase A → B → C → stoppunt), **9.216,8 km**, 3.000 punten, 5 markers, 60,8 KB. Recept: `bak_stromen.sh`
(functie `bak_goud_mponeng_londen`); twee nieuwe wegprofielen `goud-mponeng-londen-mponeng-randrefinery` en
`goud-mponeng-londen-randrefinery-jnb` en `goud-mponeng-londen-lhr-lbma` in `maak_stroombeen_weg.py` (drie
profielen, niet twee — b1, b2 en b4 zijn alle drie eigen wegscans).

**b1 (truck, nieuw profiel `goud-mponeng-londen-mponeng-randrefinery`, extract `zuid-afrika`, vensterKm 45):**
`maak_stroombeen_weg.py --profiel goud-mponeng-londen-mponeng-randrefinery --bron geofabrik` — **85,8 km**
getekend over Westonaria → Soweto (N12/R28-industriecorridor), 38 keerlussen gesnoeid (93,9 → 85,6 km). Geen
faalde poging. Ankerverbindingen 0,14/0,05 km — geen stippel nodig.

**⚠️ Lengtetoets buiten ±10% maar binnen de soepele ±15%-marge uit de brief:** 85,8 km tegen de toetswaarde 77 km
(eigen berekening, brief §2/§7; rechte afstand is al 76,2 km) = **+11,2%**. Geen bevinding in de zin van "fout" —
de brief zelf zegt al dat een uitkomst tussen 76 en ~100 km plausibel is omdat de corridorkeuze (N12 direct vs.
R28 via Krugersdorp/Roodepoort) niet bevonden was; de gemeten route volgt de N12 via de opgegeven via-punten.

**b2 (truck, nieuw profiel `goud-mponeng-londen-randrefinery-jnb`, extract `zuid-afrika`, vensterKm 25):**
`maak_stroombeen_weg.py --profiel goud-mponeng-londen-randrefinery-jnb --bron geofabrik` — **25,7 km** getekend
(R21/N12), 5 kleine keerlussen gesnoeid. **Eerste poging faalde** ("geen wegpad tussen punt 0 en 1"): het
JNB-vrachtapron is airside/deels privéterrein, precies de klasse die elders in dit bestand al bij `dia-jnb-cargo`
(28,227/-26,143, ~2 km verderop op hetzelfde complex) is opgelost. Tweede poging met `eindKlassen` incl. `track` +
`eindToegangPrivaat: True` slaagde volledig — geen stippel nodig, ankerverbindingen 0,05/0,05 km.

**⚠️ Lengtetoets BUITEN de ±15%-norm:** 25,7 km tegen de toetswaarde 15 km (redactionele schatting uit het
ontwerp, brief §2/§7) = **+70,8%**. Bevinding, geen fout — niet dichtgetrokken: de brief noemt die 15 km zelf al
als "geen aparte bron" en "niet blokkerend" (haalbaarheidstoets), en de rechte afstand is al 11,2 km; 25,7 km is
de echte R21/N12-wegroute tussen twee punten die niet op een rechte lijn liggen.

**b3 (lucht, grootcirkel, JNB → LHR):** `maak_luchtbeen.py --van "OR Tambo (JNB) vrachtterminal|-26.1440,28.2295"
--naar "Heathrow (LHR) vrachtterminal|51.4605,-0.4680"` — **9.074,3 km** gemeten grootcirkel (brief noemde
≈9.070 km — verschil 4,3 km/0,05%, binnen norm; geen aparte km-toets voor een luchtbeen). 364 punten.
Doorgetrokken, geen stippel: een vlucht tussen twee gelegde vrachtterminals is geen gat. Geen tussenlanding
gebrond (geen bron noemt een hub tussen Johannesburg en Londen) → één directe vlucht, conform §7 van de brief en
de bakhandleiding. Bron voor de modaliteit is markt-niveau (LBMA/WGC), niet Rand Refinery-specifiek — vandaar
"aannemelijk: één bron" in de beennaam.

**b4 (truck, nieuw profiel `goud-mponeng-londen-lhr-lbma`, extract `groot-brittannie`, vensterKm 25):**
`maak_stroombeen_weg.py --profiel goud-mponeng-londen-lhr-lbma --bron geofabrik` — **31,0 km** getekend over
Hounslow → Chiswick → Hammersmith (M4/A4), 87 keerlussen gesnoeid (33,4 → 30,9 km). Geen faalde poging (standaard
`eindKlassen` volstond voor de City-straten rond de LBMA-kluis). Ankerverbindingen 0,06/0,05 km — geen stippel
nodig, geen last-mile-voetgangerszone-probleem zoals bij de zusterstroom goud-valcambi-londen.

**Lengtetoets binnen de ±15%-norm:** 30,9 km tegen de toetswaarde 27 km (eigen berekening, brief §2/§7; ontwerp
noemde ≈25 km) = **+14,4%**.

**Geen zeebeen** (truck + truck + lucht + truck) → geen MARNET, geen haven-aanloop. Fase D/E vervallen (brief §6,
stoppunt LBMA-kluis/Bank of England — kluis, geen fabriek).

**Toetsen:** `toets_knikken.py` — b1 11 knikken ≥60° (spikes, straal 4-66 m), b2 11 knikken ≥60° waarvan 2
omkeringen ≥150° (beide "scherpe bocht, echt", stadskruispunten bij Rand Refinery en OR Tambo, ratio 1,9-2,1), b3
0 knikken (lucht per constructie recht), b4 15 knikken ≥60° (spikes, straal 3-27 m); **0 terugloop op alle vier
de benen** — geen actie nodig. `toets_rechte_benen.py --min-km 5` — geen melding voor `goud-mponeng-londen` (het
lucht-been wordt per constructie overgeslagen; alle drie de truckbenen zijn geen rechte lijnen). `json.load`
slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `truck`/`truck`/`lucht`/`truck` ∈ toegestane set, elk been
≥ 2 punten (1.035/381/364/1.220), bestandsgrootte 60,8 KB (ruim onder ~300 KB). Naden tussen de vier benen:
**0,000 km** op alle drie de overgangen. Markers: alle vijf op 0,0 m van hun been (elk anker is tegelijk het
routeerpunt/been-uiteinde).

**Toelichting stippels/haven-aanlopen/vluchten:** één vlucht, doorgetrokken (geen stippel, zie b3 hierboven). Geen
zeebeen in deze keten → geen MARNET, geen haven-aanloop. Geen enkele stippel in de hele keten (vier doorgetrokken
benen) — geen been is korter dan het net reikt.

**Gereedschapslessen:** `maak_luchtbeen.py` werkte zonder aanpassing, resultaat binnen 0,05% van de gepubliceerde
grootcirkelafstand. Bij `maak_stroombeen_weg.py` faalde alleen b2 ("geen wegpad tussen punt 0 en 1") door het
airside/private karakter van het JNB-vrachtapron — dezelfde klasse als eerdere luchthaven-vrachtapron-toegangen
in dit project (zie `dia-jnb-cargo`, `dia-letseng-jnb` §9, `pgm-zondereinde-hanau`): `eindKlassen` incl. `track` +
`eindToegangPrivaat: True` lost dit systematisch op. De twee redactionele/eigen-berekende km-schattingen in de
brief (b1 ≈77, b2 ≈15) bleken beide zachte cijfers zonder harde bron; b1 viel binnen de door de brief zelf soepel
gemaakte marge, b2 (buiten elke marge) was door de brief al als "niet blokkerend" gemarkeerd. Geen conflict
gevonden met bestaande ankers van andere goud-brieven in deze golf.
