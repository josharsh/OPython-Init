class Animal:

    def __init__(self):
        print("Animal created")

    def defineMe(self):
        print("This is parent class Animal")

    def eat(self):
        print("All animals have a common property, they eat!")

class Lion(Animal):

    def __init__(self):
        super().__init__()
        print("Lion created")

    def defineMe(self):
        print("This is child class Lion")

    def prey(self):
        print("I am the king of the jungle!")


# Initializing 'simba the lion'...
simba = Lion()

# Let simba define himself...
simba.defineMe()

# simba is a lion, but can also eat! It is a child of Animal class afterall!
simba.eat()

# And obviously, simba can prey, and it will! Beware!!
simba.prey()
