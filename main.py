import random
class Animal:
    def __init__(self, species, name, age, health, hunger, happines):
        super().__init__()
        self.species=species
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
        if self.happines>=5:
            self.health+=random.randint(0, 5)
            self.hunger += random.randint(0, 5)
            self.happines += random.randint(0, 5)
        else:
            print(self.name, "does not want to play")
    def __str__(self):
        return f"{self.species} - {self.name} ({self.age} years old)\n" \
        f"Health: {self.health}\nHunger: {self.hunger}\nHappines: {self.happines}\n"

class Zoo:
    def __init__(self):
        super.__init__()
        self.animals=[]

    def add_animal(self, animal):
        self.animals.append(animal)
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
    def feed_all(self):
        if animal in self.animals:
            animal.eat()
    def ply_with(self, animal):
        if animal in self.animals:
            animal.play()
    def grow_all(self):
        if animal in self.animals:
            animal.grow()
