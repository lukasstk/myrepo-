from tilgungsrechner import tilgungsrechner


class Tilgungsrechner:

    def berechne_restschuld(self, dahrlehnsbetrag):
        return tilgungsrechner(dahrlehnsbetrag, self.zinssatz, self.tilgungssatz)

    def konfigurieren(self):
        einlesen_zinssatz = input(
            "Wie hoch ist ihr Zinssatz? "
        )
        self.zinssatz = float(einlesen_zinssatz)

        einlesen_tilgungssatz = input(
            "Wie hoch ist ihr Tilgungssatz? "
        )
        self.tilgungssatz = float(einlesen_tilgungssatz)

        einlesen_dahrlehnsbetrag = input(
            "Wie hoch ist ihr Dahrlehnsbetrag? "
        )
        self.dahrlehnsbetrag = float(einlesen_dahrlehnsbetrag)

    def berechnen(self):
        return tilgungsrechner(self.dahrlehnsbetrag, self.zinssatz, self.tilgungssatz)