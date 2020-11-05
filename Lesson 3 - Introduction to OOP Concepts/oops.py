#class
class Tiger:
    pass

#object
obj = Tiger()

#Creating Class and Object in Python
class Tiger:

    # class attribute
    species = "animal"

    # instance attribute
    def __init__(self, name, age):
        """
        Initialize a new age.

        Args:
            self: (todo): write your description
            name: (str): write your description
            age: (str): write your description
        """
        self.name = name
        self.age = age

# instantiate the Tiger class
blu = Tiger("Blu", 10)
woo = Tiger("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

'''OUTPUT
Blu is a tiger
Woo is also a tiger
Blu is 10 years old
Woo is 15 years old'''

#Creating Methods in Python
class Tiger:
    
    # instance attributes
    def __init__(self, name, age):
        """
        Initialize a new age.

        Args:
            self: (todo): write your description
            name: (str): write your description
            age: (str): write your description
        """
        self.name = name
        self.age = age
    
    # instance method
    def growl(self, growl):
        """
        Return a string representation of the : class : lxml. element }.

        Args:
            self: (todo): write your description
            growl: (todo): write your description
        """
        return "{} growls {}".format(self.name, growl)

    def hunt(self):
        """
        Returns the hunt name of the hunt.

        Args:
            self: (todo): write your description
        """
        return "{} is now hunting".format(self.name)

# instantiate the object
blu = Tiger("Blu", 10)

# call our instance methods
print(blu.growl("'GROWL'"))
print(blu.hunt())

'''OUTPUT
Blu growls 'GROWL'
Blu is now hunting'''

#Use of Inheritance in Python
# parent class
class Bird:
    
    def __init__(self):
        """
        Initialize the state

        Args:
            self: (todo): write your description
        """
        print("Bird is ready")

    def whoisThis(self):
        """
        WhoisThis

        Args:
            self: (todo): write your description
        """
        print("Bird")

    def swim(self):
        """
        Swimizes the swimplements

        Args:
            self: (todo): write your description
        """
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        """
        Initialize the init

        Args:
            self: (todo): write your description
        """
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        """
        WhoisThis

        Args:
            self: (todo): write your description
        """
        print("Penguin")

    def run(self):
        """
        Run the command

        Args:
            self: (todo): write your description
        """
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

'''OUTPUT
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster'''

#Data Encapsulation in Python
class Computer:

    def __init__(self):
        """
        Initialize the object.

        Args:
            self: (todo): write your description
        """
        self.__maxprice = 900

    def sell(self):
        """
        Prints the max maxprice

        Args:
            self: (todo): write your description
        """
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        """
        Sets the maximum.

        Args:
            self: (todo): write your description
            price: (int): write your description
        """
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

'''OUTPUT
Selling Price: 900
Selling Price: 900
Selling Price: 1000'''

#Using Polymorphism in Python
class Parrot:

    def fly(self):
        """
        Print out ]

        Args:
            self: (todo): write your description
        """
        print("Parrot can fly")
    
    def swim(self):
        """
        Swimizes the swimplements

        Args:
            self: (todo): write your description
        """
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        """
        Print out ]

        Args:
            self: (todo): write your description
        """
        print("Penguin can't fly")
    
    def swim(self):
        """
        Swimizes the swimplements

        Args:
            self: (todo): write your description
        """
        print("Penguin can swim")

# common interface
def flying_test(bird):
    """
    Flying test test.

    Args:
        bird: (todo): write your description
    """
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

'''OUTPUT
Parrot can fly
Penguin can't fly'''
