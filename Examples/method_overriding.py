"""
Overriding is one of the oops concepts which allows us to change the implementation of a method
in child class that is defined in the parent class.
Conditions of overriding:
1) Inheritance should be there.
2) Child class method should have same number of parameters as parent method.

Below is an example which demonstrates method overriding.
Create an Animal class and implement feed method with print statement
Create a Vegetarian class which is inherits Animal class
and add feed method with different implementation
"""


class Animal:
    def feed(self):
        """
        Feed feed ]

        Args:
            self: (todo): write your description
        """
        print('I eat everything whatever you feed me')


class Vegetarian(Animal):
    def feed(self):
        """
        Feed feed ]

        Args:
            self: (todo): write your description
        """
        print('I eat only vegetables')


if __name__ == '__main__':
    a = Animal()
    a.feed()
    v = Vegetarian()
    v.feed()
