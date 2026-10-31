# Routebrief (licht) · nikkel — Hyuga (Miyazaki, Japan) → Shunan (Japan)

**stroom-id:** `nikkel-hyuga-shunan` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** ferronikkel van Hyuga Smelting (SMM-groep, Funaba-cho, Hyuga) gaat per zeeschip vanaf de eigen kade in de Hosojima-haven door de Hyuga-nada, het Bungo-kanaal en de Suo-nada naar de Nippon Steel Yamaguchi Works, Shunan-gebied (Tokuyama-baai); de enige gedocumenteerde band is aandeelhouderschap van Nippon Steel (aannemelijk: één bron, vervoerswijze niet gebronnd).
**Welke as van het verhaal:** *de Japanse schakel van ferronikkelsmelter naar roestvrijstaalfabriek* — Hyuga Smelting maakt ferronikkel uit erts dat volgens de bedrijfssite geheel uit Nieuw-Caledonië komt [2][4]; Nippon Steel is aandeelhouder [3]. Volume: circa 100 kt ferronikkel/j met Ni >= 16 % = circa 16 kt Ni/j (ja.wikipedia, geen peiljaar) [5]; het aandeel dat naar Shunan gaat is niet gebronnen.

## 1 · Ketenkaart
```
Hyuga-kade `ni-hyuga-kade` (Hosojima-haven) ──(b1 zee · haven-aanloop Hyuga-baai · ~33,9 km, stippel)──►
   MARNET-zeeknoop 9069 (32.1826,131.7590) ──(b2 zee · MARNET · Hyuga-nada, Bungo-kanaal, Suo-nada · ~186,6 km)──►
   MARNET-zeeknoop 5738 (33.7500,131.9000) ──(b3 zee · haven-aanloop Suo-nada → Tokuyama-baai · ~38,0 km, stippel · LETTERLIJKE KOPIE)──► Shunan-kade `ni-shunan-kade`
   ═══ site-anker Shunan Works `ni-shunan-fabriek` (geen eigen been: kade en walserij liggen op één terrein) ═══ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ni-hyuga-kade` → zeeknoop 9069 | Hyuga-baai / Hyuga-nada (kust Miyazaki) | 33,9 (gemeten door maak_havenaanloop, 55 punten, omweg 1,098 op 30,9 hemelsbreed) [toets] | maak_havenaanloop (kant-en-klaar geojson, niet opnieuw rekenen) | ja — MARNET reikt niet tot de kade (30,9 km van de zeeknoop) |
| b2 | B | zee | zeeknoop 9069 → zeeknoop 5738 | Hyuga-nada, Bungo-kanaal, Iyo-nada, Suo-nada (router beslist) | 186,6 (MARNET-meting 21 punten [toets]; hemelsbreed circa 175; geen gepubliceerde scheepsafstand) | MARNET | nee |
| b3 | B | zee | zeeknoop 5738 → `ni-shunan-kade` | Suo-nada, Tokuyama-baai | 38,0 (gemeten door maak_havenaanloop in nikkel-doniambo-shunan, 60 punten) [toets] | LETTERLIJKE KOPIE `nikkel-doniambo-shunan-aanloop-shunan-rev.geojson` | ja — MARNET reikt niet tot de kade (35,8 km) |

