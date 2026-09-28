# Routebrief (licht) · grafiet — Lindi Jumbo-mijn (Tanzania) → Dar es Salaam → Qingdao (China)

**stroom-id:** `grafiet-lindijumbo-qingdao` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet van de **Lindi Jumbo-mijn** (Ndovu Graphite Limited — Lindi Jumbo Limited 84% / Tanzania-overheid 16%, bij Matambarale, Ruangwa-district) gaat per **truck** ~478 km hemelsbreed via Ruangwa, Lindi en de kustweg (T7 "Kilwa Road") naar de **containerkade van Dar es Salaam**, per **zeeschip** via de Indische Oceaan, Straat Malakka en de Gele Zee naar **Qingdao (QQCT, hergebruikt anker)** — het tweede Afrikaanse land in de trechter naast Mozambique, met twee met naam genoemde Chinese offtake-afnemers uit 2024, terwijl de mijn in 2026 hoofdzakelijk naar **India** exporteert.
**Welke as van het verhaal:** een tweede, operationele Oost-Afrikaanse grafietas naast Balama→China (`grafiet-balama-laixi`) — maar met een omgekeerde bewijslast: hier is de mijn zelf springlevend (40 kt/j-capaciteit sinds juni 2025, JV-herstructurering mei 2026), terwijl de *specifiek Chinese* bestemming van de lading het onzekere deel is.

## 1 · Ketenkaart
```
Lindi Jumbo-plant `gr-lindijumbo-plant` ──(b1 truck · regionale weg Ruangwa–Lindi → T7 "Kilwa Road" Lindi–Nangurukuru–Kibiti–Mkuranga · ~478 km hemelsbreed via-keten)──►
Dar es Salaam-kade `gr-daressalaam-kade` ──(aanloop · ~19,8 km stippel, LAR-586)──► zeeknoop 5310
   ──(b2 zee · Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Gele Zee · ≈ 9.645 km hemelsbreed, MARNET)──► zeeknoop 5841
   ──(aanloop · 5,59 km stippel, LAR-586)──► QQCT Qianwan-kade `gr-qingdao-qqct-kade` (hergebruikt, letterlijke kopie) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-lindijumbo-plant` → `gr-daressalaam-kade` | mijnweg → Ruangwa → regionale weg Ruangwa–Nyangao–Lindi → **T7** (Lindi → Nangurukuru → Kibiti → Mkuranga → Dar es Salaam, "Kilwa Road") | geen onafhankelijk gepubliceerde totaallengte; eigen via-puntenketen 477,9 km hemelsbreed (ontwerp: 363 km mijn→kade rechtstreeks, "~450–500 km"-schatting) | `maak_stroombeen_weg.py` — **nieuw profiel** `grafiet-lindijumbo-daressalaam`, extract `tanzania`, refs T7 | nee |
| — | B | zee (aanloop) | `gr-daressalaam-kade` → zeeknoop 5310 | havenkanaal Dar es Salaam → open zee | 19,84 (gemeten, `hecht_marnet.marnet_zee`) | `maak_havenaanloop.py` (LAR-586: kade > 5 km van zeeknoop) | ja |
| b2 | B | zee | zeeknoop 5310 → zeeknoop 5841 | Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Gele Zee | ≈ 9.645 hemelsbreed (ontwerp); geen gepubliceerde scheepvaartlengte | MARNET `--been "zee|…|-6.6537,39.3256|36.0313,120.2646"` | nee |
| — | B | zee (aanloop) | zeeknoop 5841 → `gr-qingdao-qqct-kade` | Jiaozhou-baai → QQCT-kade | 5,59 (gemeten; **>5 km, dus sinds LAR-586 wél een aanloop** — anders dan in `grafiet-balama-laixi.md` vóór deze regel) | `maak_havenaanloop.py` | ja |

