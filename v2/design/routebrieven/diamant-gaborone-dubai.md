# Routebrief (licht) · diamant — Gaborone (ODC) → GBE → DXB → Dubai Diamond Exchange (Botswana → VAE)

**stroom-id:** `diamant-gaborone-dubai` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** ruwe diamant uit het ODC-kanaal (Okavango Diamond Company, het niet-De Beers-verkoopkanaal van Debswana) gaat van de DTCB/DBGSS-campus in Gaborone per truck naar de GBE-vrachtapron, vliegt als vrachtvlucht (grootcirkel, **aannemelijk: één bron**, geen directe lijn gebrond) naar DXB Cargo Village en gaat per truck naar de Dubai Diamond Exchange (DMCC, Almas Tower, JLT).
**Welke as van het verhaal:** *Botswana → de grootste afnemer.* De VAE ontvingen in 2023 US$ 1,63 mld = 37% van alle Botswaanse diamantexport (HS 7102, US$ 4,33 mld), vóór België 22% en India 15,4% [2]. Volume: het ODC-kanaal is ca. 25% van Debswana (2023, Mmegi; 30% verwacht vanaf 2025) [6] van 20,9 Mct (Jwaneng 11,86 + Orapa 9,02 + rest, sitelaag B1) [9] = **indicatie ~5,2 Mct/j**; het deel dat naar Dubai gaat is niet gepubliceerd. Eenheid Mct/j (miljoen karaat per jaar); $/karaat verschilt per mijn en zit niet in het gewicht.

## 1 · Ketenkaart
```
DTCB/DBGSS-campus Gaborone `dia-gaborone-dtc` ──(b1 truck · A1/Western Bypass · letterlijke kopie diamant-gaborone-surat b1 · 4,3 km)──►
GBE-vrachtapron `dia-gbe-cargo` ──(b2 lucht · vlucht GBE → DXB, grootcirkel, aannemelijk: één bron · 6.378,8 km)──►
DXB Cargo Village `dia-dxb-vracht` ──(b3 truck · Airport Road → Sheikh Zayed Road E11 · letterlijke kopie diamant-mbujimayi-dubai b4 · 31,2 km)──►
DMCC / Almas Tower `dia-dmcc-almas` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | DTCB/DBGSS-campus → GBE-vrachtapron | A1 / Western Bypass Road; één stadsweg, geen corridorkeuze; **letterlijke kopie** van `diamant-gaborone-surat` b1 | hemelsbreed 3,7 km, geen wegkm (gebakken kopie 4,3 km) [10] | kopie geojson | nee |
| b2 | C | lucht | GBE-vrachtapron → DXB Cargo Village | vlucht GBE → DXB, grootcirkel (aannemelijk: één bron) | 6.378,8 grootcirkel [berekend, `maak_luchtbeen.py`] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | DXB Cargo Village → DMCC/Almas Tower | Airport Road → Sheikh Zayed Road E11; **letterlijke kopie** van `diamant-mbujimayi-dubai` b4 (= `diamant-dubai-surat` b1 omgekeerd) | hemelsbreed 29,0 km, geen wegkm (gebakken kopie 31,2 km) [10] | kopie geojson | nee |

Geen zeebeen, geen haven-aanloop, geen leiding. Geen last-mile-stippel: beide wegbenen eindigen op het anker (GBE 0,12 km, DXB 0,22 km aanloop over service-wegen, al in de kopieën; patroon `goud-loulo-ticino` niet nodig — de bron-brieven tekenden dezelfde aanloop zonder stippel).

## 3 · Ankers (alle vier HERGEBRUIKT, niet opnieuw gelegd; één verse satellietblik z15 ter controle)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-gaborone-dtc` | verkoop-/sightcampus, vertrek | DTCB/DBGSS-campus (Diamond Technology Park-zone), Gaborone | -24.5859, 25.9144 | [8][10] `diamant-gaborone-surat` | bron-gelegd (z15: gebouwencluster met overdekte parking aan de noordrand van de stad, naast het Diamond Technology Park-terrein; ODC-kijkruimtes zelf niet apart gebrond, zie §7) |
| `dia-gbe-cargo` | overslag truck → lucht | GBE-vrachtapron, Sir Seretse Khama Intl Airport | -24.5550, 25.9286 | [8][10] `diamant-gaborone-surat` | aannemelijk (z15: kruis op de loodsen en de apron ten noordoosten van de terminal; geen "Cargo"-naam in de bronnen, mogelijk algemene-luchtvaart-/charterapron, zie §7) |
| `dia-dxb-vracht` | overslag lucht → truck | DXB Cargo Village / SkyCargo-loodsen, Al Garhoud | 25.25745, 55.3406 | [10] `diamant-dubai-surat`, `-mbujimayi-dubai` | bron-gelegd (z15: rij vrachtloodsen en apron ten noordwesten van de terminals, kruis op de loodsenrij) |
| `dia-dmcc-almas` | handelshub, stoppunt | DMCC / Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [4][10] `diamant-letseng-dubai` | bron-gelegd (z15: hoogbouwcluster in JLT aan de Sheikh Zayed Road, kruis op de toren) |