Zee-beennaam voor de bak (aannemelijk-vlag): `zeeschip Hyuga-kade → Shunan-kade (aannemelijk: één bron, alleen aandeelhoudersband Nippon Steel; geen bron noemt een levering of het zeevervoer van ferronikkel)`. Geen truckbeen: de Shunan-kade ligt aan de zuidrand van het fabrieksterrein, de walserij 0,2 km noordelijk [7]. Geen fase C/D/E.
Gedeeld: b3 is een letterlijke kopie van b3 van `nikkel-doniambo-shunan` (noem dat in de beennaam); het b2-pad ligt 100 % op bestaande banen (doniambo-shunan, taganito-niihama, riotuba-niihama) — nieuw is alleen b1 plus de Hyuga-site.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-hyuga-kade` | laadkade (kop van b1) | Eigen kade Hyuga Smelting, Hosojima-haven, Hyuga | 32.4460, 131.6555 | [1][9] | bron-gelegd (z15 en z16 gezien: punt op de noordoostelijke kadehoek van het smelterterrein, schip langszij aan de oostkade, ertsopslag erachter; bedrijfssite noemt een eigen kade voor schepen tot 30.000 t) |
| `ni-hyuga-fabriek` | smelter (site-anker, geen marker) | Hyuga Smelting ferronikkelfabriek, Funaba-cho 5 | 32.4455, 131.6540 | [2][9] | bron-gelegd (z16 gezien: ovenhallen met bruine daken, ertsstapels en bandtransporteurs op een landtong aan het water, 0,15 km van de kade; terrein 350.036 m2) |
| `ni-shunan-kade` | losplek (staart van b3) | Kade Nippon Steel Yamaguchi Works, Shunan-gebied (Tokuyama-baai) | 34.0537, 131.7745 | [7] | HERGEBRUIKT letterlijk uit `nikkel-doniambo-shunan.md` (bron-gelegd z17: steiger met coaster langszij aan de zuidkade) |
| `ni-shunan-fabriek` | fabriek (site-anker, geen marker) | Nippon Steel Yamaguchi Works, Shunan-gebied | 34.0590, 131.7772 | [7] | HERGEBRUIKT letterlijk uit `nikkel-doniambo-shunan.md` (GEM-coördinaat; walserij-/staalcomplex op z16) |
| — | zeeknoop (geen anker) | MARNET-zeeknoop 9069 | 32.1826, 131.7590 | [toets] | router-knoop, 30,9 km ZZO van de kade; alleen toets golf 14 |
| — | zeeknoop (geen anker) | MARNET-zeeknoop 5738 | 33.7500, 131.9000 | [8] | HERGEBRUIKT uit `nikkel-doniambo-shunan.md` |

## 4 · Via-punten
Geen — er is geen landbeen. De corridor van b2 kiest de router; b1 en b3 zijn schematische haven-aanlopen over water.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Hyuga Smelting (Hosojima) | Sumitomo Metal Mining 70,2 %, Mitsui & Co 15,0 %, Nippon Steel 14,8 % (volgens bedrijfssite; ja.wikipedia noemt SMM als moederbedrijf) | Nieuw-Caledonisch nikkelerts (circa 2 % Ni) → ferronikkel (HCS, Ni 14-25 %) + groen zand | circa 100 kt ferronikkel/j (Ni >= 16 %) [5] | [2][3][5][6] |
| Nippon Steel Yamaguchi Works, Shunan-gebied | Nippon Steel (sinds 2025-04-01) | schroot en legering → roestvrij staal, elektrische ovens | 3 ovens van 433 kt/j, één stilgelegd sinds maart 2024 | [7][8] |

## 6 · Stoppunt
De brief stopt bij de Shunan-kade: het ferronikkel wordt hier (aannemelijk) in de elektrische ovens van het roestvrijstaalbedrijf gesmolten, en geen bron noemt een volgende locatie of een leveringscontract. Fase D en E vervallen.

## 7 · Open punten
- **Geen bron noemt een levering Hyuga → Shunan.** De band is aandeelhouderschap: Nippon Steel 14,8 % van Hyuga Smelting [3]; de bedrijfssite noemt geen klanten of afnemers. Gelezen als aannemelijk, zoals `nikkel-doniambo-shunan`.
- **Vervoerswijze niet gebronnd.** De bedrijfssite noemt een eigen kade en een shiploader (voor groen zand) [3]; of het ferronikkel (als shot gegoten, "in containers" [3]) per schip naar Shunan gaat, staat nergens. Zee is de werkaanname (kade voor 30.000 t-schepen, Shunan aan zee).
- **Smelt Shunan ferronikkel?** GEM noemt Shunan schrootgebaseerd en noemt ferronikkel niet [7]; het naburige Hikari-gebied kan de nikkelafnemer zijn.
- **Aandelenpercentages wijken af:** bedrijfssite 70,2 / 15,0 / 14,8 [3]; de toets noemde ja.wikipedia met 60 / 15 / 25 (pagina niet herlezen: de lezing van nu noemt geen percentages). Geen percentages in de beennaam.
- **Terugloop bij de aanloop:** knoop 9069 ligt 30,9 km ZZO van de kade, terwijl b2 daarna weer noordwaarts langs dezelfde kust loopt; de lijn gaat dus naar zee en weer terug, een gevolg van de gekozen knoop. Bake-agent: `toets_knikken` melden, niets verschuiven.
- **Aanloop schematisch:** kortste pad over water tegen 1:10M-landpolygonen (0,95 km over land, rechte lijn zou 13,6 % NE-land kruisen); geen bevaren vaargeul.
- **Naam Shunan achterhaald:** NSSC is op 2025-04-01 opgegaan in Nippon Steel [8]. Zeeafstand: geen gepubliceerde scheepsafstand, de ±15 %-toets is een indicatie.

## 8 · Bronnen
[1] Hyuga Smelting, Bedrijfsoverzicht — terrein circa 350.000 m2 aan de industriehaven Hosojima, eigen kade voor schepen tot 30.000 t. https://www.hyuga-smelting.co.jp/company/
[2] Hyuga Smelting, startpagina — alle nikkelerts uit Nieuw-Caledonië, SMM-groep met Nippon Steel en Mitsui, nieuws t/m 2026-10. https://www.hyuga-smelting.co.jp/
[3] Hyuga Smelting, Bedrijfsgegevens — Funaba-cho 5, Hyuga; terrein 350.036 m2; aandeelhouders SMM 70,2 %, Mitsui 15,0 %, Nippon Steel 14,8 %. https://hyuga-smelting.co.jp/company/about-us/
[4] Hyuga Smelting, Productieproces — shot-gegoten ferronikkel in containers; groen zand per truck of shiploader op de eigen kade. https://hyuga-smelting.co.jp/company/process/
[5] Wikipedia (ja), 日向製錬所 — ferronikkel uit Indonesisch/Nieuw-Caledonisch erts, circa 100.000 t/j, Ni >= 16 %, Funaba-cho; dochter van SMM. https://ja.wikipedia.org/wiki/%E6%97%A5%E5%90%91%E8%A3%BD%E9%8C%AC%E6%89%80
[6] Hyuga Smelting, Ferronikkel — HCS-kwaliteit Ni 14-25 %, voor roestvrij staal en constructiestaal. https://hyuga-smelting.co.jp/products/ferronickel/
[7] GEM.wiki, Nippon Stainless Steel Yamaguchi Works (Shunan Area) — 4976 Nomuraminami-machi, 34,059009/131,777221, drie EAF van 433 kt/j. https://www.gem.wiki/Nippon_Stainless_Steel_Yamaguchi_Works_(Shunan_Area)_steel_plant
[8] Wikipedia (ja), Nippon Steel Stainless — Shunan = ex Nisshin Steel, NSSC opgegaan in Nippon Steel op 2025-04-01 (overgenomen uit `nikkel-doniambo-shunan.md` [5]). https://ja.wikipedia.org/wiki/%E6%97%A5%E9%89%84%E3%82%B9%E3%83%86%E3%83%B3%E3%83%AC%E3%82%B9
[9] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-nikkel-hyuga-shunan-hyuga-kade.png` (z15) en `-hyuga-fabriek.png` (z16); oudere blik `sat-toets-nikkel-hyuga-kade.png`.
[10] `v2/design/routebrieven/nikkel-doniambo-shunan.md` — Shunan-ankers, zeeknoop 5738 en de Shunan-aanloop (gebakken 2026-10-30).
[toets] Haalbaarheidstoets (2026-10-31): zeeknoop 9069 op 30,9 km van de kade; MARNET 9069 → 5738 = 186,6 km (21 punten); `nikkel-hyuga-shunan-aanloop-hyuga.geojson` (55 punten, 33,9 km, kade → knoop) staat in `v2/build-cache/ais/graaf/`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Uitvoer:** `v2/data/stroomroute-nikkel-hyuga-shunan.json` (3,6 KB, versie 2, lonlat) via `bash v2/tools/bak_stromen.sh nikkel-hyuga-shunan` (functie `bak_nikkel_hyuga_shunan`). Totaal 258,5 km, 136 punten, 2 markers, alleen zee.

