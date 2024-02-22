"""Program to show the OOPS concept of inheritance which is a way of creating new class
for using details of existing class without modifying it.
The newly formed class is a derived class (or child class).
Similarly, the existing class is a base class (or parent class)."""

#The child class Penguin inherits the functions of parent class Bird.
# We can see this from swim() method.
# Again, the child class Penguin modified the behavior of parent class Bird.
# We can see this from whoisThis() method.
# Furthermore, we extend the functions of parent class Bird, by creating a new run() method.


# Parent/Base class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# Child/Derived class
class Penguin(Bird):

    def __init__(self):
        #Super() function before __init__() method  to pull the content of __init__() method
        #from the parent class Bird into the child class Penguin.
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Runs faster")

# Object of penguin
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()