# Routebrief (licht) · PGM — Two Rivers → Impala Rustenburg → Springs (Zuid-Afrika)

**stroom-id:** `pgm-tworivers-springs` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** PGM-flotatieconcentraat (UG2) van de Two Rivers-concentrator (ARM/Implats-JV, Oostrand van
het Bushveld-complex bij Steelpoort, Limpopo) per **truck** over de R555 en N4 (Middelburg, Witbank, Pretoria) naar
de Impala-smelter/Mineral Processes bij Rustenburg, en vandaar per **truck** (N4 → N1 → N12) naar de Impala
Refineries in Springs (stoppunt) — geen zee-, spoor-, leiding- of luchtbeen.
**Welke as van het verhaal:** Bushveld-Oostrand (ontbrak op de bol): concentraat van een derde-partij-mijn dat via
een life-of-mine offtake met Impala Refining Services door het Impala-proces gaat. Jaarvolume **291 koz 6E in
concentraat FY2024** (juli 2023–juni 2024, 100%-basis) = **9,1 t 6E/j** (koz ÷ 32,15), mix = 6E (Pt+Pd+Rh+Ru+Ir+Au),
niet uitgesplitst [1].

## 1 · Ketenkaart
```
Two Rivers concentrator `pgm-tworivers-mijn` ──(b1 truck · R555 → N4 Middelburg–Witbank–Pretoria → N4 Platinum
  Highway · hemelsbreed 298 km, geen wegkm; OSRM ~439–456 km)──► Impala Rustenburg `pgm-rustenburg-mijn` (hergebruikt)
  ──(b2 truck · N4 → N1 → N12 · 255,8 km, LETTERLIJKE KOPIE pgm-springs-zurich b1, aannemelijk: één bron)──►
Impala Refineries Springs `pgm-springs-raffinaderij` (hergebruikt) ── stoppunt
```
Niet getekend: Marula (Oostrand) levert aan hetzelfde proces ([2]) maar is een andere mijn/keten.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Two Rivers → Impala Rustenburg | R555 Steelpoort–Stoffberg–Middelburg → N4 Witbank–Pretoria → N4 Platinum Highway | hemelsbreed 298 km, geen wegkm (indicatief OSRM ~439 via R555, 456 via R540) [1][5] | maak_stroombeen_weg | nee |
| b2 | B | truck | Impala Rustenburg → Springs | N4 → N1 → N12 — LETTERLIJKE KOPIE `pgm-springs-zurich` b1 (aannemelijk: één bron) | 255,8 gebakken | hergebruik geojson | nee |

