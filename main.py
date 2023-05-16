import random
class Animal:
    def __init__(self, species, name, age, health, hunger, happiness):
        super().__init__()
        self.apecies=species
        self.name=name
        self.age=age
        self.health=health
        self.hunger=hunger
        self.happines=happines
    def grow(self):
        self.age+=1
        self.health=random.randint(0, 10)
        self.hunger=random.randint(0, 10)
        self.happines=random.randint(0, 10)
    def eat(self):
        if self.hunger >=6:
            self.health += random.randint(0, 5)
            self.happines += random.randint(0, 5)
            self.hunger -= random.randint(5, 7)
        else:
            print(self.name, "hungry")
    def play(self):
        pass #happines

class Zoo:
    def __init__(self):
        super.__init__()
        self.animal=[]
