# AIS-collector op de VPS — opzet en bediening (M28 · LAR-529)

De verzamelaar die het tracknet voedt. Draait permanent op de Hostinger-VPS
(`root@187.124.169.172`) naast de Hermes-gateway, als systemd-service.

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
