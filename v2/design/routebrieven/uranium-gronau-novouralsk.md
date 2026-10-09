# Routebrief (licht) · uranium — Urenco Gronau (Duitsland) → Rotterdam → Sint-Petersburg → Novouralsk (Rusland)

**stroom-id:** `uranium-gronau-novouralsk` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** Verarmd uraniumhexafluoride (tails-UF6, bijproduct van Urenco-verrijking) gaan per **spoor** van Gronau
naar Rotterdam, per **zeeschip** (Shouwenbank, maart 2009) door Noordzee, Deense Straten en Oostzee naar Sint-Petersburg en per
**spoor** (Oktjabrskaja → Kirov → Perm → Jekaterinenburg) naar het Oeral Elektrochemisch Combinaat in Novouralsk, waar de tails
worden herverrijkt of opgeslagen — **stoppunt**. Peiljaar **2009**; zie §7 voor wat daarna veranderde.
**Welke as van het verhaal:** *Westerse verrijkingstails die in Rusland herverrijkt of opgeslagen worden.* Zending 03-2009: ~1.250 t UF6
≈ 845 t U (×0,676) [1]; 1996-2008 samen 27.300 t UF6 ≈ 1.420 t U/j gemiddeld, naar vier Russische sites [2][3]; 2019 hervat: ~3.600 t UF6
in zes treinen + 600 t, plan 12.000 t tot 2022 [2][3]. Eenheid t U (feed-equivalent), peiljaar 2009 (UF6 → U met 0,676, eigen omrekening).

## 1 · Ketenkaart
```
Urenco Gronau `u-gronau` ──(b1 spoor · Gronau–Bad Bentheim–Hengelo–Apeldoorn–Utrecht–Gouda–Rotterdam-Alexander · hemelsbreed 182 km,
   geen spoorkm · aannemelijk: bron noemt alleen "spoor naar Rotterdam" [1])──► Rotterdam RHB `u-rotterdam-kade`
──(b2 zee · Noordzee–Skagerrak–Deense Straten–Oostzee · MARNET 2.412 km · schip Shouwenbank 2009 [1])──►
Sint-Petersburg Petrolesport `u-stpetersburg-kade` ──(b3 spoor · Moskou–Kirov–Perm–Jekaterinenburg · letterlijke kopie uranium-tricastin-seversk, 4 benen)──►
Jekaterinenburg ──(b4 spoor · aftakking Verch-Nejvinsk · hemelsbreed 60 km · aannemelijk)──► Novouralsk UEIP `u-novouralsk-ueip` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | spoor | Gronau → Rotterdam RHB | Gronau–(Münster, router-omkering)–Bad Bentheim–Hengelo–Apeldoorn–Utrecht–Gouda–Rotterdam-Alexander–RHB | hemelsbreed 182 km, geen spoorkm; gemeten 373,9 (7 runs) | toets_spoorroute (7 runs, `BAKE_SUFFIX=-raw`) | nee — *aannemelijk: één bron, corridor eigen afleiding* |
| b2 | B | zee | Rotterdam RHB → Sint-Petersburg | Noordzee, Skagerrak, Kattegat, Deense Straten, Oostzee, Finse Golf | grootcirkel 1.820; MARNET 2.412; ontwerpschatting 2.500-2.700, geen gepubliceerde zeekm | MARNET | aanloop: geen (RHB 0,7 km; SPb 4,9 km, onder de 5) |
| b3 | C | spoor | Sint-Petersburg → Jekaterinenburg | Oktjabrskaja (Moskou) → Kirov → Perm → Oeral | hemelsbreed 1.788; gemeten 2.446,5 (4 kopieën) | letterlijke kopie `uranium-tricastin-seversk` b10-b13 | nee — *aannemelijk: geografische afleiding* |
| b4 | C | spoor | Jekaterinenburg → Novouralsk | Verch-Nejvinsk-aftakking | hemelsbreed 59,9; gemeten 80,0 (snap 0,6 km) | toets_spoorroute | nee — *aannemelijk* |
Totaal gemeten ca. 5.312 km. Een gepubliceerde spoor-/zeekilometer ontbreekt: de ±15%-toets is alleen indicatie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-gronau` | verrijking, tails-opslag (kop) | Urenco Deutschland, Gronau | 52.2154, 7.0739 | DE-wikipedia (52.21538, 7.07391) [3] | bron-gelegd (z15 gezien: complex met lange scheidingshallen, tailsopslag in de open lucht en schakelstation, kruis op de hallen). De sitelaag (`w-urenco-gronau` 52.0833, 7.0167) ligt 15,2 km mis |
| `u-rotterdam-kade` | overslag spoor → zee | Rotterdam — RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 | 51.8935, 4.4585 | letterlijk uit `uranium-porthope-almelo.md` / `routebrief-licht.md` §1 | hergebruikt; **geen bron noemt RHB** voor deze lading (Bellona: "de haven van Rotterdam" [1]) → onzeker |
| `u-stpetersburg-kade` | overslag zee → spoor | Petrolesport, Gutujevski-eiland, Sint-Petersburg | 59.8909, 30.2376 | letterlijk uit `uranium-tricastin-seversk.md` / `uranium-inkai-stpetersburg.md` | aannemelijk (eerder z15 gezien: containerstapels, kranen, spoorbundel; Bellona noemt alleen "Port of St. Petersburg" [1]) |
| `u-novouralsk-ueip` | herverrijking/opslag (eind) | Oeral Elektrochemisch Combinaat, Novouralsk | 57.2858, 60.0826 | sitelaag `w-novouralsk` (bron-gelegd) [4] | bron-gelegd (z15 gezien: lange fabriekshallen, omheind, spooraansluiting ten oosten en een rangeerspoor ten westen; kruis op de zuidrand van de hallen) |

