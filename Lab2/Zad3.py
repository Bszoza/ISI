import random
import string

def generuj_hasla():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6)) #Generuje słowo o dlugosci 6 losowych znakow

with open("passwords.txt","w") as f: #w = write
    for _ in range(1000):
        f.write(generuj_hasla()+"\n")

