# This is the example of Single inhertance
class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("every sounds made by animals")
class Cat(animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def make_sound(self):
        print("Meooo !!")
a=animal("Dog","Lebra")
a.make_sound()
b=Cat("Cat","Big Cat")

b.make_sound()
