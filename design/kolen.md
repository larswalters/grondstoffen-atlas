# Kolen — brief (ingevuld ontwerp) — hoort bij `data/coal.js`

*Peiljaar ±2023. Alle volumes in **Mt/jaar** (miljoen ton), indicatief en afgerond —
bedoeld om verhoudingen te tonen, geen handelsstatistiek. Wereldproductie ≈ **8.700 Mt**
(~8,7 miljard ton; IEA *Coal 2023* / BP-Energy Institute *Statistical Review 2024*); wereld-
**zeehandel** ≈ **1.350 Mt** (~15% van de productie). Bronnen: IEA, Energy Institute, USGS,
havenautoriteiten (Newcastle/Richards Bay), bedrijfsrapportages (Coal India, Adaro, BHP-BMA,
Teck, Glencore). Zie §7. Status: **uitgewerkt-ontwerp** — klaar om 1-op-1 naar `coal.js` te zetten.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid — het plaatje vertelt
> zichzelf. Voor lithium/koper is de vorm "alles door China-raffinage", voor goud "alles door
> Zwitserland", voor zilver "geen trechter, een bijproduct-vraagknijp". Voor kolen is de vorm
> **weer anders**: kolen kent **geen enkele mondiale flessenhals** omdat het overweldigend
> **binnenlands** is — China, India en de VS delven én verbranden hun eigen kolen; slechts ~15%
> gaat over zee. Wat de kaart wél moet laten zien is (1) enorme **binnenlandse blokken**
> (mijn→centrale, korte hops) tegenover (2) een dunnere maar **geopolitiek beladen zeehandels-
> laag**, met **China als grootste producent én grootste importeur** (de swing-koper), de
> **twee kolen** (thermisch=stroom vs. cokeskool=staal), en drie levende her-routeringen:
> de **China-Australië-kolenban** (2020-2023), de **Rusland-draai naar het oosten** (2022→) en
> de **Mongoolse cokeskool over de Gobi-grens** (het enige nieuwe landknelpunt).

---

## 0. Metadata (→ `REGISTER({...})` in `coal.js`)

