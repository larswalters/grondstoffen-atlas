# Routebrief (licht) · Uranium · Port Hope → Montréal → Mutsu-Ogawara → Rokkasho (Canada → Japan)

**stroom-id:** `uranium-porthope-rokkasho` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** natuurlijk UF6 (48Y-cilinders) uit de Port Hope Conversion Facility (Cameco, Ontario) gaat per **truck** over Hwy 401, A-20 en A-40 naar de Montréal-haven, per **zeeschip** (modelroute via Panama) naar de zeeknoop bij Hachinohe, over een schematische haven-aanloop naar de kade van Mutsu-Ogawara Port (Rokkasho) en over eigen weg naar de JNFL-verrijkingsfabriek — **aannemelijk: één bron voor de bestemming; Canadese vertrekhaven en zeeroute niet gebronnd, de Montréal-keuze is een aanname en conflicteert met een bron uit 2007 (§7).**
**Welke as van het verhaal:** de reserve-as Canada → Japanse verrijking: Cameco leverde in oktober 2025 de eerste natuurlijke UF6 aan JNFL Rokkasho in 11 jaar. Volume: **50 cilinders 48Y = 625 t UF6 ≈ 423 t U, ontvangen 7–10 okt 2025** [1][2]; 1991–2014 ontving JNFL 1.299 cilinders in 41 zendingen [3] (grof ≈ 480 t U/j, eigen omrekening ×0,676 en 12,5 t UF6 per cilinder uit de 2025-zending). Eenheid t U; fabriekscapaciteit in t U/j niet gevonden (§7).