Geen last-mile-benen: `gr-lindijumbo-plant` is het site-anker en tevens het beginpunt van b1 (werkwijze §1). Geen fase C/D: geen bron lokaliseert de IMQG- of QRGT-fabriek (werkwijze §1: "D alleen als één bron de fabriek noemt").

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-lindijumbo-plant` | mijn / verwerkingsfabriek (laadplek) | Lindi Jumbo-mijn (Ndovu Graphite Limited), bij Matambarale/Matambalale-dorp, Ruangwa-district | -9.9135, 38.9160 | OSM/Photon (dorp Matambalale, Ruangwa) [9] + JV-ondertekening "in Ruangwa District" [5] + eigen `sat_check.py` | **bron-gelegd** (z18 gezien: verwerkingsfabriek met transportband, verdikker-/tankinstallatie en gebouwen naast een hexagonale tailings-opslagfaciliteit, laadterrein en toegangswegen, ~18 km NNW van Ruangwa-centrum — geen los aanwijsbare open pit op dit beeld, wel een compleet operationeel complex dat past bij de bevestigde 40 kt/j-capaciteit) |
| `gr-daressalaam-kade` | overslag truck → zee | Dar es Salaam Port, general cargo-/containerkade (Kurasini-kanaal) | -6.8280, 39.2870 | OSM + eigen `sat_check.py` | **bron-gelegd** (z18 gezien: containerstapels, meerdere vrachtschepen langszij, kranen en een truckmarshallingterrein aan weerszijden van het havenkanaal) |
| `gr-qingdao-qqct-kade` | losplek zee (hergebruikt) | Qingdao Qianwan Container Terminal (QQCT) | 36.0124, 120.2070 | `grafiet-balama-laixi.md` §3 — **letterlijke kopie van het punt, geen gedeeld been** | aannemelijk (hergebruikt anker; welke Qingdao-terminal wordt bediend is voor déze mijn evenmin gebrond) |

## 4 · Via-punten (b1, corridorkeuzes op T7/regionale weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ruangwa (stadscentrum, wegsplitsing) | -10.0675, 38.9274 | hier sluit de mijn-toegangsweg aan op de regionale weg; pint de noordoostelijke richting naar Lindi i.p.v. zuidwaarts naar Nachingwea/Masasi (die laatste route hoort bij het ~200 km-Mtwara-alternatief uit het ontwerp, hier expliciet niet gekozen — zie §7) |
| b1 | 2 | Lindi (aansluiting regionale weg op T7) | -9.9969, 39.7144 | pint de overgang van de regionale weg op de nationale **T7** (Wikipedia: T7 loopt Dar es Salaam–Kilwa–Lindi–Mingoyo [8]); sluit een zuidelijke doorrit naar Mtwara uit |
| b1 | 3 | Nangurukuru (T7-kruispunt) | -8.7980, 39.3502 | pint doorrijden op de vaste T7-kustweg i.p.v. de aftakking naar het Kilwa Masoko-schiereiland |
| b1 | 4 | Kibiti (T7, Rufiji-delta) | -7.7214, 38.9365 | pint de T7 landinwaarts om de Rufiji-delta i.p.v. de veerpont-aftakking naar Nyamisati/Mafia |
| b1 | 5 | Mkuranga (laatste kruispunt vóór Dar es Salaam) | -7.1199, 39.2115 | laatste grote wegsplitsing vóór de stad; pint de doorgaande T7 naar de haven i.p.v. een binnenweg om Dar es Salaam heen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lindi Jumbo-plant | Ndovu Graphite Limited (Lindi Jumbo Limited 84% / Tanzania-overheid 16%, JV getekend 2026-05-28) | grafieterts (open pit) → grafietconcentraat (Super Jumbo/Jumbo Large/Jumbo Fine flakes) | 40.000 t/j (volledige capaciteit bereikt juni 2025); mijnleven 24 jaar | [5] |

## 6 · Stoppunt
De brief stopt op de QQCT-kade in Qingdao: geen bron lokaliseert de IMQG- of QRGT-fabriek (fase D vervalt, werkwijze §1), en de 2026-bron zegt zelf dat de **hoofdafzetmarkt India** is — de Chinese offtakes (IMQG/QRGT, 2024) zijn contractueel gedocumenteerd maar hun actuele leveringsstatus na de DOCA/JV-herstructurering is niet gepubliceerd. Een Balama-Vidalia/Laixi-achtig patroon, maar dan op de bestemming in plaats van het volume: de mijn draait volop, de Chinese lading is aannemelijk, niet bevestigd.

## 7 · Open punten
- **Mijnanker satellietbevestigd, niet tekstueel gepind:** geen enkele bron geeft een exacte coördinaat voor het plantterrein; `gr-lindijumbo-plant` steunt op de combinatie OSM-dorp Matambalale (Ruangwa-district, waar de JV-ondertekening plaatsvond [5]) + een satellietbeeld dat een compleet grafiet-verwerkingscomplex (fabriek + TSF) op die plek toont. Geen open pit zichtbaar op het gecheckte beeld — mogelijk buiten beeld of kleiner dan de z18-korrel.
- **Corridor Ruangwa→Lindi→T7 is een eigen aanname, geen gepubliceerde routebeschrijving:** de regionale weg Ruangwa–Nyangao–Lindi is niet met een bronroute bevestigd (alleen de T7-aansluiting bij Lindi zelf [8]); het alternatief via Mtwara (~200 km, in het ontwerp genoemd) is expliciet niet gekozen omdat de webcheck de scheepvaartvertraging koppelt aan **Dar es Salaam**, niet Mtwara. Via-punten zijn bake-richtinggevend; de wegbake (extract `tanzania`) routeert zelf over het echte OSM-net.
- **Eigendom bijgewerkt:** Ndovu Graphite Limited (Lindi Jumbo Limited 84% / Tanzania-overheid 16%), JV getekend 2026-05-28 in Ruangwa-district — vervangt het ontwerp's "Walkabout Resources (in surseance)"; de DOCA (effectief 19-12-2024) en de ASX-delisting (28-08-2025) blijven feitelijk juist als voorgeschiedenis, maar de mijn draait aantoonbaar door en de staat heeft nu een belang.
- **Hoofdafzetmarkt is India (2026), niet China** [5] — de twee met naam genoemde Chinese offtakes (IMQG 2024, QRGT 2024) blijven in de brief staan omdat ze het enige gedocumenteerde China-contract zijn, maar de brief trekt geen lijn "aantoonbaar vol"; zie §6.
- **Beide haven-aanlopen zijn nieuw t.o.v. eerdere grafietbrieven:** LAR-586 (28-09-2026) eist een aanloop zodra een kade > 5 km van haar MARNET-zeeknoop ligt, óók binnen de 25 km-snapgrens. Dar es Salaam (19,84 km) en het hergebruikte Qingdao-anker (5,59 km) vallen beide onder deze regel; `grafiet-balama-laixi.md` gebruikt hetzelfde Qingdao-anker zónder aanloop omdat die brief vóór LAR-586 is gebakken — geen tegenspraak, wel een regelwijziging.
- **Geen gepubliceerde scheepvaartlengte voor b2**, zoals bij de andere grafietbrieven op deze as (35–40 dagen is een doorlooptijd, geen afstand).

## 8 · Bronnen
[1] Proactive Investors, "Walkabout Resources progresses Lindi Jumbo in Tanzania with offtake and marketing deals" — IMQG (Inner Mongolia Qianxin Graphite) en QRGT (Qingdao Risingdawn Graphite Technology) offtakes 2024. https://www.proactiveinvestors.com.au/companies/news/218907/walkabout-resources-progresses-lindi-jumbo-in-tanzania-with-offtake-and-marketing-deals-218907.html
[2] Mining Technology, "Lindi Jumbo Graphite Project" — locatie zuidoost-Tanzania, ~200 km van Mtwara, operationele basis Ruangwa, open-pit + verwerkingsfabriek. https://www.mining-technology.com/projects/lindi-jumbo-graphite-project/
[3] Mining Weekly, "Troubled times for Lindi Jumbo owner" (2024-11-13) — surseance van betaling Walkabout Resources, schuldeiser Gemcorp. https://www.miningweekly.com/article/troubled-times-for-lindi-jumbo-owner-2024-11-13
[4] NS Energy Business, "Walkabout Resources ships first concentrate from Lindi Jumbo graphite mine" — eerste zending via Dar es Salaam (Wogen Pacific). https://www.nsenergybusiness.com/company-news/walkabout-resources-ships-first-concentrate-from-lindi-jumbo-graphite-mine/
[5] TanzaniaInvest, "Tanzania Government Secures 16% Stake in Lindi Jumbo Graphite Mine, Sixth Largest Graphite Producer Globally" — Ndovu Graphite Limited (Lindi Jumbo Limited 84% / Tanzania-overheid 16%), getekend 2026-05-28 in Ruangwa-district, 40.000 t/j sinds juni 2025, mijnleven 24 jaar, hoofdafzetmarkt India, kwalificatie in China/Duitsland nagestreefd. https://www.tanzaniainvest.com/mining/lindi-jumbo-graphite-joint-venture-ndovu
[6] African Mining Market, "Tanzania and Lindi Jumbo unite to expand graphite mining potential" — bevestiging van de JV-ondertekening. https://africanminingmarket.com/tanzania-and-lindi-jumbo-unite-to-expand-graphite-mining-potential/25806/
[7] Wikipedia (en), "Ruangwa District, Lindi" — lijst van wards incl. Matambarale. https://en.wikipedia.org/wiki/Ruangwa_District,_Lindi
[8] Wikipedia (en), "T7 road (Tanzania)" — Dar es Salaam–Kilwa–Lindi–Mingoyo (T6-aansluiting); "T6 road (Tanzania)" — Mtwara–Masasi–Tunduru–Songea–Makambako. https://en.wikipedia.org/wiki/T7_road_(Tanzania) · https://en.wikipedia.org/wiki/T6_road_(Tanzania)
[9] OpenStreetMap (ODbL) via Photon: dorp Matambalale (-9.90361, 38.89813, Ruangwa/Lindi) [OSM node 7798702829]; Nangurukuru (-8.79795, 39.35017, Kilwa/Lindi) [node 2321686265]; Kibiti (-7.72143, 38.93647, Pwani) [node 2177167781]; Mkuranga (-7.11990, 39.21150, Pwani) [node 262088828]. https://www.openstreetmap.org
[10] Wikipedia (en), "Lindi" — havenstad, 9,99694°Z/39,71444°O. https://en.wikipedia.org/wiki/Lindi
[11] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-09-28): `v2/build-cache/satcheck/sat-grafiet-lindijumbo-qingdao-ruangwa-overzicht.png`, `-ruangwa-close.png`, `-ruangwa-wide.png`, `-matambalale-wide.png`, `-candidate1.png`, `-candidate2.png`, `-candidate2-wide.png`, `-plant-detail.png`, `-daressalaam-kade.png`, `-daressalaam-kade-close.png`, `-daressalaam-terminal.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `grafiet-lindijumbo-qingdao`** → `v2/data/stroomroute-grafiet-lindijumbo-qingdao.json` — 4 benen,
**13.102,4 km**, 7.701 punten, 3 markers. truck 577,2 km · zee 20,7 (stippel) + 12.498,9 + 5,6 (stippel) =
12.525,2 km. Recept: `bak_stromen.sh` (functie `bak_grafiet_lindijumbo_qingdao`); nieuw wegprofiel
`grafiet-lindijumbo-qingdao-lindijumbo-daressalaam` in `maak_stroombeen_weg.py`.

