# Routebrief (licht) · kolen — Pniówek (JSW) → ArcelorMittal Poland Zdzieszowice (Polen)

**stroom-id:** `kolen-pniowek-zdzieszowice` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** cokeskool (type 35.1, ortokoks) uit de ondergrondse mijn KWK Pniówek (JSW, Pawłowice, Silezië) gaat per **spoor**
(Żory — Rybnik — lijn 140 naar Nędza — lijn 151 — Kędzierzyn-Koźle — lijn 136) naar de cokerij van ArcelorMittal Poland in Zdzieszowice
(Opole), waar de kool koks wordt — stoppunt, want geen bron noemt de afnemer van dit koks. Titel noemt de echte eigenaar: de cokerij is
**ArcelorMittal Poland, geen JSW KOKS** (het ontwerp zei dat; de toets en bron [3] corrigeren).
**Welke as van het verhaal:** *Poolse cokeskool voor Poolse koks* — de grootste cokesproducent van Polen draait op JSW-kool. JSW produceert
**ca. 12 Mt kolen per jaar** (en.wikipedia, jaar niet genoemd) [1]; Pniówek **11.200 t/dag gemiddeld in 2013** [2] (orde 3,7–4,1 Mt/j, afgeleid,
niet gepubliceerd); ArcelorMittal kocht **26% van de JSW-productie** (2015) [6] en meer dan de helft van de kool van zijn cokerijen kwam uit
het JSW-gebied (2015) [5]; Zdzieszowice: **>4 Mt koks/j** (2008) [3], capaciteit **4,2 Mt/j** [6]. Het aandeel van déze mijn is niet gepubliceerd (§7).

## 1 · Ketenkaart
```
Pniówek-mijn (schachten + spoorplein + steenkoolopslag) `kolen-pniowek-laad`
   ──(b1 spoor · Pawłowice → Żory → Rybnik → Nędza → Kędzierzyn-Koźle → Zdzieszowice · graaf-proef 89,5 km,
       aannemelijk: één bron voor JSW → AMP, geen bron voor Pniówek specifiek)──► Cokerij Zdzieszowice (AMP) `kolen-zdzieszowice-cokerij` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A+C | spoor | `kolen-pniowek-laad` → `kolen-zdzieszowice-cokerij` | Pniówek-sporen → Żory (lijn 159, 14,5 km Żory–Pawłowice Śl. [7]) → Rybnik (lijn 148 [8]) → lijn 140 Rybnik–Nędza [9] → lijn 151 Nędza–Kędzierzyn-Koźle → lijn 136 Kędzierzyn-Koźle–Zdzieszowice (km −0,2 → 10,4 = 10,6 km [10]) | hemelsbreed 63,4 km, geen gepubliceerde spoorkm (alleen delen: 14,5 + 10,6 km); graaf-proef 89,5 km router / 92,8 km over de 384 punten (verhouding 1,41–1,46, 0 bochten ≥60°) — de ±15%-toets is indicatie, geen norm | toets_spoorroute (1-op-1-net), één run, geen via | nee — volledig in het 1-op-1-net; "aannemelijk" staat in de beennaam |

Fase C (last mile) vervalt: beide ankers liggen op het emplacement/terrein zelf (snap kop 0,09 km, staart 0,04 km). Geen zee, weg, leiding,
lucht, haven-aanloop of kopie. Geen fase D (geen bron voor de afnemer van het koks), geen E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-pniowek-laad` | mijn / laadplek | KWK Pniówek (JSW), Pawłowice, spoorplein aan de zuidrand van het mijnterrein | 49.9681, 18.6878 | [2][11] | bron-gelegd (z15 gezien: complex met schachtgebouwen, spoorbundel die westwaarts het terrein verlaat, donkere kolenopslag aan de noordkant, parkeerterrein en woonwijk ten zuiden). Het wiki-punt 49.9672, 18.6897 [2] ligt 0,2 km ernaast op hetzelfde terrein |
| `kolen-zdzieszowice-cokerij` | verwerker / losplek | ArcelorMittal Poland, Oddział Zdzieszowice — cokesbatterijen ZO van de stad | 50.4195, 18.1430 | [3][11] | bron-gelegd (z15 gezien: groot industrieel complex van ~200 ha met batterijen en kolenopslag, een gashouder en rangeerterrein; spoorlijn langs de westzijde). Het wiki-punt 50.4228, 18.1303 [3] ligt in de woonwijk, 1,0 km WNW van het complex, en is niet gebruikt |

