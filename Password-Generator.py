# Passwort Generator by Gerrxt
# Version: 1.0

import random

# Zeichen die verwendet werden sollen
zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

# Passwortlänge
laenge = 32

# Passwort generieren
passwort = "".join(random.sample(zeichen, laenge))

# Passwort ausgeben
print(passwort)

# Passwort in Datei schreiben
datei = open("Passwort.txt", "w")
datei.write (passwort)
datei.close()                                   