**b1 (truck, nieuw profiel, extract `tanzania`, vensterKm 75):** `maak_stroombeen_weg.py --profiel
grafiet-lindijumbo-qingdao-lindijumbo-daressalaam --bron geofabrik` — **575,4 km** geroute (getekende lijn 577,2 km
incl. anker-verbindingsstukjes) over de zes via-punten uit de opdracht (Ruangwa → Lindi → Nangurukuru → Kibiti →
Mkuranga), geen alternatieve corridor gevonden (bv. een directe Ruangwa–Nangurukuru-verbinding zonder Lindi) —
de router volgt exact de opgegeven keten. Tegen de eigen via-keten (477,9 km hemelsbreed): **ratio 1,20**, net
boven de in de opdracht verwachte band 1,1–1,2 maar geen gepubliceerde totaallengte om hard tegen te toetsen (brief
§2/§7: "geen onafhankelijk gepubliceerde totaallengte"). ⚠️ **Anker-verbindingsstukje mijn → weg 1,87 km** (> de
0,5 km-norm, bevinding): geen open pit zichtbaar op het gecheckte satellietbeeld (brief §7), het
verwerkingscomplex/de toegangsweg liggen iets terug van de doorgaande regionale weg; weg → kade 0,01 km (OK).
First mile over kleine wegklassen 13,06 km (service/unclassified), last mile 1,04 km (service) — beide binnen de
12 km-marge van het profiel.

