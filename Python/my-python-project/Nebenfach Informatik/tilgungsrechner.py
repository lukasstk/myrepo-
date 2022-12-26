def tilgungsrechner(dahrlehnsbetrag, zinssatz, tilgungssatz):
    Restschuld = dahrlehnsbetrag
    Jahresrate = Restschuld * (zinssatz + tilgungssatz)/100.0

    Jahr = 1
    while Restschuld > 0.0:
        Jahreszinsen = Restschuld * zinssatz / 100
        if Restschuld + Jahreszinsen > Jahresrate:
            Jahrestilgung = Jahresrate - Jahreszinsen
            Restschuld = Restschuld - Jahrestilgung
        else:
            Jahrestilgung = Restschuld
            Restschuld = 0

        print(f"Jahr {Jahr}:\n    Jahreszinsen: {Jahreszinsen}\n    "
              f"Jahrestilgung: {Jahrestilgung}\n    Restschuld: {Restschuld}")
        Jahr += 1






