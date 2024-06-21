"""
Polymorphism means that different types respond to the same function.
https://python-intro.readthedocs.io/en/latest/polymorphism.html

In this example, we are creating two different classes, MarvelComics & DCComics.
These classes are having same methods with different functionality.
"""


class MarvelComics(object):

    def __init__(self):
        self.heroes = ["Iron Man", "Thor", "Captain America"]
        self.villains = ["Thanos", "Dormamu", "Red Sulk"]
        self.grey_characters = ["Loki"]

    def list_heroes(self):
        """
        :return: will return the value of object variable self.heroes.
        """

        return "List of Marvel heroes {0}".format(self.heroes)

    def list_villains(self):
        """
        :return: will return the value of object variable self.villains.
        """

        return "List of Marvel villains {0}".format(self.villains)

    def list_grey_characters(self):
        """
        :return: will return the value of object variable self.grey_characters.
        """
        return "List of Marvel villains {0}".format(self.grey_characters)


class DCComics(object):
    def __init__(self):
        self.heroes = ["Batman", "Superman", "Flash"]
        self.villains = ["Darkseid", "Joker", "TwoFace"]
        self.grey_characters = ["Redhood"]

    def list_heroes(self):
        """
        :return: will return the value of object variable self.heroes.
        """
        return "List of DC heroes {0}".format(self.heroes)

    def list_villains(self):
        """
        :return: will return the value of object variable self.villains.
        """
        return "List of DC villains {0}".format(self.villains)

    def list_grey_characters(self):
        """
        :return: will return the value of object variable self.grey_characters.
        """
        return "List of DC villains {0}".format(self.grey_characters)


def main():
    """
    Creating two different object of MarvelComics and DCComics Class.
    These objects are calling the same method, which are performing different functionality.
    """
    marvel_fans = MarvelComics()
    dc_fans = DCComics()
    print(marvel_fans.list_heroes())
    print(dc_fans.list_heroes())
    print(marvel_fans.list_villains())
    print(dc_fans.list_villains())


if __name__ == '__main__':
    main()
