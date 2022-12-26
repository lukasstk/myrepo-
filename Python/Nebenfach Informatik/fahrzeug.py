from point import *


class Fahrzeug:
    def __init__(self, x0: int, y0: int, anzahl_raeder0: int, leergewicht0: int, geschwindigkeit0: int):
        self.aktuelle_geschwindigkeit = geschwindigkeit0
        self.leergewicht = leergewicht0
        self.anzahl_raeder = anzahl_raeder0
        self.position = Point(x0, y0)

    def beschleunigen(self, beschleunigung):
        self.aktuelle_geschwindigkeit += beschleunigung

    def fahren(self, dx: int, dy: int):
        self.position.move(dx, dy)
        print(self.position.x, self.position.y)

    def __str__(self):
        return (f"Geschwindigkeit: {self.aktuelle_geschwindigkeit}\n"
                f"Leergewicht: {self.leergewicht}\n"
                f"Anzahl Räder: {self.anzahl_raeder}\n"
                f"x-Position: {self.position.x}\n"
                f"y-Position: {self.position.y}\n")


class Personenkraftwagen(Fahrzeug):
    def __init__(self, x0: int, y0: int, leergewicht0: int, geschwindigkeit0: int, motorleistung0: int):
        super().__init__(x0, y0, 4, leergewicht0, geschwindigkeit0)
        self.motorleistung = motorleistung0

    def __str__(self):
        return super().__str__() + f"Motorleistung: {self.motorleistung}"


class Fahrrad(Fahrzeug):
    def __init__(self, x0: int, y0: int, leergewicht0: int, geschwindigkeit0: int):
        super().__init__(x0, y0, 2, leergewicht0, geschwindigkeit0)
