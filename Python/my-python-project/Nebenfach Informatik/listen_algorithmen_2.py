from konverter import *

input_aktion = None
while input_aktion != "Beenden":
    input_aktion = input("Welche Aktion möchten sie durchführen? (Mischen, Teilmenge oder Beenden)\n")
    if input_aktion == "Mischen":

        user_input1 = str_to_list(input("Übergeben sie erste Liste, die sie mischen wollen.\n"))
        user_input2 = str_to_list(input("Übergeben sie zweite Liste, die sie mischen wollen.\n"))
        gemischte_liste = []
        while len(gemischte_liste) != len(user_input1) + len(user_input2):
            for element in range(max(len(user_input1), len(user_input2))):
                if element < len(user_input1):
                    gemischte_liste.append(user_input1[element])
                if element < len(user_input2):
                    gemischte_liste.append(user_input2[element])
        print(gemischte_liste)
    elif input_aktion == "Teilmenge":
        user_input_a = str_to_list(input("Übergeben sie eine Liste a.\n"))
        user_input_b = str_to_list(input("Übergeben sie eine Liste b .\n"))
        alle_elemente_gefunden = True
        for element_a in range(len(user_input_a)):
            element_a_gefunden = False
            for element_b in range(len(user_input_b)):
                if user_input_a[element_a] == user_input_b[element_b]:
                    element_a_gefunden = True
            if not element_a_gefunden:
                alle_elemente_gefunden = False
        print(user_input_a, user_input_b)
        if alle_elemente_gefunden:
            print("a ist Teilmengge von b!")
        else:
            print("a ist keine Teilmenge von b!")
    elif input_aktion == "Beenden":
        None
    else:
        print("Sie haben eine falsche Eingabe getätigt!")
