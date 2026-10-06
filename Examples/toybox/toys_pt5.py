class Toybox:
    def __init__(self):
        self.allMyToys = []

    def addToy(self, toy):
        self.allMyToys.append(toy) 

    def toString(self):
        if len(self.allMyToys) == 0:
            msg = "The toybox is empty."
        else:
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

# this class inherits attributes from its parent class Toy ^
class Lego(Toy):
    def __init__(self, colour, setName, pieceCount):
        self.name = "Lego set"
        self.colour = colour
        self.setName = setName
        self.pieceCount = pieceCount

    def getSetInfo(self):
        return f"I am a {self.name} called {self.setName}, and I have a piece count of: {self.pieceCount}."

# this class also inherits attributes from its parent class Toy
class Hotwheel(Toy):
    def __init__(self, colour, make, model):
        self.name = "Hotwheels car"
        self.colour = colour
        self.make = make
        self.model = model

    def getCarInfo(self):
        return f"I am a {self.name} based off of a {self.make} {self.model}."

firetruck = Lego("Red", "Firetruck", 1024) 
spaceship = Lego("Blue", "Spaceship", 2048)
awesomeFastCar = Hotwheel("Orange", "Toyota", "Prius")

print("--- Results ---")
theToybox = Toybox()
print()
print("to string without any toys:")
print(theToybox.toString())
print()
theToybox.addToy(firetruck)
theToybox.addToy(awesomeFastCar)
print()
print("to string after adding 2 toys")
print(theToybox.toString())
print()
theToybox.addToy(spaceship)
print("after adding a 3rd toy")
print(theToybox.toString())
print()
print("Toy 1:")
print(f"{theToybox.allMyToys[0].toString()}")
print()
print("Toy 2:")
print(f"{theToybox.allMyToys[1].toString()}")
print()
print("Toy 3:")
print(f"{theToybox.allMyToys[2].toString()}")