# Routebrief (licht) · Lithium — Van → Via → Naar (land)

**stroom-id:** `lithium-greenbushes-kemerton` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** spodumeenconcentraat van Talisons Greenbushes-mijn gaat per truck ~101 km noordwaarts
over de South Western Highway, de Bunbury-omleiding (Wilman Wadandi Highway) en de Forrest Highway naar
Albemarle's eigen Kemerton-hydroxidefabriek — een tweede afzetstreng naast de bestaande export via Bunbury/
Zhangjiagang (`lithium-greenbushes-zhangjiagang.md`), gebaseerd op gedeeld eigendom (Albemarle 49% van
Greenbushes + 100% van Kemerton), niet op een aangetoond contractueel spoor.
**Welke as van het verhaal:** *de eerste mijn-naar-eigen-raffinaderij-as van de atlas* — **niet** de eerste
volledig binnenlandse as: die claim behoort al aan `lithium-silverpeak-mccarran.md` (Nevada-mijn → Tesla
Gigafactory Nevada). Kemerton's hydroxidetrein is grotendeels stilgelegd sinds Albemarle's persbericht 2026,
dus dit is een structureel geplande as (al aangekondigd in `lithium-greenbushes-zhangjiagang.md` §4/§1 als
toekomstige vertakking) met een op dit moment onzeker of laag actueel volume.

## 1 · Ketenkaart
```
Greenbushes-mijn `li-gb-laadplek` ──(b1 truck — aannemelijk: eigendomsrelatie, geen brondocument ·
South Western Hwy N (Balingup–Donnybrook–Boyanup) → Wilman Wadandi Hwy (Bunbury-omleiding) →
Forrest Hwy N → Marriott Rd · ~101 km)──► Kemerton lithium hydroxide plant `li-kemerton-fabriek`
⏹ stoppunt (Albemarle 100%, hydroxidetrein grotendeels stilgelegd sinds 2026)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat — aannemelijk: eigendomsrelatie, geen brondocument) | `li-gb-laadplek` → `li-kemerton-fabriek` | Maranup Ford Rd/Stanifer St → South Western Hwy N (Balingup–Donnybrook–Boyanup) → Wilman Wadandi Hwy (Bunbury-omleiding, nabij Gelorup) → Forrest Hwy N (Leschenault) → Marriott Rd | **niet gepubliceerd**; OSRM-routering op OSM-wegnet **100,7 km** [7][8] (Maranup Ford Rd 1,7 + Stanifer St 1,3 + South Western Hwy 66,0 + Wilman Wadandi Hwy 18,8 + Forrest Hwy 6,3 + Marriott Rd 3,6 + laatste km); hemelsbreed **78,3 km** (eigen berekening, §8) tegen ontwerpschatting 78 km/geschat 100–130 km — beide géén officiële bron, dus de ±15%-toets is hier **indicatie, geen norm** | maak_stroombeen_weg (extract australie, nieuw profiel — deelt startpunt met het bestaande Greenbushes-profiel `lithium-greenbushes-bunbury`, ander eindpunt) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-gb-laadplek` | mijn / laadplek | Greenbushes-concentraatloods (Talison: Tianqi/IGO 51% · Albemarle 49%) | -33.86495, 116.05505 | **hergebruik letterlijk** uit `lithium-greenbushes-zhangjiagang.md` §2a(1) | **bron-gelegd** (z18, 2026-07-29, aldaar: "overdekte loods NE-SW, hardstand, aansluitende truckloop") |
| `li-kemerton-fabriek` | raffinaderij (losplek, stoppunt) | Kemerton lithium hydroxide plant (Albemarle 100%) | -33.2050, 115.7604 | **hergebruik** `w-li-kemerton` uit `lithium-sitelaag.json`/`.md` [B7][B8]; onafhankelijk herbevestigd op OSM: `man_made=works` "Albemarle Lithium", Kemerton Road, Wellesley/Bunbury, -33.2050123/115.7604372 — 5 decimalen identiek [7] | **bron-gelegd** (sitelaag, z15: "kruis midden op het fabrieksterrein — procesgebouwen, tanks, toegangsweg vanaf de snelweg") |

