"""
A sample code to demonstrate how Object-Oriented Programming in Python works.
In the example below, we define a class Dice.
Besides, we demonstrate usage of several dunder (magic) methods, class decorators and a private method for input values checkup
"""

import random


class Dice:

    # constructor
    def __init__(self, min_eyes=1, max_eyes=6):
        """
        Initialize the instance

        Args:
            self: (todo): write your description
            min_eyes: (int): write your description
            max_eyes: (int): write your description
        """
        self.__check_input(min_eyes, max_eyes)
        self.eyes = list(range(min_eyes, max_eyes + 1))


    # turns instances of a class into callables
    def __call__(self):
        """
        Returns a random callable.

        Args:
            self: (todo): write your description
        """
        return random.choice(self.eyes)


    # returns machine-readable representation of a type
    def __repr__(self):
        """
        Return a representation of this representation.

        Args:
            self: (todo): write your description
        """
        return "Dice {} .. {} at {}".format(min(self), max(self), hex(id(self)))


    # returns the next item in the sequence
    def __next__(self):
        """
        Returns a random random node.

        Args:
            self: (todo): write your description
        """
        return random.choice(self.eyes)


    #  returns an iterator object
    def __iter__(self):
        """
        Return an iterator over the iterable.

        Args:
            self: (todo): write your description
        """
        return self.eyes.__iter__()


    # returns object length
    def __len__(self):
        """
        Returns the number of bytes.

        Args:
            self: (todo): write your description
        """
        return len(self.eyes)


    # method for rolling the dice
    def roll(self, n=1):
        """
        Roll n times.

        Args:
            self: (todo): write your description
            n: (array): write your description
        """
        return [self() for _ in range(n)]


    # class property: expected value of the dice's eyes
    @property
    def expected_value(self):
        """
        The expected value of the expected value.

        Args:
            self: (todo): write your description
        """
        return sum(self.eyes)/len(self)


    # class property: variance of the dice's eyes
    @property
    def var(self):
        """
        Compute the variance of the distribution.

        Args:
            self: (todo): write your description
        """
        return sum([(x - self.expected_value)**2 for x in self.eyes]) / len(self)


    # class property: number of dice's sides
    @property
    def sides(self):
        """
        Returns the number of bytes.

        Args:
            self: (todo): write your description
        """
        return len(self)


    # check input values for minimum and maximum number of eyes
    # this method is private, i.e., it should only be accessed from inside the class
    def __check_input(self, min_eyes, max_eyes):
        """
        Check the input and max_eyes.

        Args:
            self: (todo): write your description
            min_eyes: (int): write your description
            max_eyes: (int): write your description
        """
        if min_eyes > max_eyes:
            raise ValueError("Min_eyes must be < max_eyes, now: {} > {}".format(min_eyes, max_eyes))
        if not isinstance(min_eyes, int):
            raise ValueError("min eyes must be numeric")
        if not isinstance(max_eyes, int):
            raise ValueError("mac_eyes must be numeric")
