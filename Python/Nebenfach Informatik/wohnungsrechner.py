class Mieteinnahmen:
    def konfigurieren(self):
        einlesen_vermietete_einheiten = input(
            "Wie viele Wohnungen haben Sie vermietet? "
        )
        self.vermietete_einheiten = int(einlesen_vermietete_einheiten)

        einlesen_miete_pro_einheit = input(
            "Wie hoch ist die monatliche Miete pro Wohnung? "
        )
        self.miete_pro_einheit = float(einlesen_miete_pro_einheit)

        einlesen_zeitraum = input(
            "Fuer wie viele Monate wollen Sie die Mieteinnahmen berechnen? "
        )
        self.zeitraum = int(einlesen_zeitraum)

    def berechnen(self):
        einnahmen = self.vermietete_einheiten * self.miete_pro_einheit * self.zeitraum
        print(
            "In "
            + str(self.zeitraum)
            + " Monaten erzielen Sie Mieteinnahmen von "
            + str(einnahmen)
            + " Euro."
        )

        return einnahmen


class Gehaltskosten:
    def konfigurieren(self):
        einlesen_weitere_mitarbeiter = "ja"
        self.sum_gehaelter = 0

        while einlesen_weitere_mitarbeiter == "ja":
            einlesen_sum_gehaelter = input(
                "Wie hoch ist das monatliche Gehalt ihres Mitarbeiters? "
            )
            self.sum_gehaelter += float(einlesen_sum_gehaelter)

            einlesen_weitere_mitarbeiter = input(
                "Haben sie weitere Mitarbeiter [ja \ nein]? "
            )

        einlesen_zeitraum = input(
            "Fuer wie viele Monate wollen Sie die Gehaltskosten berechnen? "
        )
        self.zeitraum = float(einlesen_zeitraum)

    def berechnen(self):
        gehaltskosten = self.sum_gehaelter * self.zeitraum
        print(
            "In "
            + str(self.zeitraum)
            + " Monaten, betragen alle Gehaelter zusammen genommen "
            + str(gehaltskosten)
            + " Euro."
        )

        return gehaltskosten
