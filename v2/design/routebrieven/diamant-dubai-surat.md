# Routebrief (licht) · diamant — Dubai (DMCC) → Mumbai (BOM) → Surat (India)

**stroom-id:** `diamant-dubai-surat` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken (2026-10-09)
**Keten in één zin:** ruwe diamant (rough) van de Dubai Diamond Exchange (DMCC, Almas Tower, JLT) per truck
naar de DXB-vrachtterminal, als vrachtvlucht (grootcirkel DXB → BOM, **aannemelijk: één bron**) naar het
CSMIA Air Cargo Complex in Mumbai, en per truck over de NH48 (~273 km) naar de Surat Diamond Bourse (DREAM City) —
de Dubai-trechter naar de Indiase slijpers, inclusief de via Dubai omgeleide Russische rough.
**Welke as van het verhaal:** *Dubai-rough → Surat*, ~24 Mct/j ruw (v1-checklist `design/diamant.md` §4b, natte vinger,
peiljaar 2023-24, geen waarheid; eenheid Mct/j = miljoen karaat per jaar) [1]. Context: de VAE leverden in 2025 voor
$ 8,46 mrd aan rough aan India (≈ 50% van de $ 16,76 mrd totaal; Rusland direct maar $ 406 mln) [2]. Waarde per karaat
laag tot middel (Russisch/Afrikaans mengsel) — hier niet in het gewicht.

## 1 · Ketenkaart
```
DMCC / Almas Tower `dia-dmcc-almas` ──(b1 truck · Sheikh Zayed Road E11 → Airport Road · omgekeerde kopie · 31,2 km)──►
DXB-vrachtterminal (Cargo Village) `dia-dxb-vracht` ──(b2 lucht · vlucht DXB → BOM, grootcirkel, aannemelijk · 1.928 km)──►
CSMIA Air Cargo Complex, Mumbai `dia-bom-cargo` ──(b3 truck · NH48 via Manor–Talasari–Vapi–Valsad–Navsari–Sachin · kopie · 273,4 km)──►
Surat Diamond Bourse `dia-sdb` ──(b4 truck · stippel · 0,29 km kopie)──► stoppunt (anker)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | DMCC/Almas Tower → DXB-vrachtterminal | Sheikh Zayed Road (E11) → Airport Road; **letterlijk omgekeerde kopie** van `diamant-mbujimayi-dubai` b4 (= `diamant-catoca-dubai` b4) | hemelsbreed 29,0 km, geen wegkm (gebakken kopie 31,2 km) [11] | kopie (omgekeerd) | nee |
| b2 | B | lucht | DXB-vrachtterminal → CSMIA Air Cargo Complex (BOM) | vlucht DXB → BOM, grootcirkel (aannemelijk: één bron) | 1.928,1 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | CSMIA Air Cargo Complex → Surat Diamond Bourse | NH48 Mumbai–Ahmedabad; **letterlijke kopie** van `diamant-gaborone-surat` b3 | 289 km stad-tot-stad Mumbai–Surat [6]; kopie 273,4 km = −5,4% | kopie | nee |
| b4 | C | truck | DREAM City interne toegangsweg → dia-sdb | OSM-topologiegat DREAM City | 0,29 [kopie] | kopie (stippel) | ja — eigen verbinding zonder net (letterlijk uit `diamant-gaborone-surat` b4) |

Geen zeebeen (dus geen haven-aanloop). Het DXB-platform ligt airside, maar het wegbeen-geojson begint 0,22 km van het anker op de
openbare weg en het BOM-wegbeen 0,03 km — geen extra last-mile-stippel nodig (patroon `goud-loulo-ticino` niet van toepassing).

## 3 · Ankers (één per site en per overslag — alle vier HERGEBRUIKT, niet opnieuw gelegd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-dmcc-almas` | handelshub / vertrek | DMCC/Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [3][11] (`diamant-letseng-dubai`, `-catoca-dubai`) | bron-gelegd (z15 gezien: 68-verdiepingentoren in JLT-hoogbouwcluster aan de Sheikh Zayed Road, kruis op de toren) |
| `dia-dxb-vracht` | overslag truck → lucht | DXB Cargo Village / SkyCargo-loodsen, Al Garhoud | 25.2574524, 55.3405972 | [7][11] (`diamant-mbujimayi-dubai` en drie zusters; sat-gelegd z14–z18) | bron-gelegd (z15 gezien: rij vrachtloodsen en apron NW van de terminals, kruis op de loodsenrij) |
| `dia-bom-cargo` | overslag lucht → truck | CSMIA Air Cargo Complex, Sahar, Mumbai | 19.0994, 72.8673 | [11] (`diamant-mirny-mumbai`) | bron-gelegd op site-niveau (z15 gezien: kruis net N van het luchthavenhek, ~0,3 km boven de vrachtloodsen; zelfde punt als in vijf zusterbrieven, niet verschoven) |
| `dia-sdb` | beurs + slijperijcluster / bestemming | Surat Diamond Bourse, DREAM City | 21.1097, 72.7953 | [5][11] (`diamant-gaborone-surat`) | bron-gelegd (z15 gezien: negen torens op een eigen as midden in vlak land, ver buiten de stad; routeerpunt 21.107445, 72.796653 ligt 0,29 km ervandaan) |

