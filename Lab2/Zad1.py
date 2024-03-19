class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self): #Funkcja do nadpisania
        pass  #nie rob nic


class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Hau Hau"


class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Miau Miau!"


class Fox(Animal):
    def sound(self):
        return "What does the fox say!?"