Geen fase C/D/E (geen bron noemt een vervolgbestemming van het geraffineerde metaal in déze as).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-tworivers-mijn` | mijn / concentrator | Two Rivers Platinum Mine, concentrator (ARM 54% / Implats 46%), ~35 km ZW van Burgersfort | -24.9353, 30.1053 | [1][3] | bron-gelegd (z15 gezien: verwerkingsgebouwen met bezinkvijvers en tanks precies onder het kruis, ontsluitingsweg naar het noorden; een tweede mijncomplex ~1,2 km westelijk en een tailings-dam noordoost zijn niet gekozen) |
| `pgm-rustenburg-mijn` | overslag / smelter (Impala Mineral Processes) | Impala Platinum Rustenburg-mijnencluster — letterlijk uit `pgm-springs-zurich.md` | -25.5535, 27.2176 | [2][4] | bron-gelegd (zie die brief) |
| `pgm-springs-raffinaderij` | losplek / eindraffinage | Impala Refining Services, Springs — letterlijk uit `pgm-springs-zurich.md` | -26.2227, 28.4437 | [2][4] | bron-gelegd (zie die brief) |

Satellietbeelden: `v2/build-cache/satcheck/sat-pgm-tworivers-springs-tworivers.png` (z15) en `…-tworivers-z14.png`.

## 4 · Via-punten (b1; b2 is een kopie)
Allemaal op de doorgaande weg gecontroleerd (OSRM-nearest 0–5 m); geen enkel punt in een stadscentrum.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R555 ten ZW van Steelpoort | -25.1782, 29.8920 | pint de R555 (mijnroute naar Middelburg) tegenover de R540/Belfast-variant |
| b1 | 2 | R555/R33 bij Stoffberg | -25.3549, 29.7658 | houdt de R555 vast tot Stoffberg; sluit de Burgersfort/Lydenburg-omweg uit |
| b1 | 3 | N4 ten zuiden van Middelburg | -25.8327, 29.4529 | aansluiting R555 op de N4 (westwaarts); sluit de N11/Groblersdal-route uit |
| b1 | 4 | N4 bij Witbank (eMalahleni) | -25.8948, 29.2596 | pint de N4 tussen Middelburg en Pretoria |
| b1 | 5 | N4 Pretoria-oost | -25.7646, 28.3856 | dwingt de N4-doorsteek langs Pretoria af (geen N12/Johannesburg-route) |
| b1 | 6 | N4 Platinum Highway ten W van Pretoria | -25.6540, 28.1238 | pint de N4 naar Brits/Rustenburg |
| b1 | 7 | N4 ten zuiden van Marikana | -25.7506, 27.4504 | op de N4 zelf; het eerder gebruikte Marikana-dorpspunt (-25.7043, 27.4794) snapte 5,3 km weg (zie `pgm-mimosa-springs`) |
| b1 | 8 | Rustenburg N4/R24 — hergebruikt uit `pgm-zimplats-rustenburg.md` | -25.7031, 27.2572 | laatste N4-punt vóór het Impala-complex |

Geofabrik-regio: `zuid-afrika` (alle benen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Two Rivers concentrator | African Rainbow Minerals (54%, beheerder) / Implats (46%) | UG2-erts → flotatieconcentraat | 291 koz 6E in concentraat FY2024 | [1] |
| Impala Rustenburg (Mineral Processes, smelter) | Impala Platinum (Implats) | concentraat → matte | niet gepubliceerd voor Two Rivers | [1][2] |
| Impala Refineries Springs (BMR + PMR) | Implats (IRS-model) | matte → geraffineerd Pt/Pd/Rh e.a. | refined 6E ~1,5 Moz FY2024 (hele groep) | [2][4] |

## 6 · Stoppunt
De brief stopt bij Springs: dat is de eindraffinage in de Implats-keten (BMR → PMR) en geen bron noemt een
afnemer of vervolgzending van déze partij; fase D/E vervalt.

## 7 · Open punten
- **Springs wordt in de Two Rivers-factsheet niet genoemd** [1]: die noemt "road to Impala's Mineral Processes in
  Rustenburg" en een life-of-mine offtake met IRS. Dat IRS in Springs zit en Two Rivers-concentraat verwerkt
  staat in [2] en [4]; de koppeling Rustenburg → Springs blijft daarom **aannemelijk: één bron per schakel**.
- **Wegkilometer b1: geen gepubliceerde wegkm gevonden** — alleen hemelsbreed 298 km. OSRM (zelfde OSM-bron,
  dus geen onafhankelijke toets): 439 km via R555, 456 km via R540. De ±15%-toets is indicatief.
- **Vervoerswijze Rustenburg → Springs (matte) niet gebrond**; truck is aangenomen (kopie van de bestaande lijn).
- **Beeld:** b1 en b2 lopen samen ~110 km over de N4 bij Pretoria heen en terug (Rustenburg ligt westelijk, Springs oostelijk).
- **Eigendom:** factsheet 2025 zegt ARM 54% / Implats 46%; de sitelaag noemt 45%/45%/10% (niet door mij gewijzigd).
- **Sitelaag-coördinaat** `w-two-rivers` (-24.77, 30.22) is ~22 km verwijderd van dit satelliet-gelegde anker — centraal gelijktrekken.
- Mogelijke tweede concentratorlocatie/identiteit van het westelijke complex (~1,2 km) niet onderzocht.

## 8 · Bronnen
[1] Implats, Two Rivers fact sheet 2025 (291.000 oz 6E in concentraat FY2024; "concentrate is transported by road to Impala's Mineral Processes in Rustenburg"; offtake IRS), https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-two-rivers.pdf
[2] Implats, Impala Refining Services fact sheet 2025 (Two Rivers/Marula/Mimosa-concentraat naar IRS, BMR → PMR), https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-IRS.pdf
[3] Implats, Marula fact sheet 2025 (zelfde road/offtake-formulering, Oostrand), https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-marula.pdf
[4] Implats, Impala fact sheet 2025 ("base and precious metal refineries are situated in Springs, east of Johannesburg"), https://www.implats.co.za/pdf/fact-sheets/2025/fact-sheet-impala.pdf
[5] OSRM publieke demo (OSM), Two Rivers → Impala Rustenburg: 455,8 km standaard, 448,7 km met via Stoffberg/Middelburg, 2026-10-09, https://router.project-osrm.org
[6] Wikipedia, "Two Rivers mine" (Steelpoort, Limpopo; platina/palladium-reserves), https://en.wikipedia.org/wiki/Two_Rivers_mine
[7] `v2/design/routebrieven/pgm-springs-zurich.md` en `pgm-mimosa-springs.md` — hergebruikte ankers Rustenburg/Springs, via Rustenburg N4/R24 uit `pgm-zimplats-rustenburg.md`, kopie-geojson b2 (255,8 km)
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15), zie §3

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
Recept: `bash v2/tools/bak_stromen.sh pgm-tworivers-springs` (functie `bak_pgm_tworivers_springs`), uit `v2/data/stroomroute-pgm-tworivers-springs.json` (126,5 KB, contract 2, lonlat, 3 benen, 6.173 punten, 3 markers). Wegscan b1: `python v2/tools/wegscan_puur.py --profiel pgm-tworivers-springs-tworivers-rustenburg` (zuid-afrika, venster 75 km).

| # | modaliteit | been | km gebakken | km brief | naad |
|---|---|---|---|---|---|
| 1 | truck, **stippel** | last mile Two Rivers-concentrator → terreinweg (OSM-gat 25 m) | 0,2 | n.v.t. | 0 |
| 2 | truck | Two Rivers → R555 → N4 → Impala Rustenburg (eigen scan, doorgetrokken) | 426,5 | indicatie 439 (OSRM, geen wegkm) = -2,9% | 0,00 |
| 3 | truck | Impala Rustenburg → Springs, LETTERLIJKE KOPIE pgm-springs-zurich b1 (via pgm-mimosa-springs) | 255,8 | 255,8 gebakken | 0,00 |

Totaal 682,5 km; geen naad > 0,01 km; alle drie de markers liggen op de lijn (0,0 km). Knikken: b1 0 omkeringen, 0 terugloop; b2 (kopie) 1 echte scherpe bocht, niet van mij. Lengtetoets b1 is indicatief: er is geen gepubliceerde wegkm (hemelsbreed 298 km; OSRM 439/456 is dezelfde OSM-bron).

**Stippel (1, 0,2 km).** Het anker Two Rivers (satelliet-gelegd) ligt in een los OSM-component van 13 service-ways op het terrein; tussen die cluster en terreinweg 231027166 zit 25 m niet-gekarteerd gat (OSM-API gecontroleerd). Zonder dit gat faalde de scan met "geen wegpad tussen punt 0 en 1", ook met `eindToegangPrivaat`. Het wegbeen begint daarom op het dichtstbijzijnde net-knooppunt (-24.9361,30.1033, uiteinde way 231027166, 0,22 km van het anker; dat is een gemeten OSM-punt, niet verzonnen) en het anker is via een korte rechte stippel ("geen net op deze korrel") verbonden.

**Via-ingreep.** Het via-punt "Rustenburg N4/R24" uit §4 (-25.7031,27.2572) snapte op een stomp van ~0,1 km en gaf een 180-graden-terugloop; verplaatst naar een punt op de N4 zelf (-25.7014,27.2559, 0,15 km westelijker, een bestaand knooppunt van de eerste route). Effect op km: 0,6 km korter; niet gebruikt om de toets te halen.

**Keerlus bij Stoffberg.** Het via-punt Stoffberg (-25.3549,29.7658) lag zo dat het pad een zijlus van ~13,7 km (heen en terug) maakte; de scanner snoeide die (440,1 → 426,4 km). Geen knik meer; wel een aanwijzing dat het punt dicht bij een zijtak ligt (niet verplaatst: de snoei lost het op).

**Lessen voor volgende ketens.** (1) Een concentrator-anker kan in een los OSM-component zitten ondanks een gekarteerd terrein: check de component (zie wegscan3-log) vóór je met `eindToegangPrivaat` gaat tuinieren; de oplossing is een start op het dichtstbijzijnde netpunt plus een korte stippel. (2) Een via-punt dat via 'hergebruikt' uit een andere stroom komt kan alsnog op een stomp snappen (Rustenburg N4/R24 werkte in andere ketens, hier niet door de aankomstrichting): `toets_knikken` TERUGLOOP is de verklikker.