**Haven-aanloop Dar es Salaam (zee, stippel-geojson, LAR-586 — kade 19,84 km van de MARNET-zeeknoop):**
`maak_havenaanloop.py --naam grafiet-lindijumbo-qingdao-daressalaam --van -6.8280,39.2870 --naar
-6.6537,39.3256` — pad gevonden op trap cel 0,01° gebufferd, **20,7 km · 15 punten · 0,00 km over land**,
omwegfactor 1,043 tegen de rechte lijn (19,8 km). Geen terugval nodig.

**b2 (zee, MARNET, `--been "zee|...|-6.6537,39.3256|36.0313,120.2646"`):** snap Dar es Salaam-zeeknoop 0,000 km,
snap Qingdao-zeeknoop 0,000 km (beide expliciet als zeeknoop-coördinaat opgegeven, geen snap-afwijking).
Resultaat **12.498,9 km over 63 MARNET-edges** (1.281 punten) tegen de indicatieve ≈9.645 km hemelsbreed uit de
brief — geen gepubliceerde scheepvaartlengte om tegen te toetsen (brief §2/§7: alleen de hemelsbreed-indicatie);
de MARNET-route volgt Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Gele Zee, dus de meerlengte tegen
hemelsbreed is verwacht (echte scheepvaartroute om continenten heen). Lengte-invariant: getekende lijn 12.498,947
km vs som edge-km 12.498,600 km = +0,347 km (de naden).