## 4 · Via-punten (alleen spoor; stationspunten, niet de centra)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Bad Bentheim | 52.3032, 7.1578 | Gronau–Enschede is voor treinen doodlopend [2]; de router rijdt anders 153 km om via Münster |
| b1 | 2 | Hengelo | 52.2644, 6.7937 | grensovergang Bentheim → Twente; pint de lijn naar Deventer |
| b1 | 3 | Apeldoorn | 52.2080, 5.9690 | Deventer–Apeldoorn–Amersfoort i.p.v. Zwolle |
| b1 | 4 | Utrecht | 52.0894, 5.1101 | pint Utrecht–Gouda (router-omkeringen, §7) |
| b1 | 5 | Gouda | 52.0175, 4.7036 | zonder volgende punt rijdt de router Gouda–Rotterdam via Den Haag |
| b1 | 6 | Rotterdam-Alexander | 51.9548, 4.5575 | pint de Rotterdamse aanloop naar de Waalhaven |
| b3 | 1-4 | Moskou 55.7761, 37.6573 · Kirov 58.6036, 49.6680 · Perm 58.0105, 56.2502 · Jekaterinenburg 56.8384, 60.6339 | | letterlijke kopie; de laatste knoop is gedeeld met b4 (naad 0 km) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Urenco Gronau | Urenco | natuurlijk UF6 → verrijkt UF6 + tails-UF6 (opslag 38.100 t) | verrijking 4.550 t U feed-eq./j (sitelaag, schatting); tails-opslag 38.100 t UF6 | [3] |
| UEIP Novouralsk | Rosatom/TVEL | tails-UF6 → herverrijking (of opslag) | 10 mln SWU/j, ~helft van Rusland | [4] |

## 6 · Stoppunt
De brief stopt bij Novouralsk: de enige plek die een bron voor deze lading noemt [1]. Wat daarna met de tails gebeurt (herverrijking, opslag of
deconversie) is niet per zending gedocumenteerd; terugvoer is niet getekend. Fase D/E vervallen.

## 7 · Open punten
- **Peiljaar 2009.** Haven en route zijn alleen voor 2009 gedocumenteerd (Rotterdam, Shouwenbank [1]); de 2019-treinen reden Gronau–Münster–Hamm–Ruhr naar **Amsterdam** [2]
  en in 2020 liep de aanvoer via **Ust-Luga** [5]. Contract 2019-2022; een stopzetting daarna is in geen gevonden bron bevestigd.
- **Spoor Gronau → Rotterdam is eigen afleiding:** [1] zegt alleen "spoor naar Rotterdam"; de corridor via Bentheim–Hengelo is de keuze van de haalbaarheidstoets.
- **Router-omkeringen b1:** Münster (51.9628, 7.6395), Gronau-uitrit (52.2101, 7.0749), Hilversum (52.2297, 5.1788), Utrecht-Lunetten (52.0723, 5.1372),
  Breukelen (52.1719, 4.9905), Waalhaven (51.8717, 4.4488); Apeldoorn → Gouda is 128 km tegen ~102 verwacht. Proef via Amersfoort/Woerden gaf dezelfde Utrecht-knoop-artefacten. Niet bijgeschoven.
