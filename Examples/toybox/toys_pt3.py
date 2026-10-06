# this is the base class
class Toy:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def toString(self):
        return f"I am a toy called {self.name}, and I am coloured {self.colour}!"

# this class also inherits attributes from its parent class Toy
class Hotwheel(Toy):
    def __init__(self, colour, make, model):
        self.name = "Hotwheels car"
        self.colour = colour
        self.make = make
        self.model = model

    def getCarInfo(self):
        return f"I am a {self.name} based off of a {self.make} {self.model}."

awesomeFastCar = Hotwheel("Orange", "Toyota", "Prius")

print(awesomeFastCar.toString())
print(awesomeFastCar.getCarInfo())