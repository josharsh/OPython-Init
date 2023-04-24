#This example how to effectively use class methods and instance methods with class variables and instance variables.

class Stock:
     #class variable
     company = "Example"

     #instance
     def __init__(self,name,quantity,price):
          self.name=name
          self.quantity=quantity
          self.price=price


     #instance method
     def displayStock(self):
          return("The name of the product is "+self.name +" of quantity " + str(self.quantity) + ".Price is "+str(self.price))
    

     @classmethod
     def info(cls):
         return cls.company
#creating 2 objects
obj1 = Stock('clothes',20,1200)
obj2 = Stock('shoes',3,3000)


print(obj1.displayStock())
print(Stock.info())
