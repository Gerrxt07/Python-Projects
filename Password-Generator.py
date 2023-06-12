# Passwort Generator by Gerrxt
# Version: 1.1

import random

# Characters to be used
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_."

# Length
length = 16

# Generate password
password = "".join(random.sample(characters, length))

# Password output
print(password)

# Password output to file
datei = open("password.txt", "w")
datei.write(password)
datei.close()                                   