| veld | waarde |
|---|---|
| `id` | `coal` |
| `name` | Kolen |
| `symbol` | C |
| `color` | `#6B5D4F` (warm antraciet-bruingrijs; markers — bewust wármer dan grafiet's koele grijs) |
| `flowColor` | `#C2A878` (warm taupe/as; de bogen zichtbaar tegen de donkere bol) |
| `unit` | `Mt/jaar` |
| `detail` | `uitgewerkt` |
| `blurb` | Kolen is de grondstof die de energietransitie zou moeten doden, maar op recordhoogte staat — gedreven door China en India. De vorm is fundamenteel anders dan de andere grondstoffen: geen mondiale trechter, want ~85% wordt verbrand waar het gedolven wordt (China #1, India, VS). Slechts ~15% gaat over zee, en op die dunnere laag is China zowel grootste producent als grootste importeur — de swing-koper. Twee kolen naast elkaar: thermisch (steenkool → stroom) en cokeskool (→ staal). |

## 1. Het verhaal in 3 zinnen
1. **Kolen is overweldigend binnenlands:** de reuzen (China ~50% van de wereld, India, VS, Rusland)
   delven én verbranden hun eigen kolen — slechts ~15% van de ~8.700 Mt gaat de zee over. Op de kaart:
   grote **binnenlandse clusters** (mijn → centrale, korte land/kust-hops) en daarbovenop een dunnere
   **zeehandelslaag**.
2. Op die zeelaag is **China de swing-koper**: 's werelds grootste producent maar óók grootste importeur —
   z'n marginale importvraag (uit Indonesië, Australië, Rusland, Mongolië) zet de zeeprijs, en z'n beleid
   legt hele stromen om. **India** is de #2-importeur en veruit de grootste **cokeskool**-importeur.
3. Er zijn **twee kolen**: **thermisch** (steenkool → elektriciteitscentrales) en **metallurgisch/
   cokeskool** (→ cokesovens → hoogoven-staal). De premium harde cokeskool zit geconcentreerd in het
   Australische **Bowen Basin**; de rest van het verhaal is her-routering: de **Australië-ban**, de
   **Rusland-draai** en de **Mongoolse Gobi-corridor**.

## 2. De keten & stages (→ `stage`-codes; hergebruikt de bestaande stage-styling)
Kolen wordt niet "geraffineerd" zoals metaal — de kracht van de stages ligt hier in het onderscheid
**gedolven → internationaal verhandeld → verbrand/verstaald**. Zo wordt binnenlandse kolen (alleen
`erts`+`product`, géén zeekruising) visueel ánders dan verhandelde kolen (mét de heldere `raffinaat`-
zeeboog) — precies de ~85/15-splitsing zichtbaar gemaakt.

| stap | `stage`-code | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. mijn → gewassen/gebroken ruwe kolen | `erts` | dof/donker antraciet | laag | mijn → wasserij/haven (gathering) én mijn → binnenlandse centrale (de grote domestic-hops) |
| 2. **internationaal verhandelde bulk** | `raffinaat` | volle kolenkleur | midden | haven → importterminal (de zeekruisingen) + de Mongolië-landcorridor — waar élk knelpunt/ban/her-routeringsverhaal leeft |
| 3. **eindgebruik** (stroom / staal) | `product` | licht, bijna wit | hoog | importterminal → centrale (verbranding) en cokeskool → cokesoven/staalfabriek |

> De **thermisch vs. cokeskool**-tweedeling loopt niet via `stage` (dat blijft de ketenpositie) maar via
> `note` + een aparte `tension` — net zoals nikkel z'n class-1/class-2 via note/tension draagt, niet via stage.

## 3. Nodes (locaties)
> Alle `type`-waarden bestaan al in de rendering-laag: `mine`/`refinery`/`port`/`market`.
> **Géén nieuwe marker-styling nodig** (kolen gebruikt géén `recycler`/`exchange`/`cb`). Coördinaten:
> **west = negatief** (gecontroleerd). `share` = % van ~8.700 Mt wereldproductie. Elke mijn krijgt een
> `note` die thermisch/cokeskool + binnenlands/export benoemt.

### 3a. Winning (`type: mine`, met `share`) — de binnenlandse reuzen + de exportmijnen
*Som hieronder ≈ 75% wereld. De eerste blok = binnenlandse verbranders (delven+verstoken thuis); de tweede
blok = de exporteurs die de zeehandelslaag voeden. `note` benoemt telkens thermisch/cokeskool + binnenlands/export.*

**Binnenlandse reuzen (verbranden grotendeels thuis):**

| id | naam | land | lat | lon | share | tier | operator | ~Mt/jr | note |
|---|---|---|---|---|---|---|---|---|---|
| coal-shanxi | Shanxi (kolenbasis) | China | 37.87 | 112.55 | 16.0 | 1 | div. (staat + privaat) | ~1400 | Thermisch + cokeskool; het hart van China's "Drie West" (Shanxi/Shaanxi/Binnen-Mongolië ≈ 70% van China). Binnenlands: per spoor naar Qinhuangdao, dan kustvaart zuid. |
| coal-innermongolia | Binnen-Mongolië (Ordos) | China | 39.60 | 109.80 | 15.0 | 1 | div. | ~1300 | Thermisch; grootste provincie-output. Ook het ontvangstpunt van de Mongoolse import over de Gobi-grens. |
| coal-india | Jharkhand/Odisha (Coal India) | India | 23.70 | 85.30 | 11.0 | 1 | Coal India Ltd | ~950 | Thermisch (Odisha) + cokeskool (Jharkhand/Dhanbad); India #2. Verstookt vrijwel alles binnenlands, maar importeert tóch premium thermisch + cokeskool (eigen kool is asrijk). |
| coal-us-powder | Powder River Basin | VS (Wyoming) | 44.50 | -105.50 | 4.0 | 1 | Peabody/Arch | ~330 | Thermisch, laag-zwavel; bijna volledig binnenlands (VS-kolenvraag daalt structureel). |
| coal-russia-kuzbass | Kuzbass (Kemerovo) | Rusland | 54.00 | 86.50 | 5.0 | 1 | SUEK/div. | ~440 | Thermisch + cokeskool; landlocked Siberië → 4.000+ km spoor naar de Pacific-havens of de Baltische. De export-heroriëntatie na 2022 draait om dit spoor. |

**Exporteurs (voeden de zeehandelslaag):**

| id | naam | land | lat | lon | share | tier | operator | ~Mt/jr | note |
|---|---|---|---|---|---|---|---|---|---|
| coal-indonesia | Oost-Kalimantan | Indonesië | -0.50 | 117.00 | 9.0 | 1 | Bumi/Adaro/Kideco | ~775 | **#1 thermisch-exporteur ter wereld**; goedkoop, laag-calorisch, dichtbij China/India. Kolen per rivierpont naar transhipment-ankerplaatsen, dan bulkschip. |
| coal-australia-qld | Bowen Basin (Queensland) | Australië | -22.30 | 148.00 | 2.8 | 1 | BHP-Mitsubishi (BMA)/Anglo/Glencore | ~245 | **#1 metallurgische (cokeskool)-exporteur**; premium harde cokeskool voor hoogoven-staal. Per spoor naar Hay Point/Dalrymple Bay + Gladstone. |
| coal-australia-nsw | Hunter Valley (NSW) | Australië | -32.50 | 151.00 | 2.2 | 1 | Glencore/Yancoal | ~190 | Thermisch (hoog-calorisch); per spoor naar Newcastle — 's werelds grootste kolen-exporthaven. |
| coal-southafrica | Mpumalanga (Highveld) | Zuid-Afrika | -26.00 | 29.20 | 3.0 | 1 | Glencore/Thungela/Exxaro | ~230 | Thermisch; binnenlands (Eskom) + export via Richards Bay. Afzet sinds 2022 verschoven van Europa → India/Azië. |
| coal-colombia | Cerrejón (La Guajira) | Colombia | 11.10 | -72.60 | 0.7 | 2 | Glencore | ~55 | Thermisch; Atlantische export → Europa (kortstondig terug in 2022) + Azië via Panama. |
| coal-mongolia | Tavan Tolgoi (Zuid-Gobi) | Mongolië | 43.60 | 105.50 | 0.7 | 1 | Erdenes Tavan Tolgoi | ~60 | **Cokeskool, landlocked** → per truck/spoor over de Gobi-grens naar China. Backfilde de Australische cokeskool tijdens de ban. |
| coal-canada | Elk Valley (BC) | Canada | 49.90 | -114.90 | 0.6 | 2 | Teck | ~25 | Metallurgische cokeskool; per spoor naar Westshore/Vancouver → Aziatische staalindustrie. |
| coal-us-appalachia | Appalachen (West Virginia) | VS | 38.00 | -81.50 | 2.0 | 2 | div. | ~170 | Cokeskool + thermisch; het export-deel gaat via Hampton Roads (Norfolk) → Europa/India-staal (Atlantisch). |
| coal-mozambique | Moatize (Tete) | Mozambique | -16.10 | 33.70 | 0.2 | 3 | Vulcan (ex-Vale) | ~12 | Cokeskool + thermisch; per spoor (Nacala-corridor) naar de kust → India/Azië. Nieuwe mijn, lange landcorridor (koper/Copperbelt-parallel). |

### 3b. Winning — projecten
*(n.v.t. voor kolen v1 — het verhaal zit in de bestaande stromen, niet in nieuwe mijnen. Nieuwe kolencapaciteit
is politiek omstreden; de groei zit in India/Indonesië-uitbreiding van bestáánde bekkens, al meegenomen in de shares.)*

### 3c. "Raffinage" — n.v.t. (kolen wordt niet geraffineerd)
*Kolen kent geen raffinaderij-stap zoals metaal. De enige echte transformatie is **cokeskool → cokes** in
cokesovens, en die zitten pal bij de staalfabrieken (gemodelleerd als `market`-staalhubs, niet als aparte
`refinery`-nodes). Er zijn dus géén `refinery`-nodes; de `raffinaat`-stage draagt hier de **verhandelde bulk**.*

### 3d. Havens / exportterminals (`type: port`) — waar de kolen de zee op gaat
| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| coal-port-newcastle | Newcastle | Australië | -32.92 | 151.78 | 's Werelds grootste kolen-exporthaven (Hunter-thermisch) → NO-Azië |
| coal-port-haypoint | Hay Point / Dalrymple Bay | Australië | -21.28 | 149.30 | Bowen-cokeskool → staal Azië/India |
| coal-port-kalimantan | Bontang / Muara-ankerplaats | Indonesië | -0.10 | 117.55 | Indonesische thermisch-transhipment → China/India |
| coal-port-richards-bay | Richards Bay (RBCT) | Zuid-Afrika | -28.80 | 32.08 | Grootste kolenterminal van Afrika → India/Azië (was Europa) |
| coal-port-vostochny | Vostochny / Nachodka (Pacific) | Rusland | 42.75 | 133.08 | Russische kolen-Pacific-draai → China/Japan/Korea/India |
| coal-port-ustluga | Ust-Luga (Baltisch) | Rusland | 59.67 | 28.30 | Russische kolen → Europa (pre-2022) / nu Turkije/omweg |
| coal-port-cerrejon | Puerto Bolívar | Colombia | 12.23 | -71.98 | Colombiaanse thermisch → Atlantische markten |
| coal-port-hampton | Hampton Roads (Norfolk) | VS | 36.90 | -76.30 | US-cokeskool/thermisch export → Europa/India (Atlantisch) |
| coal-port-vancouver | Westshore (Roberts Bank) | Canada | 49.00 | -123.15 | Canadese cokeskool → Aziatische staalhubs |
| coal-port-nacala | Nacala | Mozambique | -14.54 | 40.68 | Moatize-cokeskool via de Nacala-spoorcorridor → India |
| coal-port-qinhuangdao | Qinhuangdao | China | 39.90 | 119.60 | **Binnenlandse** transhipment-hub: Shanxi-kolen per spoor → kustvaart naar Zuid-China. De Chinese benchmarkhaven. |

### 3e. Eindbestemming / consumptie (`type: market`) — centrales & staalfabrieken
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| coal-mkt-china-power | China — kustcentrales (Guangdong) | China | 23.10 | 113.30 | 1 | De grootste importvraag: kustprovincies verstoken binnenlandse (per kustvaart) + geïmporteerde thermisch |
| coal-mkt-china-steel | China — staal (Hebei/Tangshan) | China | 39.63 | 118.18 | 1 | 's Werelds grootste staalindustrie → grootste cokeskool-sink (binnenlands + Mongolië/Australië/Rusland) |
| coal-mkt-india-power | India — kustcentrales (Mundra/Gujarat) | India | 22.75 | 69.70 | 1 | Geïmporteerd hoog-calorisch thermisch voor de kustcentrales (Adani/Tata) |
| coal-mkt-india-steel | India — staal (Odisha/Jharkhand) | India | 21.50 | 85.80 | 1 | **#1 cokeskool-importeur ter wereld** — eigen kool is ongeschikt voor cokes |
| coal-mkt-japan | Japan — stroom + staal | Japan | 34.90 | 137.00 | 1 | Grote thermisch- + cokeskool-importeur (Chubu/Nagoya); vaste Australische leverancier |
| coal-mkt-korea | Zuid-Korea — stroom + staal (POSCO) | Zuid-Korea | 35.99 | 129.38 | 1 | Thermisch + cokeskool; Pohang-staal. Nam Australische kolen op tijdens de China-ban |
| coal-mkt-taiwan | Taiwan — stroom | Taiwan | 24.00 | 120.50 | 2 | Thermisch-importeur (Taichung, een van 's werelds grootste kolencentrales) |
| coal-mkt-vietnam | Vietnam — stroom (Haiphong) | Vietnam | 20.85 | 106.75 | 2 | Snelst groeiende Zuidoost-Aziatische importeur |
| coal-mkt-eu | EU — stroom + staal (Ruhr/ARA) | Duitsland | 51.40 | 6.80 | 2 | Structureel dalend; kortstondige heropleving 2022 (gascrisis). Bevoorraad via Rotterdam/ARA |

### 3f. Extra lagen (optioneel) — **géén** voor kolen v1
*Kolen heeft geen zinvol CB-/beurs-/recycling-equivalent: er zijn geen bovengrondse "kluisvoorraden" zoals
bij edelmetalen, en kolen wordt niet gerecycled (het wordt verbrand). Chinese haven-/centralevoorraden zijn
een belangrijk marktsignaal maar marginaal in tonnage → bewust **geen toggle-laag** (zoals PGM's exchange-laag
naar de backlog ging). Dat houdt de engine ook schoon terwijl de parallelle grafiet-sessie draait (sectie J).*

## 4. Stromen (flows) — indicatief, ~Mt/jr
*Modi: **`ship`** (intercontinentale bulk — bestaande zee-A\*), **`rail`/`road`** (binnenlandse hops mijn→haven/
centrale + de Mongolië-landcorridor). `via` = havens + bestaande `wp-*`-vaarpunten/knelpunten. **Harde regel:**
elke ship-leg landt op een kustpunt (`port`/`coastal`/`wp-*`). Nieuw knelpunt: alléén de Mongolië-Gobi-grens.*

### 4a. Binnenlandse kolen — mijn → centrale/staal (stage `erts` + `product`) — de ~85%
*De grote binnenlandse blokken: geen zeekruising, dus alleen `erts` (mijn→hub) en `product` (hub→verbranding).*

| from | to | ~Mt/jr | mode | stage | via | note |
|---|---|---|---|---|---|---|
| coal-shanxi | coal-port-qinhuangdao | 1000 | rail | erts | — | Shanxi-kolen per spoor naar de transhipment-benchmarkhaven Qinhuangdao |
| coal-port-qinhuangdao | coal-mkt-china-power | 1000 | ship | product | wp-taiwan | Kustvaart zuid naar de Guangdong-centrales (binnenlandse zeeroute langs de kust) |
| coal-innermongolia | coal-mkt-china-steel | 900 | rail | erts | — | Ordos-kolen → de Hebei/Tangshan-staal- en stroomcluster (binnenlands over land) |
| coal-india | coal-mkt-india-steel | 700 | rail | erts | — | Coal India → binnenlandse staal/stroom (Odisha/Jharkhand), grotendeels binnenlands |
| coal-us-powder | coal-mkt-... (VS-binnenlands) | 300 | rail | erts | — | Powder River → Amerikaanse centrales (binnenlands; modelleer als korte hop of laat impliciet) |
| coal-russia-kuzbass | coal-port-vostochny | 200 | rail | erts | — | Kuzbass → 4.000 km spoor naar de Pacific-haven (de post-2022 oost-draai) |

> *Opmerking bouw:* voor de VS-binnenlandse burn kan een lichte `coal-mkt-us`-node worden toegevoegd, óf de
> Powder-River-hop impliciet gelaten (VS-export loopt via Appalachia). Houd het aantal China-nodes beheersbaar;
> Qinhuangdao draagt het binnenlandse China-verhaal al.

### 4b. Zeehandel thermisch — exporteur → importeur (stage `erts` naar haven, `raffinaat` over zee, `product` bij centrale)
| from | to | ~Mt/jr | mode | stage | via | note |
|---|---|---|---|---|---|---|
| coal-indonesia | coal-mkt-china-power | 200 | ship | raffinaat | coal-port-kalimantan, wp-makassar, wp-scs, wp-taiwan | Indonesische thermisch → Zuid-China (kortste zeehandelsroute; gathering-leg per pont) |
| coal-indonesia | coal-mkt-india-power | 130 | ship | raffinaat | coal-port-kalimantan, wp-singapore, wp-malakka, wp-aceh | Indonesische thermisch → India-westkust via Malakka |
| coal-indonesia | coal-mkt-vietnam | 40 | ship | raffinaat | coal-port-kalimantan, wp-scs | → de groeiende Vietnamese centralevraag |
| coal-australia-nsw | coal-mkt-japan | 80 | ship | raffinaat | coal-port-newcastle, wp-pac-west | Hunter-thermisch → Japan (de vaste, premium relatie) |
| coal-australia-nsw | coal-mkt-korea | 45 | ship | raffinaat | coal-port-newcastle, wp-pac-west, wp-taiwan | → Korea (nam Australische kolen op tijdens de China-ban) |
| coal-australia-nsw | coal-mkt-taiwan | 30 | ship | raffinaat | coal-port-newcastle, wp-pac-west, wp-scs | → Taiwan (Taichung) |
| coal-southafrica | coal-mkt-india-power | 60 | ship | raffinaat | coal-port-richards-bay, wp-moz-noord, wp-malakka, wp-aceh | Richards Bay → India (de post-2022 verschuiving van Europa naar India) |
| coal-colombia | coal-mkt-eu | 30 | ship | raffinaat | coal-port-cerrejon, wp-atl-west, wp-gibraltar | Colombiaanse thermisch → Europa (piekte in 2022 door de gascrisis) |
| coal-russia-kuzbass | coal-mkt-china-power | 90 | ship | raffinaat | coal-port-vostochny, wp-taiwan | Russische Pacific-kolen → China (de oost-draai na de EU-embargo aug-2022) |
| coal-russia-kuzbass | coal-mkt-eu | 25 | ship | raffinaat | coal-port-ustluga, wp-deense-straten | Legacy Baltische stroom → Europa (grotendeels weggevallen na 2022; dun draadje) |

### 4c. Zeehandel cokeskool — exporteur → staalfabriek (stage `raffinaat` over zee, `product` = cokes/staal)
| from | to | ~Mt/jr | mode | stage | via | note |
|---|---|---|---|---|---|---|
| coal-australia-qld | coal-mkt-india-steel | 55 | ship | raffinaat | coal-port-haypoint, wp-lombok, wp-makassar... | **de grootste cokeskool-stroom**: Bowen Basin → India-staal (India #1 cokeskool-importeur) |
| coal-australia-qld | coal-mkt-japan | 35 | ship | raffinaat | coal-port-haypoint, wp-pac-west | Premium harde cokeskool → Japanse hoogovens |
| coal-australia-qld | coal-mkt-korea | 25 | ship | raffinaat | coal-port-haypoint, wp-pac-west, wp-taiwan | → POSCO-staal (Pohang) |
| coal-canada | coal-mkt-japan | 20 | ship | raffinaat | coal-port-vancouver, wp-pac-noord | Elk Valley → Japans staal (Pacific great-circle) |
| coal-us-appalachia | coal-mkt-eu | 25 | ship | raffinaat | coal-port-hampton, wp-atl-west, wp-gibraltar | Appalachische cokeskool → Europees staal (Atlantisch) |
| coal-us-appalachia | coal-mkt-india-steel | 20 | ship | raffinaat | coal-port-hampton, wp-atl-west, wp-kaap, wp-moz-noord, wp-malakka, wp-aceh | US-cokeskool → India-staal (backfilde toen Rusland/Australië wegvielen) |
| coal-mozambique | coal-mkt-india-steel | 8 | ship | raffinaat | coal-port-nacala, wp-moz-noord, wp-malakka, wp-aceh | Moatize → India-staal via de Nacala-spoorcorridor |
| coal-mongolia | coal-mkt-china-steel | 55 | rail | raffinaat | grens-gashuunsukhait | **De landcorridor**: Tavan-Tolgoi-cokeskool per truck/spoor over de Gobi-grens → China-staal |

### 4d. Eindgebruik-hops (stage `product`) — optioneel, bij de importhubs
*Waar een importterminal en de centrale/staalfabriek niet samenvallen, een korte `product`-hop. Voor de meeste
markt-nodes valt de haven samen met de verbrander (coastal) → dan draagt de zeeboog al de `product`-lezing bij aankomst.*

| from | to | ~Mt/jr | mode | stage | note |
|---|---|---|---|---|---|
| (de meeste zeekruisingen eindigen `coastal:true` op de markt-node — geen aparte product-hop nodig) | | | | | Houd markt-nodes `coastal:true` zodat de ship-leg netjes landt |

## 5. Knelpunten & de "knijp"
- Kolen heeft **géén enkele mondiale flessenhals** — dat *is* het eigen aha, net als bij zilver, maar om een
  andere reden: niet inelastisch bijproduct, maar **binnenlandsheid**. ~85% wordt verbrand waar het gedolven
  wordt; de zeehandelslaag (~15%) is dun en gespreid over vele routes.
- **Eén nieuw landknelpunt:** `grens-gashuunsukhait` (Gashuun Sukhait / Ganqimaodu), de Mongolië-China-Gobi-grens
  waar de Mongoolse cokeskool oversteekt — exact het `grens-kasumbalesa`/`grens-ruili`-patroon (`kind:"grensovergang"`,
  landpunt, houdt de landkaart open). Alléén kolen verwijst ernaar → regressievrij.
- **Bestaande `wp-*` die kolen hergebruikt:** Lombok/Makassar/SCS/Taiwan (Australië/Indonesië → NO-Azië),
  Malakka/Aceh (Indonesië/Zuid-Afrika/US → India), Moz-noord (Zuid-Afrika/Mozambique), Kaap (US-cokeskool → India),
  Panama/Atl-west/Gibraltar (Colombia/US → Europa/Azië), Pac-west/Pac-noord (Australië-oost/Canada → Japan),
  Deense Straten (Rusland-Baltisch → Europa). Kolen is de **vierde** grondstof (na nikkel/zilver/... ) die geen
  nieuw zéé-knelpunt toevoegt — alleen de landcorridor.
- **De drie her-routeringsverhalen** (institutionele "knijp", via `tension`, geen `wp-`):
  1. **China-Australië-ban (okt 2020 – begin 2023):** China verbood informeel Australische thermisch+cokeskool;
     de Australische kolen werden omgelegd naar India/Japan/Korea, China backfilde met Indonesië/Rusland (thermisch)
     en Mongolië/Rusland/VS/Canada (cokeskool). De keten legde zichzelf om.
  2. **Rusland-oost-draai (2022→):** na de EU-embargo (aug 2022) draaide Russische kolen van de Baltische havens
     naar de Pacific (Vostochny/Vanino) en per overbelast spoor (Trans-Siberië/BAM) → China/India.
  3. **Mongolië-Gobi-corridor:** de landcorridor die tijdens de ban de Australische cokeskool in China verving.

## 6. Emergent plaatje-check (de lat bij oplevering)
1. **Grote binnenlandse blokken** in China (Shanxi/Ordos → Qinhuangdao → Guangdong; Ordos → Hebei-staal), India,
   VS en Rusland — dominant qua tonnage, dof `erts`/`product`, géén zeekruising.
2. Een dunnere maar helder oplichtende **zeehandelslaag** (`raffinaat`, volle kolenkleur) vanaf Indonesië/Australië/
   Zuid-Afrika/Rusland/Colombia/VS/Canada naar de Aziatische kust — met **China + India** als de grote sinks.
3. De **twee kolen** zichtbaar: dikke thermisch-bogen naar centrales (Indonesië→China, Australië-NSW→Japan) naast
   de cokeskool-bogen naar staalhubs (Australië-Qld→India-staal, Mongolië→China-staal).
4. De **Mongolië-Gobi-landcorridor** als enige nieuwe grensmarker; de Australische export **waaiert naar India/Japan/
   Korea** (het naspel van de ban), Russische kolen loopt **oostwaarts** naar de Pacific.
5. Géén enkel zee-knelpunt dat "oplicht" zoals bij olie — de boodschap is juist de **afwezigheid** van een trechter
   plus de **binnenlandsheid**.
6. Alles beweegt over **zee + land** (bulkschepen + spoor); géén luchtbogen (dat is goud/PGM).

## 7. Bronnen (peiljaar ±2023)
- **IEA — *Coal 2023* / *Coal Mid-Year Update 2024*:** wereldproductie/-vraag ~8,7 Gt (recordniveau), gedreven door
  China/India; zeehandel ~1,3-1,4 Gt (~15%); thermisch vs. metallurgisch ~7,3 : 1,1 Gt.
- **Energy Institute — *Statistical Review of World Energy 2024*** (voorheen BP): landenproductie/-consumptie —
  China ~50%, India, Indonesië, VS, Australië, Rusland, Zuid-Afrika, Kazachstan, Colombia.
- **USGS / nationale bronnen** voor mijn-locaties + Coal India, Adaro, BHP-Mitsubishi Alliance (BMA), Teck, Glencore,
  Thungela, Erdenes Tavan Tolgoi (Mongolië).
- **Havenautoriteiten:** Port of Newcastle (grootste kolen-exporthaven), Richards Bay Coal Terminal (RBCT),
  Dalrymple Bay/Hay Point, Qinhuangdao (Chinese benchmark).
- **Her-routeringen:** China-Australië-kolenban (okt 2020 – jan 2023, informeel; formeel opgeheven begin 2023);
  EU-kolenembargo op Rusland (aug 2022) → Pacific-heroriëntatie; Mongolië-China-grenshandel Tavan Tolgoi.

## 8. Open vragen / research-TODO (vóór of tijdens `coal.js`)
- [ ] Volumes zijn indicatief/afgerond; de exact-tonnages per bilaterale stroom (bv. hoeveel Indonesisch kool naar
  China vs. India) fluctueren jaar-op-jaar sterk (de ban/embargo maakten 2021-2023 atypisch) — als "illustratief" labelen.
- [ ] China-binnenlands is als 2 mijn-clusters + Qinhuangdao gemodelleerd; overweeg of een derde cluster (Shaanxi/Yulin)
  nodig is of dat de kaart in China dan te druk wordt.
- [ ] VS-binnenlandse burn: aparte `coal-mkt-us`-node toevoegen of impliciet laten (export loopt via Appalachia)?
  Beslissing bij de bouw — kleine node houdt de Powder-River-hop zinvol.
- [ ] Thermisch/cokeskool-splitsing draagt via `note`+`tension`; check bij de headless-render of het onderscheid
  visueel voldoende leest, of dat een lichte kleur-/hoogtenuance per stage nodig is (liever niet — stage-styling is generiek).
- [ ] De ~85% binnenlands is de kernboodschap; check dat de binnenlandse `erts`/`product`-hops dik genoeg zijn t.o.v.
  de zeelaag zodat de verhouding klopt (value-schaal).

---

## Build-handoff (naar de bouw-issues)
- **Nieuwe 14e grondstof (milestone M17)** — er is nog géén `data/coal.js`: aanmaken + `<script src="data/coal.js">`
  toevoegen aan `index.html` (na `silver.js`) + kolen-sanity-check in `build-standalone.py`. Dit is het
  concrete "anders dan het patroon" (zoals zilver de 11e was) → **apart issue** (plumbing).
- **Géén nieuwe marker-types** — `mine`/`port`/`market` bestaan; kolen gebruikt géén `refinery`/`recycler`/`exchange`/`cb`.
- **Géén nieuwe render-modus** — schip+land, hergebruikt zee-A\*/land-A\* + scheeps-voyages (koper/nikkel/zilver-patroon).
- **Eén nieuw chokepoint** — `grens-gashuunsukhait` (Mongolië-China-Gobi-grens) in een eigen gelabeld COAL-blok in
  `data/_chokepoints.js` (`kind:"grensovergang"`); alleen kolen verwijst ernaar. Dit is het grondstof-eigen "nieuwe element".
- **Géén optionele toggle-laag** — kolen heeft geen zinvol CB/beurs/recycling-equivalent (zie §3f). Houdt de engine
  schoon tijdens de parallelle grafiet-sessie (sectie J).
- **Co-locatie-check** — houd kolen-nodes van dezelfde stad ~30-45 km uit elkaar (Qinhuangdao-haven vs. de China-power-markt;
  India-mijn vs. India-steel-markt) zodat geen `degDist:0`-arc ontstaat.
- **`coal.js` (bouw-issue):** dit bestand 1-op-1 omzetten + `REGISTER` + toevoegen aan `index.html`-laadvolgorde.