Hergebruik: geen bestaand anker (geen eerdere Poolse kolenketen; sitelaag heeft geen Poolse sites).

## 4 · Via-punten
Geen. De graaf-route volgt zonder via de bronlijnen: gemeten langs de 384 punten passeert hij Żory op 0,8 km (route-km 19,6), Rybnik op 0,6 km (33,8),
Rydułtowy op 0,8 km (44,3), Nędza op 0,5 km (59,8; hier sluit lijn 140 aan op lijn 151 [9]) en Kędzierzyn-Koźle op 0,1 km (82,6); Racibórz ligt 10 km
ernaast (lijn 158/Chałupki wordt dus niet gebruikt) en Gliwice 22 km. Een via op een station is niet nodig en zou een bocht kunnen afdwingen.
Geen corridorkeuze die een via-punt rechtvaardigt: de enige alternatieve lijn (via Racibórz) is een omweg.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| KWK Pniówek | Jastrzębska Spółka Węglowa (sinds 1993) | steenkool, type 35.1 (ortokoks) → spoor | 11.200 t/dag (2013), 14.500 t/dag (2008); reserves 101,9 Mt | [2][5] |
| Cokerij Zdzieszowice | ArcelorMittal Poland (sinds 31-12-2010, daarvoor Zakłady Koksownicze Zdzieszowice) | cokeskool → koks, cokesgas, benzol, teer, zwavel | >4 Mt koks/j (2008); 4,2 Mt/j capaciteit; ~200 ha | [3][6] |

## 6 · Stoppunt
De brief stopt bij de cokerij van Zdzieszowice: de kool houdt daar op als grondstof, en het koks (grotendeels geëxporteerd [3]) heeft geen
door één bron genoemde volgende locatie.

## 7 · Open punten
- **Koppeling Pniówek → Zdzieszowice: niet gebrond.** Bronnen zeggen alleen dat JSW de cokerijen van ArcelorMittal in Zdzieszowice en Kraków
  voedt [5][6] en dat er in 2026 een jaarcontract van 2,1 mld zloty is (13-03-2026, geen mijn, geen cokerij genoemd) [4]. Pniówek levert type 35.1
  (ortokoks, de basis van metallurgisch koks) [2] — dat maakt de koppeling aannemelijk, niet bewezen. Status: aannemelijk.
- **Spoor-aansluiting van Pniówek op het net niet gebrond** (geen pagina noemt een bocznica van de mijn); alleen het satellietbeeld toont een spoorplein.
- **Spoorlengte:** geen gepubliceerde totale spoorkm; de ±15%-toets is dus indicatie. De route over lijn 159 begint met ~19 km via Żory.
- **Aandeel Pniówek** in de AMP-aanvoer en jaarvolume van de mijn niet gepubliceerd; 3,7–4,1 Mt/j is afgeleid uit 11.200 t/dag.
- **Peiljaren:** de volumes van JSW (~12 Mt/j) en het 26%-aandeel zijn jaren oud (2015 en eerder); Zdzieszowice-productie 2008.
- **Sitelaag:** `kolen-sitelaag.json` heeft geen Poolse sites; Pniówek en Zdzieszowice kunnen centraal als sites met productie/capaciteit erbij.

