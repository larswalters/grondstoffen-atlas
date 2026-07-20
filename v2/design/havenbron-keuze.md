# Havenbron-keuze — weging na het bronnenpanel (2026-07-21)

*Context: `searoute`'s ports.geojson bleek een UN/LOCODE-locatielijst, geen havenlijst
(630 punten liggen >10 km van welk water dan ook — sinds `?v=039` van de kaart gefilterd,
zie `tools/toets_havens.py`). Twee gebreken blijven: posities zijn plaatscentroïdes, en er
is geen attribuut dat een vrachthaven van een jachthaven scheidt of spooraansluiting geeft.
Vijf zoekhoeken → 79 kandidaten → 8 dossiers volledig uitgezocht (5 dossiers, waaronder
World Port Index, sneuvelden op een sessielimiet — WPI hieronder deels zelf geverifieerd).*

## De uitkomst in één zin

**Er bestaat geen wereldwijde bron die alles levert — de rol wordt verdeeld:** één wereldwijde
verrijkings-/filterbron (WPI, te verifiëren), regionale positie-correctie waar de licentie het
toestaat (EMODnet), redactionele meetlatten voor de aangewezen lijst (UNECE Blue Book, USACE),
en `ports.json` blijft het routeer-skelet totdat `knooppunten.json` (overslag-ontwerp §3a) de
identiteit draagt.

## Rolverdeling

| bron | rol | waarom | status |
|---|---|---|---|
| **NGA World Port Index (Pub 150)** | wereldwijde verrijking + vrachtfilter | "over 100 key characteristics of thousands of ports" (zelf gelezen op msi.nga.mil via de Browser-pane); VS-overheidswerk → naar verwachting publiek domein; officiële REST-API bestaat (`msi.nga.mil/api/swagger-ui.html`). Naar verwachting o.a. havengrootte + spoor-veld — **dat is precies eis 2+3** | ⚠️ dossier gesneuveld; velden/licentie/download **verifiëren vóór gebruik** (curl kreeg 403, Browser-pane werkt — zelfde patroon als UNECE) |
| **EMODnet Main Ports** (CC-BY 4.0, geverifieerd) | positie-correctie Europa | posities objectief getoetst: **mediaan 0,60 km van de kust** (zelfde toets als die searoute onderuit haalde); LOCODE-gekoppeld via `port_id`; 946 punten, open WFS | bruikbaar; alleen-Europa, geen spoorveld |
| **UNECE Blue Book E-ports** | redactionele meetlat voor de aangewezen lijst | **`RAILACCESS`-veld bestaat echt** (Available 259 · Not available 94 · No information 79 van 432) + `CARGOHACA`-tonnageklasse — exact wat de knooppunten-redactie nodig heeft voor EU-binnenhavens | ⚠️ **licentie verbiedt herdistributie** → waarden mogen een redactioneel besluit onderbouwen, de data zelf mag niet mee in de repo |
| **USACE Port Statistical Areas** (370 polygonen) + **NTAD** (publiek domein) | VS-verrijking | echte havengebied-polygonen incl. rivierhavens (Memphis, Cincinnati); NTAD-terminals op Street-View-niveau geplaatst | bruikbaar, alleen-VS, geen LOCODE |
| **UN/LOCODE CSV-mirror** (ODC-PDDL) | sleutelregister, meer niet | coördinaten zijn hele boogminuten (~1,85 km resolutie — kade-niveau principieel onbereikbaar); functiecode spoor onbetrouwbaar | alleen als koppeltabel |
| NOAA ENC · UKHO | **afgewezen** | VS-only en 73% jachthavens · resp. alleen UK-zeegrenzen, geen havens | — |

## Wat dit betekent voor de bouwvolgorde

1. **Niets hiervan blokkeert LAR-520 (stitchen) of de overslag-router** — die draaien op de
   bestaande `ports.json` + het watervlak-filter.
2. **Eerste concrete actie** (klein, eigen sessie): WPI verifiëren via de Browser-pane —
   licentietekst, veldenlijst (spoor? havengrootte? LOCODE?), downloadvorm. Slaagt dat, dan is
   het vervolg: WPI-attributen op LOCODE aan `ports.json` hangen → de mintgroene kandidaten op
   de kaart worden "vrachthaven mét spoor" i.p.v. "raakt twee netten", en de jachthaven-pier
   verdwijnt uit de kandidaten.
3. **De aangewezen `knooppunten.json` wordt met de hand geredigeerd** (20–40 entries eerst),
   met WPI/UNECE/USACE als bewijs naast elke entry — de machine meet, de redacteur oordeelt.

## Open verificaties (uit de gesneuvelde weerleg-ronde)

- WPI: licentie + velden + download (zie boven) — **hoogste prioriteit**.
- EMODnet: CC-BY-attributietekst in de HUD zodra data meereist (naast de bestaande OSM/Esri-regels).
- NTAD/USACE-licenties zijn wél dubbel gelezen (publiek domein, letterlijk geciteerd in de dossiers).