## 4 · Via-punten (alleen b3; b1 heeft er geen — één doorgaande stadsweg, kopie)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Manor (NH48-knooppunt) | 19.7228, 72.9096 | NH48 buigt hier van de kustvlakte het binnenland in |
| b3 | 2 | Talasari | 20.1222, 72.9164 | deelstaatgrens Maharashtra–Gujarat, NH48-flyover |
| b3 | 3 | Vapi | 20.3720, 72.9170 | eerste grote Gujarat-industriestad op de corridor |
| b3 | 4 | Valsad-bypass (NH48-trunk) | 20.5968, 72.9512 | trunk omzeilt Valsad ~3 km zuidwestelijk; de stadscentroïde snapte op een stompje |
| b3 | 5 | Navsari | 20.9500, 72.9300 | doorgaande NH48-stad vlak vóór Surat |
| b3 | 6 | Sachin | 21.0853, 72.8805 | corridor buigt af naar de Hajira–Sachin Bypass richting DREAM City |
Geofabrik-regio's: b1 `gcc-staten`; b3 `india`. (Kopie: geen nieuwe wegscan nodig.)

## 5 · Verwerkingsknopen
Geen fysieke bewerking: DMCC is veiling/handel (en voor Russische stenen de plek waar de herkomst "wit wordt" — beweerd, niet
bewezen [8]); CSMIA is overslag + douane (Air Special Cargo / Precious Cargo Customs Clearance [4]); het slijpen gebeurt ná het stoppunt in Surat.

## 6 · Stoppunt
De brief stopt bij de Surat Diamond Bourse: hij combineert handel, douane-afhandeling en fabricage-units [5], en geen bron
koppelt déze Dubai-lading aan één slijperij — fase D vervalt, fase E vervalt.

## 7 · Open punten
- **De vlucht DXB → BOM is een aanname (één bron):** [4] documenteert 2019 Dubai-rough (Unifacet Diam DMCC → Kiran Gems, 139.032 ct)
  aangemeld bij de Air Special Cargo-douane in Mumbai, en [3] dat ladingen "in Mumbai landen" en dezelfde dag naar Surat gaan; geen bron noemt
  vluchtnummer of vrachtterminal-naam, geen bron sluit een tussenlanding uit → één directe vlucht (stippel zou verkeerd zijn: geen gat).
- **Het Russische deel:** de claim "Russische rough gaat via Dubai naar India" is reportage + handelsdata-inferentie [2][8][9], geen document; het
  directe Rusland-aandeel (2,4%) zegt niets over de omweg. Niet apart getekend: de lading is in de data niet van Dubai-rough te scheiden.
