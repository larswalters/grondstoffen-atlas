# AIS-collector op de VPS — opzet en bediening (M28 · LAR-529)

De verzamelaar die het tracknet voedt. Draait permanent op de Hostinger-VPS
(`root@187.124.169.172`) naast de Hermes-gateway, als systemd-service.

> **⚠️ SINDS 2026-07-26 · WERELDABONNEMENT + CLASS B + LIVE GZIP.** De collector draait met
> `--wereld --live-gz` en op **vijf** berichtsoorten. De vensters hieronder filteren niets
> meer — ze zijn **health-banen** geworden (rapportage per corridor in `journalctl`).
>
> **Waarom wereld:** de héle aisstream-feed is gemeten **~9.800 berichten/min**, en 13
> vensters trokken daar al ~1.600 van. Bij die verhouding is een vensterlijst voortijdige
> zuinigheid die later een corridor kost die je niet meer kunt terughalen. Na de omzetting
> gemeten: **7.858 ber/min · ~850 MB/dag gegzipt · 80% van de berichten valt buiten de oude
> vensters.**
>
> **Waarom Class B:** `PositionReport` is **uitsluitend Class A** (msg 1/2/3). Class B komt
> binnen als `StandardClassBPositionReport` / `ExtendedClassBPositionReport` en zijn naam/type
> als `StaticDataReport` (msg 24). Gemeten: **9.655 ber/min en 8.089 unieke MMSI mét** tegen
> **4.465 en 4.269 zonder**. Per corridor: meren-seaway **+77%**, schelde-antw **+42%**,
> noord-dld +21%, Rijn +12–15% unieke schepen.
>
> **Waarom live gzip verplicht is:** ruw ~8,5 GB/dag tegen ~1 GB gegzipt bij ~22 GB vrij. De
> code **weigert `--wereld` zonder `--live-gz`**. gzip staat concatenatie toe, dus append over
> een herstart heen blijft geldig; een ongegzipt dagbestand van vóór de omzetting gaat naar
> `<dag>-a.jsonl` en wordt alsnog ingepakt.
>
> **Gevolg voor het beheer:** `haal_ais_data.py --opruimen` is onderhoud geworden, geen luxe —
> ~20 dagen marge, en de harde ondergrens stopt alléén het schrijven (de stream loopt door).

## Wat waar staat

| Pad | Wat |
|---|---|
| `/opt/ais-collector/collector.py` | de collector (bron: `v2/tools/ais_collector.py`) |
| `/opt/ais-collector/dekkingstest.py` | de go/no-go-test (bron: `v2/tools/ais_dekkingstest.py`) |
| `/opt/ais-collector/vensters.json` | de actieve corridors: `{naam: [zuid, west, noord, oost]}` |
| `/opt/ais-collector/aisstream.key` | de API-key, `chmod 600` — **nooit in git** |
| `/opt/ais-collector/venv/` | eigen venv (Ubuntu 24.04 is PEP 668, geen systeem-pip) |
| `/var/lib/ais-collector/ais/` | `YYYY-MM-DD.jsonl`, afgesloten dagen als `.jsonl.gz` |
| `/etc/systemd/system/ais-collector.service` | de unit |

## Bediening

```bash
ssh root@187.124.169.172 'systemctl start ais-collector'
```

```bash
ssh root@187.124.169.172 'systemctl status ais-collector; journalctl -u ais-collector -n 40 --no-pager'
```

De collector schrijft elke 5 minuten een `health`-regel met berichten/min en
unieke MMSI's per venster. Blijft die op nul staan terwijl de verbinding er wél
is, dan is dat een **dekkingsprobleem**, geen storing — precies het onderscheid
dat we bij de Yangtze willen kunnen maken.

Vensters wijzigen = `vensters.json` aanpassen + `systemctl restart ais-collector`.
De collector leest het bestand alleen bij start. Vensters die niets opleveren worden
in de health-regel compact als `stil: …` genoemd, zodat het signaal niet verdrinkt in
een rij nullen.

## De wereldwijde dekkingsmeting (2026-07-26, 1 uur, alles)

`v2/tools/ais_wereldscan.py` neemt één abonnement op de héle wereld **zonder berichtfilter**
en telt per rastercel; `analyseer_wereldscan.py` legt dat naast de 3.963 havens uit
`ports.json`. Zo meet je **hun** netwerk in plaats van onze abonnementskeuze.

