# bake_aisnet.py — de eerste AIS-watergraaf (M27, pilot).
#
# Leidt uit de World Bank-density (0037580, Commercial) per venster de vaargeul
# af en schrijft polylijnen naar v2/data/aisnet-pilot.json, zodat de bol ze als
# zichtbare laag kan tekenen (aisnet.js). Dit is bewust de KIJK-stap van de
# ombouw: eerst moeten de lijnen op de juiste plek liggen (Lars' visuele
# controle op Tongling + Nederland), pas daarna wordt dit een echte graaf met
# knopen/edges en aanhechting op de havens.
#
# De stappen per venster:
#   1. drempel   — geul = cel met ≥ DREMPEL AIS-berichten (2015–2021). De
#                  waarden zijn ruwe positieberichten (elke 2–10 s), dus een
#                  echt bevaren cel staat orden van grootte boven de ruis
#                  (open zee: enkele berichten; Rijn/Yangtze: 15–25 miljoen).
#   2. skelet    — skimage.skeletonize brengt de geul terug tot een lijn van
#                  1 cel breed (de middellijn van de dichtheidsrug).
#   3. sporen    — het skelet wordt gevolgd tot polylijnen: knikpunten op
#                  kruisingen (>2 buren) en uiteinden (1 buur).
#
# ⚠️ Bekend en bewust open in de pilot: ankergebieden en havenbekkens zijn
# brede VLEKKEN, geen lijnen — het skelet trekt daar een middellijn-web
# doorheen. Dat is zichtbaar (Shanghai) en wordt in de graaf-stap gefilterd
# (vlek-detectie: breedte van de geul per skeletcel); voor de kijk-stap laten
# we het staan zodat we zien wáár het speelt.
#
# Draaien:  python v2/tools/bake_aisnet.py

import json
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import from_bounds
from scipy import ndimage
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

# Eén absolute drempel voor alle vensters. IJkpunten uit de verkenning: open
# zee ruist op enkele berichten per cel, de Chileense kustcorridor zit op
# ~3 miljoen, binnenvaartgeulen op 15–60 miljoen. 100k ligt daar ruim onder
# maar ver boven de ruis (≈ een schip dat er in 6 jaar ~3 dagen vaart).
DREMPEL = 100_000

# ADAPTIEF VERDUNNEN — de ankervlek/zeevlak-les uit de eerste bake. Een geul is
# smal; een druk zeegebied, ankerplaats of havenbekken is een breed VLAK boven
# de drempel, en het skelet van een vlak is een honingraat-web (zichtbaar op de
# Noordzee in de eerste ronde). Waar het masker breder is dan MAX_BREEDTE
# cellen (~1,5 km halfbreedte) hogen we de drempel per gebied stap voor stap op
# tot alleen de dichtheidsRUG overblijft — dáár varen de schepen echt; de
# stille randen van het vlak vallen af. Smalle geulen raakt dit per constructie
# niet (die zijn nergens breder dan de grens).
MAX_BREEDTE = 3          # halfbreedte in cellen waarboven een gebied "vlak" is
VERDUN_KWANTIEL = 60     # per ronde blijft de top-40% van het gebied staan
VERDUN_RONDES = 12

# Spoor-snoei: skeletlijnen van ≤ SPUR_CELLEN met een los uiteinde zijn
# artefacten van de rasterisatie (de driehoekjes op kruisingen), geen geulen.
SPUR_CELLEN = 3

# Confetti-filter: losse componenten kleiner dan dit (in cellen) zijn zee-ruis
# (een enkele drukke cel op open water), geen geul. 8 cellen ≈ 4 km lijn.
MIN_CELLEN = 8

# De rug-beslissingen (waar ligt de vaarroute in een breed vlak) rekenen op een
# GLAD log-veld i.p.v. de ruwe tellingen: AIS-dichtheid is per cel grillig en
# het skelet van een grillige rest is krulwerk — zichtbaar op de Noordzee in
# ronde 2. σ=1 cel (~500 m) middelt de ruis en laat de corridor staan.
GLAD_SIGMA = 1.0


