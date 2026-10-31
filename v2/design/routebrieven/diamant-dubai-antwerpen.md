# Routebrief (licht) · diamant — Dubai (DMCC) → DXB → Brussels Airport → Antwerpen (VAE → België)

**stroom-id:** `diamant-dubai-antwerpen` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** diamant (rough en polished, niet gesplitst) van de Dubai Diamond Exchange (DMCC, Almas Tower, JLT) per truck naar de DXB-vrachtterminal,
als vrachtvlucht (grootcirkel DXB → BRU, **aannemelijk: één bron, handelsstroom gebrond, vlucht niet**) naar Brucargo (Brussels Airport), en per truck over de E19 naar het AWDC/Diamond Office
in Antwerpen — de Golf-tak naar Europa, de tweede bestemming van de VAE-diamanthandel.
**Welke as van het verhaal:** *Dubai → Antwerpen*. HS 7102 (diamant), VAE-export 2023: België **3,29 mld USD = 17%**, tweede bestemming na India (8,99 mld, 46%) [1]. Een karaatcijfer voor deze boog is **niet gevonden**
(Mct/j onbekend; de v1-atlas heeft de boog `dia-dubai → dia-antwerp` niet [6]). Context: Antwerpse rough-invoer uit de VAE +53% in volume in H1 2026 (waarde niet genoemd) [2]. Waarde per karaat
verschilt sterk per herkomst en is hier niet in het gewicht verwerkt. De ODC-road-show van 2021 uit het ketenontwerp is **bindend uit de bronnenbasis gehaald** (§7).

## 1 · Ketenkaart
```
DMCC / Almas Tower `dia-dmcc-almas` ──(b1 truck · Sheikh Zayed Road E11 → Airport Road · letterlijke kopie diamant-dubai-surat b1 · 31,2 km)──►
DXB-vrachtterminal (Cargo Village) `dia-dxb-vracht` ──(b2 lucht · vlucht DXB → BRU, grootcirkel, aannemelijk: één bron · 5.147,6 km)──►
Brucargo, Brussels Airport `dia-brucargo` ──(b3 truck · E19 via Mechelen · letterlijke kopie diamant-jwaneng-antwerpen b4 · 37,4 km)──►
AWDC / Diamond Office, Antwerpen `dia-awdc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | DMCC/Almas Tower → DXB-vrachtterminal | Sheikh Zayed Road (E11) → Airport Road; **letterlijke kopie** (geen omkering: bestand loopt al DMCC → DXB) van `diamant-dubai-surat` b1 | hemelsbreed 29,0 km, geen wegkm (kopie 31,2) [7] | kopie | nee |
| b2 | C | lucht | DXB-vrachtterminal → Brucargo (BRU) | vlucht DXB → BRU, grootcirkel (aannemelijk: één bron) | 5.147,6 grootcirkel [berekend, `maak_luchtbeen.py`] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Brucargo → AWDC/Diamond Office | E19 via Mechelen; **letterlijke kopie** (zelfde richting Brucargo → AWDC) van `diamant-jwaneng-antwerpen` b4 (`…-weg-brucargo-antwerpen.geojson`) | hemelsbreed 34,4 km, geen wegkm (kopie 37,4; OSRM-webcheck 37,7 in die brief) [7] | kopie | nee |

Geen zeebeen (dus geen haven-aanloop), geen spoor, geen leiding. Het b1-geojson eindigt 0,22 km van het DXB-anker op de openbare weg en het b3-geojson begint 0,03 km van het BRU-anker
(50.9056, 4.4576): het luchtbeen loopt **van het b1-eindpunt (25.257452, 55.340597) naar het b3-beginpunt (50.9056, 4.4576)**, dus naden 0. Geen airside-stippel nodig (beide wegbenen
raken de openbare weg; patroon `goud-loulo-ticino` niet van toepassing).

## 3 · Ankers (één per site en per overslag — alle vier HERGEBRUIKT, niet opnieuw gelegd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-dmcc-almas` | handelshub / vertrek | DMCC/Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [3][7] (`diamant-dubai-surat`) | bron-gelegd (z15 gezien: kruis in het dichte JLT-hoogbouwcluster langs de Sheikh Zayed Road, naast de zandvlakte NO van het cluster) |
| `dia-dxb-vracht` | overslag truck → lucht | DXB Cargo Village / SkyCargo-loodsen, Al Garhoud | 25.25745, 55.3406 | [4][7] (`diamant-dubai-surat`, `-mbujimayi-dubai`) | bron-gelegd (z15 gezien: kruis op de rij langwerpige vrachtloodsen en apron W van de terminalgebouwen) |
| `dia-brucargo` | overslag lucht → truck | Brucargo, Brussels Airport | 50.90628, 4.45584 | [5][7] (`diamant-antwerpen-newyork`) | bron-gelegd (z15 gezien: kruis in de cargozone N van de startbaan, loodsen en bedrijfsterreinen langs de A201/R0-aansluiting) |
| `dia-awdc` | handels-/certificeringshub / bestemming | AWDC/Diamond Office, Hoveniersstraat 22, Antwerpen | 51.2152, 4.4187 | [8][7] (`diamant-antwerpen-newyork`) | bron-gelegd (z15 gezien: dicht stedelijk bouwblok ZW van Antwerpen-Centraal, Diamantwijk, geen eigen terrein) |

