"""By Using OOPS in Python, we can restrict access to methods and variables.
This way of preventing data from direct modification is called encapsulation and is done by using underscore as prefix i.e single “ _ “ or double “ __“.
"""

# In the following program, we defined a class Bag. We use __init__() method to store the maximum selling price of Bag.
# We tried to modify the price. However, we can’t change it because Python treats the __maxprice as private attributes.
# To change the value, we used a setter function i.e setMaxPrice() which takes price as parameter.

class Bag:

    def __init__(self):
        # maxprice is a private attribute
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

# Creating object of class Computer
c = Bag()
c.sell()

# Change the price of private attribute
c.__maxprice = 1000
c.sell() #can't change it

# Using setter function we xan change the value of private attribute
c.setMaxPrice(1000)
c.sell()

"""Output :-
Selling Price: 900
Selling Price: 900
Selling Price: 1000
 """

