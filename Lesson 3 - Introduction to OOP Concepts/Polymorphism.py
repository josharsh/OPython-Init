# Example of Polymorphism

class Animal:
    def speak(self):
        pass  # Abstract idea — every animal speaks differently

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function showing polymorphism
def make_animal_speak(animal):
    print(animal.speak())

# Using different animal objects
dog = Dog()
cat = Cat()
cow = Cow()

for animal in [dog, cat, cow]:
    make_animal_speak(animal)


#OUTPUT:
    # Woof!
    # Meow!
    # Moo!