- **RHB en Petrolesport zijn niet als terminal van deze lading gepubliceerd.** Bij Sint-Petersburg is de naad zee → spoor 4,7 km (net onder 5), geen marge.
- **Bestemming Novouralsk: één bron** (activist Slivyak, in [1]); Seversk en Angarsk (opslag) ontvingen ook tails [2]; de **Siberische opslag** wordt in [1] genoemd.
- **Geen spoorkm gepubliceerd**; toets b2 in de bak: hemelsbreed 1.820 km, MARNET 2.412 km (+33%, Deense Straten), ontwerpschatting 2.500-2.700 (−3 tot −11%).
- **Sitelaag Gronau staat 15 km mis** (zie §3); centraal gelijktrekken met `u-gronau`.
- **Hengelo-run:** de router meldt "route korter dan grootcirkel" (25,0 tegen 25,1 km) door snapverschil; geen bug in de lijn.

## 8 · Bronnen
[1] Bellona, "Russian environmental groups protest arrival of more nuclear waste", 03-2009 (Shouwenbank, 1.250 t, Gronau → Rotterdam per spoor, Novouralsk). https://bellona.org/news/nuclear-issues/radioactive-waste-and-spent-nuclear-fuel/2009-03-russian-environmental-groups-protest-arrival-of-more-nuclear-waste
[2] urantransport.de, "Uranmüll aus Gronau nach Russland" (27.300 t 1995-2009; 2019: 8 transporten 5.100 t via Münster-Hamm naar Amsterdam; Gronau–Enschede doodlopend). https://urantransport.de/hintergrund/transportrouten/uranmuell-aus-gronau-nach-russland/
[3] Wikipedia (DE), "Urananreicherungsanlage Gronau" (coördinaat, tailsopslag 38.100 t, 1996-2008 27.300 t, 2019 ~3.600 t in zes treinen, plan 12.000 t tot 2022). https://de.wikipedia.org/wiki/Urananreicherungsanlage_Gronau
[4] World Nuclear Association, "Russia's Nuclear Fuel Cycle" (Novouralsk 10 mln SWU/j, grootste van vier plants). https://world-nuclear.org/information-library/country-profiles/countries-o-s/russia-nuclear-fuel-cycle
[5] The Moscow Times, 23-09-2020, "Russia's nuclear imports likely larger than declared: Greenpeace" (Ust-Luga, opslag UEIP, 600 t gedeclareerd, plan 12.000 t 2019-2022). https://themoscowtimes.com/2020/09/23/russias-nuclear-imports-likely-larger-than-declared-greenpeace-a71520
[6] Eigen briefs: `uranium-tricastin-seversk.md` (b3 + ankers SPb), `uranium-porthope-almelo.md` (RHB), sitelaag `uranium-sitelaag.json` (w-novouralsk, w-urenco-gronau).
[sat] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-uranium-gronau-novouralsk-gronau.png`, `…-novouralsk.png`, `…-rhb.png` (z15).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-uranium-gronau-novouralsk.json` (138,6 KB, versie 2, punt_formaat lonlat) · functie `bak_uranium_gronau_novouralsk()` in
`v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh uranium-gronau-novouralsk` · 13 benen · 7.917 punten · 4 markers · **totaal 5.322,8 km**
(brief: ca. 5.312; +0,2%). Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen), geen luchtbeen, geen leiding, geen stippel, geen haven-aanloop.

| # | modaliteit | been | km (bake) | km (brief) | naad | stippel |
|---|---|---|---|---|---|---|
| 1-7 | spoor | Gronau → Bad Bentheim 112,6 · Bentheim → Hengelo 25,9 · Hengelo → Apeldoorn 71,4 · Apeldoorn → Utrecht 83,5 · Utrecht → Gouda 47,2 · Gouda → Rotterdam-Alexander 13,3 · Alexander → RHB 28,1 | **382,0** | gemeten 373,9 (+2,2%); geen gepubliceerde spoorkm | 0,00 | nee |
| 8 | zee | zeeschip Rotterdam RHB → Sint-Petersburg (MARNET, kade → kade) | 2.412,1 | MARNET 2.412 | 0,73 | nee |
| 9-12 | spoor | letterlijke kopieen `uranium-tricastin-seversk`: SPb → Moskou 664,5 · Moskou → Kirov 899,6 · Kirov → Perm 488,9 · Perm → Jekaterinenburg 393,5 | **2.446,5** | 2.446,5 (0,0%) | 4,74 (zee-eind zeeknoop 6849 → Petrolesport), daarna 0,00 | nee |
| 13 | spoor | Jekaterinenburg → Novouralsk UEIP | 82,2 | gemeten 80,0 (+2,8%) | 0,00 | nee |

