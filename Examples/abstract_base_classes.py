# abc is module which stands for abstract base class
# ABC is name of the class
# abstractmethod is a funtion that we will use as a decorator
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


""" To make this Stream class abstract we should derive it from ABC class """


class Stream(ABC):
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

    @abstractmethod  # we want all type of streams to have read method
    def read(self):
        pass


class Audio(Stream):
    def read(self):
        print("Reading data from a audio")


class HDmovie(Stream):
    def read(self):
        print("Reading data from a video")


# If we uncommment this, we have red underline because of the abstract method we created,we cant create an instance of abstract class
""" stream = Stream()
stream.open() """  # we have red underline because of the abstract method we created,we cant create an instance of abstract class

# Now we create a new type of stream in the future like AnimatedStream


""" class AnimatedStream(Stream):
    pass """


# If we uncommment this ,we have red underline because our new class AnimatedStream is also abstract as it derived from the Stream class
""" stream = AnimatedStream()
stream.open() """

""" To fix this, we rewrite AnimatedStream class as """


class AnimatedStream(Stream):
    def read(self):
        print("Reading data from a animation")


stream = AnimatedStream()
stream.open()
