word = input("Podaj wyraz: ")
#Iteruje od ostatniej litery do pierwszej
#len zwraca mi długosc wyrazu
for x in range(len(word)-1,-1,-1):
    print(word[x])