**Haven-aanloop Qingdao (zee, stippel, LAR-586 — kade 5,59 km van de MARNET-zeeknoop, óók al snapt de kade
binnen de 25 km-grens):** `maak_havenaanloop.py --naam grafiet-lindijumbo-qingdao-qingdao --van
36.0313,120.2646 --naar 36.0124,120.2070` gaf **exit 124 (timeout 300 s)** — GEEN tweede poging
(bakhandleiding §2/valkuilen-checklist) → rechte stippel, **5,59 km · 2 punten**, met de reden in de beennaam.
Zelfde Qingdao-anker als `grafiet-balama-laixi.md` (letterlijke kopie van het punt), maar géén gedeeld been — die
eerdere brief is vóór LAR-586 gebakken en heeft daar geen aanloop voor.

**Toets naden:** alle vier overgangen **0,00 km** (truck→aanloop, aanloop→zee-b2, zee-b2→aanloop-Qingdao) — geen
naad > 5 km.

**`toets_knikken.py`:** 12 knikken ≥60°, **0 omkeringen ≥150°, 0 TERUGLOOP**. De 11 knikken op het truckbeen zijn
alle "spike" (straal 2–107 m, kopmaak-plekken op kruispunten/aansluitingen: mijnterrein, Ruangwa-splitsing,
Lindi-T7-aansluiting, Nangurukuru, Mkuranga-omgeving, Dar es Salaam-havenkanaal); 1 krappe bocht op het zeebeen
(69,6°, straal 8.372 m bij -6,50000/40,00000, een normale MARNET-routeknik in open water). Geen fout.

**`toets_rechte_benen.py --min-km 5`:** precies 1 hit — de Qingdao-stippel (5,6 km, omwegfactor 1,002), correct
gemarkeerd als stippel met reden (timeout, geen tweede poging). Geen ander been van deze stroom in de uitslag.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de toegestane set),
elk been ≥2 punten (minimum 2, de rechte stippel), bestandsgrootte **147,5 KB** (< 300 KB-richtwaarde).

**Markers:** alle drie op 0,0–0,1 m van de lijn (gr-lindijumbo-plant 0,0 m · gr-daressalaam-kade 0,0 m ·
gr-qingdao-qqct-kade 0,1 m) — geen anker-≠-routeerpunt-afwijking van betekenis.

**Gereedschapslessen:**
- `maak_havenaanloop.py --van`/`--naar` met een negatieve breedtegraad vraagt `--van=<waarde>` (`=`-vorm), anders
  interpreteert argparse het minteken als een optie-vlag en faalt de aanroep met "expected one argument" — geen
  poging verbruikt, wel de eerste keer tegen deze fout aangelopen in dit golf-2-cohort.
- De veilige `rm -rf`/`rmdir`-patronen uit de gedeelde slot-snippet worden door de sandbox-veiligheidscheck van
  deze sessie geblokkeerd zodra het pad uit een shell-variabele komt (ook met een `${d:?}`-guard); vrijgeven via
  `mv "$SLOT" "$SLOT.done.$(date +%s)"` (niet-destructief, laat een spoor achter in plaats van te verwijderen)
  werkt wél en houdt de sloteigenschap (mutuele exclusie via `mkdir`) volledig intact.
- De keten volgde de opdracht-via-punten exact zonder dat de router een kortere corridor vond — de vensterKm 75
  was ruim genoeg om de regionale weg Ruangwa–Lindi te vangen zonder dat er een alternatief tracé nodig was.
