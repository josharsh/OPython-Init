

# Object-Oriented Basics Using Python

(Source: [https://www.tutorialspoint.com/python/python_classes_objects.htm](https://www.tutorialspoint.com/python/python_classes_objects.htm))

Python has been an object-oriented language since it existed. Because of this, creating and using classes and objects are downright easy. This chapter helps you become an expert in using Python's object-oriented programming support.If you do not have any previous experience with object-oriented (OO) programming, you may want to consult an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts.However, here is a small introduction of Object-Oriented Programming (OOP) to bring you at speed −


## Overview of OOP Terminology



*   Class − A user-defined prototype for an object that defines a set of attributes that characterize an object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
*   Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
*   Data member − A class variable or instance variable that holds data associated with a class and its objects.
*   Function overloading − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.
*   Instance variable − A variable that is defined inside a method and belongs only to the current instance of a class.
*   Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.
*   Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
*   Instantiation − The creation of an instance of a class.
*   Method − A special kind of function that is defined in a class definition.
*   Object − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.
*   Operator overloading − The assignment of more than one function to a particular operator.

EXAMPLE:


```
class Student:
   'Common base class for all Students'
   stuCount = 0

   def __init__(self, name, marks):
      self.name = name
      self.marks = marks
      Student.stuCount += 1

   def displayCount(self):
     print "Total Student %d" % Student.stuCount

   def displayStudent(self):
      print "Name : ", self.name,  ", marks: ", self.marks
```



## **Python Objects (Instances)**

(Source: [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/))

While the class is the blueprint, an _instance_ is a copy of the class with _actual_ values, literally an object belonging to a specific class. It's not an idea anymore; it's an actual animal, like a dog named Roger who's eight years old.

Put another way, a class is like a form or questionnaire. It defines the needed information. After you fill out the form, your specific copy is an instance of the class; it contains actual information relevant to you.

You can fill out multiple copies to create many different instances, but without the form as a guide, you would be lost, not knowing what information is required. Thus, before you can create individual instances of an object, we must first specify what is needed by defining a class.

### CREATING CLASS AND OBJECT IN PYTHON

```
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
# instantiate the Parrot class
~~~
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
~~~
# access the class attributes
~~~
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))
~~~
# access the instance attributes
~~~
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
~~~

## **Python Inheritance **

(Source: [https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/](https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/)

Inheritance is one of the core concepts of object-oriented programming (OOP) languages. It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.


## **Python Encapsulation **

Source: https://www.geeksforgeeks.org/encapsulation-in-python/

Encapsulation is one of the core principles of Object-Oriented Programming. It refers to the bundling of data (variables) and methods (functions) that operate on that data within a single unit called a class. It helps protect the internal state of an object by restricting direct access and allowing modification only through controlled interfaces like getters and setters.
In simple terms, encapsulation ensures data security and control over how attributes are accessed or modified.

## **Python Polymorphism **

Source: https://www.geeksforgeeks.org/polymorphism-in-python/

Polymorphism means “many forms.” In Python OOP, it allows the same function name or operator to behave differently based on the object or data type it is applied to. This makes code more flexible and extensible.
It is commonly implemented through method overriding (same method name in a derived class) and method overloading (same method name with different parameters, though Python handles this differently than some languages).

## ** Python Abstraction **

Source: https://www.geeksforgeeks.org/abstraction-in-python/

Abstraction focuses on hiding the complex implementation details and showing only the essential features of an object.
In Python, abstraction is achieved using abstract classes and abstract methods from the abc module.
It helps developers work with high-level functionality without worrying about the underlying complexity — improving code clarity and modularity.

## **Python Classes and Objects **

Source: https://www.geeksforgeeks.org/python-classes-and-objects/

Classes and Objects form the foundation of Object-Oriented Programming in Python.
A class acts as a blueprint or template for creating objects, defining their properties (attributes) and behaviors (methods).
An object is an instance of a class that holds actual data and can perform actions defined by the class.
Together, they provide the structure that enables code reuse, organization, and real-world modeling in programming.