class Point:
    """Diese Klasse dient zu Repraesentation eines Punkts"""

    def __init__(self, x0=0, y0=0):
        """Konstruktor und Initilisierung eines Punktes,
            wobei dessen x- und y-Koordinate gegeben sein muessen.

        Parameters:
            x0 (int): x-Koordinate des Punktes
            y0 (int): y-Koorsinate des Punktes
        """
        self.x = x0
        self.y = y0

    def move(self, dx, dy):
        """Diese Methode verschiebt den Punkt um dx auf der x-Achse
            und dy auf der y-Achse.

        Parameters:
            dx (int): Distanz der Verschiebung auf der x-Achse
            dy (int): Distanz der Verschiebung auf der y-Achse
        """
        self.x += dx
        self.y += dy
