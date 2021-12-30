# Example of Object Oriented Programming (OOP) classes and objects.

# First we need to declare the class that will serve us as a "template".
class Plane:
    def __init__(self, model, seats):
        # The init function is the function executed when we first create (instanciate)
        # the class in the main program. When we instanciate a class we have an object.
        # In this init we declare the variables that we are going to use for the class.
        self.plane_model = model
        self.number_seats = seats

    # These two functions will return the value of the object when we call them on the
    # main program.
    def model(self):
        return self.model

    def seats(self):
        return self.seats

    # And with this two functions we can change the values of the class variables.
    def change_model(self, model):
        self.plane_model = model

    def change_seats(self, seats):
        self.number_seats = seats


def main():
    # To use a class, first we have to create an object of that class (instanciate it).
    # And since we defined the init function with two parameters, we have to pass them
    # to the class. As you can see here we have an object "boeing" and an "object" cesna,
    # both of the class "Plane".
    boeing = Plane('Boeing 787', '200')
    cesna = Plane('Cesna', '4')

    # And now with the objects we can call the other functions we have defined.
    print(boeing.model())
    print(cesna.seats())

    # We can also change the values of the object with the functions we have made.
    boeing.change_seats(202)
    cesna.change_model('Cesna 070')


if __name__ == "__main__":
    main()
