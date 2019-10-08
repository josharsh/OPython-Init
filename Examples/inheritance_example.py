class Animals: #parent Class
    def __init__(self, name): #__init__  is the construction in Python #self variable represents the name of the object itself
        self.name = name        
    def animal_info(self):
        print("hey! My name is "+self.name ) #In this function the Animal introduces itself
        
class Dog(Animals): #Derived Class Dog from parent class Animals
    def sound(self):
        Animals.animal_info(self) #Dog can use this method from Parent class Animals
        print("Woof! Woof!") #A dog goes Woof! Woof!

class Cat(Animals):
    def sound(self):
        Animals.animal_info(self) #Similarly, Cat can also used this function originally described in parent class Animals
        print("Meow! Meow!") #A cat goes Meow! Meow!

#Similary we can create as many Child classes from our parent class as we like!
class Pig(Animals):
    def sound(self):
        Animals.animal_info(self)
        print("Oink! Oink!")

class Cow(Animals):
    def sound(self):
        Animals.animal_info(self)
        print("Moo! Moo!")
        
sven = Dog("Sven") #We have created a Dog object named him Sven
sven.sound() #we are calling the sound function described in the derived class Dog
print("_"*10) #this is just for sepration
ulla_britta = Cat("Ulla Britta") #we have created a Cat object and named her Ulla Britta
ulla_britta.sound() #we are calling the sound function described in the derived class Cat

