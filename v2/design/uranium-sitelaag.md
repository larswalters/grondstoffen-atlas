# Uranium-sitelaag wereldwijd — lichte ronde

*Gemaakt 2026-09-28 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in
`gloednodes-uranium.json` verwerkt (droge run van `voeg_sites_toe.py` gecontroleerd, niet geschreven).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein/molen, conversiefabriek, verrijkingsfabriek, splijtstoffabriek)
plus een **capaciteit mét bron en peiljaar** voor de belangrijkste sites van de uraanketen, aanvullend op
`data/uranium.js` (v1-register, 9 landcentroïdes) en `design/uranium.md` (het ontwerpskelet). De lijst is de
invoer voor de wereldwijde gloedlaag — de v1-gewichten waren `share`-schattingen per land, dit zijn echte
site-capaciteiten.

**Eenheid — kern van deze grondstof (bevestigd door webcheck):** tU/jaar (ton uraan-inhoud) is optelbaar over
winning, conversie en splijtstoffabricage, precies zoals v1 al vastlegde. **Verrijking is NIET optelbaar in tU**
— een verrijkingsfabriek splitst UF6-voeding in verrijkt product + verarmde tails (minder massa in het
product dan erin ging), dus voor de verrijkingsrol staat in `capaciteit_kt` het geschatte **aandeel in de
wereld-SWU-capaciteit (%)**, met `eenheid_site` erbij zodat een optelling nooit per ongeluk % bij tU optelt.
Rosatom/TVEL ≈ 44% van de wereld-SWU-capaciteit (bevestigd: meerdere onafhankelijke bronnen 2024-2026,
Al Habtoor Research Centre / RUSI / Wikipedia-Rosatom komen op 44-45% uit, naast Urenco ~28-30% en Orano ~12%
en CNNC ~10-15%; percentages tellen niet exact tot 100% omdat schattingen van verschillende jaren/definities
door elkaar lopen — vandaar "indicatief" bij elke losse site).

> **Correctie 2026-09-28 (keuze Lars, "maak de uraniumgloed"):** met het percentage als gewicht vielen de
> verrijkingssites in de gloed vrijwel weg: 6 tot 23, naast mijnen van 4.000 tot 8.000 tU. Daarom staat er voor
> verrijking nu een **omgerekend voeding-equivalent in t U/j**: geschat aandeel wereld-SWU × ~65.000 t U/j
> wereldvoeding (WNA-reactorbehoefte 2023/24). Een aandeel van 1% komt dus neer op ~650 t U/j. Novouralsk komt
> uit op ~14.950 t U/j, Georges Besse II op ~7.800 en Urenco Almelo op ~5.200.
> ⚠️ **Dit is een schatting op een schatting.** De aandelen per fabriek zijn zelf geschat en de wereldvoeding is
> een ordegrootte. Het staat daarom vooraan in `capaciteit_bron` ("OMGEREKEND, SCHATTING") en dus ook in
> `gewicht_bron` van de gloedlaag. Het oorspronkelijke percentage staat in `aandeel_wereld_swu_pct`.
> De percentages in de tabel hieronder zijn ongewijzigd: het zijn de bronwaarden.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia-geohack, mindat, NRC-vergunnings-
  documenten en bedrijfs-/officiële adressen. Geen coördinaat verzonnen — waar geen bron een coördinaat gaf
  (CNNC Hanzhong, CNNC Yibin) is de site naar `sites_zonder_gewicht` gegaan met `lat`/`lon`: null, als open punt.
- **Eén coördinaat bleek fout en is expliciet vervangen**: Husab's Wikipedia-coördinaat (-22,7667/14,5167) ligt
  in de Atlantische Oceaan (satellietblik toonde alleen zee); vervangen door de mindat-coördinaat
  (-22,57769/15,05325), die wél op de actieve open pit ligt.
- **Eén operator-toekenning uit de meegeleverde kandidatenlijst was fout** en is gecorrigeerd: Four Mile is
  100% Quasar Resources/General Atomics, niet Boss Energy — Boss Energy's Zuid-Australische ISR-asset is het
  nabijgelegen, in 2024 heropende Honeymoon (dat wél in de kandidatenlijst stond als top-site, maar zonder
  operator-check).
