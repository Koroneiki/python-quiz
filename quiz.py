import random
import time

# Fragen und Antworten
fragen_antworten = {
    "Bayern": "München",
    "Nordrhein-Westfalen": "Düsseldorf",
    "Baden-Württemberg": "Stuttgart",
    "Niedersachsen": "Hannover",
    "Hessen": "Wiesbaden",
    "Sachsen": "Dresden",
    "Rheinland-Pfalz": "Mainz",
    "Berlin": "Berlin",
    "Brandenburg": "Potsdam",
    "Schleswig-Holstein": "Kiel",
}

# Funktion für das Quiz
def quiz():
    richtig = 0

    # Zufällige Reihenfolge der Fragen
    fragen = list(fragen_antworten.keys())
    random.shuffle(fragen)

    for frage in fragen:
        antwort = input(f"Frag: Was ist die Hauptstadt von {frage}? ")

        # Überprüfen der Antwort
        if antwort.lower() == fragen_antworten[frage].lower():
            print("Richtig!\n")
            richtig += 1
        else:
            print(f"Falsch. Die richtige Antwort ist: {fragen_antworten[frage]}\n")

    # Anzeige der Ergebnisse
    print(f"Quiz beendet! Du hast {richtig} von {len(fragen)} Fragen richtig beantwortet.")
    time.sleep(10)  # Warte 10 Sekunden

# Quiz starten
print("Willkommen zum deutschen Bundesländer-Hauptstädte-Quiz!\n")
quiz()