Beelden: `v2/build-cache/satcheck/sat-diamant-dubai-antwerpen-{dmcc-almas,dxb-vracht,brucargo,awdc}.png`. Geen anker verschoven.

## 4 · Via-punten (b1 en b3 zijn kopieën: geen nieuwe wegscan; b2 is lucht)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | E19 bij Mechelen | 51.0213, 4.4481 | blijft op de E19, niet via de R6/centrum Mechelen |
| b3 | 2 | E19/R1-knooppunt Antwerpen-Zuid (Wilrijk) | 51.1103, 4.4319 | trekt de route om de Antwerpse ring i.p.v. een sluipweg door de stad |
(Uit het bronbestand van `diamant-jwaneng-antwerpen` b4; b1 heeft er geen: één doorgaande stadsweg.) Geofabrik-regio's: **geen scan nodig** (`gcc-staten` en `belgie` bestaan al; beide wegbenen zijn kopieën).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| DMCC / Dubai Diamond Exchange | DMCC | handel en vault-opslag, geen fysieke bewerking | ±1.000 diamantbedrijven in Almas Tower | [3] |
| AWDC / Diamond Office | AWDC | import-/exportklaring, certificering | "one-stop import & export clearing" | [8] |
Geen smelter of slijperij; het slijpen gebeurt ná het stoppunt (elders).

## 6 · Stoppunt
De brief stopt bij het AWDC/Diamond Office: het is de importklaring en handelspoort van Antwerpen, en geen bron koppelt déze VAE-lading aan een slijperij of afnemer — fase D en E vervallen.

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** de ODC-road-show (okt 2021, The Patriot) is **niet gebruikt** als bron of basis; de as steunt op Trendeconomy HS 7102 2023 (België 2e, 3,29 mld USD, 17%) [1].
- **Geen bron voor een vrachtvlucht DXB → BRU met diamant.** Gebrond zijn de handelsstroom [1][2], dat Antwerpse diamant per beveiligde wagen naar Brussels Airport en daar het toestel in gaat [5],
  en dat Emirates sinds 2014 passagiersvluchten Dubai–Brussel vliegt (belly-cargo) en sinds 25-10-2015 met 777F-vrachtvliegtuigen [9]. Geen bron noemt diamant op die vluchten,
  een vluchtnummer, een terminal of een tussenlanding; de lading kan ook via Londen, Zürich of een andere hub gaan. Eén directe vlucht aangenomen: de claim is "van deze terminal naar die", niet "langs deze lijn".
- **Freighters vliegen vanaf Dubai World Central (DWC)**, niet vanaf het DXB Cargo Village [9 (zoekresultaat)]; het DXB-anker blijft gekozen omdat het in alle zusterketens (`-surat`, `-ramatgan`) staat en belly-cargo op DXB laadt. Niet verschoven.
- **Volume onbekend in Mct/j:** alleen waarde (3,29 mld USD, 2023, rough + polished niet gesplitst) en een mutatiecijfer (+53% volume, H1 2026, alleen rough) [2]. Centraal te kiezen: een natte-vinger-gewicht of alleen de dollarwaarde tonen.
- **Verstoring maart 2026** (Iran-conflict, vluchtannuleringen naar de VAE) is volgens de haalbaarheidstoets weer genormaliseerd; de kaart toont de vaste vorm.
- **b1 en b3: geen echte wegkm** (alleen hemelsbreed 29,0 en 34,4 km); de ±15%-toets is voor deze kopieën een indicatie. b3 begint 0,03 km van `dia-brucargo`, b1 eindigt 0,22 km van `dia-dxb-vracht`.
- **Verschil met het ontwerp:** b3 is niet de omgekeerde `diamant-antwerpen-newyork` b1 maar de letterlijke, al correct gerichte kopie uit `diamant-jwaneng-antwerpen` b4 (zelfde geometrie, 37,4 km, geen omkering nodig).
- Alleen via zoekresultaat gezien, niet geciteerd: Rapaport "Antwerp and Dubai: A Tale of Two Diamond Hubs" (timeout), de AWDC-halfjaarcijfers 2026 zelf (alleen via [2]).

