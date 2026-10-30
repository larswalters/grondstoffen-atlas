# Routebrief (licht) · Zeldzame aardmetalen · Santoku Kobe → Rokko Island → Los Angeles/Long Beach → Noveon San Marcos (Japan → Verenigde Staten)

**stroom-id:** `ree-santoku-sanmarcos` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Strip-cast (SC) NdFeB-legering van Santoku Corporation (Kobe) gaat per truck (Route 43, Hanshin Kobe Line, Rokko-brug) naar een containerkade op Rokko Island, per containerschip over de Stille Oceaan naar Los Angeles (B/L; Long Beach als stand-in, zelfde baai) en per truck (I-10, I-35) naar Noveon Magnetics in San Marcos, Texas. Aannemelijk: de B/L noemt Kobe CY en Los Angeles, geen terminal.
**Welke as van het verhaal:** de Japanse legeringsschakel naar een VS-magneetmaker (spiegel van Zuid-Korea, `ree-cheongju-sanmarcos`). Volume: 13 containers, 173,7 t legering (HS 7224.10), wekelijks aug-okt 2026, laatste B/L 2026-10-28 [1][2]; geen jaarcijfer, eenheid kt legering, peiljaar 2026.
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** Kobe-kade gelegd op Rokko Island zuidkade (ontwerp had geen kade); haven-aanloop Kobe verplicht (kade 11,6 km van zeeknoop 5737); B/L zegt Los Angeles, Long Beach is stand-in; Santoku-plant onzeker welke van de vier; km hemelsbreed, geen wegkm. Eindpunt = id (Noveon San Marcos), geen afwijking.

## 1 · Ketenkaart
```
Santoku Kobe `ree-santoku-fabriek` ──(b1 truck · Route 43 → Hanshin 3 → Rokko Ohashi · hemelsbreed 5,5 km)──►
Rokko Island-kade `ree-rokko-kade` ──(b2a haven-aanloop, STIPPEL · ca. 12,9 km)──► zeeknoop 5737 ──(b2 zee · MARNET · 9.639,9 km)──►
zeeknoop 4488 ──(b3 haven-aanloop, STIPPEL · 8,5 km)──► Long Beach-kade `ree-longbeach-kade` ──(b4 truck · I-10 → I-35 · hemelsbreed 1.960 km)──►
Noveon San Marcos `ree-noveon-fabriek` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-santoku-fabriek` → `ree-rokko-kade` | Fukaekitamachi → Route 43 → Hanshin Kobe Line (Route 3) → Rokko Ohashi → Rokko Island-ringweg | hemelsbreed 5,5 km, geen wegkm (OSRM 8,3 km is OSM-afgeleid, indicatie) [8] | maak_stroombeen_weg (extract japan, 2 punten) | nee |
| b2a | B | zee (haven-aanloop) | `ree-rokko-kade` → zeeknoop 5737 (34.5767, 135.2637) | Rokko Island-aanloop (kade 11,6 km van de knoop > 5 km, LAR-586) | ca. 12,9 (handgelegd, z14) | stippel-geojson | **ja** — MARNET reikt niet tot de kade |
| b2 | B | zee (aannemelijk: B/L Los Angeles, LB stand-in) | zeeknoop 5737 → zeeknoop 4488 (33.7039, -118.1945) | Osaka-baai → Stille Oceaan | 9.639,9 (MARNET-proef 2026-10-30, 58 edges, snaps 0) [9] | MARNET | nee |
| b3 | B | zee (haven-aanloop) | zeeknoop 4488 → `ree-longbeach-kade` | Long Beach-havenbekken (6,47 km > 5 km) | 8,5 (LETTERLIJKE KOPIE `ree-yunsheng-longbeach`) [12] | stippel-geojson | **ja** |
| b4 | D | truck (aannemelijk: modaliteit niet gebronnd) | `ree-longbeach-kade` → `ree-noveon-fabriek` | SR-91 → CA-60 → I-10 (Blythe, Phoenix, Tucson, El Paso) → Loop 1604 → I-35 | 2.278 getekend; hemelsbreed 1.960, geen wegkm (OSRM 2.249) — LETTERLIJKE KOPIE `ree-cheongju-sanmarcos` b4 [12] | been-geojson (kopie) | nee |