## 4 · Via-punten
Geen: b1 en b3 zijn letterlijke kopieën van gebakken wegbenen (één doorgaande stadsweg, geen corridorkeuze); b2 is een grootcirkel. Geofabrik-regio's (alleen ter info, geen nieuwe wegscan): b1 `botswana`; b3 `gcc-staten`.

## 5 · Verwerkingsknopen
Geen fysieke bewerking: de campus is sorteer-/verkoopaggregatie, DMCC/DDE is handels- en veilingplek (ODC houdt er sinds de MoU van maart 2022 veilingen en kijkdagen [3][4]); slijpen gebeurt elders (overwegend Surat, buiten deze keten).

## 6 · Stoppunt
De brief stopt bij de Dubai Diamond Exchange: geen bron koppelt deze Botswaanse lading aan een vervolgbestemming — fase D en E vervallen.

## 7 · Open punten
- **De vlucht GBE → DXB is een aanname (één bron voor de handelsas, geen bron voor de vlucht):** gebrond zijn alleen de handelsstroom (VAE = 37% van de Botswaanse export [2]), de ODC-kijkdagen en veilingen op de DDE (okt 2021 [3], mrt 2022 [4]) en het corridor-akkoord van juli 2026 [5]; geen bron noemt vluchtnummer, vrachtvlucht of tussenlanding (bv. JNB). Eén directe grootcirkel getekend, "aannemelijk: één bron" staat in de beennaam; een stippel zou verkeerd zijn (geen gat in het net).
- **Het ODC-kijkevent van 2021 is geen vervoersbron** [3]: het noemt geen transport, alleen een eenmalige kijkdag (13-15 okt 2021, >650.000 ct). Het Gulf News-artikel noemt logistiek alleen als samenwerkingsgebied, zonder routes [5].
- **GBE-vrachtapron zonder Cargo-naam:** kruis op een apron met loodsen; geen bron bevestigt dat ODC-rough hier vertrekt in plaats van als koerierlading op een lijnvlucht via de hoofdterminal (zelfde punt als in `diamant-gaborone-surat` §7).
- **Eerste ODC-tenders op de DDE worden eind 2026 verwacht** [5]: de as is dus deels toekomstgericht; de kaart toont de vaste vorm, niet een gedocumenteerde zending.
- **Aandeel Dubai in het ODC-volume onbekend;** 25% (2023) en 30% (2025) komen uit Mmegi [6]; het Anglo American-persbericht van 2025-02-25 noemt in de geraadpleegde tekst geen ODC-percentage [7]. OEC-pagina (UAE 2,31 mld, 2022) niet leesbaar (JS-only) en niet gebruikt; het Trendeconomy-cijfer [2] is een handelsdatabase, geen jaarverslag.
- **Dubai-luchtvracht in maart 2026 verstoord (West-Azië-conflict)** volgens de haalbaarheidstoets (GJEPC, Rapaport 2026-03-01); niet zelf geraadpleegd, niet geciteerd als feit.
- Beide wegbenen: geen onafhankelijke wegkm (alleen hemelsbreed); het verschil met de gebakken kopie (+16% op b1, +8% op b3) is een indicatie, geen norm.

## 8 · Bronnen
[1] Ketenontwerp M31 golf 19 + haalbaarheidstoets (orchestrator-invoer), intern.
[2] Trendeconomy, Botswana HS 7102 (diamant) 2023: UAE US$ 1,63 mld (37%), België 22%, India 15,4%, totaal US$ 4,33 mld. https://trendeconomy.com/data/h2/Botswana/7102
[3] The Patriot, "ODC shines bright in Dubai" (inaugurele kijkdag op de DDE 13-15 okt 2021, EXPO 2020). https://thepatriot.co.bw/odc-shines-bright-in-dubai/amp/
[4] DMCC, MoU met ODC (14 maart 2022, Almas Tower; ODC-veilingen en kijkdagen op de DDE; eerste veiling 14-19 maart 2022). https://dmcc.ae/latest-news/dmcc-signs-mou-botswanas-odc-support-development-industry
[5] Gulf News, 2026-07-15, "Botswana's diamonds get a direct route to Dubai under new trade corridor" (DMCC–Botswana Stock Exchange Group, eerste ODC-DDE-tenders eind 2026). https://gulfnews.com/business/markets/botswanas-diamonds-get-a-direct-route-to-dubai-under-new-trade-corridor-1.500608551
[6] Mmegi, 2023-09-18, ODC verkoopt 25% van Debswana, verwacht 30%. https://mmegi.bw/business/odc-debuts-diamond-sales-to-citizens/news
[7] Anglo American persbericht 2025-02-25 (Debswana 50:50, 10-jarig verkoopakkoord; geen ODC-percentage in de geraadpleegde tekst). https://www.angloamerican.com/media/press-releases/2025/25-02-2025
[8] Wikipedia, "Sir Seretse Khama International Airport" (diamond hub-zone sinds 2017). https://en.wikipedia.org/wiki/Sir_Seretse_Khama_International_Airport
[9] `v2/design/diamant-sitelaag.json` B1 (Debswana 2023: Jwaneng 11,86 + Orapa 9,02 Mct; Botswana 25,1 Mct).
[10] Brieven `diamant-gaborone-surat` (b1, ankers GBE/DTC), `diamant-mbujimayi-dubai` (b4), `diamant-dubai-surat`, `diamant-letseng-dubai` (ankers DXB/DMCC).
[11] Esri World Imagery via `sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-gaborone-dubai-{dtc,gbe-cargo,dxb-vracht,dmcc-almas}.png`.
[12] `data/diamond.js` en `design/diamant.md` (v1-checklist, geen ankerbron).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)