- **Mumbai-freighters gepauzeerd** van aug 2026 t/m mei 2027 (Apron G; Navi Mumbai als alternatief) [10]: geldt vrachtvliegtuigen; rough reist ook als
  beveiligde koerierlading in passagiersvluchten. De kaart toont de vaste vorm, niet de tijdelijke omleiding.
- **Surat Airport (STV)** zit niet in de keten: SDB-douane exporteert nog via Mumbai [5]; STV-rough-import niet gevonden.
- **Jaarvolume 24 Mct/j** is natte vinger; SDB-douane telde FY2025-26 512,75 lakh ct (51,3 Mct) rough + lab-grown seeds, alle herkomsten [3] — niet hieraan te koppelen.
- b1 en b3: geen onafhankelijke wegkm (alleen stadsafstand [6]); `dia-bom-cargo` ligt op site-niveau, niet op pandniveau.
- AWDC-jaarcijfers 2025 en Business Standard (2015) uit het ketenontwerp niet geraadpleegd (PDF/403) — niet geciteerd.

## 8 · Bronnen
[1] Ketenontwerp M31 golf 7 + `design/diamant.md` §4b / `data/diamond.js` (flow dia-dubai → dia-surat, 24, air) — intern.
[2] Interfax, 2026-02-26: India's rough-invoer 2025 $16,76 mrd; VAE $8,46 mrd; Rusland $406 mln. https://interfax.com/newsroom/top-stories/116339/
[3] DeshGujarat, 2026-04-01: SDB-douane FY2025-26, transshipment Mumbai→Surat dezelfde dag. https://deshgujarat.com/2026/04/01/surat-diamond-bourse-customs-logs-%e2%82%b942636-crore-trade-in-2025-26/
[4] CESTAT Mumbai, appeals 87726/2022 e.a. (Kiran Gems / Unifacet Diam DMCC Dubai; Air Special Cargo). https://cestat.gov.in/weborders/file/mumbai/232554
[5] Wikipedia, "Surat Diamond Bourse" (customs clearance house; export via Mumbai). https://en.wikipedia.org/wiki/Surat_Diamond_Bourse
[6] Wikipedia, "Surat" (289 km ten noorden van Mumbai; ~90% van de wereld-diamant geslepen). https://en.wikipedia.org/wiki/Surat
[7] Wikipedia, "Dubai International Airport" (Cargo Village). https://en.wikipedia.org/wiki/Dubai_International_Airport
[8] Rapaport, "Where Are All the Russian Diamonds?" (via zoekresultaat). https://rapaport.com/news/where-are-all-the-russian-diamonds/
[9] Bloomberg/mining.com, 2022-04-22 (via zoekresultaat). https://www.mining.com/web/the-diamond-world-is-scrambling-to-keep-buying-russian-gems/
[10] STAT Times, Mumbai freighter-pauze aug 2026. https://www.stattimes.com/air-cargo/freighter-operations-at-mumbai-airport-to-pause-from-aug-2026-1357612
[11] Brieven `diamant-mbujimayi-dubai`, `-catoca-dubai`, `-letseng-dubai`, `-mirny-mumbai`, `-gaborone-surat` (ankers + kopieerbare benen).
[12] Esri World Imagery via `sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-dubai-surat-{dmcc-almas,dxb-vracht,bom-cargo,sdb}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
Bestand `v2/data/stroomroute-diamant-dubai-surat.json` (76,0 KB, contract versie 2, `lonlat`), functie `bak_diamant_dubai_surat` in
`v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh diamant-dubai-surat`). Geen profiel in `maak_stroombeen_weg.py`, geen wegscan,
geen zee-/haven-aanloop: alle vier de benen zijn kopieën of een luchtbeen. Totaal **2.233,0 km · 3.847 punten · 4 markers**.

| # | modaliteit | km | punten | naad naar vorig been | toets |
|---|---|---|---|---|---|
| b1 | truck (omgekeerde kopie) | 31,2 | 406 | — | alleen hemelsbreed 29,0 km in de brief (geen wegkm): +7,6% is een indicatie, geen norm |
| b2 | lucht (grootcirkel, doorgetrokken) | 1.928,1 | 79 | 0,00 km | = berekend met maak_luchtbeen; omwegfactor 1,000 per constructie |
| b3 | truck (letterlijke kopie) | 273,4 | 3.360 | 0,00 km | −5,4% tegen 289 km stad-tot-stad Mumbai–Surat (Wikipedia, wegtype niet gespecificeerd): binnen ±15% |
| b4 | truck, stippel | 0,29 | 2 | 0,00 km | = brief (0,29); eigen verbinding zonder net |

Markers (4): `dia-dmcc-almas` 0,014 km van de b1-lijn · `dia-dxb-vracht` 0,000 km (kop b2 / staart b1) · `dia-bom-cargo` 0,000 km (staart b2 / kop b3) ·
`dia-sdb` 0,000 km van de b4-stippel. Naden 0,00 km overal (nul naden).

**Recept.** b1: `diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson` met de coördinatenvolgorde omgedraaid (406 punten, properties overgenomen,
`naam`/`id` herschreven, van/naar-velden omgewisseld) naar `diamant-dubai-surat-weg-dmcc-dxb.geojson`; `hecht_marnet.py` accepteerde de
omgekeerde lijn (kop 25,06906/55,14117, staart 25,25745/55,34060), dus de terugval met een omgedraaid profiel was niet nodig.
b2: `maak_luchtbeen.py --van "DXB-vrachtterminal|25.2574524,55.3405972" --naar "CSMIA Air Cargo Complex|19.0994,72.8673"` (1.928,1 km, 79 punten).
b3: `diamant-gaborone-surat-weg-bom-sdb.geojson` ongewijzigd (letterlijke kopie). b4: `--stippel` letterlijk uit `bak_diamant_gaborone_surat`.

**Toelichting per bijzonder been.**
- *Vlucht (b2):* doorgetrokken, geen stippel (een vlucht tussen twee gelegde vrachtterminals is geen gat). "aannemelijk: één bron" staat in de
  beennaam en in §7, niet in de lijnstijl. De bol tilt het luchtbeen zelf op.
- *Stippel (b4):* het enige stuk waar het net niet reikt: de eigen toegangsweg van DREAM City, 0,29 km, OSM-topologiegat tussen het
  wegenstelsel van de bourse en het publieke net. Geen last-mile-stippel bij DXB: het wegbeen eindigt 0,22 km van het anker op de openbare weg.
- *Geen leiding, geen haven-aanloop, geen zeebeen.*

**Knikken en rechte benen.** `toets_knikken.py`: b1 6 knikken, 0 omkeringen; b2 0; b3 33 knikken waarvan 1 terugloop (153,4° bij
19,10609/72,85372, vlak bij het BOM-anker) — **pre-existent**, byte-identiek aan `diamant-gaborone-surat` b3 (die meldt 38 knikken met dezelfde terugloop)
en als kopie bewust niet aangeraakt. `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom met omwegfactor 1,000 behalve het luchtbeen
(overgeslagen: per constructie recht); b1 1,075, b3 1,224.

**Lessen.**
1. Een omgekeerde kopie van een gebakken wegbeen kan in een paar regels (lijst omdraaien, properties meedraaien) en `hecht_marnet.py` neemt hem
   zonder klacht aan: een wegscan voor de omgekeerde richting is niet nodig.
2. De gedeelde brief-ankers (`dia-dxb-vracht`, `dia-bom-cargo`, `dia-sdb`) vallen exact op de kop/staart van de kopieën, dus naden zijn 0,00 km;
   alleen `dia-dmcc-almas` ligt 0,014 km van de lijn (anker ≠ routeerpunt, kop van b1 is 0,05 km).
3. Slot-afhandeling in deze omgeving: `rm -rf "$d"` met een variabele wordt door de veiligheidscheck geweigerd; een slot is met `mkdir` te nemen
   en met `rm -f …/sinds` + `rmdir` op een letterlijk pad vrij te geven.