## 8 · Bronnen
[1] Trendeconomy, UAE export HS 7102 (diamant) 2023: India 8,99 mld (46%), België 3,29 mld (17%), Hongkong 2,15 mld (11,1%). https://trendeconomy.com/data/h2/UnitedArabEmirates/7102
[2] Rapaport, 2026-07-12, "Antwerp's Diamond Trade Sees Positive Momentum" (H1 2026: rough-invoer uit de VAE +53% in volume; totale rough-waarde −15%). https://rapaport.com/news/antwerps-diamond-trade-sees-positive-momentum/
[3] Wikipedia, "Dubai Multi Commodities Centre" (Almas Tower, DDE, ±1.000 diamantbedrijven en kluizen). https://en.wikipedia.org/wiki/Dubai_Multi_Commodities_Centre
[4] Wikipedia, "Dubai International Airport" (vrachtterminal met een capaciteit van 3 miljoen ton/j). https://en.wikipedia.org/wiki/Dubai_International_Airport
[5] Wikipedia, "Brussels Airport diamond heist" (Brink's-wagen uit Antwerpen naar het toestel op Brussels Airport, 2013). https://en.wikipedia.org/wiki/Brussels_Airport_diamond_heist
[6] v1 `data/diamond.js` + `design/diamant.md` §4 (geen flow `dia-dubai → dia-antwerp`) — intern.
[7] Brieven `diamant-dubai-surat` (ankers + b1-kopie), `diamant-jwaneng-antwerpen` (b3-kopie, ankers), `diamant-antwerpen-newyork` (ankers `dia-brucargo`, `dia-awdc`).
[8] Wikipedia, "Antwerp World Diamond Centre" (Diamond Office, one-stop import & export clearing). https://en.wikipedia.org/wiki/Antwerp_World_Diamond_Centre
[9] Emirates SkyCargo, 2020-11-02, "marks key freighter anniversaries" (777F-vrachtdienst naar Brussel sinds 25-10-2015, een jaar na de passagiersdienst; pharma en bederfelijk genoemd, geen diamant). https://www.skycargo.com/media-centre/emirates-skycargo-marks-key-freighter-anniversaries/
[10] Esri World Imagery via `sat_check.py` (z15, 2026-10-31): `v2/build-cache/satcheck/sat-diamant-dubai-antwerpen-*.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-diamant-dubai-antwerpen.json` (21,2 KB, versie 2, punt_formaat lonlat) · **functie:** `bak_diamant_dubai_antwerpen` in `v2/tools/bak_stromen.sh` · **totaal 5.216,2 km · 1.048 punten · 4 markers.**

| # | modaliteit | km gebakken | km brief | naad naar vorige | stippel |
|---|---|---|---|---|---|
| b1 | truck | 31,2 | hemelsbreed 29,0, geen wegkm (+7,6%, indicatie) | 0 | nee |
| b2 | lucht | 5.147,6 | 5.147,6 grootcirkel | 0 | nee, doorgetrokken |
| b3 | truck | 37,4 | hemelsbreed 34,4, geen wegkm (+8,7%, indicatie) | 0 | nee |

**Recept:** geen wegscan, geen profiel, geen zee. b1 en b3 zijn byte-kopieen (`cmp` identiek) van `diamant-dubai-surat-weg-dmcc-dxb.geojson` en `diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson`, onder de prefix `diamant-dubai-antwerpen-` in `build-cache/ais/graaf/`; b2 is `maak_luchtbeen.py` (207 punten, van het b1-eindpunt naar het b3-beginpunt). Bake via `hecht_marnet.py route` met drie `--been-geojson`-regels (truck, lucht, truck) en vier `--marker`-regels, zonder `--stippel`.

**Markers (4, afstand tot de lijn):** dia-dmcc-almas 0,02 km · dia-dxb-vracht 0,00 km · dia-brucargo 0,15 km · dia-awdc 0,03 km. Alle ankers hergebruikt, niet verschoven.

**Toelichting:** geen stippel (beide wegbenen raken de openbare weg; geen airside-stippel nodig), geen haven-aanloop (geen zeebeen), geen leiding. De vlucht is doorgetrokken en AANNEMELIJK (een bron): de handelsstroom is gebrond, de vlucht niet; "aannemelijk: één bron" staat in de beennaam. De ±15%-toets is een indicatie omdat de brief alleen hemelsbrede km kent.

**Toetsen:** naden 0 / 0 km; versie 2, lonlat, modaliteiten truck/lucht/truck, elk been ≥ 2 punten. `toets_knikken.py`: 12 knikken ≥ 60 gr (alle spikes van 3–55 m rond de ankers en in de geerfde kopieen), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py`: geen melding voor deze stroom.

**Lessen:** (1) een stroom die alleen uit kopieen en een luchtbeen bestaat bakt in seconden; de kosten zitten in het checken van richting en naden van de kopieen. (2) De Emirates-freighters vliegen vanaf DWC, niet DXB; het DXB-anker blijft om de zusterketens gelijk te houden. (3) Centraal: de blik op de bol (console, atlasmodus) en de registerregel.