- **Satellietblik** (`python v2/tools/sat_check.py`, Esri z13–z15, beelden in `v2/build-cache/satcheck/` met
  prefix `sitelaag-uranium-`) voor de top-6 winningssites en top-6 verwerkers, zoals de opdracht vraagt:
  Inkai · McArthur River · Husab · Olympic Dam · Priargunsky · Navoi/Uchkuduk (mijnen) en Novouralsk ·
  Urenco Almelo · Port Hope · Tricastin · Westinghouse Columbia · CNNC Lanzhou (verwerkers). Uitkomst: **6 van
  de 12 bron-gelegd** (Inkai, Husab, Olympic Dam, Priargunsky, Novouralsk, Tricastin — kruis lag zichtbaar op
  het juiste terrein), **5 aannemelijk** (McArthur River, Navoi/Uchkuduk, Urenco Almelo, Port Hope,
  Westinghouse Columbia, CNNC Lanzhou — coördinaat plausibel maar geen ondubbelzinnige visuele bevestiging op
  deze zoom, meestal omdat ISR-wellvelden/registerpunten te fijnkorrelig zijn voor z14, of omdat het punt in
  bebouwing viel die niet met zekerheid het juiste gebouw is). Voor de overige 27 sites is géén aparte
  satellietblik gedaan deze lichte ronde (tijdbudget) — status staat op "aannemelijk" of "onzeker" al naar
  gelang het aantal bronnen.
- **Capaciteit:** ~2 bronnen per site waar mogelijk (WNA, Cameco/Kazatomprom/Orano/Rosatom-TVEL/Urenco/
  Namibian Uranium Association jaarcijfers, NRC/GEM); `[Bn]` verwijst naar de bronnenlijst onderaan. Elke
  winnings-/conversie-/splijtstofsite draagt de oorspronkelijke eenheid + omrekening waar nodig (bv. U3O8→U
  ×0,848 bij Husab). **Voor verrijking is géén enkele bron een per-site-SWU-cijfer publiek** (alleen
  company-brede totalen) — het percentage per site is daarom een **schatting o.b.v. relatieve fabrieksgrootte**,
  expliciet als zodanig gemarkeerd in `capaciteit_bron` en status vaak "onzeker".
- **Chinese sites:** geen publieke register-/lijstbron met coördinaten (CNNC publiceert geen sitecoördinaten) —
  net als bij koper moet elke Chinese node individueel gevonden en satellietgecheckt worden. Dit is bij Lanzhou
  gelukt (Wikipedia-geohack + satellietblik op een plausibel industriecomplex aan de Gele Rivier); bij Hanzhong
  en Yibin niet — die blijven open punten.
- **Eerlijkheidsregel (M30):** alleen sites met een gebronde capaciteit ÉN (aannemelijke) productie krijgen
  gewicht in `sites`; projecten, geschorste/gesloten sites en sites zonder cijfer staan in `sites_zonder_gewicht`
  (wel gedocumenteerd, niet in de gloed) — Arlit (geschorst sinds 2023), COMINAK (gesloten 2021), Ranger
  (gesloten 2021), Honeymoon/Beverley (te vers heropend, nog geen jaarcijfer), VostGOK (oorlogssituatie, geen
  betrouwbaar actueel cijfer), CNNC Hanzhong/Yibin (geen coördinaat).

## Sites (32 met gewicht + 9 zonder gewicht = 41 kandidaten)

