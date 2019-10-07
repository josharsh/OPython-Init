class Animals: #parent Class
    def __init__(self, name):
        self.name = name        
    def animal_info(self):
        print("hey! My name is "+self.name )
        
class Dog(Animals): #Derived Class Dog from Animals
    def sound(self):
        Animals.animal_info(self) #Dog can use this method from Parent class Animals
        print("Woof! Woof!") 

class Cat(Animals):
    def sound(self):
        Animals.animal_info(self)
        print("Meow! Meow!")

class Pig(Animals):
    def sound(self):
        Animals.animal_info(self)
        print("Oink! Oink!")

class Cow(Animals):
    def sound(self):
        Animals.animal_info(self)
        print("Moo! Moo!")
        
sven = Dog("Sven")
sven.sound()
print("_"*10)
ulla_britta = Cat("Ulla Britta")
ulla_britta.sound()

