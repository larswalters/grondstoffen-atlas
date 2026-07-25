# bake_aisnet.py — de eerste AIS-watergraaf (M27, pilot): het RUG-recept.
#
# ⚠️⚠️ STATUS SINDS 2026-07-25: FALLBACK, GEEN ROUTEERBRON MEER (M28, LAR-534).
# Het density/skeleton-plan is vervangen door het AIS-TRACKNET: de tracks van
# individuele schepen (ping-reeksen per MMSI via aisstream.io) zijn nu de bron
# van de vaargraaf — één doorvaart = één vloeiende edge op GPS-precisie, tot aan
# de kade, zonder threshold en zonder skeleton. Zie de Linear-milestone
# "M28 · AIS-tracknet" (LAR-528 t/m LAR-535) en v2/tools/ais_dekkingstest.py.
#
# Deze pijplijn blijft bestaan en werkend als FALLBACK voor corridors waar we te
# weinig eigen tracks krijgen — in de praktijk de Yangtze, want de aisstream-
# stationskaart heeft in China alleen kustdekking (landinwaarts richting Tongling
# staat geen ontvanger). Gebruik hem daar bewust en gedocumenteerd; bouw er geen
# nieuw werk meer bovenop.
#
# Leidt uit de World Bank-density (0037580, Commercial) per venster de vaargeul
# af en schrijft polylijnen naar v2/data/aisnet-pilot.json, zodat de bol ze als
# zichtbare laag kan tekenen (aisnet.js). Dit is bewust de KIJK-stap van de
# ombouw: eerst moeten de lijnen op de juiste plek liggen (Lars' visuele
# controle), pas daarna wordt dit een echte graaf met knopen/edges en
# aanhechting op de havens.
#
# ⚠️ TWEEDE RECEPT (2026-07-25). Het eerste recept (drempel 100k → adaptief
# verdunnen → skelet, zie git-historie t/m ?v=084) is gemeten en vervangen:
# de binaire drempel knipte geulen op elke dip (gaten in de Tongling-oostgeul
# én de Rijn), het verdunnen liet het net hoekig en dunner achter dan de
# dichtheidsfoto's beloven, en het skelet van een vlak bleef een honingraat.
#
# Het rug-recept werkt op het CONTINUE veld in plaats van op een binair masker:
#   1. rug-NMS    — Steger-stijl: Hessiaan van het log-veld op twee schalen
#                   (fijn = geulen, grof = brede zeecorridors, sigma^2-
#                   genormaliseerd); een cel is rug als het veld dwars op de
#                   rug een lokaal maximum is. Een ankervlek is een blob (geen
#                   dwars-maximum) en valt er per constructie uit — de ringen
#                   die sato/vesselness om blobranden trok ook.
#   2. hysteresis — sterk >= RUG_HOOG zaait, zwak >= RUG_LAAG loopt door:
#                   zwakke maar aaneengesloten stukken geul blijven één lijn
#                   (dit dicht de oostgeul- en Rijn-gaten van het oude recept).
#   3. bezetting  — twee eisen per getraceerde lijn, geijkt op de Tongling-
#                   oostgeul (moet blijven) vs de Patache-drijfzone (moet weg):
#                   STRIKT (merendeel van de lijncellen zelf bevaren; draad
#                   >= 0,53 ondanks artefact-gaatjes, speckle-web <= 0,40) en
#                   COMP (de lijn ligt op een GROOT aaneengesloten helder
#                   component; een geul is een draad, een web valt uiteen).
#   4. kruimels   — geïsoleerde mini-netwerkjes (< 30 cellen totaal) weg;
#                   echte geulen hangen aan het net.
#   5. gladstrijken — bewegend gemiddelde over de binnenpunten (uiteinden
#                   blijven exact liggen voor gedeelde juncties): het hoekige
#                   45°-trapjeswerk van een rasterskelet verdwijnt.
#
# ⚠️ GEMETEN EN VERWORPEN (niet opnieuw proberen):
#   - NMS-tolerantie (crest-jitter overbruggen met een marge): maakt de mask
#     dik, waarna het skelet naast de 1-cels geuldraad loopt en de
#     bezettingstoets de echte geul afkeurt. Strikte NMS + masker-closing dicht
#     de jittergaatjes al.
#   - vlak-bezetting (fractie bezette buurtcellen): land naast een smalle
#     rivier telt als "onbezet" → een 2 cellen brede geul haalt de eis nooit.
#   - max-filter-bezetting (elke 3x3-buur telt): laat drijfzone-webben door,
#     want in een dicht speckle-veld heeft bijna elke cel een heldere buur.
#
# ⚠️ WAT ER ECHT IN HET RASTER STAAT (gemeten, bepaalt het ontwerp):
#   - geulen zijn vaak 1-cels DRADEN met uniforme waarden (oostgeul: 17,8M per
#     cel) en losse artefact-nullen erin (zelfs hele nul-rijen — tegelnaden in
#     de World Bank-verwerking; de zwarte band bij Shanghai is er ook een);
#   - drijf-/ankerzones (Patache) dragen dezelfde ~3M-waarden als de corridor
#     ernaast, maar als SPECKLE (p50 van de bezette cellen: 2 berichten) —
#     alleen geometrie (draad vs losse spikkels) onderscheidt ze, geen drempel.
#
# Draaien:  python v2/tools/bake_aisnet.py