## 8 · Bronnen
[1] en.wikipedia, Jastrzębska Spółka Węglowa — ~12 Mt kolen/j, reserves 503,4 Mt. https://en.wikipedia.org/wiki/Jastrz%C4%99bska_Sp%C3%B3%C5%82ka_W%C4%99glowa
[2] pl.wikipedia, Kopalnia Węgla Kamiennego „Pniówek” — Pawłowice, 49°58′02″N 18°41′23″E, JSW sinds 1993, type 35.1, 11.200 t/dag (2013). https://pl.wikipedia.org/wiki/Kopalnia_W%C4%99gla_Kamiennego_%E2%80%9EPni%C3%B3wek%E2%80%9D
[3] pl.wikipedia, ArcelorMittal Poland Oddział w Zdzieszowicach — 50.4228, 18.1303, >4 Mt koks (2008), ~200 ha, eigenaar AMP. https://pl.wikipedia.org/wiki/ArcelorMittal_Poland_Oddzia%C5%82_w_Zdzieszowicach
[4] WorldCoal, 20-03-2026, JSW and ArcelorMittal Poland sign coking coal supply contract — 2,1 mld zloty, 2026. https://www.worldcoal.com/mining/20032026/jsw-and-arcelormittal-poland-sign-coking-coal-supply-contract (idem JSW-persbericht https://www.jsw.pl/en/press-office/news/archive/archive-news-article/jsw-and-arcelormittal-poland-sign-a-pln-21-billion-contract)
[5] Bankier/PAP, 02-02-2015, ArcelorMittal Poland wciąż czeka na węgiel z JSW — JSW-kool voedt Zdzieszowice en Kraków; type 35 voor koks. https://www.bankier.pl/wiadomosc/ArcelorMittal-Poland-wciaz-czeka-na-wegiel-z-JSW-3281791.html
[6] Bankier, 06-02-2015, Główny klient JSW znalazł inne źródło węgla — AMP koopt 26% van JSW; Zdzieszowice 4,2 Mt koks/j. https://www.bankier.pl/wiadomosc/Glowny-klient-JSW-znalazl-inne-zrodlo-wegla-7236450.html
[7] pl.wikipedia, Linia kolejowa nr 159 — Żory – Pawłowice Śląskie 14,529 km. https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_159
[8] pl.wikipedia, Linia kolejowa nr 148 — Pszczyna – Żory – Rybnik, 36,612 km. https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_148
[9] pl.wikipedia, Linia kolejowa nr 140 — Katowice Ligota – Nędza 67,203 km via Rybnik; Nędza sluit aan op lijn 151. https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_140
[10] pl.wikipedia, Linia kolejowa nr 136 — Kędzierzyn-Koźle (km −0,206) – Zdzieszowice (km 10,375) – Opole Groszowice. https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_136
[11] Esri World Imagery via `v2/tools/sat_check.py`; OSM-spoornet via `toets_spoorroute.mjs` (2026-10-09) — `v2/build-cache/satcheck/sat-kolen-pniowek-zdzieszowice-laad.png`, `-cokerij.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-kolen-pniowek-zdzieszowice.json` (7,4 KB, contract versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh kolen-pniowek-zdzieszowice` (functie `bak_kolen_pniowek_zdzieszowice`).

| # | modaliteit | been | km | punten | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | spoor | trein Pniówek (JSW) → ArcelorMittal Poland Zdzieszowice (via Żory, Rybnik, Nędza en Kędzierzyn-Koźle; aannemelijk) | 92,8 | 384 | — (enige been) | nee |

Totaal 92,8 km · 1 been · 2 markers (85 m resp. 44 m van de lijn; anker ≠ routeerpunt, snap kop 0,09 en staart 0,04 km).

- **Recept:** één `toets_spoorroute.mjs`-run (`BAKE_SUFFIX=-raw`, 1-op-1-net, `--hoofd-km=100`, geen via) → `spoorroute-kolen-pniowek-zdzieszowice-pniowek-zdzieszowice.geojson` (FeatureCollection) als `--been-geojson "spoor|…"`; geen weg, zee, leiding, lucht, haven-aanloop, stippel of kopie.
- **Km-toets:** geen gepubliceerde totale spoorkm, dus indicatie en geen norm. Router 89,5 km, 92,8 km over de 384 punten (de getekende lijn), hemelsbreed 63,4 km, verhouding 1,46 op de grootcirkel; deelstukken uit de bronnen (lijn 159 Żory–Pawłowice Śl. 14,5 km, lijn 136 Kędzierzyn-Koźle–Zdzieszowice 10,6 km) liggen er plausibel in. De verhouding is hoog voor een spoorlijn maar volgt de bronlijnen (Żory, Rybnik, Nędza, Kędzierzyn-Koźle); de directe lijn via Racibórz is een omweg.
- **Naden:** geen (één been). **Knikken/omkeringen:** 0 knikken ≥60°, 0 omkeringen (`toets_knikken.py`). **Rechte benen:** het been is niet recht (`toets_rechte_benen.py` meldt het niet).
- **Aannemelijk, niet gebrond:** de koppeling Pniówek → Zdzieszowice (bronnen noemen alleen JSW → AMP-cokerijen); staat in de beennaam, de lijn is doorgetrokken (gemeten, geen gat).
- **Open:** spoor-aansluiting van Pniówek alleen op satelliet gezien; aandeel/volume van de mijn niet gepubliceerd; sitelaag kolen heeft geen Poolse sites (centraal toevoegen).
- **Lessen:** (1) een bestaande, complete tussenuitvoer (geojson uit de eerdere poging) kon ongewijzigd hergebruikt worden: de bake duurde minder dan een minuut; (2) bij een enkel gemeten spoorbeen zonder via-punten volstaat de router-uitvoer als toets, zolang de bronlijnen langs de route zijn nagelopen (stations binnen 0,1–0,8 km).
