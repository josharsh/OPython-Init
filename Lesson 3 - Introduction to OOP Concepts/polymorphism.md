## ** Python Polymorphism **

(Source: [https://www.geeksforgeeks.org/polymorphism-in-python/](https://www.geeksforgeeks.org/polymorphism-in-python/))

What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.

EXAMPLES (adapted from Geeks for Geeks source cited above): 

# Polymorphism and class methods:
In this example, objects of class Car() and class Boat() are created. Both classes share class 
methods speed() and color(), which allows for an instance of both a Boat() and a Car() to be looped over
in a for loop, calling the class methods speed() and color() on each object in turn 

```
class Car():
    # class method
    def speed(self):
        print("My top speed is 50 miles per hour")
    
    # class method
    def color(self):
        print("My color is red")

class Boat():
    # class method
    def speed(self):
        print("My top speed is 30 knots")
    
    # class method
    def color(self):
        print("My color is blue")

# create instances of Car and Boat classes
example_car = Car()
example_boat = Boat()

# loop through tuple containing car and boat instances
# and access speed() and color() class methods for each 
for vehicle in (example_car, example_boat):
    vehicle.speed()
    vehicle.color()
```

# Polymorphism and Inheritance
In this example, classes Car() and Boat() inherit from the Vehicle() class - allowing instances of 
Car() and Boat() objects to be initialized using the same init method. The print_speed() method is changed
in each child class (which is called "method overriding") so that print_speed() behaves differently when
called on a Car() instance versus a Boat() instance. The print_color() method behaves the same for Car() and Boat() objects, as that method was not changed after being inherited from the parent Vehicle() class. 
```
class Vehicle():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def print_speed(self):
        print("My top speed is: {}".format(self.speed))

    def print_color(self): 
        print("My color is: {}".format(self.color))

class Car(Vehicle):
    # uses method override to include miles per hour 
    def print_speed(self):
        print("My top speed is: {} miles per hour".format(self.speed))

class Boat(Vehicle):
    # uses method override to include knots 
    def print_speed(self):
        print("My top speed is: {} knots".format(self.speed))

# both Car and Boat instances are created using same init method from
# Vehicle class 
example_car = Car(50, "blue")
example_boat = Boat(70, "red")

# Car instance uses miles per hour when printing speed, otherwise behaves the same 
example_car.print_speed()
example_car.print_color()

# Boat instance uses knots when printing speed, otherwise behaves the same 
example_boat.print_speed()
example_boat.print_color()
```

# Polymorphism and Functions + Objects: 
In this example, two different classes, Car() and Boat(), are declared, each with a print_speed()
and print_color() method. Then, a function access_class_methods(object) is declared, which calls
the print_speed() and print_color() class methods on whatever object is passed in as a parameter to the function. This function is then passed an instance of a Boat() object, as well as an instance of a Car() object. The function is able call the class methods of both objects. 

```
class Car():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def print_speed(self):
        print("My top speed is: {} miles per hour".format(self.speed))

    def print_color(self):
        print("My color is: {}".format(self.color))

class Boat():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def print_speed(self):
        print("My top speed is: {} knots".format(self.speed))

    def print_color(self):
        print("My color is: {}".format(self.color))

# this function calls class methods print_speed() and print_color() on whatever object is passed in to the 
# function as a parameter 
def access_class_methods(object):
    object.print_speed()
    object.print_color()

# initialize instances of Car() and Boat() classes
example_car = Car(50, "Blue")
example_boat = Boat(70, "Red")

# call same function on both instances successfully 
access_class_methods(example_boat)
access_class_methods(example_car)
```