import json
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import from_bounds
from scipy import ndimage
from skimage.filters import apply_hysteresis_threshold
from skimage.morphology import skeletonize

HIER = Path(__file__).resolve().parent
TIF = HIER.parent / "build-cache" / "ais" / "commercial" / "ShipDensity_Commercial1.tif"
UIT = HIER.parent / "data" / "aisnet-pilot.json"

# Dezelfde vensters als verken_ais.py — de zwakke plekken van het oude net.
VENSTERS = {
    "tongling":  (117.40, 30.65, 118.15, 31.35),
    "nederland": (3.40, 51.20, 6.80, 52.40),
    "patache":   (-70.75, -21.30, -69.90, -20.10),
    "shanghai":  (120.60, 30.60, 122.70, 31.90),
}

# --- de knoppen van het rug-recept -------------------------------------------
SIGMAS = [1.5, 3.5]    # fijn (geulen/binnenwater) + grof (brede zeecorridors)
RUG_HOOG = 1.1         # hysteresis-hoog op sigma^2-genormaliseerde rugsterkte
RUG_LAAG = 0.35        # hysteresis-laag: zwak maar aaneengesloten loopt door
ACT_FLOOR = 10_000     # glad (sigma 2) aantal berichten dat een rug moet dragen
BEZET_MIN = 500        # cel "bezet" vanaf dit aantal berichten (6 jaar AIS)
BEZET_STRIKT = 0.45    # min. fractie lijncellen die zélf bezet zijn
BEZET_COMP = 0.85      # min. fractie lijncellen op/naast een groot helder component
COMP_MIN = 20          # cellen: vanaf hier telt een helder component als draad
MIN_CELLEN = 8         # confetti: kleinere masker-componenten zijn ruis
SPUR_CELLEN = 8        # iteratieve spur-snoei: vrije uiteinden korter dan dit weg
KRUIMEL_CELLEN = 30    # geïsoleerde lijn-netwerkjes kleiner dan dit (totaal) weg
GLADSTRIJK_RONDES = 2  # rondes bewegend gemiddelde over de polylijn


def steger_rug(L: np.ndarray, sigma: float):
    """Steger-stijl rugdetectie: Hessiaan van het (log-)veld; een cel is rug
    als het veld dwars op de rug (richting van de sterkst negatieve kromming)
    een lokaal maximum is. Een blobrand is een trede, geen maximum -> valt af.
    Geeft (rugmasker, sigma^2-genormaliseerde rugsterkte)."""
    Lrr = ndimage.gaussian_filter(L, sigma, order=(2, 0))
    Lcc = ndimage.gaussian_filter(L, sigma, order=(0, 2))
    Lrc = ndimage.gaussian_filter(L, sigma, order=(1, 1))
    Lg = ndimage.gaussian_filter(L, sigma)

    som, verschil = Lrr + Lcc, Lrr - Lcc
    wortel = np.sqrt(verschil * verschil + 4 * Lrc * Lrc)
    lam2 = (som - wortel) / 2          # meest negatieve eigenwaarde
    # sigma^2-normalisatie (Lindeberg) zodat één drempel over beide schalen werkt
    sterkte = np.clip(-lam2, 0, None) * sigma * sigma

    # eigenvector bij lam2 = dwarsrichting van de rug; twee formules, kies per
    # cel de numeriek stabielste
    v1r, v1c = Lrc, lam2 - Lrr
    v2r, v2c = lam2 - Lcc, Lrc
    gebruik1 = np.hypot(v1r, v1c) >= np.hypot(v2r, v2c)
    vr = np.where(gebruik1, v1r, v2r)
    vc = np.where(gebruik1, v1c, v2c)
    norm = np.hypot(vr, vc)
    norm[norm == 0] = 1
    vr, vc = vr / norm, vc / norm

    # strikt lokaal maximum dwars op de rug (bilineair op +/- 1 cel)
    rijen, kolommen = np.indices(L.shape)
    plus = ndimage.map_coordinates(Lg, [rijen + vr, kolommen + vc], order=1, mode="nearest")
    minus = ndimage.map_coordinates(Lg, [rijen - vr, kolommen - vc], order=1, mode="nearest")
    return (Lg >= plus) & (Lg >= minus), sterkte


