# parent class defined 
class animal:
        def __init__(self, dogname):
                self.name= dogname

        def define(self):
                print("my name is dog") 

        def eat(self,food):
                print("i eat"+ food)

#child class defined
class dog(animal):
        def eat(self,food):
                print("i eat "  + food)

#initialize dog class
d=dog("mike")
#using parent's function
d.define()
#using own's function
d.eat("dog's things")
