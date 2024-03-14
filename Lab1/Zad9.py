word = input()
#usuwam spacje przecinki i kropki ze zdania
word = word.replace(" ", "")
word = word.replace(".", "")
word = word.replace(",", "")
#Pozbywam sie wielkich liter
word = word.lower()
#Odwracam slowo
wordrev = word[::-1]
print(word)
print(wordrev)
if wordrev == word:
    print("Slowo jest palindromem")
else:
    print("Slowo nie jest palindromem")





