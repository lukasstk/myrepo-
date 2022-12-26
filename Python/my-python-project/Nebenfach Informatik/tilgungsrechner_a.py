from tilgungsrechner import tilgungsrechner


class Tilgungsrechner:
    def __init__(self, zinssatz0, tilgungssatz0):
        self.zinssatz = zinssatz0
        self.tilgungssatz = tilgungssatz0

    def berechne_restschuld(self, dahrlehnsbetrag):
        return tilgungsrechner(dahrlehnsbetrag, self.zinssatz, self.tilgungssatz)


"""Objekt1 = Tilgungsrechner(2, 10)
Objekt1.berechne_restschuld(10000)
Objekt1.berechne_restschuld(20000)

rechner = Tilgungsrechner ("2", "10")
rechner . berechne_restschuld (" 20000 ")  # multiplikation zwischen strings ist nicht möglich"""