def spoor_polylijnen(skelet: np.ndarray) -> list[list[tuple[int, int]]]:
    """Volgt een 1-cel-breed skelet en geeft polylijnen in pixelcoördinaten.

    Splitst op kruisingen (>2 buren): elke polylijn loopt van uiteinde/kruising
    naar uiteinde/kruising, zodat de latere graaf-stap er direct knopen van kan
    maken. Cycli zonder kruising (een rondje) worden als gesloten lijn gelopen.
    """
    hoogte, breedte = skelet.shape
    buren8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def buren(r: int, k: int):
        for dr, dk in buren8:
            rr, kk = r + dr, k + dk
            if 0 <= rr < hoogte and 0 <= kk < breedte and skelet[rr, kk]:
                yield rr, kk

    graad = {}
    for r, k in zip(*np.nonzero(skelet)):
        graad[(r, k)] = sum(1 for _ in buren(r, k))

    bezocht_kant = set()   # gerichte stap (a→b) die al gelopen is
    lijnen = []

    def loop(start, eerste):
        """Loop vanaf `start` richting `eerste` tot een uiteinde/kruising."""
        lijn = [start, eerste]
        bezocht_kant.add((start, eerste))
        bezocht_kant.add((eerste, start))
        terwijl = eerste
        vorige = start
        while graad.get(terwijl, 0) == 2:
            volgende = next((b for b in buren(*terwijl) if b != vorige), None)
            if volgende is None or (terwijl, volgende) in bezocht_kant:
                break
            bezocht_kant.add((terwijl, volgende))
            bezocht_kant.add((volgende, terwijl))
            lijn.append(volgende)
            vorige, terwijl = terwijl, volgende
        return lijn

    # eerst vanaf alle uiteinden en kruisingen (de "echte" lijnstukken)
    for cel, g in graad.items():
        if g == 2:
            continue
        for b in buren(*cel):
            if (cel, b) not in bezocht_kant:
                lijnen.append(loop(cel, b))

    # dan resterende cycli (rondjes zonder kruising of uiteinde)
    for cel, g in graad.items():
        if g == 2:
            for b in buren(*cel):
                if (cel, b) not in bezocht_kant:
                    lijnen.append(loop(cel, b))

    return lijnen


def snoei_sporen(lijnen: list, min_cellen: int) -> list:
    """Iteratief: dangling lijntjes (een vrij uiteinde) korter dan min_cellen
    weg. Lijnen tussen twee juncties blijven staan; een lange geïsoleerde lijn
    (bv. een kustcorridor) ook."""
    while True:
        graad = {}
        for l in lijnen:
            for cel in (l[0], l[-1]):
                graad[cel] = graad.get(cel, 0) + 1
        houd = []
        weg = 0
        for l in lijnen:
            vrij = (graad[l[0]] == 1) or (graad[l[-1]] == 1)
            if vrij and len(l) <= min_cellen:
                weg += 1
            else:
                houd.append(l)
        lijnen = houd
        if weg == 0:
            return lijnen


def snoei_kruimels(lijnen: list, min_cellen: int) -> list:
    """Verwijdert geïsoleerde mini-netwerkjes: union-find over gedeelde
    uiteinden; componenten met minder dan min_cellen totaal gaan eruit."""
    ouder = {}

    def vind(x):
        while ouder.setdefault(x, x) != x:
            ouder[x] = ouder[ouder[x]]
            x = ouder[x]
        return x

    for l in lijnen:
        a, b = vind(l[0]), vind(l[-1])
        if a != b:
            ouder[a] = b
    gewicht = {}
    for l in lijnen:
        w = vind(l[0])
        gewicht[w] = gewicht.get(w, 0) + len(l)
    return [l for l in lijnen if gewicht[vind(l[0])] >= min_cellen]


