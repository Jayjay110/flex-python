import os

# Bestandsnaam in variabele zetten
bestandsnaam = "nieuwe_naam.txt"

# Vraag de huidige map op en sla op in variabele: huidige_map
huidige_map = os.getcwd()

# met de os.path module kun je paden naar bestanden samenstellen
volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("Dit bestand gaan we hernoemen: " + volledige_pad)

nieuwe_naam = input("Nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    # Map en nieuwe bestandsnaam gebruiken om volledige pad samen te stellen
    volledige_nieuwe_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + volledige_nieuwe_pad)

    # Bestand hernoemen 
    os.rename(volledige_pad, volledige_nieuwe_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")