**Stroom `diamant-gaborone-dubai`** → `v2/data/stroomroute-diamant-gaborone-dubai.json` — 3 benen (2 truck
doorgetrokken, 1 lucht doorgetrokken), **6.414,3 km**, 762 punten, 4 markers, 16,2 KB. Geen stippel.
Recept: `bak_stromen.sh` (functie `bak_diamant_gaborone_dubai`); geen wegprofiel, geen wegscan, geen extract, geen
zee, geen haven-aanloop; één luchtbeen met `maak_luchtbeen.py` (bakhandleiding-licht §2 "Lucht"); twee
letterlijke kopieën van bestaande wegbenen. Bake via `hecht_marnet.py route` (17 s).

**b1 (truck, 4,3 km, 99 punten):** letterlijke kopie van `diamant-gaborone-surat-weg-dtc-gbe.geojson` (A1/Western
Bypass Road, DTCB/DBGSS-campus → GBE-vrachtapron). 4,253 km tegen hemelsbreed 3,7 km = +14,9%: GEEN wegkm in de
bron, dus indicatie en geen norm (§7).

**b2 (lucht, 6.378,8 km, 257 punten):** `maak_luchtbeen.py` GBE-vrachtapron (-24,5550/25,9286) → DXB Cargo Village
(25,2574524/55,3405972), grootcirkel, DOORGETROKKEN. Km komt exact overeen met de brief (6.378,8). Aannemelijk:
één bron voor de handelsas, geen bron voor de vlucht; "aannemelijk: één bron" staat in de beennaam, niet in de
lijnstijl. Geen tussenlanding aangenomen.

**b3 (truck, 31,2 km, 406 punten):** letterlijke kopie van `diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson`
(Airport Road → Sheikh Zayed Road E11), loopt al DXB → DMCC, geen omkering nodig. 31,244 km tegen hemelsbreed
29,0 km = +7,7% (geen wegkm in de bron, indicatie).

**Toetsen:** naden b1→b2 en b2→b3 **0,000 km**; markers op ≤ 0,02 km van hun lijn (drie op 0,000, `dia-dmcc-almas`
0,018 km). `toets_knikken.py`: b1 5 knikken (spikes, R 5-42 m), b3 6 knikken (spikes, R 5-55 m, stadsgeometrie van de
kopieën), lucht 0; 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom
(luchtbeen per constructie overgeslagen). `json.load`: versie 2, `punt_formaat` lonlat, modaliteiten truck/lucht,
elk been ≥ 2 punten, 16,2 KB. Het bestand `bak_stromen.sh` heeft 0 CRLF-regeleinden.

**Toelichting stippels/aanloop/vlucht/leiding:** geen stippel (beide wegbenen eindigen op het anker; de 0,12 km
GBE-aanloop en 0,22 km DXB-aanloop over servicewegen zitten al in de kopieën, dus geen airside-stippel). Eén
vlucht (b2), doorgetrokken grootcirkel tussen twee ankers; DXB-anker bron-gelegd, GBE-anker aannemelijk. Geen
haven-aanloop (geen zeebeen), geen leiding.

**Lessen:** een stroom van drie hergebruikte onderdelen bakt in één pas zonder wegscan; de enige nieuwe geometrie is
het luchtbeen. Beide wegbenen zijn kopieën zonder echte wegkm: de ±15%-toets is hier alleen indicatie. Het
GBE-anker (-24,5550/25,9286) is hetzelfde als in `diamant-gaborone-surat`; `diamant-jwaneng-antwerpen` legt het
GBE-vrachtapron ~0,5 km verderop (-24,5576/25,9242), niet samengevoegd en niet aangepast (melding).
