def bonsupunkte(bonuspunkte_pro_tag):
    Tag = 1
    for zahl in range(0, bonuspunkte_pro_tag):
        Tag += zahl
        print(f"Ab Tag {Tag} erhält man pro Einkauf: {zahl + 1} Bonuspunkte")


bonsupunkte(int(input(f"Geben sie ihre erwünschten Bonuspunkte pro Tag an!\n")))