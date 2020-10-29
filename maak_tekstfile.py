bestand = open("test.txt", "w")

# Een tekst naar het bestand schrijven
bestand.write("Test 123!");  

# Vergeet bestand niet te sluiten!
bestand.close()

bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")

import io

# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
inhoud = bestand2.read()

# De inhoud op het scherm zetten:
print("De inhoud van het bestand is:")
print(inhoud)
