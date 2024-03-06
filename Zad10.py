import random
wygrana = False
rand = random.randint(1,100)
print("Zgadnij liczbe z przedzialu 1 do 100:")
print(rand)
while wygrana != True:
    guess=input()
    if int(guess)==rand:
        print("Udalo Ci sie zgadnac!")
        wygrana=True
        continue
    elif int(guess)<rand:
        print("Wylosowana liczba jest wieksza")
    elif int(guess) > rand:
        print("Wylosowana liczba jest mniejsza")