**588.627 berichten · 41.812 unieke schepen · 4.207 cellen van 0,25°.** Hun walstations zenden
zichzelf uit als `BaseStationReport`, dus de stationskaart is gemeten in plaats van geloofd:

| regio | stations | posities | aandeel |
|---|---|---|---|
| Europa | **397** | 277.185 | **73,9%** |
| Noord-Amerika | 171 | 62.704 | 16,7% |
| Oceanië | 20 | 13.488 | 3,6% |
| Oost-Azië | 22 | 11.102 | 3,0% |
| Afrika/Midden-Oosten | 20 | 5.076 | 1,4% |
| Zuid-Amerika | 11 | 3.532 | 0,9% |
| **Zuid-Azië/Golf** | — | **163** | **0,0%** |

**Per haven — de vraag die telt.** Van de 3.963 havens heeft **1.402 (35,4%)** enig signaal en
**1.169 (29,5%) varend verkeer**; alleen daar valt een spoor náár de kade te bouwen (stilliggers
geven een ligplaats, geen route). **Nul havens met varend verkeer:** Chili (47) · Peru (28) ·
VAE (22) · Egypte (18) · Nigeria (18) · Roemenië (16) · Angola (12) · Iran (12) ·
Saoedi-Arabië (11) · Filipijnen (58) · Vietnam (21) · Tanzania (8) → het koperbeen, Hormuz,
Lobito, Constanța en Suez blijven op MARNET + density.

⚠️ **Eén uur is een momentopname.** "0 in dit uur" bewijst geen afwezigheid van dekking bij een
haven met weinig bewegingen; wat wél binnenkwam is hard bewijs van aanwezigheid. Voor de
extremen (Zuid-Azië + Golf samen 163 berichten) is toeval uitgesloten. ⚠️ En bij 30 km straal
delen buurhavens cellen — de ranglijst leest als regio, niet als haven.

## Gemeten dekking per corridor (2026-07-25, steekproeven van 3 min)

Voordat een venster aangaat is het één test waard: aisstream draait op een open
stationsnetwerk en de dekking is **geografisch grillig**, niet evenredig met
scheepvaartdrukte. Gemeten, in berichten/min:

| corridor | /min | oordeel |
|---|---|---|
| noord-dld (Elbe/Weser/NOK) | 353 | dicht |
| rijnmond | 427 | dicht |
| rijn-corridor (t/m Duisburg) | 234 | dicht |
| schelde-antw | 218 | dicht |
| japan-korea | 139 | goed |
| meren-seaway | 66 | goed |
| malakka | 24 | dun |
| donau-boven (Wenen–Boedapest) | 16 | dun |
| ohio-illinois | 5 | zeer dun |
| Straat Taiwan | 12 | dun |
| **mississippi (New Orleans–Memphis)** | **0** | geen dekking |
| **donau-onder (IJzeren Poort–Constanța)** | **0** | geen dekking |
| **shanghai-mond · ningbo-beilun · tongling** | **0** | geen dekking |
| gibraltar · panama | 1–2 | vrijwel niets |

**Twee dingen die dit vertelt.** Ten eerste: **het Chinese vasteland is ook aan de kust
donker.** Dat is met een positieve controle vastgesteld en niet uit een uitblijvend
signaal afgeleid — in dezelfde subscriptie leverden Busan 220 en Tokio-baai 71
berichten terwijl Shanghai op 0 stond, dus het is geen box-limiet of subscriptiefout.
De stippen die op de dekkingskaart bij China lijken te staan, zijn Korea, Japan en
Taiwan.

Ten tweede: **de dekking is sterk waar walstations dicht bij druk vaarwater staan en
zwak op open zee** (Gibraltar 2/min, Panama 1/min) — logisch bij een walbereik van
40–80 km. Dat bevestigt de taakverdeling van M28 langs een onafhankelijke weg: open
zee blijft MARNET, AIS levert kust/riviermonding/binnenwater/havens.

Altijd-stille vensters blijven bewust staan (`mississippi`, `shanghai-mond`,
`ningbo-beilun`, `tongling`): ze kosten niets en zijn de goedkoopste manier om te
merken dat er alsnog een station bijkomt.

## Schijf — de reden dat dit expliciet is

De VPS had bij opzet **22 GB vrij van 96 GB**. Daarom:

* afgesloten dagen worden automatisch gegzipt (ruwe JSONL comprimeert ~10×);
* onder **2 GB vrij** stopt de collector met schrijven en logt hij dat elke
  health-ronde — de stream loopt door, de schijf loopt niet vol.

