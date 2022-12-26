# 4-3 Benzinverbrauch
BENZIN_PRO_100KM = 6.7
ÖL_PRO_1000KM = 0.6


def verbrauch(fahrstrecke):
    benzin_pro_1km = BENZIN_PRO_100KM / 100
    öl_pro_1km = ÖL_PRO_1000KM / 1000

    benzin_verbrauch = fahrstrecke * benzin_pro_1km
    öl_verbrauch = fahrstrecke * öl_pro_1km

    '''oder:
    benzin_verbrauch = fahrstrecke * BENZIN_PRO_100KM / 100
    öl_verbrauch = fahrstrecke * ÖL_PRO_1000KM / 1000 '''

    print(f"Dein Benzinverbrauch beträgt: {benzin_verbrauch} und dein Ölverbrauch beträgt: {öl_verbrauch}")
    return benzin_verbrauch, öl_verbrauch


verbrauch(0.1)
verbrauch(3)
verbrauch(100.13)

# 4-4 Pizza
PIZZA_BASIS_PREIS = 5.50
BELAG_PREIS = 0.75


def pizzaservice(anzahl_belag):
    pizza_gesamt_preis = PIZZA_BASIS_PREIS + (BELAG_PREIS * anzahl_belag)
    print(f"Der Preis deiner Pizza beträgt: {pizza_gesamt_preis}")
    return pizza_gesamt_preis


pizzaservice(1)
pizzaservice(5)
pizzaservice(23)

# 4-5 int_sortierung
x = 5
y = 3
z = 1

'''if x < y < z:
    print(f"{z} ist größer als {y} und {y} ist größer als {x}")
elif y < x < z:
    print(f"{z} ist größer als {x} und {x} ist größer als {y}")
elif x < z < y:
    print(f"{y} ist größer als {z} und {z} ist größer als {x}")
elif z < x < y:
    print(f"{y} ist größer als {x} und {x} ist größer als {z}")
elif z < y < x:
    print(f"{x} ist größer als {y} und {y} ist größer als {z}")
elif y < z < x:
    print(f"{x} ist größer als {z} und {z} ist größer als {y}")'''


def sortieren2(zahl1, zahl2):
    if zahl1 < zahl2:
        return zahl1, zahl2
    else:
        return zahl2, zahl1


x, y = sortieren2(x, y)
x, z = sortieren2(x, z)
y, z = sortieren2(y, z)
print(x, y, z)

# 4-6 steuerfantasia
GRENZEN_LEDIG = [9275, 37650, 91150, 190150, 413350, 415050]
GRENZEN_VERHEIRATET = [18550, 75300, 151900, 231450, 413350, 466950]
STEUERSATZ = [10, 15, 25, 28, 33, 35, 39.6]
def steuersatz(brutto_gehalt, ledig):
    grenzen = GRENZEN_LEDIG
    if not ledig:
        grenzen = GRENZEN_VERHEIRATET
    for index in range(6):
        if brutto_gehalt <= grenzen[index]:
            return STEUERSATZ[index]
    return STEUERSATZ[len(STEUERSATZ) - 1]

def steuerfantasia(brutto_gehalt, ledig):
    netto_gehalt = brutto_gehalt - (brutto_gehalt * (steuersatz(brutto_gehalt, ledig) / 100))
    print(netto_gehalt)
    return netto_gehalt


steuerfantasia(600000, False)