| id | naam | land | rol | lat, lon | capaciteit | status |
|---|---|---|---|---|---|---|
| w-inkai | Inkai (JV Kazatomprom/Cameco) | Kazachstan | mijn (ISR) | 45.2865, 67.5330 | 4.090 tU/j (2023) [B1][B2] | bron-gelegd |
| w-keylake | Key Lake mill (McArthur River-erts) | Canada | mijn+molen | 57.20667, -105.65917 | 7.815 tU/j (2024, wereldrecord) [B3][B4] | aannemelijk |
| w-cigarlake | Cigar Lake (mijn) / McClean Lake (molen) | Canada | mijn+molen | 58.06861, -104.54056 | ~7.100 tU/j (2024, 100%-basis) [B3][B5] | aannemelijk |
| w-husab | Husab (Swakop Uranium, CGN) | Namibië | mijn | -22.57769, 15.05325 | ~5.300 tU/j (2024/25, grootste open-pit) [B6][B7] | **bron-gelegd** |
| w-rossing | Rössing (CNNC) | Namibië | mijn | -22.4833, 15.0333 | 2.920 tU/j (2023) [B7][B8] | aannemelijk |
| w-langerheinrich | Langer Heinrich (Paladin Energy) | Namibië | mijn | -22.8147, 15.3338 | ~800 tU/j (2024, ramp-up-jaar) [B9][B10] | aannemelijk |
| w-olympicdam | Olympic Dam (BHP) | Australië | mijn (bijproduct Cu) | -30.4393, 136.86288 | ~4.000 tU/j (indicatief) [B11][B12] | **bron-gelegd** |
| w-fourmile | Four Mile (Quasar/General Atomics) | Australië | mijn (ISR) | -30.1468, 139.5066 | ~700 tU/j (indicatief) [B11][B13] | aannemelijk |
| w-priargunsky | Priargunsky (Rosatom/ARMZ) | Rusland | mijn | 50.0640, 118.1350 | ~2.500 tU/j [B14] | **bron-gelegd** |
| w-navoi-uchkuduk | Navoiyuran — noordelijk ISR-district | Oezbekistan | mijn (ISR) | 42.1667, 63.5667 | ~3.500 tU/j [B15] | aannemelijk |
| w-porthope | Port Hope Conversion Facility (Cameco) | Canada | conversie | 43.9576, -78.2942 | 12.500 tU/j vergund [B3][B4] | aannemelijk |
| w-malvesi | Orano Malvési (Comurhex I) | Frankrijk | conversie (→UF4) | 43.2074, 2.9812 | ~15.000 tU/j indicatief [B16] | aannemelijk |
| w-tricastin-conversie | Orano Tricastin — Comurhex II | Frankrijk | conversie (→UF6) | 44.3250, 4.7167 | ~15.000 tU/j [B16][B17] | **bron-gelegd** |
| w-metropolis | Metropolis Works (Honeywell) | VS | conversie | 37.1500, -88.7333 | ~15.000 tU/j vergund [B18] | aannemelijk |
| w-seversk-conversie | Seversk (Rosatom/SKhK) | Rusland | conversie | 56.6000, 84.9000 | ~12.000 tU/j indicatief [B14] | onzeker |
| w-novouralsk | Novouralsk (Rosatom/TVEL) | Rusland | verrijking | 57.2858, 60.0826 | ~23% wereld-SWU (schatting) [B19][B20][B21] | **bron-gelegd** |
| w-angarsk | Angarsk (Rosatom/TVEL) | Rusland | verrijking | 52.5000, 103.9000 | ~8% wereld-SWU (schatting) [B19][B20] | onzeker |
| w-zelenogorsk | Zelenogorsk (Rosatom/TVEL) | Rusland | verrijking | 56.1167, 94.5833 | ~7% wereld-SWU (schatting) [B19][B20] | onzeker |
| w-seversk-verrijking | Seversk (Rosatom/SKhK) | Rusland | verrijking | 56.6000, 84.9000 | ~6% wereld-SWU (schatting) [B19][B20] | onzeker |
| w-urenco-almelo | Urenco Nederland | Nederland | verrijking | 52.3383, 6.6939 | ~8% wereld-SWU (schatting) [B22][B23] | aannemelijk |
| w-urenco-gronau | Urenco Deutschland | Duitsland | verrijking | 52.0833, 7.0167 | ~7% wereld-SWU (schatting) [B22][B23] | onzeker |
| w-urenco-capenhurst | Urenco UK | Verenigd Koninkrijk | verrijking | 53.2667, -2.8833 | ~6% wereld-SWU (schatting) [B22][B23] | onzeker |
| w-urenco-eunice | Urenco USA (Eunice, NM) | VS | verrijking | 32.4667, -103.1833 | ~9% wereld-SWU (schatting, groeiend) [B22][B24] | aannemelijk |
| w-tricastin-verrijking | Orano Georges Besse II | Frankrijk | verrijking | 44.3250, 4.7167 | ~12% wereld-SWU (schatting) [B17][B19] | **bron-gelegd** |
| w-cnnc-lanzhou | CNNC Lanzhou | China | verrijking | 36.150744, 103.518431 | ~10% wereld-SWU (schatting) [B25][B26] | aannemelijk |
| w-westinghouse-columbia | Westinghouse Columbia | VS | splijtstoffabricage | 33.8811, -80.9233 | ~1.400 t HM/j [B27] | aannemelijk |
| w-gnf-wilmington | Global Nuclear Fuel-Americas | VS | splijtstoffabricage | 34.1667, -77.9333 | ~1.200 t HM/j indicatief [B28] | onzeker |
| w-framatome-romans | Framatome Romans-sur-Isère | Frankrijk | splijtstoffabricage | 45.0500, 4.9667 | ~1.600 t HM/j indicatief [B29] | onzeker |
| w-framatome-lingen | Framatome/ANF Lingen | Duitsland | splijtstoffabricage | 52.5167, 7.3167 | ~800 t HM/j indicatief [B29] | onzeker |
| w-westinghouse-springfields | Westinghouse Springfields | VK | splijtstoffabricage | 53.7500, -2.8000 | ~700 t HM/j indicatief [B27] | onzeker |
| w-tvel-novosibirsk | TVEL Novosibirsk (NZHK) | Rusland | splijtstoffabricage | 54.9667, 82.8833 | ~1.200 t HM/j indicatief [B30] | onzeker |
| w-tvel-elektrostal | TVEL Elektrostal (MSZ) | Rusland | splijtstoffabricage | 55.7833, 38.4333 | ~1.200 t HM/j indicatief, VVER-lock-in [B30] | onzeker |

