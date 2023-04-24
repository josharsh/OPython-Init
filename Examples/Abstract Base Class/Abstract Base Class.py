#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 1


from abc import ABC, abstractmethod 

class Parent(ABC):
    def message(self):
        pass
    
class child1(Parent):
    def message(self):
        print("This is first subclass")
        
class child2(Parent):
    def message(self):
        print("This is second subclass")
        
# driver code

ob1=child1()
ob1.message()

ob2=child2()
ob2.message()


# In[6]:


# Task 2

from abc import ABC, abstractmethod 

class Bank(ABC):
    def getBalance(self):
        pass
    
class BankA(Bank):
    def getBalance(self):
        print("$100 is deposited in the bank.")
        
class BankB(Bank):
    def getBalance(self):
        print("$150 is deposited in the bank.")
        
class BankC(Bank):
    def getBalance(self):
        print("$200 is deposited in the bank.")    
        
# driver code

ob1=BankA()
ob1.getBalance()

ob2=BankB()
ob2.getBalance()        

ob3=BankC()
ob3.getBalance()        


# In[2]:


# Task 3

from abc import ABC, abstractmethod 

class Marks(ABC):
    def getPercentage(self):
        pass
    
class studentA(Marks):
    
    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        
    def getPercentage(self,marks1,marks2,marks3) :
        percentage=((self.marks1+self.marks2+self.marks3)*100)/300
        print("The percentage achieved is",percentage,"%")
        
class studentB(Marks): 
    
    def __init__(self,marks1,marks2,marks3,marks4):
        
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.marks4 = marks4
        
    def getPercentage(self,marks1,marks2,marks3,marks4) :
        percentage=((self.marks1+self.marks2+self.marks3+self.marks4)*100)/400
        print("The percentage achieved is",percentage,"%")
        
# driver code

ob1=studentA(80,78,87)
ob1.getPercentage(80,78,87)

ob2=studentB(80,78,87,78)
ob2.getPercentage(80,78,87,78)


# In[3]:


# Task 4

from abc import ABC, abstractmethod 

class Abstract(ABC):
    def __init__(self,x="This is the constructor of abstract class"):
        self.x=x
        
    def a_method(self):
        pass
    
    def concreteMethod():
        print("This is a normal method of abstract class")
        
class subClass(Abstract):
    
    Abstract.concreteMethod() 
    def a_method(self):
        print("This is abstract method")
        
# driver code 

ob=subClass()
ob.a_method()


# In[10]:


# Task 5

from abc import ABC, abstractmethod 

class Animals(ABC):
    
    def cats(self):
        pass
    
    def dogs(self):
        pass
    
class Cats(Animals):
    
    def cats(self):
        print("Cat Meows")
        
class Dogs(Animals):
    
    def dogs(self):
        print("Dogs barks") 
        
# driver code

ob1=Cats()
ob1.cats()

ob2=Dogs()
ob2.dogs()


# In[11]:


# Task 6

from abc import ABC, abstractmethod 

class Shapes(ABC):
    
        def RectangleArea(length,breadth):
            pass
        
        def SquareArea(sides):
            pass
        
        def CircleArea(radius):
            pass
        
class Area(Shapes):
    
        def RectangleArea(self,length,breadth):
            area=length*breadth
            print("The area of rectangle is",area,"units.")
            
        def SquareArea(self,side):
            area=side**2
            print("The area of square is",area,"units.")
            
        def CircleArea(self,radius):
            area=3.142*(radius**2)
            print("The area of circle is",area,"units.")
            
# Driver code

obj=Area()
obj.RectangleArea(2,4)
obj.SquareArea(2)
obj.CircleArea(5)


# In[13]:


# Task 7

from abc import ABC, abstractmethod 

class Shapes(ABC):
    
        def RectangleArea(length,breadth):
            pass
        
        def SquareArea(sides):
            pass
        
        def CircleArea(radius):
            pass
        
class Area(Shapes):
    
        def RectangleArea(self,length,breadth):
            area=length*breadth
            print("The area of rectangle is",area,"units.")
            
        def SquareArea(self,side):
            area=side**2
            print("The area of square is",area,"units.")
            
        def CircleArea(self,radius):
            area=3.142*(radius**2)
            print("The area of circle is",area,"units.")
            
# Driver code

objects=Area()
recLen=[5,7,43,78]
recWid=[9,0,4,3]
sqSide=[80,8,5,2]
cirRad=[32,87,5,0,8]

for i in range(0,4):
    obj.RectangleArea(recLen[i],recWid[i])
    
for j in range(0,4):
    obj.SquareArea(sqSide[j])
    
for k in range(0,5):
    obj.CircleArea(cirRad[k])

