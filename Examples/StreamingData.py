# STREAMING OF DATA(INHERITANCE EXAMPLE)
""" We can read a stream of data from an audio or from a video or some animation,all these 
streams have some functions as common,we can open them ,we can close them,we can read
data from them,but how we read data from the stream is dependent on the type of the stream.
As reading data from an audio is different from reading data from a video """

""" we create a custom exception """


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


""" Inheriting from stream class """


class Audio(Stream):
    def read(self):
        print("Reading data from a audio")


class HDmovie(Stream):
    def read(self):
        print("Reading data from a video")


""" Note that we dont have multilevel inheritance here,we only have two levels
in our hierarchy where Stream is at top of hierarchy and we have two subclasses
Audio and HDmovie  """

stream = Stream()
stream.open()

""" ISSUES:

1.Stream is an abstract concept,we dont know what type of stream we are
working with like a Audio stream or a Video stream so we shouldnt be able to 
directly create an instance of this stream class we should always subclass it
and then create an instance of the subclass.We created stream class for reusing 
the code later accross different kinds of streams 

2.Both Audio and HDmovie have read methods,if we create a new streaming type 
in future it would be helpful to have a common interface across these different types of streams """

# For resolving these type of issues we use abstract base class concept and make Our Stream class an abstract base class