Begin daarom klein: eerst één dag meten met een bescheiden venster, dán pas de
corridor uitbreiden. Een ruime box om de hele Rijn tot de Duitse grens is één
regel in `vensters.json`, maar wel een veelvoud aan volume.

## Waarom `ShipStaticData` er vanaf dag één bij zit

LAR-529 noemt dit als "later evt.", maar hetzelfde issue draagt het principe dat
verzamelde data **nooit opnieuw hoeft**. Het scheepstype (tanker/bulk/container)
komt uitsluitend uit `ShipStaticData` en is precies wat de terminal-typering in
LAR-531 nodig heeft. Het kost nauwelijks volume — één bericht per schip per ~6
minuten tegen één per 2–10 seconden voor posities. Alsnog uitzetten kan met
`--soorten PositionReport`.

## De pings-debuglaag (LAR-535)

De atlas draait op GitHub Pages en is statisch, dus de bol kan niet in de JSONL op
de VPS kijken. Daar zit een publicatie-stapje tussen:

1. **`ais_pings_publiceren.py`** (systemd-timer `ais-publiceren.timer`, elk kwartier)
   leest de laatste 24 uur, dunt uit en schrijft `pings.json` + een voorgecomprimeerde
   `pings.json.gz` naar `/var/lib/ais-collector/publiek/`.
2. **nginx** (container `ais-pings`, `/docker/ais-pings/`) serveert die map op
   `127.0.0.1:8088`, met `gzip_static on` en `Cache-Control: max-age=60`.
3. **Traefik** routeert `https://ais.187.124.169.172.nip.io` daarheen via de
   file-provider (`/docker/traefik/dynamic/ais-pings.yml`), met een Let's
   Encrypt-certificaat en CORS voor `larswalters.github.io` plus de
   localhost-dev-poorten.
4. **`v2/src/aispings.js`** fetcht dat bestand achter de HUD-knop *"AIS-pings (debug)"*
   en tekent de punten. Standaard uit; ververst zichzelf elke 5 minuten zolang de laag
   aan staat.

**Het uitdunnen is waar het interessant wordt.** Een schip aan de kade zendt ~30×
per uur vrijwel dezelfde positie. Op één gedeelde tijdkorrel eten die ligplaats-pings
het puntenbudget op, waarna de zelfregulering de korrel grover maakt en juist de
trackvorm van de vàrende schepen sneuvelt — het omgekeerde van wat je wilt zien.
Daarom hebben stilliggers (SOG < 0,5 kn) een eigen, veel grovere korrel (1 uur):
ze dragen alleen "hier is een ligplaats", en dat zegt één punt per uur net zo goed.
Effect gemeten op dezelfde data: **22.543 → 6.093 punten**, 506 → 157 KB.

Blijft het na uitdunnen boven `MAX_PUNTEN` (120.000), dan wordt de korrel voor
varende schepen vanzelf grover (1 → 2 → 5 → 10 → 30 min). Zo blijft het bestand
hanteerbaar als er drukkere vensters bij komen zonder dat iemand een limiet nastelt.

**Kleur zegt twee dingen tegelijk:** varend loopt wit → cyaan → donkerblauw met de
ouderdom van de ping (verse doorvaarten springen eruit), stilliggend is warm oranje
zonder tijdsverloop — dat zijn de ligplaatsen, en die zijn juist als *plek*
interessant (ze worden de terminal-nodes in LAR-531).

## De ruwe data naar de PC (LAR-530)

`v2/tools/haal_ais_data.py` trekt de afgesloten `.jsonl.gz`-dagen naar
`v2/build-cache/ais/tracks/`. Trekken in plaats van duwen, omdat de PC niet altijd
aan staat en geen inkomende toegang heeft; de bestaande SSH-sleutel doet het werk.
De dag van vandaag wordt overgeslagen (die groeit nog). Met `--opruimen` gaat een dag
ná een op grootte gecontroleerde kopie van de VPS af — nodig, want daar is maar
~22 GB vrij.

## Verwerking gebeurt hier NIET

De collector is bewust dom: ruwe berichten erin, ruwe JSONL eruit. Tracks bouwen,
varend/stilliggend knippen, opschonen en bundelen zit in de aparte
verwerkingsstap (LAR-530), zodat een verbeterd recept nooit nieuwe verzameltijd
kost.
