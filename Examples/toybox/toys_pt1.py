# this here is a toy class. 

class Toy():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def toString(self):
        return f"I am a toy called {self.name}, and I am coloured {self.colour}!"


# instantiate a toy object:
teddy = Toy("Bob", "Brown")

# before running.. think about what the following might output:
print (teddy.toString())