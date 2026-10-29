# Routebrief (licht) · diamant — Udachny (Jakoetië) → Moskou → Dubai (VAE)

**stroom-id:** `diamant-udachny-dubai` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** ruwe diamant van Alrosa's Udachny-divisie (Udachnaya-put en GOK) gaat per truck naar Polyarny Airport (PYJ, thuisbasis Alrosa-luchtvaart), vliegt als vrachtvlucht (grootcirkel) naar Sheremetyevo-Cargo (SVO) en door naar het DXB-vrachtcomplex, en gaat per truck naar DMCC / Dubai Diamond Exchange (Almas Tower, JLT).
**Welke as van het verhaal:** *tweede Russische productiekern (Udachny, naast Mirny) naar het Gulf-handelscentrum, via Moskou.* Udachny MPD 3,8 Mct/j (2016, Wikipedia Alrosa [3]); sitelaag `w-udachny` 4,5 Mct/j (orde-grootte). Aandeel via Dubai niet gebrond (zie §7). Eenheid Mct/j; waarde per karaat niet gebrond. Dubai-staart rust op één bron: Alrosa-DMCC-akkoord 8-4-2014 en Alrosa's Dubai-dochter Arcos East DMCC [6][7].

## 1 · Ketenkaart
```
Udachnaya-put / Udachny GOK `dia-udachny-put` ──(b1 truck · mijn-/dorpsweg Udachny → Polyarny · hemelsbreed 13 km, geen wegkm)──►
Polyarny Airport (PYJ), vrachtplatform `dia-pyj-vracht` ──(b2 lucht · vlucht PYJ → SVO, grootcirkel · 3.894 km)──►
Sheremetyevo-Cargo (SVO), Moskou `dia-svo-cargo` ──(b3 lucht · vlucht SVO → DXB, grootcirkel · 3.709 km)──►
DXB-vrachtcomplex (Cargo Village) `dia-dxb-vracht` ──(b4 truck · letterlijke kopie diamant-mbujimayi-dubai b4 · 31,2 km)──►
DMCC / Almas Tower, JLT `dia-dmcc-almas` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Udachnaya-put/GOK → Polyarny Airport vrachtplatform | mijn- en dorpsweg Udachny – Polyarny (service/primary), geen corridorkeuze | hemelsbreed 13,0 km, geen wegkm (OSRM/OSM-indicatie 21,9 km, geen publicatie [11]) | maak_stroombeen_weg (rusland-verrehoosten), geen via-punten | nee (hooguit ≤100 m airside-stuk) |
| b2 | B | lucht | PYJ → SVO | vrachtvlucht PYJ → SVO, grootcirkel (aannemelijk zonder vrachtbron) | 3.894,4 (berekend, grootcirkel) | maak_luchtbeen | nee, doorgetrokken |
| b3 | B | lucht | SVO → DXB | vrachtvlucht SVO → DXB, grootcirkel (aannemelijk: één bron voor Dubai-afzet) | 3.709,5 (berekend, grootcirkel) | maak_luchtbeen | nee, doorgetrokken |
| b4 | C | truck | DXB-vrachtcomplex → DMCC/Almas Tower | Airport Road → Sheikh Zayed Road/Al Ittihad Road | 31,2 km gebakken weg (hemelsbreed 29,0; geen gepubliceerde wegkm) | LETTERLIJKE KOPIE `diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-udachny-put` | mijn / laadplek | Udachnaya-put en Udachny GOK (Alrosa Udachny MPD), Jakoetië | 66.4342, 112.3175 | [3][4] | bron-gelegd (z14 gezien: grote terrassenput, kruis in de put; verwerkingsfabriek met schoorsteen en tailingmeer direct zuidoost) |
| `dia-pyj-vracht` | vrachtplatform / vertrek luchtvracht | Polyarny Airport (PYJ), apron en loodsen | 66.3995, 112.0378 | [1][2] | bron-gelegd (z15 gezien: verhard platform met gebouwen en loodsen oost van de baan, wegen sluiten aan; deels wolken ten westen; geen vrachttoestellen zichtbaar). NIET het Wikipedia-punt 66.4167,112.05: dat ligt in bos ca. 2 km oost van de baan |
| `dia-svo-cargo` | vrachtterminal / aankomst+vertrek luchtvracht | Sheremetyevo-Cargo, Moskou | 55.9696, 37.4362 | [9] (hergebruik `diamant-mirny-mumbai`) | bron-gelegd (daar z15: vrachtgebouw ten zuiden van het passagiersapron, vrachttoestellen op het platform) |
| `dia-dxb-vracht` | vrachtterminal / aankomst luchtvracht | DXB Cargo Village / Emirates SkyCargo, Al Garhoud | 25.2574524, 55.3405972 | [10] (hergebruik `diamant-mbujimayi-dubai`, `-dubai-surat`) | bron-gelegd (daar z14–z15: loodsenrij en apron) |
| `dia-dmcc-almas` | handelshub / eindpunt | DMCC / Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [6][10] | bron-gelegd (daar z15: toren in het JLT-cluster; 0,05 km van de lijn) |

## 4 · Via-punten
*(geen: b1 is een korte mijn-/dorpsweg zonder corridorkeuze, b4 een kopie, b2 en b3 zijn luchtbenen. Bak-aanwijzing: `vensterKm` 30 voor b1, `eindKlassen` service/unclassified/tertiary.)*

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Udachny GOK (verwerking) | Alrosa Udachny MPD | erts → ruwe diamant | 3,8 Mct/j geproduceerd (2016) | [3] |
| Moskou-verkoop (sortering/verkoop, locatie onbekend) | Alrosa (hoofdkantoor Mirny en Moskou) | ruw → gesorteerd ruw | n.v.t. | [3] |
| Arcos East DMCC, Dubai (verkoop) | Alrosa-dochter | ruw → tenders/spot | USD 100 mln gekocht in 9 mnd 2014 | [6][7] |

## 6 · Stoppunt
De brief stopt bij DMCC/Almas Tower: het gebrond handelsadres van Alrosa-ruw in Dubai [6][7]; een bron die Udachny-ruw aan een vervolgafnemer (slijperij Surat) koppelt ontbreekt, dus fase D vervalt, E ook.

## 7 · Open punten
- **Geen vrachtbron voor PYJ → SVO.** Alrosa vliegt vanuit PYJ passagiers (Moskou, Mirny); dat Udachny-ruw per vracht via Moskou gaat staat in geen bron, beide vluchten zijn aannemelijk (zonder vrachtbron). Lijn Udachny–Moskou (Flight 514, 2010) was een passagiersvlucht; actuele dienst PYJ–Moskou onduidelijk (aggregatoren: laatste vlucht 2021-12-26 [14]).
- **Alrosa-luchtvaart bedient Vnukovo en Domodedovo, niet SVO** [12]; SVO-Cargo is de bestaande conventie uit `diamant-mirny-mumbai`. Risico: werkelijke Moskou-luchthaven kan VKO/DME zijn.
- **Sortering kan in Mirny of Moskou liggen**; dan loopt de keten via MJZ (lijkt op afgewezen mirny-dubai: hier andere mijn, ander vliegveld, eigen b1/b2).
- **b1 is hemelsbreed 13,0 km, geen wegkm**; OSRM/OSM-indicatie 21,9 km (eigen meting 23-24 km): ±15%-toets geldt niet als norm, alleen indicatie.
- **PYJ-anker** is op z15 deels wolkbedekt; platform herkend, vrachtloodsen niet apart te onderscheiden. Platform ligt airside: laatste stuk eventueel stippel ≤100 m.
- **Udachny-anker in de put**, niet op de GOK-fabriek (66.428, 112.328, niet apart gelegd); site-niveau volstaat. De put is sinds ca. 2014 uitgemijnd/ondergronds [3][4]: mijn = ondergrondse Udachny-mijn onder dezelfde site.
- **Aandeel via Dubai** (en volume Udachny-specifiek) niet gebrond; sitelaag 4,5 Mct/j is orde-grootte, jaar 2016 voor 3,8 Mct/j.
- Mining Weekly-artikel [8] gaf 403 en is niet gelezen; DMCC-pagina [6] en Mining.com [7] zijn gebruikt.

## 8 · Bronnen
[1] Wikipedia, "Polyarny Airport" (PYJ, 66.4167/112.05; 12 km west van Udachny; Alrosa-thuisbasis). https://en.wikipedia.org/wiki/Polyarny_Airport
[2] Wikipedia, "Alrosa (airline)" (bases MJZ en PYJ). https://en.wikipedia.org/wiki/Alrosa_(airline)
[3] Wikipedia, "Alrosa" (Udachny MPD: Udachnaya en Zarnitsa; 11% van productie, 3,8 Mct in 2016; hoofdkantoor Mirny en Moskou). https://en.wikipedia.org/wiki/Alrosa
[4] Wikipedia, "Udachnaya pipe" (66.43417/112.3175; open put, ondergrondse overgang gepland 2010). https://en.wikipedia.org/wiki/Udachnaya_pipe
[5] Wikipedia, "Udachny" (stad aan de Markha, 508 km van Mirny). https://en.wikipedia.org/wiki/Udachny
[6] DMCC, "Dubai Diamond Exchange signs Cooperation Agreement with ALROSA", 2014. https://www.dmcc.ae/news/dubai-diamond-exchange-signs-cooperation-agreement-with-alrosa
[7] Mining.com, "ALROSA and the Dubai Diamond Exchange sign memorandum of understanding", 2014-04. https://www.mining.com/web/alrosa-and-the-dubai-diamond-exchange-sign-memorandum-of-understanding/
[8] Mining Weekly, 2014-04-08 (403, niet gelezen). https://www.miningweekly.com/article/dubai-diamond-exchange-signs-cooperation-agreement-with-alrosa-2014-04-08
[9] Routebrief `diamant-mirny-mumbai` (anker `dia-svo-cargo`). `v2/design/routebrieven/diamant-mirny-mumbai.md`
[10] Routebrieven `diamant-mbujimayi-dubai` en `diamant-dubai-surat` (ankers DXB/DMCC, b4-geojson). `v2/design/routebrieven/`
[11] OSRM-demo (OSM-routing), put → apron: 21,9 km, snap 107 m / 59 m. https://router.project-osrm.org
[12] ALROSA Airline, Vnukovo-samenwerking (samenvatting uit zoekresultaat, pagina niet gelezen). https://aero.alrosa.ru/en/airline/news/aviakompaniya-alrosa-i-mezhdunarodnyy-aeroport-vnukovo-otmetili-pervyy-god-uspeshnogo-sotrudnichestv/
[13] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-diamant-udachny-dubai-udachnaya-put.png`, `-pyj-apron.png`.
[14] FlightsFrom, PYJ–DME (aggregator, zwak bewijs). https://www.flightsfrom.com/PYJ-DME

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh diamant-udachny-dubai` → `v2/data/stroomroute-diamant-udachny-dubai.json` (19,4 KB, versie 2, lonlat). Totaal 7.657,0 km, 4 benen, 5 markers, geen stippel, geen naad (alle 0,00 km), alle markers ≤ 0,02 km van de lijn.

| # | modaliteit | been | km gebakken | km brief | toets |
|---|---|---|---|---|---|
| b1 | truck | Udachnaya-put/GOK → PYJ-vrachtplatform | 21,9 (weg 21,7 + ankerverbindingen 0,11/0,06) | hemelsbreed 13,0, geen wegkm (OSRM 21,9) | alleen indicatie: −1,4% tegen 22; OSRM-route bevestigd |
| b2 | lucht | vlucht PYJ → SVO, grootcirkel | 3.894,4 | 3.894,4 berekend | gelijk |
| b3 | lucht | vlucht SVO → DXB, grootcirkel | 3.709,5 | 3.709,5 berekend | gelijk |
| b4 | truck | DXB → DMCC/Almas Tower, kopie | 31,2 | 31,2 gebakken | letterlijke kopie |

**Recept.** b1: profiel `diamant-udachny-dubai-put-pyj` in `maak_stroombeen_weg.py` (extract rusland-verrehoosten, alleen de twee ankers als via-punten, vensterKm 30, eindKlassen service/unclassified/tertiary, geen refs), gescand met `wegscan_puur.py` (40 s). b2 en b3: `maak_luchtbeen.py` (157 en 150 punten). b4: `diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson` letterlijk, niet omgekeerd, in de beennaam genoemd. Functie `bak_diamant_udachny_dubai()`.

**Toelichting.**
- *Stippel:* geen. De ankers snappen op 0,11 en 0,06 km, dus het airside-stuk van PYJ blijft ruim onder 100 m en vraagt geen last-mile-stippel.
- *Haven-aanloop / leiding:* niet van toepassing (geen zee, geen leiding).
- *Vluchten:* doorgetrokken grootcirkels. PYJ → SVO heeft geen vrachtbron en SVO is een conventie uit diamant-mirny-mumbai (Alrosa-luchtvaart vliegt VKO/DME); SVO → DXB rust op één bron (Alrosa-DMCC-akkoord 2014). Beide staan "aannemelijk" in de beennaam, niet in de lijnstijl.
- *Knikken:* 12 knikken ≥ 60 gr (6 in b1, 6 in de kopie b4), allemaal korte spikes van 5–67 m op wegknooppunten, 0 omkeringen, 0 terugloop.
- *Id en eindpunt:* het id belooft Dubai en de lijn eindigt in DMCC/Almas Tower, Dubai: geen afwijking.

**Lessen.** (1) Een korte mijn-/dorpsweg op rusland-verrehoosten scant in 40 s en snapt direct op beide ankers; `service`/`unclassified`/`tertiary` als eindKlassen volstond. (2) Een bestaande OSRM-indicatie als gepubliceerdKm geeft een zinvolle indicatie-toets, maar de brief moet dan letterlijk "hemelsbreed X km, geen wegkm" zeggen. (3) Het PYJ-anker is deels wolkbedekt: het platform is herkend, de loodsen niet apart onderscheiden (open punt blijft).