⚠️ **Coördinaat-harmonisatie voor de bak-agent:** `lithium-greenbushes-zhangjiagang.md` §2a-2 (negatieve ankers,
been 2) noemt Kemerton op -33.20850, 115.75797 — 0,5 km van de waarde hierboven, binnen dezelfde OSM-
werkspolygoon (bbox −33.2086…−33.2019 / 115.7545…115.7664). Neem bij het bakken **de sitelaagwaarde** hierboven
als de ene geharmoniseerde coördinaat (haalbaarheidstoets-aanpassing).

## 4 · Via-punten (b1 — corridorkeuzes)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Balingup | -33.7861, 115.9832 | deelt de corridor met been `li-gz-b2` uit `lithium-greenbushes-zhangjiagang.md`: enige noordwaartse route vanaf de mijn over de South Western Highway |
| b1 | 2 | Donnybrook | -33.5774, 115.8251 | zelfde gedeelde corridor; hier komen ook wegen uit het Boyup Brook-gebied samen (ontwerp-corridorbeschrijving) |
| b1 | 3 | Boyanup | -33.4844, 115.7289 | laatste punt op de gedeelde Bunbury-corridor vóór deze as afslaat |
| b1 | 4 | South Western Hwy → Wilman Wadandi Hwy (Bunbury-omleiding), nabij Gelorup | -33.3997, 115.6981 | corridorkeuze: deze as neemt de oostelijke Bunbury-omleiding i.p.v. door te rijden naar de haven/CBD (been `li-gz-b2`) |
| b1 | 5 | Wilman Wadandi Hwy → Forrest Hwy, nabij Leschenault | -33.2651, 115.7522 | corridorkeuze: de as neemt de kustweg noordwaarts i.p.v. verder om Bunbury heen te blijven rijden |
| b1 | 6 | Forrest Hwy → Marriott Road, Leschenault | -33.2158, 115.7223 | corridorkeuze: laatste afslag van de doorgaande kustweg naar het Kemerton-industrieterrein |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kemerton lithium hydroxide plant | Albemarle (100%) | spodumeenconcentraat (herkomst niet uitgesplitst naar mijn) → lithiumhydroxide | 2×50 kt LiOH/j nameplate ≈ 88 kt LCE-equivalent; **hydroxidetrein grotendeels stilgelegd sinds Albemarle-persbericht 2026** — actueel volume onzeker/laag | [B7][B8] (lithium-sitelaag.md) |

## 6 · Stoppunt
De brief stopt bij de poort van Kemerton: dit is de eigen raffinaderij van de mede-eigenaar van Greenbushes en
er is geen gedocumenteerde volgende locatie voor het hydroxide op déze as. ⚠️ **Kemerton's hydroxidetrein
staat grotendeels stil sinds 2026** (Albemarle-persbericht, [B2]) — deze kaart tekent de fysieke route, niet
een actief volume; zie §7.

## 7 · Open punten
- **Geen brondocument koppelt Greenbushes-concentraat specifiek aan Kemerton.** De as steunt uitsluitend op
  gedeeld eigendom (Albemarle 49% Greenbushes + 100% Kemerton) — vandaar het label *aannemelijk:
  eigendomsrelatie, geen brondocument* in de beennaam (haalbaarheidstoets-aanpassing, bindend).
- **Kemerton's hydroxidetrein staat grotendeels stil sinds 2026** — het actuele jaarvolume over deze as is
  daardoor onzeker, mogelijk laag of nul op dit moment; al vastgelegd in de sitelaag [B8].
- **Geen officiële/gepubliceerde wegkilometer gevonden** voor Greenbushes→Kemerton; de 100,7 km in §2 komt uit
  een eigen OSRM-routering op het OSM-wegnet, niet uit een bedrijfs- of overheidsopgave.
