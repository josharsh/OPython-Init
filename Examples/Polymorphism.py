#This is an Example of Polymorphism in Python

# polymorphism means the same function name (but different signatures) being used for different types.

class Fruit:

    def intro(self):
        print("There are many types of fruit :) ")

    def sweet(self):
        print("Some of them are sweet! ")

class Mango(Fruit):

    def sweet(self):
        print("Mango is sweet :) ")

class Grapes(Fruit):

    def sweet(self):
        print("Grapes are sour not sweet :x")

obj_Fruit = Fruit()
obj_Mango = Mango()
obj_Grapes = Grapes()

obj_Fruit.intro()
obj_Fruit.sweet()
obj_Mango.sweet()
obj_Grapes.sweet()



