def wczytaj_tekst(sciezka):
    odpowiedz = ""
    with open(sciezka, 'r') as file: # r = read
        for line in file:
            for word in line.split(): # czytaj po słowie
                if len(word) > len(odpowiedz):
                    odpowiedz = word
    return odpowiedz

print(wczytaj_tekst("test.txt"))