def verdun_vlakken(data: np.ndarray, masker: np.ndarray) -> np.ndarray:
    """Dunt brede vlakken tot hun vaarrug; smalle geulen blijven onaangeraakt.

    ⚠️ Les uit de eerste poging: heel Nederland-water is ÉÉN verbonden component
    (rivieren hangen aan de zee), dus per-component herdrempelen sloopte ook de
    rivieren tot streepjes. Daarom wordt het brede gebied eerst LOKAAL
    uitgesneden — de kern (dieper dan MAX_BREEDTE van de rand) plus zijn eigen
    rand — en alleen dáárbinnen wordt de drempel per deelgebied opgehoogd tot
    de rug overblijft. Een rivier raakt hooguit zijn monding kwijt waar hij het
    vlak in stroomt; dat hecht de graaf-stap later weer.
    """
    def zonder_confetti(m: np.ndarray) -> np.ndarray:
        labels, _ = ndimage.label(m, structure=np.ones((3, 3)))
        tel = np.bincount(labels.ravel())
        return m & (tel[labels] >= MIN_CELLEN)

    afstand = ndimage.distance_transform_edt(masker)
    kern = afstand > MAX_BREEDTE
    if not kern.any():
        return zonder_confetti(masker)

    # het vlak = de brede kern + zijn rand tot aan open water/land
    vlak = ndimage.binary_dilation(kern, iterations=MAX_BREEDTE + 1) & masker
    smal = masker & ~vlak

    # binnen het vlak: per deelgebied de drempel ophogen tot het dun genoeg is,
    # beslist op het GLADDE veld zodat de rug een corridor is en geen krulwerk
    glad = ndimage.gaussian_filter(np.log1p(np.clip(data, 0, None)), GLAD_SIGMA)
    vlak = vlak.copy()
    for _ in range(VERDUN_RONDES):
        afstand = ndimage.distance_transform_edt(vlak)
        if afstand.max() <= MAX_BREEDTE:
            break
        labels, _ = ndimage.label(vlak, structure=np.ones((3, 3)))
        te_breed = np.unique(labels[afstand > MAX_BREEDTE])
        for lab in te_breed:
            if lab == 0:
                continue
            gebied = labels == lab
            grens = np.percentile(glad[gebied], VERDUN_KWANTIEL)
            gebied_dun = gebied & (glad >= grens)
            vlak[gebied] = gebied_dun[gebied]

    # confetti-filter: mini-componenten zijn ruis, geen geul
    return zonder_confetti(smal | vlak)


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


def bak_venster(naam: str, bbox, bron) -> list[dict]:
    w, z, o, n = bbox
    venster = from_bounds(w, z, o, n, bron.transform)
    data = bron.read(1, window=venster)
    data = np.where(data == bron.nodata, 0, data)
    ruw = data >= DREMPEL
    masker = verdun_vlakken(data, ruw)

    skelet = skeletonize(masker)
    lijnen_px = spoor_polylijnen(skelet)

    # spoor-snoei: mini-lijntjes met een los uiteinde zijn rasterisatie-
    # artefacten (driehoekjes op kruisingen), geen geulen
    graad_tel = {}
    for lijn in lijnen_px:
        for cel in (lijn[0], lijn[-1]):
            graad_tel[cel] = graad_tel.get(cel, 0) + 1
    lijnen_px = [
        l for l in lijnen_px
        if len(l) > SPUR_CELLEN
        or (graad_tel[l[0]] > 1 and graad_tel[l[-1]] > 1)
    ]

    # pixel → lon/lat van het celmidden, via de venster-transform
    vt = bron.window_transform(venster)
    lijnen = []
    for lijn in lijnen_px:
        punten = []
        for r, k in lijn:
            lon, lat = vt * (k + 0.5, r + 0.5)
            punten.append([round(lon, 5), round(lat, 5)])
        if len(punten) >= 2:
            lijnen.append({"venster": naam, "punten": punten})

    km = sum(len(l["punten"]) for l in lijnen) * 0.5
    print(f"  {naam:10s} geul {int(ruw.sum()):6d} → verdund {int(masker.sum()):6d} cellen · "
          f"skelet {int(skelet.sum()):6d} · {len(lijnen):4d} lijnen · ~{km:,.0f} km")
    return lijnen


def main() -> None:
    alle = []
    with rasterio.open(TIF) as bron:
        print(f"bake_aisnet · drempel {DREMPEL:,} berichten/cel")
        for naam, bbox in VENSTERS.items():
            alle.extend(bak_venster(naam, bbox, bron))

    uit = {
        "bron": "World Bank / IMF Global Shipping Traffic Density (0037580), "
                "laag Commercial, jan 2015 - feb 2021, CC-BY 4.0",
        "drempel": DREMPEL,
        "vensters": {n: list(b) for n, b in VENSTERS.items()},
        "lijnen": alle,
    }
    UIT.write_text(json.dumps(uit, separators=(",", ":")), encoding="utf-8")
    kb = UIT.stat().st_size / 1024
    print(f"→ {UIT.name} · {len(alle)} lijnen · {kb:,.0f} KB")


if __name__ == "__main__":
    main()