- **Twee licht verschillende Kemerton-coördinaten in de projectdata** (zie §3, harmonisatienoot) — opgelost
  in deze brief door de sitelaagwaarde als geharmoniseerde coördinaat aan te wijzen.
- **Aandeel van Greenbushes' output dat specifiek naar Kemerton gaat** (i.p.v. naar de Tianqi/IGO-Kwinana-JV
  of naar export via Bunbury/Zhangjiagang) is niet apart gepubliceerd — vandaar geen jaarvolume-getal voor
  déze as, alleen de context-nameplates in §5.

## 8 · Bronnen
[1] Australian Mining, 'Greenbushes sustains solid production' — https://www.australianmining.com.au/greenbushes-sustains-solid-production/
[2] Albemarle, 'Albemarle Announces Plans to Idle its Kemerton Lithium Hydroxide Processing Plant' (2026) — https://investors.albemarle.com/news-and-events/news/news-details/2026/Albemarle-Announces-Plans-to-Idle-its-Kemerton-Lithium-Hydroxide-Processing-Plant/default.aspx
[3] `v2/design/lithium-sitelaag.json`/`.md` — ankers `w-li-greenbushes` (-33.86495, 116.05505) en
`w-li-kemerton` (-33.2050, 115.7604), beide bron-gelegd, met bronverwijzing [B1][B2][B7][B8] aldaar.
[4] `v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md` §2a(1) en §2a-2 (negatieve ankers) —
hergebruikt anker `li-gb-laadplek` (satelliet-gelegd z18, 2026-07-29) en de eerder gelegde
Kemerton-negatiefankercoördinaat (harmonisatienoot §3).
[5] Albemarle, 10-K FY2025, Exhibit 96-1 Greenbushes Technical Report Summary — https://www.sec.gov/Archives/edgar/data/915913/000091591326000018/ex961greenbushes2025trs.htm
[6] Argus Media, 'Australia's IGO, Tianqi in talks over lithium refinery' (WA-raffinagecontext/Kwinana) — https://www.argusmedia.com/en/news-and-insights/latest-market-news/2725675-australia-s-igo-tianqi-in-talks-over-lithium-refinery
[7] OpenStreetMap (ODbL) via Nominatim — "Albemarle Lithium" (`man_made=works`, Kemerton Road, Wellesley,
Bunbury, -33.2050123/115.7604372); plus opzoekingen voor Maranup Ford Road, Stanifer Street, Marriott Road,
Forrest Highway, Wilman Wadandi Highway, Boyanup, Donnybrook, Dardanup. https://nominatim.openstreetmap.org
[8] OSRM-demoroutering (project-osrm.org) over het OSM-wegnet, Greenbushes-anker → Kemerton-anker: 100,7 km
via South Western Highway → Wilman Wadandi Highway (Bunbury-omleiding) → Forrest Highway → Marriott Road,
opgevraagd 2026-09-28. http://router.project-osrm.org
[9] `data/lithium.js`/`data/lithium.md` (v1-register) — `li-greenbushes`, `li-ref-kwinana` ("Kwinana /
Kemerton"), context voor de bestaande Kwinana-flow (20 kt via weg) waarnaast deze as een tweede wegstreng is.
[10] Geofabrik, `australie-latest.osm.pbf` — lokaal in `v2/build-cache/geofabrik/`, wegnet-extract voor de
bak-agent (`maak_stroombeen_weg.py`).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Eén been, doorgetrokken.** b1 (truck, fase A) — spodumeenconcentraat
Greenbushes-mijn → Kemerton lithium hydroxide plant: **102,1 km · 1.241
punten · 2 markers**. Geen zee, geen haven-aanloop, geen spoor/leiding/
binnenvaart — zuiver enkel truckbeen zoals `lithium-silverpeak-mccarran`.
Bestand: `v2/data/stroomroute-lithium-greenbushes-kemerton.json` (27,3 KB).

**Recept:** nieuw profiel `lithium-greenbushes-kemerton-greenbushes-kemerton`
in `v2/tools/maak_stroombeen_weg.py` (extract `australie`, `--bron geofabrik`)
→ `v2/build-cache/ais/graaf/lithium-greenbushes-kemerton-weg-greenbushes-kemerton.geojson`
→ `bak_lithium_greenbushes_kemerton()` in `v2/tools/bak_stromen.sh` (`bash
v2/tools/bak_stromen.sh lithium-greenbushes-kemerton`).

**Startanker LETTERLIJK gedeeld** met het bestaande profiel
`lithium-greenbushes-bunbury` (116,05505,-33,86495) — alleen het beginpunt,
een ander eindpunt; geen gedeeld-been-kopie nodig (nieuw profiel, ook al
overlapt de eerste ~66 km corridormatig met de Bunbury-as). Eindanker =
de **geharmoniseerde Kemerton-coördinaat** uit de sitelaag (-33,2050,
115,7604, zie §3) — niet opnieuw satelliet gecheckt (letterlijk hergebruik
toegestaan).

**Km-toets (indicatie, geen norm — brief §2/§7):** de bake geeft **102,1 km**
getekend (101,6 km corridor + twee korte anker-verbindingen plant→weg
0,06 km en weg→kade 0,45 km, beide `[OK]`) tegen de OSRM-werkwaarde van
100,7 km — **+1,4%**, ruim binnen elke redelijke marge, ook al is er geen
officiële bron en geldt de ±15%-toets hier alleen als indicatie.

**`toets_knikken.py`:** 6 knikken ≥60°, waarvan **1 omkering** (159,1° bij
-33,21520,115,72205, radius 7 m) — geclassificeerd als "scherpe bocht, echt"
(v=1,1, dus een echte bocht, geen terugloop) op de Forrest Hwy→Marriott Rd-
afslag bij Leschenault; **0 terugloop** (de enige klasse die reparatie
vraagt). De vijf overige knikken zijn spikes <60 m radius, karakteristiek
voor OSM-kruispuntgeometrie, geen actie.

**`toets_rechte_benen.py --min-km 5`:** geen bevinding voor deze stroom (het
been is geen rechte lijn, geen omwegfactor 1,000).

**Structuur-toets:** `versie: 2` · `punt_formaat: lonlat` · modaliteit
`truck` ∈ toegestane set · been ≥2 punten (1.241) · naad 0,000 km (enkel
been, geen naadprobleem) · beide markers exact op de lijnuiteinden (0,0 km
van de lijn).

**Bevindingen (geen wijziging, alleen vastgelegd):**
- De beennaam draagt het label **"aannemelijk: eigendomsrelatie, geen
  brondocument"** conform §2/§6/§7 — geen bron koppelt Greenbushes-
  concentraat specifiek aan Kemerton, de as steunt uitsluitend op gedeeld
  eigendom (Albemarle 49% Greenbushes + 100% Kemerton).
- Kemerton's hydroxidetrein staat grotendeels stil sinds 2026
  (Albemarle-persbericht) — het actuele jaarvolume over deze as is
  onzeker/mogelijk laag, ongewijzigd t.o.v. §5/§7.
- Geen gepubliceerde wegkilometer; 100,7 km blijft een eigen OSRM-routering,
  geen bedrijfs- of overheidsopgave (§2/§8).

**Les voor latere agenten:** een enkel truckbeen met een letterlijk gedeeld
startanker en een geharmoniseerde eindcoördinaat uit de sitelaag bakt in één
`hecht_marnet.py route`-aanroep zonder verrassingen zodra het profiel al
op een bewezen corridor (South Western Hwy N) aansluit — de default
`eindKlassen` (residential/service/tertiary/unclassified binnen 12 km)
volstond voor Maranup Ford Rd/Stanifer St bij de mijn, geen override nodig.
