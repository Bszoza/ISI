import random
wygrana = False
rand = random.randint(1,100)
count_guess=0
print("Zgadnij liczbe z przedzialu 1 do 100:")
print(rand)
while wygrana != True:
    guess=input()
    if int(guess)==rand:
        count_guess=count_guess+1
        print("Udalo Ci sie zgadnac!")
        print("W probie numer: ", count_guess)
        wygrana=True
        continue
    elif int(guess)<rand:
        print("Wylosowana liczba jest wieksza")
        count_guess = count_guess + 1
    elif int(guess) > rand:
        print("Wylosowana liczba jest mniejsza")
        count_guess = count_guess + 1






