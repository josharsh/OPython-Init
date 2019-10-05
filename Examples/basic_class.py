# Example of a class and how to instanciate it.


class Plane:
    def __init__(self, model, seats):
        self.plane_model = model
        self.number_seats = seats

    def model(self):
        return self.model

    def seats(self):
        return self.seats


def main():
    boeing = Plane('Boeing 787', '200')
    cesna = Plane('cesna', '4')

    print(boeing.model())
    print(boeing.seats())
    print(cesna.model())
    print(cesna.seats())


if __name__ == "__main__":
    main()
