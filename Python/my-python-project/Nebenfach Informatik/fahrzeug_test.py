from fahrzeug import Fahrzeug

auto = Fahrzeug(1, 2, 4, 1234.5, 100.0)
fahrrad = Fahrzeug(3, 4, 2, 33.3, 18.3)

print("Auto: aktuelle Geschwindigkeit=" + str(auto.aktuelle_geschwindigkeit))

print("Fahrrad: aktuelle Geschwindigkeit=" + str(fahrrad.aktuelle_geschwindigkeit))

auto.beschleunigen(11.1)

print("Auto: aktuelle Geschwindigkeit=" + str(auto.aktuelle_geschwindigkeit))

print("Fahrrad: aktuelle Geschwindigkeit=" + str(fahrrad.aktuelle_geschwindigkeit))

fahrrad.fahren(5, 3)

