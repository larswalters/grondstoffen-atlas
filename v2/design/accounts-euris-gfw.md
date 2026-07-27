# Registratiebrief — EuRIS en Global Fishing Watch (M28)

*Opgesteld 2026-07-27. Elke HTTP-status, elk aantal en elke veldwaarde hieronder is
**zelf gemeten** met echte requests zónder account, op die datum. Documentatie-uitspraken
staan expliciet als citaat gemarkeerd. Waar docs en meting elkaar tegenspreken staat dat er
bij, mét de gemeten waarde als winnaar.*

**Voor Lars: jouw actie is twee accounts + twee tokens in één `.env`.** ~3 min EuRIS, ~2 min
GFW. **Maar lees eerst het kader hieronder — voor EuRIS is de uitkomst niet wat we hoopten,
en tegelijk beter dan verwacht op een ander punt.**

---

## Het kader vooraf — dit verandert de opdracht

### EuRIS, antwoord 1: een account levert GEEN tracks van derden. Definitief.

De openstaande vraag in `ais-bronnen-wereldwijd.md` was: *"⚠️ GDPR-clausule — of tracks van
derden echt terugkomen is onbevestigd tot we een account testen."*

**Die vraag is beantwoord, en het antwoord is nee — en het account is niet de reden.** De
Tracks-API v3 heeft in totaal **vier** endpoints, en geen daarvan levert een historische lijn
van een schip van iemand anders:

| endpoint | auth | wat het teruggeeft | gemeten |
|---|---|---|---|
| `GET /api/v3/tracks/bounding-box` | **nee** | momentopname van álle schepen in een bbox | **200 OK** |
| `GET /api/v3/tracks/fairway-section` | nee | idem, gefilterd op vaarwegsectie + hectometer | 200, maar **lat/lon = 0.0** |
| `GET /api/v3/tracks/followed` | ja | *"followed tracks for the current user"* | — |
| `GET /api/v3/tracks/owned` | ja | *"owned tracks for the current user"* | — |

De twee endpoints die een token eisen zijn dus precies de twee die **jouw eigen schepen**
teruggeven. Lars bezit geen binnenvaartschip, dus die zijn per definitie leeg. En cruciaal:
alle vier geven volgens de docs *hetzelfde objecttype* terug — een **actuele positie**, geen
puntenreeks. **Er is in de v3-API geen historie-endpoint.**

Het oude `GET /api/AISTracks/GetTrack` (waar de vorige ronde op hoopte) is een v1-restant:
swagger zegt `auth=nee` maar hij geeft gemeten **401**, en zijn responseschema is leeg
(`{"type":"object"}`). Ik zou er niet op rekenen.

**De privacy-kant, ter volledigheid.** De privacyklasse is een instelling van de **schipper**,
niet van jouw accountniveau. EuRIS' eigen documentatie, letterlijk: *"The default privacy
class is 2, that means everyone will have access to data of privacy class 1 and 2 without
requesting for specific insights."* MMSI, naam, roepnaam, ENI, IMO, scheepstype en
vaarrichting staan alle zeven op **minimum klasse 3**. Geen token verhoogt de klasse van
andermans schip. Gemeten over vijf vensters:

| venster | tracks | varend | MMSI ≠ 0 | scheepstype bekend |
|---|---|---|---|---|
| Donau-onder (RO/BG) | 197 | 45 | 8 | 8 |
| Donau-midden (HU/RS) | 83 | 9 | 2 | 2 |
| Donau-boven (AT/SK/HU) | 246 | 40 | 2 | 2 |
| Rijn Duisburg–Keulen | 216 | 65 | **0** | 0 |
| Rijnmond/Waal NL | 1.100 | 189 | 2 | 2 |
| **totaal** | **1.842** | **348** | **14 (0,8 %)** | 14 |

Op de hele Donau: **526 tracks, 94 varend, 12 met MMSI (2,3 %)**.

**Conclusie: EuRIS is bruikbaar als één ding — een POLLER op het anonieme
bounding-box-endpoint.** Wij bouwen de tracks zelf door elke paar minuten een momentopname te
nemen en te stikken op `trackId`. Het account koopt daar precies één ding voor: een **hogere
rate limit**. Dat is nuttig, niet blokkerend.

### EuRIS, antwoord 2 — de onverwachte vondst: de VAARWEG zelf ligt open

Zoekend naar de tracks stuitte ik op iets dat voor de atlas waarschijnlijk meer waard is. EuRIS
heeft naast de API een **"emulated ArcGIS"**-laag, en drie feature-services daarvan zijn
**volledig anoniem op te halen, mét geometrie**:

| laag | features | geometrie | inhoud | compleet? |
|---|---|---|---|---|
| `fairways/0` | **7.122** | polyline | **CEMT-klasse · max diepgang · max lengte · max breedte** per vaarwegsectie | ja |
| `terminals/0` | **3.969** | punt | ISRS-code · naam · operator · **goederensoort** | ja |
| `berths/0` | **5.841** | polyline (kadelijn) | naam · max diepgang · terminal-verwijzing · oever | ja |

"Compleet" is gemeten, niet aangenomen: `exceededTransferLimit = False` en een onafhankelijke
`returnIdsOnly`-telling geeft exact dezelfde aantallen (7.122 / 3.969 / 5.841).

**En het haalt de lengtetoets.** In de idioom van dit project — lengte tegen een bekende route,
niet puntafstand:

| toets | secties | gemeten | verwacht | afwijking |
|---|---|---|---|---|
| **Donau** (Kelheim rkm 2414 → Sulina rkm 0) | 273 | **2.471,6 km** | 2.414 km | **+2,4 %** |
| Rijn (Bazel → Hoek van Holland) | 322 | 1.321,1 km | ~1.233 km | +7,1 % ⚠️ |

De Donau-toets is scherp en geslaagd: +2,4 % ligt binnen wat dit project routinematig accepteert
(Main +1,9 %, Copperbelt→Durban +2,3 %), en de overschrijding is verklaarbaar — de 273 secties
bevatten ook de delta-armen (Sulina/Chilia) en het Donau-Zwarte Zeekanaal. ⚠️ De Rijn-toets is
**niet conclusief**, niet omdat de data slecht is maar omdat mijn referentiegetal dubbelzinnig
is (welke delta-armen tel je mee?). Niet gebruiken als bewijs in beide richtingen.

**En de samenhang is getoetst, want kilometers zijn geen graaf.** Op exact gedeelde uiteinden
valt de Donau (303 secties bij ruimere naammatch, 2.807 km) uiteen in **8 componenten**:
177 secties/1.600,8 km · 55/516,4 · 18/314,3 · 34/199,3 · 14/170,4 · en drie slivers van ~1–4 km.
De grootste is 57 % van het geheel. **Maar de gaten zijn nietig:** van de 76 componentparen
binnen 5 km zijn de kleinste **3 m · 8 m · 13 m · 13 m · 71 m · 75 m …**, met **12 paren onder
250 m** en **50 onder 2 km**.