| # | modaliteit | km gemeten | km brief | naad | punten |
|---|---|---|---|---|---|
| b1 | zee, stippel (haven-aanloop Hyuga-baai) | 33,9 | 33,9 | 0 | 55 |
| b2 | zee, MARNET zeeknoop 9069 → 5738, doorgetrokken | 186,6 | 186,6 (MARNET-meting; geen gepubliceerde afstand) | 0,000 | 21 |
| b3 | zee, stippel (haven-aanloop Shunan/Tokuyama-baai, letterlijke kopie) | 38,0 | 38,0 | 0,000 | 60 |

**Markers:** `ni-hyuga-kade` (32.4460, 131.6555) en `ni-shunan-kade` (34.0537, 131.7745), beide 0,0 km van de lijn. De twee fabrieksankers zijn geen marker.

**Recept:** b1 = bestaand `nikkel-hyuga-shunan-aanloop-hyuga.geojson` (maak_havenaanloop, kade → knoop, FeatureCollection, niet opnieuw gerekend). b2 = `--been zee` met beide zeeknopen exact opgegeven (snap 0,000 km, 3 MARNET-edges). b3 = letterlijke kopie van `nikkel-doniambo-shunan-aanloop-shunan-rev.geojson` (knoop → kade, al in reisvolgorde).

**Toelichting stippels:** beide aanlopen zijn stippel omdat MARNET niet tot de kade reikt (30,9 en 35,8 km van de zeeknoop); het pad is kortste pad over water en geen waargenomen vaargeul. b2 is doorgetrokken; "aannemelijk: één bron" staat in de beennaam, niet in de lijnstijl.

**Toets:** geen naad > 0,001 km; omwegfactoren 1,098 / 1,068 / 1,064; geen echte scheepsafstand gepubliceerd, dus de ±15 %-toets is een indicatie. `toets_knikken` op het bestand: 0 knikken, 0 omkeringen (het toetst alleen het doorgetrokken b2). Aan de naad b1 → b2 (zeeknoop 9069) is wel een keerpunt van circa 121 gr: de aanloop eindigt zuidoostwaarts op de knoop (peiling 149) en b2 vertrekt noordoostwaarts (peiling 28). `toets_rechte_benen`: geen treffer voor deze stroom.

**Afwijkingen van het ontwerp:** geen; eindpunt en id kloppen.

**Lessen:** (1) een kade-eerst geschreven aanloop mag niet worden omgekeerd als hij het eerste been is, het tweede (Shunan) moet al knoop → kade zijn: de `-rev`-kopie hier gebruiken. (2) De terugloop bij knoop 9069 is een gevolg van de gekozen zeeknoop (30,9 km ZZO van de kade); niets verschoven, wel melden. (3) Open punten uit §7 blijven staan: geen bron noemt een levering Hyuga → Shunan en de vervoerswijze is niet gebronnd.
