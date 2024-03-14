counter3 = 0
counter4 = 0
for x in range(1,100):
   if x%3==0:
       print(x)
       counter3 += 1
   elif x%4==0:
       print(x)
       counter4 += 1
print("Ilosc iczb podzielnych przez 3: "+str(counter3))
print("Ilosc iczb podzielnych przez 4: "+str(counter4))