def gladstrijk(lijn: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Bewegend gemiddelde (1-2-1) over de binnenpunten; de uiteinden blijven
    exact liggen zodat juncties gedeeld blijven."""
    pts = [list(p) for p in lijn]
    for _ in range(GLADSTRIJK_RONDES):
        if len(pts) < 3:
            break
        nieuw = [pts[0]]
        for i in range(1, len(pts) - 1):
            nieuw.append([
                (pts[i - 1][0] + 2 * pts[i][0] + pts[i + 1][0]) / 4,
                (pts[i - 1][1] + 2 * pts[i][1] + pts[i + 1][1]) / 4,
            ])
        nieuw.append(pts[-1])
        pts = nieuw
    return [tuple(p) for p in pts]


def bak_venster(naam: str, bbox, bron) -> list[dict]:
    w, z, o, n = bbox
    venster = from_bounds(w, z, o, n, bron.transform)
    data = bron.read(1, window=venster).astype(np.float64)
    if bron.nodata is not None:
        data = np.where(data == bron.nodata, 0, data)
    data = np.clip(data, 0, None)

    L = np.log1p(data)
    act = ndimage.gaussian_filter(data, 2.0)
    draagt = act >= ACT_FLOOR

    # 1+2 · multi-schaal rug-NMS, gecombineerd als max-sterkte, dan hysteresis
    kandidaat = np.zeros_like(L)
    for sigma in SIGMAS:
        rug, sterkte = steger_rug(L, sigma)
        kandidaat = np.maximum(kandidaat, np.where(rug & draagt, sterkte, 0.0))
    masker = apply_hysteresis_threshold(kandidaat, RUG_LAAG, RUG_HOOG)
    # 1-cels NMS-jittergaatjes dichten vóór het skelet
    masker = ndimage.binary_closing(masker, structure=np.ones((3, 3)))

    # confetti
    labels, _ = ndimage.label(masker, structure=np.ones((3, 3)))
    tel = np.bincount(labels.ravel())
    masker = masker & (tel[labels] >= MIN_CELLEN)

    skelet = skeletonize(masker)
    lijnen_px = spoor_polylijnen(skelet)

    # 3 · bezettingstoets (geijkt op oostgeul-draad vs Patache-drijfzone)
    bezet = data >= BEZET_MIN
    dicht = ndimage.binary_closing(bezet, structure=np.ones((3, 3)))
    clabels, _ = ndimage.label(dicht, structure=np.ones((3, 3)))
    ctel = np.bincount(clabels.ravel())
    groot = dicht & (ctel[clabels] >= COMP_MIN)

    def occ_ok(lijn):
        strikt = np.mean([bezet[r, k] for r, k in lijn])
        if strikt < BEZET_STRIKT:
            return False
        raak = sum(bool(groot[max(r - 1, 0):r + 2, max(k - 1, 0):k + 2].any())
                   for r, k in lijn)
        return raak / len(lijn) >= BEZET_COMP

    lijnen_px = [l for l in lijnen_px if occ_ok(l)]

    # 4 · snoei
    lijnen_px = snoei_sporen(lijnen_px, SPUR_CELLEN)
    lijnen_px = snoei_kruimels(lijnen_px, KRUIMEL_CELLEN)

    # 5 · gladstrijken in pixelruimte, dan pixel -> lon/lat van het celmidden
    vt = bron.window_transform(venster)
    lijnen = []
    for lijn in lijnen_px:
        punten = []
        for k, r in gladstrijk([(k, r) for r, k in lijn]):
            lon, lat = vt * (k + 0.5, r + 0.5)
            punten.append([round(lon, 5), round(lat, 5)])
        if len(punten) >= 2:
            lijnen.append({"venster": naam, "punten": punten})

    km = sum(len(l["punten"]) for l in lijnen) * 0.5
    print(f"  {naam:10s} masker {int(masker.sum()):6d} · skelet {int(skelet.sum()):6d} · "
          f"{len(lijnen):4d} lijnen · ~{km:,.0f} km")
    return lijnen


def main() -> None:
    alle = []
    with rasterio.open(TIF) as bron:
        print(f"bake_aisnet · rug-recept: NMS sigma {SIGMAS} · "
              f"hysteresis {RUG_LAAG}/{RUG_HOOG} · bezetting {BEZET_STRIKT}/{BEZET_COMP}")
        for naam, bbox in VENSTERS.items():
            alle.extend(bak_venster(naam, bbox, bron))

    uit = {
        "bron": "World Bank / IMF Global Shipping Traffic Density (0037580), "
                "laag Commercial, jan 2015 - feb 2021, CC-BY 4.0",
        "recept": {
            "naam": "rug",
            "sigmas": SIGMAS,
            "hysteresis": [RUG_LAAG, RUG_HOOG],
            "actFloor": ACT_FLOOR,
            "bezetting": [BEZET_STRIKT, BEZET_COMP],
        },
        "vensters": {n: list(b) for n, b in VENSTERS.items()},
        "lijnen": alle,
    }
    UIT.write_text(json.dumps(uit, separators=(",", ":")), encoding="utf-8")
    kb = UIT.stat().st_size / 1024
    print(f"→ {UIT.name} · {len(alle)} lijnen · {kb:,.0f} KB")


if __name__ == "__main__":
    main()
