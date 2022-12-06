# Passwort Generator by Gerrxt
# Version: 1.0

import random

# Characters to be used
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+."

# Length
length = 32

# Generate password
password = "".join(random.sample(characters, length))

# Password output
print(password)

# Password output to file
datei = open("Password.txt", "w")
datei.write(password)
datei.close()                                   
