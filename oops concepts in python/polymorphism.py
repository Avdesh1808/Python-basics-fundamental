# example of polymorphism it means many forms of class examples
# method overriding
class animal: # This is base class to be overriding
    def speak(self):
        pass
class cat(animal):
    def speak(self):
        return "mioo!"
class dog(animal):
    def speak(self):
        return "bark!"
class lion(animal):
    def speak(self):
        return "roar!"
class car(animal):
    def drive(self): #(1) is we change its atributs drive(self) into speak(self) so the output will be Hon! in terminal
        return "Honk!" 
animals=[cat(),dog(),lion(),car()]# in the last class car will give non! in  output which is different from base class atributs check (1)
for animal in animals:
    print(animal.speak())