Beennaam b2: "… (aannemelijk: B/L Los Angeles, Long Beach als stand-in, geen terminal)". Geen luchtbeen: de B/L toont een 20-voets container op de MOL PROFICIENCY (ONE-master) [1]. LA of Long Beach: [1] noemt voor Santoku historisch beide (Santoku America en Molycorp via Long Beach, Noveon via Los Angeles); beide liggen in dezelfde baai (ca. 12 km), dus de kopie van b3/b4 is geen tweede keuze maar het bestaande anker.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-santoku-fabriek` | legeringsfabriek (kop b1) | Santoku Corporation, Kobe-fabriek en hoofdkantoor, 4-14-34 Fukaekitamachi, Higashinada-ku | 34.7247, 135.2906 | [1][3] adres; ArcGIS-geocode (score 100) uit de haalbaarheidstoets | **aannemelijk** (z15 gezien: dicht woon- en bedrijvenblok tussen Route 43 en de kust, geen fabriek aanwijsbaar; welke van de vier plants de SC-legering maakt is niet gebronnd [3][4]) |
| `ree-rokko-kade` | overslag truck → zee | containerkade Rokko Island, zuidfront (RC-4 t/m RC-7; terminal voor deze lading ongenoemd, B/L: Kobe CY) | 34.6812, 135.2625 | [1][5] B/L en terminaltabel; punt eigen z15 | **aannemelijk** (z15 gezien: kranenrij en containerstapels langs de zuidkade; ankerpunt ligt in de yard, 50 m van het routeerpunt van OSRM [8]) |
| `ree-longbeach-kade` | overslag zee → truck | containerkade Long Beach, westkade oostelijk havenbekken | 33.7600, -118.2132 | hergebruikt letterlijk uit `ree-yunsheng-longbeach.md` §3 [12] | aannemelijk (daar gezien: portaalkranen, stapels; terminal onbekend) |
| `ree-noveon-fabriek` | losplek / magneetfabriek | Noveon Magnetics, 1550 Clovis R. Barker Rd, San Marcos TX | 29.8413, -97.9554 | hergebruikt letterlijk uit `ree-larochelle-sanmarcos.md` §3 [12]; adres [2] | aannemelijk (straatniveau, pand niet te onderscheiden) |

Haven Kobe: zeeknoop 5737 (34.5767, 135.2637) op 11,6 km van de kade (eigen MARNET-meting 2026-10-30). Aanloop = handgelegd op Esri z14/z13: een rechte lijn kade → knoop snijdt de westdijk van het stortvak ten zuiden van Rokko Island (dijk 34.672-34.663, 135.260-135.267); daarom west eromheen. Punten in reisvolgorde (lat, lon): 34.6812,135.2625 → 34.6770,135.2600 → 34.6745,135.2490 → 34.6640,135.2490 → 34.6580,135.2580 → 34.5767,135.2637 (12,85 km; speling tot de boog en de pier van Port Island 0,3-0,5 km). Schematisch, geen vaargeul; eerste ca. 0,3 km kade-water valt in de 1:10M-kust als land.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | — | geen via-punten (bindend: profiel met 2 punten, de beide ankers) | — | geen corridorkeuze in een stedelijke korte rit; OSRM [8] rijdt Route 43 → Hanshin 3 → 六甲大橋 → Rokko Island west- en zuidweg (laatste punt 50 m van het anker) |
| b1 | reserve | Rokko Ohashi (brug), alleen als de scan een omweg of "geen wegpad" geeft | 34.7029, 135.2672 | pint de enige verbinding Kobe-vasteland → Rokko Island; op de doorgaande brug, niet in een centrum |
| b4 | — | geen nieuw profiel: letterlijke kopie van het geojson van `ree-cheongju-sanmarcos` b4 (daar 8 via-punten, venster 75) | — | |
Alternatief dat de ontwerp-corridor noemde (Hanshin Bayshore Route 5) wordt niet gevolgd: OSRM kiest Route 43/3 en de Rokko-brug.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Santoku Kobe (plants Kobe, Miki, Akashi, Tsuruga) | Santoku Corporation | zeldzame-aardoxiden/metaal → NdFeB-magneetlegering (strip cast), samarium-legering, waterstofopslaglegering | niet gepubliceerd per plant; deze stroom 173,7 t legering in aug-okt 2026 | [1][3][4] |
| Noveon Magnetics, San Marcos | Noveon | NdFeB-legering → gesinterde magneten | niet gepubliceerd | [2] |

## 6 · Stoppunt
Bij Noveon San Marcos: de enige afnemer in de B/L-records [1][2] en tegelijk het adres van de laatste schakel; fase E vervalt (geen gedocumenteerde klant erna).

## 7 · Open punten
- **Welke Santoku-plant de SC-legering maakt is niet gebronnd:** [3] noemt vier plants (Kobe, Miki, Akashi, Tsuruga) zonder productkoppeling; het B/L-adres is het Kobe-hoofdkantoor [1]. Anker kop aannemelijk, plantgebouw niet gezien.
- **Strip cast (SC) en NdFeB zijn afgeleid:** de B/L zegt "Sc Alloy", HS 7224.10; SC = strip cast volgens het Santoku-profiel [4] (PDF niet leesbaar, alleen via zoekresultaat); alleen een gratis ImportGenius-samenvatting, geen volledig record.
- **Kobe-terminal ongenoemd:** B/L noemt "Kobe CY" onder ONE/MOL; Rokko Island RC-6/7 (NYK/Mitsubishi Logistics) is de enige in [5] met Noord-Amerika-westkust, maar de kade is aanname. Aanloop b2a is schematisch en handgelegd (`maak_havenaanloop` liep in de timeout, 300 s).
- **Los Angeles of Long Beach:** B/L zegt Los Angeles (kandidaat TraPac, OSM 33.7636, -118.2692, MOL-terminal, aanname, niet getekend); Long Beach blijft stand-in met het bestaande anker. Truck LB → San Marcos is aanname (dray).
- **Km:** geen gepubliceerde wegkm; de ±15%-toets is een indicatie op OSM-afgeleide OSRM-lengtes (8,3 en 2.249 km).
- **Volume:** 13 containers/173,7 t is een steekproef; bij één container per week ruwweg 0,8 kt/j, een rekensom en geen bron.
- Overlap: b3 en b4 zijn kopieën (`ree-yunsheng-longbeach`, `ree-cheongju-sanmarcos`); unieke km ca. 81 procent (Kobe-been en 9.640 km zee).

## 8 · Bronnen
[1] ImportGenius, Santoku Corporation (Kobe): 130 zendingen, 13 containers/173.683 kg naar Noveon (LA), laatste B/L MQLAJPUSH26A0040 2026-10-28, 60 vaten van 16.320 kg, HS 7224.10 Sc Alloy, MOL PROFICIENCY 257E, Kobe CY, master ONEYOSAG56561700; historisch Santoku America/Molycorp via Long Beach. https://www.importgenius.com/suppliers/santoku-corporation
[2] ImportGenius, Noveon Magnetics: 1550 Clovis Barker Rd San Marcos, 87 zendingen, Santoku grootste partner, havens o.a. Kobe, Pusan. https://www.importgenius.com/importers/noveon-magnetics-inc
[3] Santoku Corporation, fabrieken: Kobe 4-14-34 Fukaekitamachi, Miki, Akashi, Tsuruga; producten o.a. neodymium-magneetlegering, samarium-legering. https://www.santoku-corp.co.jp/company/factory.html
[4] Prefectuur Hyogo, Santoku-profiel (SC-technologie, Kobe/Miki), via zoekresultaat; PDF niet gelezen. https://web.pref.hyogo.lg.jp/sr07/onlyone/documents/santokucorporation.pdf
[5] Hanshin Port, containerterminals: RC-4/5 (K Line, 14 m) en RC-6/7 (NYK, 16 m, Noord-Amerika-westkust, ONE). https://hanshinport.co.jp/en/facilities/terminal/
[6] Molycorp 10-K FY2013: overname Santoku America 2011-04-15; verkopen aan Santoku Corporation. https://www.sec.gov/Archives/edgar/data/0001489137/000148913714000014/mcp1231201310k.htm
[7] Mining Weekly, 2023-05-16: ASM-Noveon-afspraak (context: andere legeringsleverancier). https://www.miningweekly.com/article/asm-signs-offtake-deal-with-us-noveon-2023-05-16
[8] OSRM demo-router, eigen meting 2026-10-30: Santoku → Rokko 8,3 km (Route 43, Hanshin 3, Rokko Ohashi). OSM-afgeleid, indicatie. https://router.project-osrm.org/
[9] MARNET `hecht_marnet.py route`, eigen proef 2026-10-30: zeeknoop 5737 → 4488 = 9.639,9 km; Rokko-kade → 5737 op 11,6 km.
[10] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-ree-santoku-sanmarcos-{fab-z15,rokko-z15,aanloop-z14,aanloop-z13}.png`.
[11] USGS Mineral Commodity Summaries 2026, rare earths (startpunt, niet gelezen). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-rare-earths.pdf
[12] Eigen briefs: `ree-yunsheng-longbeach.md` §3/§9 (Long Beach-anker, aanloop 8,5), `ree-cheongju-sanmarcos.md` §2/§9 (b4-kopie), `ree-larochelle-sanmarcos.md` §3 (Noveon-anker).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Recept:** `bash v2/tools/bak_stromen.sh ree-santoku-sanmarcos` (functie `bak_ree_santoku_sanmarcos`) → `v2/data/stroomroute-ree-santoku-sanmarcos.json` (versie 2, lonlat, 315,4 KB, 5 benen, 4 markers). Totaal 11.947,1 km, alle naden 0,000 km (alle vijf op 0 m), markers 0,0 m van de lijn.

