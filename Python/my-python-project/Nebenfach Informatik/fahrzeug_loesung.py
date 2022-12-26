from fahrzeug import *


def konfiguriere_geschwindigkeit():
    aktuelle_geschwindigkeit = input("Geben sie die aktuelle Geschwindigkeit(int) an.\n")
    return int(aktuelle_geschwindigkeit)


def konfiguriere_leergewicht():
    leergewicht = input("Geben sie das Leergewicht(int) an.\n")
    return int(leergewicht)


def konfiguriere_anzahl_raeder():
    anzahl_raeder = input("Geben sie die Anzahl der Räder(int) an.\n")
    return int(anzahl_raeder)


def konfiguriere_x_Position():
    x_position = input("Geben sie die aktuelle x-Position(int) an.\n")
    return int(x_position)


def konfiguriere_y_Position():
    y_position = input("Geben sie die aktuelle y-Position(int) an.\n")
    return int(y_position)


def konfiguriere_motorleistung():
    motorleistung = input("Geben sie die Motorleistung(int) an.\n")
    return int(motorleistung)


input_allgemein = input("Was für ein Fortbewegungsmittel möchten sie erzeugen?\n"
                        "Mögliche Fortbewegungsmittel wären: PKW, Fahrrad oder Fahrzeug.\n")


if input_allgemein == "PKW":
    aktuelle_geschwindigkeit = konfiguriere_geschwindigkeit()
    leergewicht = konfiguriere_leergewicht()
    x_position = konfiguriere_x_Position()
    y_position = konfiguriere_y_Position()
    motorleistung = konfiguriere_motorleistung()
    fahrzeug = Personenkraftwagen(x_position, y_position, leergewicht, aktuelle_geschwindigkeit, motorleistung)

elif input_allgemein == "Fahrrad":
    aktuelle_geschwindigkeit = konfiguriere_geschwindigkeit()
    leergewicht = konfiguriere_leergewicht()
    x_position = konfiguriere_x_Position()
    y_position = konfiguriere_y_Position()
    fahrzeug = Fahrrad(x_position, y_position, leergewicht, aktuelle_geschwindigkeit)

elif input_allgemein == "Fahrzeug":
    aktuelle_geschwindigkeit = konfiguriere_geschwindigkeit()
    leergewicht = konfiguriere_leergewicht()
    x_position = konfiguriere_x_Position()
    y_position = konfiguriere_y_Position()
    fahrzeug = Fahrrad(x_position, y_position, leergewicht, aktuelle_geschwindigkeit)

else:
    print("Sie haben eine ungültige Eingabe übergeben! Bitte geben sie nur "
          "gültige Fortbewegunggsmittel an!")

print(fahrzeug)
input_beschleunigung = int(input("Um wie viel soll ihr Fahrzeug beschleunigen?\n"))
fahrzeug.beschleunigen(input_beschleunigung)
print(fahrzeug)


