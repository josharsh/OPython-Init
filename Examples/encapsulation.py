# Python program to demonstrate private members and the OOP concept of Encapsulation

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "HelloWorld"
        self.__c = "HelloWorld"

# Creating a derived class
class Derived(Base):
    def __init__(self):
        
        # Calling constructor of
        # Base class
        Base.__init__(self) 
        print("Calling private member of base class: ")
        print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)
#print(obj1.c)
#obj2 = Derived()

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class 
# is called inside derived class