## 1 · Ketenkaart
```
Port Hope `u-porthope-conversie` ──(b1 truck · Hwy 401 → A-20 → A-40 · LETTERLIJKE KOPIE uranium-porthope-gronau b1 · 454,1 km getekend, hemelsbreed 420, geen wegkm)──► Montréal Viau `u-montreal-kade` (onzeker)
  ──(b2 zee · St.-Laurent → Atlantisch → Panamakanaal → Stille Oceaan · MARNET 20.052,8 km, modelmatig)──► zeeknoop 5690 (40.6265, 141.5863)
  ──(b3 stippel · haven-aanloop over water · 41,1 km, schematisch)──► Mutsu-Ogawara-kade `u-rokkasho-kade` (aannemelijk)
  ──(b4 stippel · last mile eigen weg, geen net · 4,8 km hemelsbreed)──► JNFL verrijkingsfabriek `u-rokkasho-verrijking` ── stoppunt
```
**Afwijking t.o.v. het ontwerp:** geen; de haalbaarheidstoets (bindend) is toegepast: b1 kopie, b2 naar de zeeknoop met "aannemelijk" in de beennaam, b3 en b4 stippel.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | Port Hope → Montréal Viau-kade (aannemelijk: Canadese haven niet genoemd) | Hwy 401 → A-20 → A-40 (kopie `uranium-porthope-gronau` b1) | 454,1 getekend; hemelsbreed 420, geen wegkm | **letterlijke kopie** `uranium-porthope-gronau-weg-porthope-montreal.geojson` | nee |
| b2 | C | zee | Montréal Viau-kade → zeeknoop 5690 (aannemelijk: Canadese haven niet genoemd) | St.-Laurent, Atlantisch, Panamakanaal, Stille Oceaan (routerkeuze, geen bron) | router 20.052,8 (zelf getest, 135 MARNET-edges, geen landkruising) | MARNET (`--been zee`) | nee: kade-snap 3,38 km (zeeknoop 6358) |
| b3 | C | zee (haven-aanloop) | zeeknoop 5690 → kade Mutsu-Ogawara Port | open Pacifische kust, Shimokita | 41,1 getekend (hemelsbreed 38,9, omwegfactor 1,056); geen gepubliceerde km | `maak_havenaanloop` (gelukt, 63 punten, `v2/build-cache/ais/graaf/uranium-porthope-rokkasho-aanloop-mutsuogawara.geojson`) | **ja** — kade 38,9 km van de zeeknoop (> 5 km) |
| b4 | C | truck (last mile) | kade → JNFL-verrijkingsfabriek | eigen weg van JNFL [3] | hemelsbreed 4,8; niet gepubliceerd | rechte stippel | **ja** — last mile, geen net op deze korrel |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-porthope-conversie` | conversie (kop) | Port Hope Conversion Facility (Cameco), 1 Eldorado Place | 43.9437, -78.2955 | letterlijk uit `uranium-porthope-gronau` §3 / `uranium-mcarthurriver-porthope` §3 | bron-gelegd (daar z15: fabrieksterrein aan Lake Ontario) |
| `u-montreal-kade` | overslag truck → zee | Port of Montréal, Viau-zijde | 45.5900, -73.5065 | letterlijk uit `uranium-porthope-gronau` §3 | **onzeker**: terminal niet gepubliceerd (daar z15: containerstapels en kranen langs de Saint-Laurent) |
| `u-rokkasho-kade` | overslag zee → weg | Mutsu-Ogawara Port, Rokkasho: kade aan het havenbekken | 40.9385, 141.3775 | haalbaarheidstoets; haven genoemd door JNFL/JAIF [2][3] | **aannemelijk** (z15 gezien, `sat-uranium-porthope-rokkasho-kade.png`: verharde kadevloer met opslagplek op de noordrand van een havenbekken aan de Pacifische kust, wegverbinding het bos in; de kade zelf niet in een bron) |
| `u-rokkasho-verrijking` | verrijking (staart, stoppunt) | JNFL uranium enrichment plant (日本原燃 ウラン濃縮工場), Rokkasho | 40.9778, 141.3541 | OSM (Photon: landuse industrial "日本原燃 ウラン濃縮工場" op 40.9778, 141.3541) [4] + haalbaarheidstoets | **bron-gelegd** (z15 gezien, `sat-uranium-porthope-rokkasho-plant.png`: kruis op een omheind complex met grote lange cascadehallen, ommuurd en met eigen weg; de opwerkingsfabriek ligt 2,7 km westelijker) |
Zeeknoop 5690 (40.6265, 141.5863; 38,9 km van de kade, 43,7 km van de fabriek) is geen anker maar het routeerpunt, letterlijk uit `nikkel-riotuba-hachinohe` §3.

## 4 · Via-punten
Geen eigen: b1 is een kopie van `uranium-porthope-gronau` b1 (daar vijf via-punten, §4 van die brief); b2 is router; b3 en b4 zijn stippel.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Port Hope Conversion Facility | Cameco | UO3 → UF6 | vergund 12,5 Mkg U als UF6/j | via `uranium-porthope-gronau` §5 |
| Mutsu-Ogawara Port (kade) | Aomori/MLIT-haven, JNFL-gebruik | lossen met kraan op trailers, dosimetrie- en uiterlijkcontrole | niet gepubliceerd | [2][3] |
| JNFL Rokkasho verrijkingsfabriek | Japan Nuclear Fuel Ltd | natuurlijk UF6 → verrijkt UF6 | niet in t U/j gevonden; WISE noemt 37,5 t SWU/j voor de eerste cascade en een voornemen van 1.500 t SWU/j [1] (SWU, geen feed) | [1] |

## 6 · Stoppunt
De brief stopt bij de JNFL-verrijkingsfabriek: de afnemer uit het ontwerp en de enige afnemer die de bronnen noemen; geen bron noemt een vervolgbestemming van deze lading (fase D en E vervallen).

## 7 · Open punten
- **Conflict met een bron uit 2007:** een PATRAM-paper van Transnuclear [5] beschrijft natuurlijke UF6 van een conversiefabriek in Ontario naar Japan met ca. **4.000 km overland per B-train naar een westkusthaven** van Canada (haven niet genoemd) en daarna een eigen zeeschip. Dat wijst op de Pacifische kant, niet op Montréal/Panama. Voor de zending van 2025 noemt geen bron de Canadese haven; de Montréal-keuze (bindende toets) is een aanname en het zeebeen (20.053 km via Panama) is modelmatig. Westkust (Vancouver/Prince Rupert) is het alternatief en zou een heel andere lijn geven; niet getekend.
- **Port Hope → Montréal niet voor Japan gebronnd:** WISE meldt wel UF6-trucks van Port Hope naar de Port of Montréal (ongeval 29-6-2020, Orano) [6], maar dat is Europa-vracht. Geen wegkm gepubliceerd: hemelsbreed 420 km, geen wegkm (454,1 km getekend is OSM-afgeleid); ±15% is indicatie.
- **Kade Mutsu-Ogawara niet gepubliceerd:** de bron noemt Mutsu-Ogawara Port [3]; het kadepunt komt uit de haalbaarheidstoets en één satellietblik (aannemelijk). De haven-aanloop (41,1 km) is gelukt zonder landkruising midden op de lijn; 0,93 km grenst aan de kade (1:10M-kust kent het havenbekken niet); schematisch.
- **Zeeknoop 5690 is geen haven:** Hachinohe-knoop, 38,9 km van de kade; open water, geen satellietbeeld.
- **Geen cilindertelling per route:** 2025 was één zending van 50 cilinders na 11 jaar [1]; het volume is geen jaarvolume. JNFL-capaciteit in t U/j niet gevonden (WISE-cijfers in SWU, onderling ongelijk; ANS/JAIF geven geen SWU voor de oude fabriek).
- **Sitelaag:** `uranium-sitelaag.json` heeft geen JNFL-record; centraal bijmaken (40.9778, 141.3541).

## 8 · Bronnen
[1] WISE Uranium Project, "Uranium enrichment plants — JNFL Rokkasho-mura" (7-10 okt 2025: 50 cilinders 48Y, 625 t UF6 / 423 t U, van Cameco Canada, eerste in 11 jaar; capaciteitsregels) https://www.wise-uranium.org/eopasi.html
[2] ANS Nuclear Newswire, "Japan gets new U for enrichment…" (27-10-2025; eerste verse UF6 in 11 jaar; geen haven of route) https://www.ans.org/news/2025-10-27/article-7496/japan-gets-new-u-for-enrichment-as-global-power-and-fuel-plans-grow/
[3] JAIF, nieuwsbericht 14-10-2025 (kraan op trailers in Mutsu-Ogawara Port, Rokkasho, onder toezicht MLIT; eigen weg naar de fabriek; 1991–2014: 1.299 cilinders in 41 zendingen; Cameco) https://www.jaif.or.jp/en/news/industry/7682
[4] OSM via Photon: "日本原燃 ウラン濃縮工場" landuse industrial 40.9778, 141.3541 (Rokkasho) https://photon.komoot.io
[5] Transnuclear Ltd., "Experience of natural UF6 transport from Canada to Japan", PATRAM 2007 (Ontario → ca. 4.000 km B-train → westkusthaven → eigen schip → Japanse haven) https://resources.inmm.org/patram-proceedings/experience-natural-uf6-transport-canada-japan
[6] WISE Uranium Project, "Transport incidents" (Port Hope-truck met 48Y in Port of Montréal, 29-6-2020; Hamburg-zendingen 2022) https://www.wise-uranium.org/etiss.html
[7] Haalbaarheidstoets `uranium-porthope-rokkasho` (bindend): ankers z15, kade 38 km van zeeknoop 5690, MARNET Montréal → knoop 20.053 km; `nikkel-riotuba-hachinohe` §3 (zeeknoop 5690); `uranium-porthope-gronau` §2–§4 (b1)
[sat] Esri World Imagery (`v2/tools/sat_check.py`): `v2/build-cache/satcheck/sat-uranium-porthope-rokkasho-{plant,kade}.png`; hergebruikt `sat-uranium-porthope-gronau-montreal-viau.png`

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`bash v2/tools/bak_stromen.sh uranium-porthope-rokkasho` → `v2/data/stroomroute-uranium-porthope-rokkasho.json` (109,3 KB, versie 2, lonlat). **4 benen · 20.552,8 km · 5.467 punten · 4 markers · 2 stippel (haven-aanloop en last mile).**

| # | modaliteit | km gebakken | km brief | naad naar vorige | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 454,1 | hemelsbreed 420, geen wegkm (indicatie) | 0 | letterlijke kopie `uranium-porthope-gronau-weg-porthope-montreal.geojson`, 3.330 punten |
| b2 | zee | 20.052,8 | router 20.052,8 | 3,38 | 135 MARNET-edges, 2.072 punten; kade-snap 3,377 km (zeeknoop 6358) < 5 km; eind snapt op 5690 met 0,000 km |
| b3 | zee (stippel) | 41,1 | 41,1 getekend | 0 | haven-aanloop zeeknoop 5690 → kade, 63 punten |
| b4 | truck (stippel) | 4,8 | hemelsbreed 4,8 | 0 | last mile kade → JNFL, 2 punten |

**Recept.** b1: `--been-geojson truck` met het bestaande Port Hope → Montréal-geojson van `uranium-porthope-gronau` (geen eigen profiel, geen wegscan); b2: `--been zee` 45.5900,-73.5065 → 40.6265,141.5863; b3: `maak_havenaanloop` was al gelukt (kade → knoop); het geojson is omgekeerd opgeslagen als `uranium-porthope-rokkasho-aanloop-mutsuogawara-rev.geojson` en via `--stippel-geojson` gebruikt; b4: `--stippel truck` rechte lijn. Geen via-punten, geen extract, geen lucht, geen leiding. Bak 16 s.

**Toelichting stippels.** b3 is een haven-aanloop (net reikt niet tot de kade, 38,9 km van de zeeknoop; 0,93 km grenst aan de kade omdat de 1:10M-kust het havenbekken niet kent; schematisch, geen vaargeul). b4 is een last mile over de eigen weg van JNFL, geen net op deze korrel.

**Toets.** Alle naden <= 3,38 km (geen > 5 km); de 3,38 km is de zee-snap van Montréal en is identiek aan `uranium-porthope-gronau`. Markers alle 0,0 km van hun lijn. `toets_knikken`: 22 knikken >= 60 gr, 0 omkeringen, 0 terugloop (de pieken zitten in de gekopieerde b1 bij Port Hope en Montréal-Est en de krappe bochten in het Panamakanaal en de St.-Laurent). `toets_rechte_benen`: geen treffer (b3 en b4 zijn stippel). `json.load` ok, versie 2, lonlat, modaliteiten {truck, zee}, elk been >= 2 punten.

**Lessen.** (1) Een haven-aanloop uit een eerdere poging kan kade → knoop lopen terwijl het zeebeen ervoor op de knoop eindigt: keer het geojson om in plaats van opnieuw te rekenen. (2) Een gekopieerd landbeen (b1) erft zijn spikes en de naad van de zee-snap; dat is bewust. (3) Bevinding voor centraal: de sitelaag mist een JNFL-record (40.9778, 141.3541).
