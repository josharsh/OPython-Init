class Toybox:
    def __init__(self):
        self.allMyToys = []

    def addToy(self, toy):
        self.allMyToys.append(toy) 

    def toString(self):
        msg = 'All toys:\n'
        for toy in self.allMyToys:
            msg += f"A {toy.colour} coloured {toy.name}\n"

        return msg

# this here is a toy class. 
class Toy():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def toString(self):
        return f"I am a toy called {self.name}, and I am coloured {self.colour}!"


# instantiate a toy object:
teddy = Toy("Bob", "Brown")
car = Toy("Car", "Red")
theToybox = Toybox()

theToybox.addToy(teddy)
theToybox.addToy(car)

print(theToybox.toString())