## Buiten scope / zonder gewicht (9)

| id | naam | land | reden |
|---|---|---|---|
| w-mcarthurriver-erts | McArthur River (ertslichaam) | Canada | productie al toegekend aan de Key Lake-molen; satellietpass toonde geen zichtbare mijninfra (mogelijk ondergronds/klein voetprint) |
| w-arlit | Arlit/SOMAIR | Niger | geschorst sinds de coup 2023 + grenssluiting Niger-Benin; geen gebronde export |
| w-cominak | Akouta/COMINAK | Niger | definitief gesloten maart 2021 |
| w-ranger | Ranger | Australië | mijnbouw gestopt 2012, laatste erts verwerkt jan. 2021 |
| w-honeymoon | Honeymoon (Boss Energy) | Australië | heropend 2024, nog geen volledig gebrond kalenderjaar |
| w-beverley | Beverley (Boss Energy) | Australië | op stand-by, geen actuele productie |
| w-cnnc-hanzhong | CNNC Hanzhong | China | geen coördinaat gevonden (geen Chinese registerbron met coördinaten) |
| w-cnnc-yibin | CNNC Yibin | China | idem — geen coördinaat gevonden |
| w-vostgok | VostGOK/SkhidGZK | Oekraïne | oorlogssituatie, geen betrouwbaar actueel productiecijfer |

## Kazachstaanse JV-mijnen niet individueel opgenomen (open punt)

Kazachstan levert ~40-43% van de wereldwijde uraanwinning, verspreid over ~14 ISR-JV's naast Inkai (Karatau/
Budenovskoye, Kharasan, Zarechnoye, South Inkai, Akdala, Central Mynkuduk/Ortalyk e.a.), elk met een eigen
Kazatomprom-JV-structuur. Voor geen van deze overige velden is deze ronde een betrouwbare, individuele
coördinaat gevonden (Kazatomprom/Cameco-technische rapporten geven wél deposit-namen en productiecijfers,
maar zelden een exacte site-coördinaat in graden/decimalen) — in lijn met de regel "nooit een coördinaat
verzinnen" zijn deze velden **niet** opgenomen, ook niet als open punt met een gok-coördinaat. Vervolgronde:
Kazatomprom's eigen technische rapporten (NI 43-101, per JV) doorzoeken op UTM/lat-lon-tabellen.

## Amerikaanse ISR-herstarts niet opgenomen (open punt)

Smith Ranch-Highland (Cameco), Lance/Ross (voorheen Peninsula Energy, nu enCore Energy) en Christensen Ranch/
Willow Creek (eigendom recent gewijzigd van Uranium One naar enCore Energy, 2024) zijn in 2024 herstart met
bescheiden productie (samen orde grootte 500-1.000 tU/j). Niet opgenomen deze ronde: eigendomsstructuur is
recent en verwarrend gewijzigd, en een verkeerde operator-toekenning (zoals bij Four Mile/Boss Energy hierboven
al één keer gebeurde) leek een groter risico dan het gewicht van deze relatief kleine sites waard is. Aparte
verificatieronde aanbevolen.

## Bronnen

