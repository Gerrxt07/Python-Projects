# Passwort Generator by Gerrxt
# Version: 1.0

import random

# Characters to be used
zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+."

# Length
laenge = 32

# Generate password
passwort = "".join(random.sample(zeichen, laenge))

# Password output
print(passwort)

# Password output to file
datei = open("Passwort.txt", "w")
datei.write(passwort)
datei.close()                                   