| # | modaliteit | km gebakken | brief | geometrie |
|---|---|---|---|---|
| b1 | truck | 7,9 (weg 7,8) | hemelsbreed 5,5, OSRM 8,3 (indicatie) | wegscan_puur, profiel `ree-santoku-sanmarcos-fukae-rokko`, extract japan, 2 punten, geen via, vensterKm 40, `eindToegangPrivaat`; -2,5% op gepubliceerdKm 8 |
| b2a | zee, STIPPEL | 12,8 | ca. 12,85 | handgelegd, `ree-santoku-sanmarcos-aanloop-rokko.geojson`, 6 punten kade → knoop 5737 |
| b2 | zee | 9.639,9 | 9.639,9 (proef) | MARNET, snaps 0,000 / 0,000, 58 edges, 995 punten |
| b3 | zee, STIPPEL | 8,5 | 8,5 | LETTERLIJKE KOPIE `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (knoop 4488 → kade) |
| b4 | truck | 2.278,0 | getekend 2.278 | LETTERLIJKE KOPIE `ree-cheongju-sanmarcos-weg-longbeach-sanmarcos.geojson` (13.744 punten) |

**Toelichting.** b1: de scan (refs leeg) gaf 7,8 km tegen OSRM 8,3 zonder omweg; de wegnummers (Route 43, Hanshin 3, Rokko Ohashi) zijn niet nagelopen op de gebakken lijn. Reserve-via (34.7029, 135.2672) bleek niet nodig. Eerste 0,55 km en laatste 2,84 km over kleine klassen (service/tertiary/unclassified, de Rokko Island-terminalwegen). Ankerstukjes 0,06 en 0,05 km. De km-toets is hier een indicatie: geen gepubliceerde wegkm. b2a: stippel omdat MARNET niet tot de kade reikt (kade 11,6 km van knoop 5737, LAR-586); de gelegde punten gaan op z14 west om de dijk van het stortvak en blijven ruim uit de buurt van de Port Island-boog; schematisch, geen vaargeul. b3: stippel met dezelfde reden (6,47 km). b4: geen nieuwe scan, kopie van de cheongju-stroom; aannemelijk (modaliteit en LB-keuze niet gebronnd). Geen lucht, leiding, spoor of binnenvaart.

**Toets.** `toets_knikken`: de knikken liggen in de kopie b4 (stedelijke rotondes en kruispunten rond Long Beach) en in b1 op rotondes en afritten bij Rokko Island (spikes met straal 5-39 m, 109-131 graden); 2 omkeringen, 0 terugloop; geen reparatie nodig. `toets_rechte_benen`: geen stippel met omwegfactor 1,000 in deze stroom. Bestand 315 KB: net boven de ~300 KB-norm door de kopie b4 (354 KB bron); de bol leest de bundel.

**Lessen.** (1) De pbfways-cache van de eerder afgebroken poging (hash 61ec909008b4) paste niet meer: de hash hangt aan via-namen, venster, eindklassen en `eindToegangPrivaat`; een nieuwe japan-scan kostte ca. 10 min (bij een eerste run zonder reus-slot afgebroken op 580 s timeout en daarna opnieuw onder slot gedraaid). Cache nu: `ree-santoku-sanmarcos-fukae-rokko-pbfways-<hash>.json`, bij herbakken van b1 niets aan het profiel (namen, via, venster) wijzigen. (2) Geen herscan nodig voor b2a-b4: handgelegd of kopie. (3) Open punten uit §7 blijven staan; Santoku-plant, Kobe-terminal, LA/Long Beach en jaarvolume niet verder gebronnd.