Dat is exact de **LAR-520-klasse**: de bron heeft de geometrie maar deelt de junctie-vertex niet
(zoals bij Tongling het 107 m-gaatje, en zoals OSM's riviernet). Dit project heeft daar de
machinerie al voor — de twee-traps heal in `binnenwaternet()` (tier-1 ≤250 m cross-component,
tier-2 ≤2 km met richtingsguard). **Er is dus geen nieuw recept nodig om de Donau uit deze laag
sluitend te krijgen**, alleen de bestaande heal erop.

Waarom dit de opdracht raakt: **`CEMT` is gevuld op 7.105/7.122 (100 %) en `MDRAUGHTCM` op
4.831/7.122 (68 %)** — max lengte en breedte op 7.120/7.122. Dat is exact het vier-maten-veld
dat LAR-514 heeft ontworpen, per sectie, van de **vaarwegbeheerder zelf** (`WWAUTHORIT` staat
erbij). Het besluit van 2026-07-20 was: *"CEMT-presets vullen ALLEEN lengte en breedte;
diepgang uitsluitend uit een echte meting."* `MDRAUGHTCM` per sectie **is** die echte meting.
Donau-secties: CEMT VII (154×), VIb (58×), VIc (37×), Vb (16×), VIa (6×), Va (2×); diepgang
250–550 cm.

⚠️ **Dekking is niet uniform — dit is de belangrijkste beperking.** `fairways` dekt 12 landen
maar zwaar westelijk: NL 4.035 · FR 1.374 · BE 637 · DE 625 · RO 180 · CZ 115 · AT 66 · RS 34 ·
HU 29 · SK 17 · HR 9 · LU 1. **Bulgarije ontbreekt volledig in `fairways`** (wel 41 terminals en
143 berths). En `berths` mist **Nederland en Duitsland helemaal** (FR 2.907 · BE 2.382 · CZ 280 ·
BG 143 · RO 94 · RS 18 · HR 17). Reken dus niet op een homogeen Europees bestand.

**Gemeten dood spoor, niet opnieuw proberen:** `locks`, `bridges`, `berthlines`, `berthareas`,
`risindex`, `TracksV2`, `lockstatus`, `bridgestatus` geven alle **0 features**, óók zonder
bbox-filter. De laag bestáát in de API maar levert anoniem niets. (Sluizen en bruggen zouden de
doorvaarthoogte hebben gedragen — die blijft dus onbekend, precies zoals LAR-514 al aannam.)

De drie bestanden staan al op schijf, in `v2/build-cache/ais/euris/` (gitignored):
`euris_fairways.json` 8,6 MB · `euris_terminals.json` 3,4 MB · `euris_berths.json` 5,5 MB.
Eén keer gehaald, dus een rijkere vraag kost later geen nieuwe download — zelfde regel als de
collector en `haal_marinecadastre.py`.

### GFW: harde poort, geen twijfel

`4wings/report`, `/v3/events` **en** `/v3/datasets` geven zonder token alle drie
**401 `{"error":"invalid token"}`**. Er is geen anonieme weg naar binnen, ook niet om de
datasetlijst te zien. Registratie is self-service, geen goedkeuringsronde.

---

## BRON 1 — EuRIS

### 1. Wat moet je aanmaken

**Eén gewoon EuRIS-portaalaccount.** Geen ontwikkelaarsaccount, geen organisatie-aanvraag,
geen goedkeuring.

Registratiepagina (gemeten **HTTP 200**, formulier in het Nederlands):

```
https://authgw.eurisportal.eu/realms/euris/protocol/openid-connect/registrations?client_id=account&response_type=code
```

Of gewoon: <https://www.eurisportal.eu> → rechtsboven inloggen → "Registreer".

Gevraagde velden — **vijf, meer niet**: gebruikersnaam · wachtwoord (+ bevestiging) ·
e-mailadres · voornaam · achternaam.

**Er is géén organisatie-veld en géén doel-/gebruiksveld.** De vraag "wat vul ik in bij doel"
is bij EuRIS niet aan de orde; er valt niets te verklaren over het niet-commerciële karakter
van de atlas.

Daarna het token, uit EuRIS' eigen *Getting started* (letterlijk geciteerd):

1. *"Log in to https://www.eurisportal.eu (top right corner)"*
2. *"Go to top right corner Username > My Account > API Tokens"*
3. *"Click Add"*
4. *"Choose a name and expiry date for your token"*

> **⚠️ *"Created tokens are only shown once after creation and will not be stored in EuRIS, be
> sure to save them."*** Direct in het `.env`-bestand plakken. Tokens zijn geldig tot maximaal
> **één jaar**, zijn in te trekken, en je krijgt bericht vóór het verlopen.

Naamsuggestie: `grondstoffen-atlas`.

### 2. Welke toestemmingen / scopes

**Geen.** Bij een Personal Access Token kies je alleen naam en vervaldatum — er is geen
scope-keuzescherm.

> **⚠️ De OAuth2-documentatie in de Swagger-specs is verouderd — niet volgen.** Elke spec
> (`AisTracks`, `Fairway_v2`, `Tracks_v3`, …) noemt een client-credentials-flow op
> `https://authgw.eurisportal.eu/realms/connect/token` met scope `visuris.full_access`.
> Gemeten: die URL geeft **HTTP 404 `{"error":"Realm does not exist"}`**. Het echte realm heet
> **`euris`**, en `visuris.full_access` komt **niet** voor in de 14 scopes van het levende
> discovery-document. EuRIS' eigen docs bevelen expliciet het PAT-systeem aan. Dus: **PAT, geen
> OAuth2.**
>
> Wél levend, mocht een client-credentials-flow ooit nodig zijn: issuer
> `https://authgw.eurisportal.eu/realms/euris`, token-endpoint
> `.../protocol/openid-connect/token`.

Het token gaat mee als header — letterlijk uit de docs:
`Authorization: Bearer YOUR_TOKEN_HERE`.

Volgens *Getting started* eisen maar twee API's authenticatie: *"Electronic messages"* en
*"Tracks"* (en van Tracks alleen `followed`/`owned`, zie het kader).

### 3. Waar komt de credential terecht

Bestaande projectconventie: secrets in een `.env` **buiten** het repo, zoals
`~/.claude/pinecone_memory.env`. **Eén bestand voor beide bronnen:**

**Pad:** `C:\Users\lars\.claude\grondstoffen-atlas.env`

```dotenv
# Grondstoffen Atlas — API-tokens. NOOIT in git.
EURIS_API_TOKEN=<plak hier het EuRIS Personal Access Token>
GFW_API_TOKEN=<plak hier het Global Fishing Watch API-token>
```

Zo lezen wij hem — geen extra dependency:

```python
import os
from pathlib import Path

def laad_env(pad=Path.home() / ".claude" / "grondstoffen-atlas.env"):
    """Leest KEY=VALUE-regels. Bewust buiten het repo: een token hoort niet in git."""
    if not pad.exists():
        raise SystemExit(f"ontbreekt: {pad} — zie v2/design/accounts-euris-gfw.md")
    for regel in pad.read_text(encoding="utf-8").splitlines():
        regel = regel.strip()
        if regel and not regel.startswith("#") and "=" in regel:
            k, v = regel.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

laad_env()
TOKEN = os.environ["EURIS_API_TOKEN"]
```

Het repo bevat hier **niets** van: geen token, geen voorbeeldwaarde, geen `.env` in `v2/`.

### 4. De testcall

Twee dingen te toetsen. De eerste werkt nu al zonder token (dat is de nulmeting), de tweede
bewijst dat je token leeft.

**Stap A — de anonieme basis (werkt nu al, gemeten 200):**

```bash
curl -s "https://www.eurisportal.eu/api/v3/tracks/bounding-box?minLon=22.5&minLat=43.6&maxLon=28.8&maxLat=45.4&pageSize=5"
```

**Stap B — bewijst dat het token werkt.** `followed` is de goedkoopste: hij eist auth en heeft
geen quota-kosten.

```bash
curl -s -o /dev/null -w "%{http_code}\n" \
  "https://www.eurisportal.eu/api/v3/tracks/followed" \
  -H "Authorization: Bearer $EURIS_API_TOKEN" -H "Accept: application/json"
```

**Geslaagd = `200`** (met vermoedelijk een **lege lijst**, want je volgt geen schepen — dat is
de verwachte en juiste uitkomst, geen fout). Zonder token gemeten: **401**.

**Stap C — de GDPR-toets, kant-en-klaar.** Draai mét en zónder token en vergelijk. Hij telt
unieke MMSI en de privacyklassen voor een venster met aantoonbaar veel verkeer:

```python
# toets_euris.py — komen er tracks van DERDEN terug, met identiteit?
import collections, json, os, urllib.request

TOKEN = os.environ.get("EURIS_API_TOKEN")   # leeg = anonieme nulmeting
VENSTER = (22.5, 43.6, 28.8, 45.4)          # Donau-onder (RO/BG)

def haal(skip=0):
    a, b, c, d = VENSTER
    u = ("https://www.eurisportal.eu/api/v3/tracks/bounding-box"
         f"?minLon={a}&minLat={b}&maxLon={c}&maxLat={d}&pageSize=100&skip={skip}")
    r = urllib.request.Request(u, headers={"User-Agent": "grondstoffen-atlas"})
    if TOKEN:
        r.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(r, timeout=60) as resp:
        j = json.loads(resp.read().decode())
    return j["items"] if isinstance(j, dict) else j

items, skip = [], 0
while True:                       # pageSize is HARD gecapt op 100 -> pagineren
    blok = haal(skip)
    items += blok
    if len(blok) < 100:
        break
    skip += 100

print(f"token: {'JA' if TOKEN else 'nee'}   tracks: {len(items)}")
print(f"varend:            {sum(1 for x in items if x.get('isMoving'))}")
print(f"unieke MMSI:       {len({x['mmsi'] for x in items if x.get('mmsi')})}")
print(f"unieke trackId:    {len({x['trackId'] for x in items})}")
print(f"scheepstype bekend:{sum(1 for x in items if (x.get('aisShipType') or -1) != -1)}")
print(f"privacyklassen:    {dict(collections.Counter(x.get('privacyClass') for x in items))}")
```

**Gemeten nulmeting zónder token (vergelijk hiertegen):**
197 tracks · 45 varend · **8 unieke MMSI** · 197 unieke trackId · 8 met scheepstype ·
privacyklassen `{2: 189, 6: 7, 3: 1}`.

**Hoe je de uitslag leest:**
- Blijft "unieke MMSI" rond 8 van 197 → **bevestigd**, identiteit blijft afgeschermd. Dit is de
  verwachte uitkomst en die verandert niets aan het plan.
- Springt "unieke MMSI" naar ~197 → de privacy-documentatie klopt niet en EuRIS wordt meteen een
  volwaardige tweede collector-bron. Onwaarschijnlijk.

### 5. Wat de uitslag betekent voor de atlas

**De beslisvraag is verschoven.** Niet meer *"komt er identiteit terug?"* (nee, definitief, en
niet vanwege je account) maar: ***"blijft `trackId` lang genoeg stabiel om een doorvaart aan
elkaar te stikken?"***

Dat is de kern, want `bouw_tracks.py` heeft geen MMSI nodig — het heeft een **groepeersleutel**
nodig. En de documentatie zelf noemt die sleutel verdacht: `TrackId` heeft minimum klasse
**"1/3"** met de toelichting *"Id of the ship (typically MMSI number). **When privacy class < 3
IncrementalID is returned in this field**"*, en `IncrementalID` is gedocumenteerd als een
***"Randomized numeric id of the ship"***. Bij 99 % van de schepen krijgen we dus een
gerandomiseerd nummer, niet de MMSI.

**Gemeten stabiliteit** (Donau-onder, anonieme snapshots elke 4 min, basis = 197 trackId's):

| verstreken | tracks | nog aanwezig | % | **nieuw t.o.v. basis** |
|---|---|---|---|---|
| 4,0 min | 196 | 196 | 99,5 % | **0** |
| 8,0 min | 196 | 196 | 99,5 % | **0** |
| 12,1 min | 194 | 194 | 98,5 % | **0** |
| 16,1 min | 195 | 195 | 99,0 % | **0** |

**De rechterkolom is de beslissende meting, niet de derde.** Bij herrandomisatie zou een oud id
verdwijnen *en een nieuw id opduiken* — het totaal blijft dan gelijk terwijl de identiteiten
wisselen. Gemeten: gemiddeld 0,8 weg en 0,2 nieuw per snapshot, en **nul** nieuwe id's ten
opzichte van de basis over de hele reeks. Dat is het patroon van *"een schip vaart het venster
uit"*, niet van hernummering. Controle dat het echte schepen zijn: van de 195 blijvers bewogen
er 58 meer dan 50 m in 16 min (mediaan 0,00 km — de meesten liggen stil, max 4,55 km).

⚠️ **Wat dit niet uitsluit:** een periodieke herrandomisatie op een langere cyclus (per etmaal,
per sessie). Daarvoor is een poller nodig die een nacht draait; 16 minuten kan het niet
beantwoorden. Dit blijft het echte risico voor EuRIS-als-trackbron.

**Wat er overblijft als `trackId` wél periodiek herrandomiseert:** dan levert EuRIS geen tracks
maar wel een **dichtheidswolk** van echte posities op de Donau — nog altijd beter dan het
World-Bank-raster (binnenwater, 0,0001°-precisie). De geul is er dan uit te halen zoals in M27.

**En los daarvan, onafhankelijk van de hele trackId-vraag:** de vaarweglaag uit het kader dicht
het Donau-gat **geometrisch** al — mét CEMT-klasse en diepgang per sectie, en die is niet
afhankelijk van een account of van scheepsverkeer. Voor een routeergraaf (wat de atlas ís) is
dat vermoedelijk het grotere deel van de winst; de tracks voegen daar drukte en werkelijk
gevaren lijnen aan toe.

Wat we in geen geval uit EuRIS krijgen: **scheepstype** (klasse 3) → géén cargo/tanker-filter.
Op de Donau is dat minder erg dan op zee, want daar is vrijwel alles vracht.

### 6. Wat er daarna gebeurt (onze kant)

1. **Nu al, zonder dat jij iets doet** — de vaarweg-, terminal- en berth-laag zijn binnen
   (build-cache). Volgende stap: `fairways` omzetten naar het vaarwegformaat van de atlas en de
   Donau-secties als graaf inhangen, mét `CEMT`/`MDRAUGHTCM`/`MLENGTHCM`/`MWIDTHCM` als het
   vier-maten-veld van LAR-514.
2. **`trackId`-stabiliteit over een etmaal** meten. Dat beslist tracks-vs-dichtheidswolk, kan
   **zonder account**, en is de enige echt openstaande vraag. Recept (draai dit een nacht en
   analyseer daarna op "hoeveel NIEUWE id's per snapshot" — dat is de discriminant, niet het
   totaal):

   ```python
   # poll_trackid.py — draai een nacht: python poll_trackid.py > poll.log 2>&1 &
   import json, time, urllib.request
   from datetime import datetime, timezone

   VENSTER = (22.5, 43.6, 28.8, 45.4)   # Donau-onder
   INTERVAL, DUUR = 240, 24 * 3600      # elke 4 min, 24 uur

   def snapshot():
       items, skip = [], 0
       while True:
           a, b, c, d = VENSTER
           u = ("https://www.eurisportal.eu/api/v3/tracks/bounding-box"
                f"?minLon={a}&minLat={b}&maxLon={c}&maxLat={d}"
                f"&pageSize=100&skip={skip}")
           r = urllib.request.Request(u, headers={"User-Agent": "grondstoffen-atlas"})
           with urllib.request.urlopen(r, timeout=60) as resp:
               j = json.loads(resp.read().decode())
           blok = j["items"] if isinstance(j, dict) else j
           items += blok
           if len(blok) < 100 or skip > 900:
               return items
           skip += 100

   begon = time.monotonic()
   with open("trackid_snapshots.jsonl", "a", encoding="utf-8") as fh:
       while time.monotonic() - begon < DUUR:
           try:
               it = snapshot()
               fh.write(json.dumps({"t": datetime.now(timezone.utc).isoformat(),
                                    "n": len(it),
                                    "ids": [x["trackId"] for x in it]}) + "\n")
               fh.flush()
           except Exception as e:
               fh.write(json.dumps({"t": datetime.now(timezone.utc).isoformat(),
                                    "fout": repr(e)}) + "\n"); fh.flush()
           time.sleep(INTERVAL)
   ```

   **Leesregel:** blijft "nieuw t.o.v. basis" laag terwijl het totaal ~gelijk blijft → `trackId`
   is stabiel en EuRIS is een track-bron. Springt "nieuw" omhoog bij een gelijk totaal → er is
   hernummerd en EuRIS wordt een dichtheidsbron.
3. Zodra het token er is: `followed` één keer aanroepen (rooktest) en de nieuwe rate limit
   nameten — dat is het enige dat het token feitelijk toevoegt.
4. Dan `haal_euris.py` bouwen — spiegelbeeld van `haal_marinecadastre.py`: pollt de bounding-box
   over de Donau-corridor, schrijft **collector-JSONL in het aisstream-schema**, hervatbaar,
   0-byte-val op respons**grootte**.
5. **Twee omzet-valkuilen die ik heb gemeten** (niet aangenomen — zie §bijlage): het tijdstempel
   moet worden herschreven, en de snelheid staat in **km/u**, niet knopen.
6. Rate limit 100 req/min per IP is ruim zat: de hele Donau in ~8 vensters elke 2 min = 4 req/min.
7. Attributie in de HUD (verplicht):
   `API/Service [naam] incorporated from EuRIS (eurisportal.eu)`.

---

## BRON 2 — Global Fishing Watch

### 1. Wat moet je aanmaken

**Een gratis GFW-account**, daarna zelf een API-token. Self-service, geen wachttijd.

Registratiepagina (gemeten **HTTP 200**):

```
https://gateway.api.globalfishingwatch.org/v3/auth/registration?locale=en&cohort=
```

(Ook via <https://globalfishingwatch.org/our-apis/tokens> → inlogpagina → "Sign up". Inloggen
met Google kan ook.) Het formulier meldt dat het account ook geldt voor *"the Map, Marine
Manager, Vessel Viewer, API Portal and Data Download Portal"*.

Velden op **pagina 1 van 2** — gemeten door de pagina te lezen, niets ingevuld:

| veld | wat erin hoort voor dit project |
|---|---|
| First name / Last name | |
| Email | |
| Country | Netherlands |
| **Organization** | verplicht vrij tekstveld; er is géén "particulier"-optie. `Persoonlijk project — Grondstoffen Atlas` of je eigen naam dekt het |
| **Organization category** | keuze uit GOVERNMENT / INTERGOVERNMENTAL ORGANIZATION / NONPROFIT, NGO / SCIENCE AND RESEARCH / MEDIA / PRIVATE SECTOR / **OTHER**. Voor een niet-commercieel persoonlijk kaartproject is **OTHER** het eerlijkst; *SCIENCE AND RESEARCH* is verdedigbaar maar suggereert een instelling |
| Password + confirm | |

⚠️ **Pagina 2 heb ik niet geopend** — daarvoor moet je het formulier doorlopen, en dat is jouw
stap. Verwacht daar de akkoordverklaring met de voorwaarden.

Daarna: inloggen op <https://globalfishingwatch.org/our-apis/tokens> en een token aanmaken.

> **⚠️ Bij het doel/organisatie-veld:** GFW's voorwaarden staan **uitsluitend niet-commercieel
> gebruik** toe (CC BY-NC 4.0). De atlas is een persoonlijk, niet-commercieel kaartproject en
> valt daar netjes binnen. Beschrijf het ook zo — niet mooier.

### 2. Welke toestemmingen / scopes / datasets

**Geen scopes, en geen dataset-keuze bij het aanmaken**: één token dekt de publieke
`public-global-*`-datasets; de dataset kies je per request. Wat je wél accepteert zijn de
voorwaarden (niet-commercieel + attributie).

⚠️ Dat "één token dekt alles" komt **uit de documentatie, niet uit een meting** — ik kon het
niet verifiëren omdat óók `/v3/datasets` zonder token 401 geeft. Eerste echte controle is dus
de rooktest hieronder.

Grenzen volgens de documentatie (niet zelf te meten zonder token):
- **50.000 requests per dag** en **1.500.000 per maand**, per **gebruiker** (niet per token)
- maximaal **5 tokens** per gebruiker; ze tellen bij elkaar op
- overschrijding → **429**; dag blokkeert 24 u, maand 30 dagen
- standaard **één gelijktijdig 4wings-rapport** per token
- responseheaders dragen de teller (`x-ratelimit-daily-limit-requests` e.a.)

Ruim zat: wij hebben enkele tientallen requests per corridor nodig.

### 3. Waar komt de credential terecht

Zelfde bestand als EuRIS: `C:\Users\lars\.claude\grondstoffen-atlas.env`, variabele
**`GFW_API_TOKEN`**. Zie het codeblok bij EuRIS §3 — `laad_env()` leest beide.

### 4. De testcall

**Rooktest eerst** — één regel, geen rapport-quota:

```bash
curl -s -o /dev/null -w "%{http_code}\n" \
  -G "https://gateway.api.globalfishingwatch.org/v3/events" \
  -H "Authorization: Bearer $GFW_API_TOKEN" \
  --data-urlencode "limit=1" --data-urlencode "offset=0" \
  --data-urlencode "datasets[0]=public-global-port-visits-events:latest"
```

**`200` = token werkt.** Zonder token gemeten: **401 `{"error":"invalid token"}`**.

**Dan het echte werk** — het presence-raster met cargo-filter, als **POST** met een eigen
polygoon (dat is de vorm die wij gaan gebruiken; de GET-variant eist een `region-id` uit GFW's
eigen regio-datasets en bestaat vooral voor caching):

```bash
curl -s -X POST "https://gateway.api.globalfishingwatch.org/v3/4wings/report?datasets[0]=public-global-presence:latest&date-range=2025-06-01T00:00:00.000Z,2025-07-01T00:00:00.000Z&spatial-resolution=HIGH&temporal-resolution=ENTIRE&format=CSV" \
  -H "Authorization: Bearer $GFW_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"geojson":{"type":"Polygon","coordinates":[[[-70.6,-21.0],[-70.0,-21.0],[-70.0,-23.8],[-70.6,-23.8],[-70.6,-21.0]]]}}' \
  -o gfw_presence.zip
```

(De polygoon hierboven is Patache–Antofagasta, de voorgestelde pilotcorridor.)

**Geslaagd = HTTP 200 en een ZIP** (caveat-bestand + het resultaat). **Controleer op
bestandsgrootte, niet op status** — zelfde 0-byte-val als elders in dit project.

**Twee valkuilen uit hun documentatie:**
- **429** bij een tweede gelijktijdig rapport → rapporten strikt serieel draaien.
- **524** als een rapport >100 s duurt; het rapport is dan **niet** weg maar op te halen via het
  `last-report`-endpoint. Bouw dat meteen in, geen retry-lus.

### 5. Wat de uitslag betekent voor de atlas

- **`public-global-presence:latest`** — vaartuigaanwezigheid uit AIS, **één positie per uur per
  schip**, 2012 → 96 uur geleden, wereldwijd, filterbaar op `vessel_type='cargo'` (ook `flag` en
  snelheidsband). `spatial-resolution=HIGH` = 0,01° ≈ 1 km. Dit is de aanvulling voor de
  corridors waar de collector nul dekking meet: Chili (het koperbeen), Hormuz, Lobito, Suez,
  Constanța.
  **⚠️ CORRECTIE 2026-07-27, gemeten mét het echte token — dit is beter dan hierboven stond.**
  De oorspronkelijke tekst zei *"dit zijn geen tracks, een dichtheidsraster, géén losse
  doorvaarten"*. Dat was afgeleid uit de documentatie zonder token, en het is **onjuist**. Het
  rapport levert per rij: `Lat · Lon · Time Range · Vessel ID · Flag · Vessel Name · Entry/Exit
  Timestamp · Gear Type · Vessel Type · MMSI · IMO · CallSign · Vessel Presence Hours`. Er zit
  dus **scheepsidentiteit** in, en met `temporal-resolution=HOURLY` staat er per rij één cel per
  uur per schip. Sorteren op MMSI en tijd geeft daarmee een reconstrueerbaar spoor.
  Gemeten op Patache–Antofagasta (2025-06, polygoon uit §4): ENTIRE 3.577 rijen / 27.741
  aanwezigheidsuren; 2 dagen HOURLY 1.668 rijen, DAILY 404 rijen. HTTP 200, ZIP 422 KB, met een
  readme en GFW's AIS-caveat-PDF erin.
  **Wat wél blijft gelden:** de korrel is 1 positie per uur, en dat is exact de AMSA-situatie —
  een varend schip legt in een uur ~20 km af, dus dit beschrijft een **corridor**, geen geul en
  zeker geen kade. Behandel het als dekkings-/corridorlaag, niet als graaf-geometrie. Dat is
  precies de rol die het moet vervullen: de nul-dekking-corridors (Chili, Hormuz, Lobito, Suez,
  Constanța) hebben nu helemaal niets.
  ⚠️ **Shell-valkuil:** `datasets[0]=` in de URL wordt door bash als glob gelezen en de request
  mislukt zonder duidelijke fout. Schrijf `datasets%5B0%5D=`.
- **`public-global-port-visits-events:latest`** via `/v3/events` — havenbezoeken als
  **node-bron**: welke kade werkelijk wordt aangelopen. Bruikbaar naast/na LAR-531.

Wat GFW **niet** oplost: het blijft een raster, dus voor de nul-dekking-corridors krijgen we
geen graaflijnen "tot áán de kade" zoals uit echte tracks. Die corridors houden MARNET als
open-zeenet; GFW verbetert de geul-geometrie en de haven-nodes.

### 6. Wat er daarna gebeurt (onze kant)

1. Rooktest (`/v3/events`) → token leeft.
2. Eén corridor als pilot: **Chili/Patache–Antofagasta**, want daar staat de atlas op 47 havens
   met nul varend verkeer en hangt het koperbeen op fallback-geometrie.
3. **Meten en extrapoleren vóór opschalen**: doorlooptijd en bestandsgrootte van één
   corridor-maand, dán de rest. Let op de 100 s/524-grens.
4. `haal_gfw.py`: polygoon in → CSV-raster in `v2/build-cache/ais/gfw/` (gitignored),
   hervatbaar, 0-byte-val op grootte.
5. Attributie in de HUD (verplicht): **"Powered by Global Fishing Watch."** met link naar
   <https://globalfishingwatch.org>, plus CC BY-NC 4.0 naast de bestaande AMSA-BY-NC-notitie.

---

## Bijlage A — de twee omzet-valkuilen, gemeten

**1. Het tijdstempel faalt rauw.** `bouw_tracks.py` doet
`strptime(t[:26], "%Y-%m-%d %H:%M:%S.%f")`. EuRIS levert ISO-8601 mét `T`-scheiding en zeven
decimalen. Gemeten:

```
EuRIS levert:              '2026-07-27T09:33:37.6463173+00:00'
rauw door bouw_tracks:     FAALT  -> time data '2026-07-27T09:33:37.646317'
                                     does not match format '%Y-%m-%d %H:%M:%S.%f'
na omzetting:              '2026-07-27 09:33:37.646317000 +0000 UTC'
omgezet door bouw_tracks:  GELUKT -> 2026-07-27 09:33:37.646317
```

De omzetting die dus in `haal_euris.py` moet:

```python
from datetime import datetime, timezone
tijd = (datetime.fromisoformat(x["positionMeasuredAt"])
        .astimezone(timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S.%f") + "000 +0000 UTC")
```

**2. `speedGround` staat in km/u, niet in knopen.** De docs zeggen letterlijk *"Speed over
ground (km/h)"*. `bouw_tracks.py` rekent in knopen (`VARE_GRENS = 0.5`, `MAX_KNOPEN = 40`) en
het aisstream-schema heeft `Sog` in knopen. Dus `Sog = speedGround / 1.852`. Zonder die deling
lijkt elk schip 1,85× te snel en knipt de sprong-filter tracks die heel zijn.

**Veldafbeelding EuRIS → aisstream-schema** (op wat gemeten gevuld is):

| aisstream | EuRIS | opmerking |
|---|---|---|
| `MetaData.MMSI` | `trackId` (naar int) | de groepeersleutel; MMSI zelf is 0 |
| `MetaData.ShipName` | `name` | is `"Track 545618"` bij klasse 2 = geen echte naam |
| `MetaData.time_utc` | `positionMeasuredAt` | **omzetten**, zie hierboven |
| `…PositionReport.Latitude/Longitude` | `lat` / `lon` | |
| `…PositionReport.Sog` | `speedGround / 1.852` | **km/u → knopen** |
| `…PositionReport.Cog` | `courseGround` | |
| `…PositionReport.NavigationalStatus` | `navigationalStatus` | gevuld 50/100 |
| `ShipStaticData.Dimension.A` / `.C` | `length` / `beam` | gevuld 94 resp. 95/100 |
| `ShipStaticData.Type` | `aisShipType` | **slechts 5/100** (klasse 3) |
| `ShipStaticData.MaximumStaticDraught` | — | ⚠️ **bestaat niet in de v3-respons** |

⚠️ Die laatste regel is een valstrik: de privacy-documentatie noemt wél diepgangvelden
(`InlDrAIS`, `MaxDrAIS`) op klasse 2, maar dat zijn veldnamen uit een **andere** representatie
(v2/ArcGIS). De v3 bounding-box-respons heeft geen diepgangveld — niet naar zoeken.

**Bijvangst die de moeite waard is:** `isrsPosition` + `isrsPositionName` zijn gevuld op
**69/100** en geven een officiële RIS-locatiecode mét naam (bv. `ROXXX00001ACHAL02945` =
*"Anchorage Area"*, `ROXXX000010000004940` = *"DISTANCE MARK ALONG WATERWAY AXIS"*). Dat is een
directe join op de terminal-laag (die is 100 % op ISRS gecodeerd) — dus je kunt een liggend
schip aan een **benoemde** kade of ankerplaats koppelen zonder enige identiteit te kennen. Dat
is LAR-531-materiaal.

## Bijlage B — alle gemeten feiten op een rij

*Gemeten 2026-07-27, zonder account, met echte requests.*

| # | wat | gemeten uitkomst |
|---|---|---|
| 1 | `GET /api/v3/tracks/bounding-box` anoniem | **200 OK**, echte posities van derden |
| 2 | `mmsi` / `name` / `aisShipType` bij klasse 2 | `0` / `"Track 545618"` / `-1` |
| 3 | `GET /api/AISTracks/GetTrack` anoniem | **401**, `WWW-Authenticate: Bearer` (swagger zei auth=nee) |
| 4 | `GET /api/AISTracks/Connect` anoniem | **400** |
| 5 | Tracks v3: aantal endpoints | **4**; `followed`/`owned` = auth **én** eigen schepen; **geen historie-endpoint** |
| 6 | `GET /api/v3/tracks/fairway-section` | 200 maar **lat/lon = 0.0**, alle velden leeg |
| 7 | `pageSize` | hard gecapt op **100** (250 en 500 geven ook 100); `skip` pagineert, 0 overlap |
| 8 | 5 vensters totaal | **1.842 tracks · 348 varend · 14 met MMSI (0,8 %)** |
| 9 | Donau (3 vensters) | **526 tracks · 94 varend · 12 met MMSI (2,3 %)** |
| 10 | `trackId`-stabiliteit | 99,5 % over 4 min · 98,5 % over 12 min · 99,0 % over 16 min, en **0 nieuwe id's** |
| 10b | Donau-samenhang `fairways` | **8 componenten**; gaten 3 m/8 m/13 m/…; 12 paren <250 m, 50 <2 km = LAR-520-klasse |
| 11 | versheid `positionMeasuredAt` | ~6 s oud → live feed, geen archief |
| 12 | rate limit (docs) | 100 req/min per bron-IP → 429; **geen rate-headers in de respons** |
| 13 | gedocumenteerde OAuth2 `tokenUrl` | **404 `{"error":"Realm does not exist"}`** — verouderd |
| 14 | echt realm | `euris`; `visuris.full_access` **niet** in de 14 `scopes_supported` |
| 15 | EuRIS-registratieformulier | 5 velden, **geen** organisatie- of doel-veld |
| 16 | EuRIS soft-404 | onbekend pad geeft **HTTP 200** + HTML-foutpagina → controleer **inhoud**, niet status |
| 17 | `fairways/0` anoniem | **200 · 7.122 polylines · 8,6 MB**, CEMT 100 %, diepgang 68 % |
| 18 | `terminals/0` anoniem | **200 · 3.969 punten**, ISRS 100 %, operator 1.376, goederensoort 687 |
| 19 | `berths/0` anoniem | **200 · 5.841 kadelijnen**, naam 100 %, diepgang 2.148, terminal-ref 1.828 |
| 20 | volledigheid van die drie | `exceededTransferLimit=False` + `returnIdsOnly` telt exact gelijk |
| 21 | **lengtetoets Donau** | **2.471,6 km over 273 secties tegen 2.414 km = +2,4 %** |
| 22 | lengtetoets Rijn | 1.321,1 km over 322 secties (+7,1 % — referentie dubbelzinnig, niet conclusief) |
| 23 | landen in `fairways` | 12; NL 4.035 · FR 1.374 · BE 637 · DE 625 · RO 180 · … · **BG ontbreekt** |
| 24 | landen in `berths` | 7; FR 2.907 · BE 2.382 · CZ 280 · BG 143 · RO 94 · **NL en DE ontbreken** |
| 25 | `locks`/`bridges`/`berthlines`/`berthareas`/`risindex`/`TracksV2` | **0 features**, ook zonder bbox → anoniem leeg |
| 26 | tijdstempel rauw door `bouw_tracks.py` | **FAALT** (`T`-scheiding); omzetting getest en werkt |
| 27 | `speedGround` eenheid | **km/u** (docs) → delen door 1,852 voor `Sog` |
| 28 | GFW `4wings/report` anoniem | **401 `{"error":"invalid token"}`** |
| 29 | GFW `/v3/events` anoniem | **401** |
| 30 | GFW `/v3/datasets` anoniem | **401** — ook de datasetlijst zit dicht |
| 31 | GFW-registratieformulier | 8 velden, **pagina 1 van 2**, verplichte Organization + categorie |
| 32 | docs-site over plain HTTP | alle 9 doc-paden geven **hetzelfde 16.253-byte-omhulsel** → JS-gerenderd |

**Openstaand en eerlijk onzeker:**
- **Of `trackId` over een etmaal stabiel blijft.** Gemeten over 16 min: 99 % behouden en **0
  nieuwe id's**, dus binnen dat bestek geen herrandomisatie. De docs noemen het veld echter
  letterlijk *"Randomized"*, en een cyclus per etmaal/sessie is hiermee niet uitgesloten.
  **Dit is de bepalende vraag voor EuRIS als track-bron**, en hij is zónder account te
  beantwoorden met een poller die een nacht draait.
- Wat `AisTracks/GetTrack` inhoudelijk teruggeeft (401, responseschema leeg in swagger). Op grond
  van punt 5 verwacht ik géén historie, maar dat is een gevolgtrekking, geen meting.
- Hoeveel hoger de rate limit met een token wordt — de docs zeggen alleen "increased", geen getal.
- Of de paginacap van 100 meebeweegt met een token. Niet gedocumenteerd.
- Alle GFW-quotagetallen: documentatie, niet gemeten (alles zit achter 401).
- Wat op pagina 2 van het GFW-formulier staat (bewust niet doorlopen — dat is Lars' stap).
- De goederencodes op de terminal-laag (`TRSHGD`: 1…10, met code 2 in 541 gevallen) zijn een
  RIS-codelijst waarvan ik de sleutel **niet** heb. Niet gokken; opzoeken vóór gebruik.

## Bronnen

- EuRIS developer-docs (JS-gerenderd; via browser gelezen) —
  `developer.eurisportal.eu/docs/fundamentals/privacy`, `/fundamentals/rate-limits`,
  `/getting-started`, `/entities/tracks/v3`, `/entities/fairway-v2`, `/entities/terminal-v1`
- EuRIS Swagger-index (43 specs) — <https://www.eurisportal.eu/doc/api>, o.a.
  `swagger/docs/Tracks_v3`, `ArcGIS_v1`, `Fairway_v2`, `Terminals_v1`, `Berth_v2`
- Global Fishing Watch API-documentatie — <https://globalfishingwatch.org/our-apis/documentation>
- Global Fishing Watch tokens — <https://globalfishingwatch.org/our-apis/tokens>
