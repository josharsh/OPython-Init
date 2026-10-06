# this is the base class
class Toy:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def toString(self):
        return f"I am a toy called {self.name}, and I am coloured {self.colour}!"

# this class inherits attributes from its parent class Toy ^
class Lego(Toy):
    def __init__(self, colour, setName, pieceCount):
        self.name = "Lego set"
        self.colour = colour
        self.setName = setName
        self.pieceCount = pieceCount

    def getSetInfo(self):
        return f"I am a {self.name} called {self.setName}, and I have a piece count of: {self.pieceCount}."


# instantiate a toy object:
firetruck = Lego("Red", "Firetruck", 1024) 

# before running have a think about what this might output?
print(firetruck.getSetInfo())

# because firetruck is a child of Toy it also inherits methods from Toy aswell
print(firetruck.toString())