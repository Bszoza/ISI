class dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def sound(self):
        print(self.name," is barking!")
dog1 = dog("Rubi",2,"White")
dog1.sound()
dog2 = dog("Dino",4,"Black")
dog2.sound()
dog3 = dog("Tosia",1,"Red")
dog3.sound()





