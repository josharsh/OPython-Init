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
        self.name = name
        self.age = age
    
    # instance method
    def growl(self, growl):
        return "{} growls {}".format(self.name, growl)

    def hunt(self):
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
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
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

# Parent Class
class Person:
    def __init__(self, fName, lName, birthday, phone_number):
        self.fName = fName
        self.lName = lName
        self.birthday = birthday
        self.phone_number = phone_number
        print("Person instantiated.")

    def getName(self):
        print(self.fName, self.lName)

    def getNumber(self):
        print(self.phone_number)

# Child Class
class Student(Person):
    def __init__(self, fName, lName, birthday, phone_number,
                 gradYear, major, school):
        super().__init__(fName, lName, birthday, phone_number)
        self.gradYear = gradYear
        self.major = major
        self.school = school

    def getGradYear(self):
        print(self.gradYear)

    def getMajor(self):
        print(self.major)

    def getSchool(self):
        print(self.school)

jack = Student("Jackson", "Maxwell", "09/24/2020", "(959) 943-9596",
               2022, "Computer Science", "University of California - San Diego")
jack.getName()
jack.getGradYear()
jack.getMajor()
jack.getSchool()

'''OUTPUT
Person instantiated.
Jackson Maxwell
2022
Computer Science
University of California - San Diego'''


#Data Encapsulation in Python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
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
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
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