Voor de spoorbenen is er geen gepubliceerde spoorkm: de ±15%-toets is indicatie en wordt gehaald. Het verschil met de brief komt doordat `hecht_marnet.py` de lengte
uit de getekende polyline herrekent (haversine) i.p.v. de route-km van de spoorrouter te nemen.

**Markers (4):** `u-gronau` 0,28 km van de lijn · `u-rotterdam-kade` 0,00 · `u-stpetersburg-kade` 0,36 · `u-novouralsk-ueip` 0,56 (net boven de ~0,5 km: anker op de zuidrand van de hallen, spoor loopt oostelijk; bevinding, niet bijgeschoven).

**Toelichting**
- **Geen stippel, geen haven-aanloop:** RHB ligt 0,7 km en Petrolesport 4,9 km van hun MARNET-zeeknoop (6818 resp. 6849), beide onder de 5 km. De naad zee → SPb-spoor is 4,74 km: binnen de norm maar zonder marge (bevinding).
- **b3 = vier letterlijke kopieen** van `uranium-tricastin-seversk` (b10-b13, bestandsnamen `spoorroute-uranium-tricastin-seversk-{stpetersburg-moskou,moskou-kirov,kirov-perm,perm-jekaterinenburg}`), in de beennamen genoemd.
- Fase D/E vervallen (stoppunt Novouralsk); geen leiding, lucht of weg.

**Toets**
- json.load OK · versie 2 · punt_formaat lonlat · modaliteiten {spoor, zee} · elk been >= 2 punten (min 68) · 138,6 KB.
- Naden: max 4,74 km (b8 -> b9); b7 -> b8 0,73 km; rest 0,00.
- `toets_rechte_benen.py --min-km 5`: geen stippels in de stroom, geen been met omwegfactor 1,000 (zee 1,327; spoor 1,05-1,14).
- `toets_knikken.py`: 14 knikken >= 60 gr, 12 omkeringen waarvan 9 terugloop; alle router-artefacten, niet bijgeschoven: Hilversum (52.2297, 5.1788), Utrecht-Lunetten (52.0723, 5.1372), Breukelen (52.1719, 4.9905), Waalhaven (51.8717, 4.4488),
  SPb-begin (59.8728, 30.1949), Kirov (58.6141, 49.6467), Perm-Jekaterinenburg (58.0096, 56.1217); Hengelo-Apeldoorn heeft een echte scherpe bocht (52.1602, 6.2143). Zee: twee krappe bochten (Hoek van Holland 52.00, 3.90; Sont 55.31, 12.68).

**Recept (kort):** 7 spoorruns b1 + 1 run b4 met `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (vooraf gedraaid, tussenuitvoer `v2/build-cache/ais/graaf/spoorroute-uranium-gronau-novouralsk-*.geojson`),
MARNET `--been zee` kade -> kade, vier `--been-geojson` kopieen, vier `--marker`s. Gebakken via het zwaar-slot; een run (16 s), rc 0.

**Lessen**
- Slot nemen met `mkdir` op letterlijke paden en vrijgeven met `rmdir` op een letterlijk pad werkt; slot1 en slot2 waren bezet.
- Alle bevindingen uit §7 blijven staan: peiljaar 2009, RHB en Petrolesport niet als terminal van deze lading gepubliceerd, bestemming Novouralsk een bron, sitelaag `w-urenco-gronau` 15,2 km mis (centraal gelijktrekken met 52.2154, 7.0739).
- Registerregel (centraal): `{ "sleutel": "u-gn", "bestand": "stroomroute-uranium-gronau-novouralsk.json", "grondstof": "uranium", "label": "Gronau → Novouralsk", "aan": true, "noot": "M31 · golf 8 (2026-10-09): tails-UF6 per spoor Gronau-Rotterdam, per schip naar Sint-Petersburg, per spoor naar Novouralsk (peiljaar 2009)" }`.
