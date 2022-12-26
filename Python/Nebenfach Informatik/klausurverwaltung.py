class Student:  # Student ist ein dictionary mit keys martrikelnummer und name
    def __init__(self, martrikelnummer0, name0):
        self.matrikelnummer = martrikelnummer0
        self.name = name0


class Klausur:  # Klausur ist ein dictionnary mit einem tupel aus titel und der maximalen anzahl an studenten
    def __init__(self, titel0, max_anzahl0):
        self.titel = titel0
        self.max_anzahl = max_anzahl0


input_main = None
while input_main != "Beenden":
    input_main = input("Suchen sie sich eine Aktion aus: Student erstellen, Klausur erstellen, Klausur verwalten oder "
                       "Beenden\n")
    if input_main == "Klausur verwalten":
        input_klausur_verwalten = input("Welche Vorlesung möchten sie verwalten?\n")
        if input_klausur_verwalten is None:
            print("Diese Vorlesung existiert nicht, bitte  wählen sie eine andere aus!")
        else:
            input_vorlesung_verwalten = input(
                "Suchen sie eine Aktion aus: Teilnehmer suchen, Student anmelden,  Student"
                " abmelden oder Note eintragen\n")
    if input_main == "Student erstellen":
        input_martrikelnummer = input("Welche Martrikelnummer hat ihr Student?\n")
        input_name = input("Welchen Namen hat ihr Student?\n")


        def student_erstellen(input_martrikelnummer, input_name):
            studenten = {}
            if input_martrikelnummer in studenten:
                print("Ihr ausgewählter Student ist schon im System festgehalten!")
            else:
                studenten = {input_name: input_martrikelnummer}
                print("Ihr ausgewählter Student wurde im System vermerkt!")
        student_erstellen(input_martrikelnummer, input_name)
    if input_main == "Klausur erstellen":