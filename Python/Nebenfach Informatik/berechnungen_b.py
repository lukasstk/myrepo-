from wohnungsrechner import Mieteinnahmen, Gehaltskosten
from tilgungsrechner_b import Tilgungsrechner


def berechnung_durchfuehren(rechner):
    rechner.konfigurieren()
    ergebnis = rechner.berechnen()
    print()


berechnung_durchfuehren(Mieteinnahmen())

berechnung_durchfuehren(Gehaltskosten())

berechnung_durchfuehren(Tilgungsrechner())
