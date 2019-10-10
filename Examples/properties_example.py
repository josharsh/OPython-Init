""" An Example for how to use properties in python"""


class Person:
    """
    A person class
    Person's fields are his name and his age
    """

    def __init__(self, name, age):
        # underscore before the field's name declares it as private
        self._name = name
        self._age = age

    # Use the property decorator (@property) to declare the function as a property getter """

    @property
    def name(self):
        """ This function returns the name of the person """
        return self._name

    # To set a setter property use the the name of the getter function (name in this case) and add .setter

    @name.setter
    def name(self, value):
        """  Sets the value of the name with the value variable """
        self._name = value

    """ The same with the age """

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


def main():
    person = Person('john', 26)

    # this is how you use the property getters
    print("the name of this person is {0} and he is {1} years old".format(person.name, person.age))

    person.age = person.age + 1  # this is how you use property setters
    print("now {0} is {1} years old".format(person.name, person.age))


if __name__ == '__main__':
    main()