[B1] Cameco, *2024 Inkai Operation Technical Report* (NI 43-101), Turkestan Region, Kazachstan.
[B2] Kazatomprom, *Annual Report 2023*; World Nuclear News, "Kazatomprom to increase uranium production in 2024" (2024).
[B3] Cameco, *2024 Annual Report* / Form 40-F (SEC), uraniumsegment-productiecijfers per site.
[B4] Cameco, "McArthur River/Key Lake" en "Port Hope"-bedrijfspagina's (cameco.com).
[B5] World Nuclear News, "Cameco announces Cigar Lake production outlook"; Orano Canada, "Mining and Milling" (mcclean Lake).
[B6] The Extractor Magazine, "Husab finds its rhythm 10 years on" (okt. 2025); The Namibian, "Husab production increases by 45%".
[B7] Namibian Uranium Association, "Husab Mine" / "Rössing Mine"-pagina's (namibianuranium.org).
[B8] World Nuclear Association, "Namibia" landprofiel (world-nuclear.org).
[B9] World Nuclear News, "Paladin to restart Langer Heinrich uranium mine"; NucNet, "Paladin Announces First Commercial Production" (apr. 2024).
[B10] Uranium Royalty Corp., Form 6-K/40-F (SEC) — Langer Heinrich-portfolio-update.
[B11] World Nuclear Association, "Australia's Uranium Mines" (world-nuclear.org/information-library/appendices).
[B12] BHP, jaarverslag Olympic Dam-productiecijfers (bhp.com).
[B13] Mining-technology.com / NS Energy Business, "Four Mile Uranium Mine"-projectpagina's.
[B14] World Nuclear Association, "Russia's Nuclear Fuel Cycle" landprofiel.
[B15] World Nuclear Association, "Uranium in Uzbekistan" landprofiel; Navoiyuran State Enterprise, persberichten (navoiyuran.uz).
[B16] Orano Group, "Comurhex"/Malvési-bedrijfspagina's (orano.group).
[B17] Orano Group, *Annual Activity Report 2024*.
[B18] Honeywell / NRC-vergunningsdocumentatie Metropolis Works.
[B19] World Nuclear Association, "Uranium Enrichment" (world-nuclear.org/information-library).
[B20] Rosatom Newsletter, "Global Nuclear Fuel Supply"; RUSI/Al Habtoor Research Centre, analyses Rosatom-marktaandeel (2024-2026).
[B21] Wikipedia/NTI/GlobalSecurity, "Ural Electrochemical Combine (Novouralsk)".
[B22] Urenco Group, bedrijfspagina's per land (urenco.com/global-operations) + *Contact*-pagina (adresgegevens).
[B23] World Nuclear News, "Urenco doubles expansion plans for uranium enrichment in the Netherlands" (2025).
[B24] The National Interest / raw-science.org, analyses VS-importban Russisch verrijkt uranium en Urenco USA-uitbreiding.
[B25] IPFM/Fissile Materials Working Paper, "China's Uranium Enrichment and Plutonium Recycling" (Hui Zhang).
[B26] Belfer Center, "China's Uranium Enrichment Capacity: Rapid Expansion to Meet Commercial Needs"; Wikipedia, "Lanzhou uranium enrichment plant".
[B27] Westinghouse Nuclear, bedrijfspagina's Columbia/Springfields; NRC-vergunningsdocumentatie Columbia Fuel Fabrication Facility.
[B28] Global Nuclear Fuel / GE-Hitachi, bedrijfsinformatie Wilmington NC.
[B29] Framatome, bedrijfspagina's Romans-sur-Isère en Lingen (framatome.com).
[B30] TVEL/Rosatom, bedrijfspagina's Novosibirsk en Elektrostal (rosatom-centralasia.com e.a.).

## Ketens uit deze golf (referentie, nog niet als routebrief geschreven)

De zes ketens uit de opdracht (`uranium-inkai-poti`, `uranium-mcarthurriver-porthope`,
`uranium-rossing-walvisbay`, `uranium-arlit-cotonou`, `uranium-olympicdam-portadelaide`,
`uranium-inkai-stpetersburg`) hergebruiken de ankers `w-inkai`, `w-keylake`/`w-mcarthurriver-erts`, `w-rossing`,
`w-arlit`, `w-olympicdam` uit deze sitelaag. Er bestaan nog geen `v2/design/routebrieven/uranium-*.md`-brieven
(de map bevat ze niet) — deze sitelaag is bewust de eerste stap; de routebrieven zijn een vervolgtaak.
