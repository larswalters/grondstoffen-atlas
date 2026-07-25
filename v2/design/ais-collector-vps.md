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
De collector leest het bestand alleen bij start.

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

## Verwerking gebeurt hier NIET

De collector is bewust dom: ruwe berichten erin, ruwe JSONL eruit. Tracks bouwen,
varend/stilliggend knippen, opschonen en bundelen zit in de aparte
verwerkingsstap (LAR-530), zodat een verbeterd recept nooit nieuwe verzameltijd
kost.
