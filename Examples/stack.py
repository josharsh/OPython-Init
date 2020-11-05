
# Stack
* A stack is a group of elements stored in LIFO (Last In First Out) order. The element which is stored as a last element into the stack 
* will be the first element to be removed from the stack. The stack is used by operating system to save the program execution environment. 
* basically there are five operations we are performing on stack.
* Push operation: Inserting element into stack
* Pop operation: Removing element from stack
* Search operation: Searching an element in the stack
* Peep/Peak operation: Returning the topmost element of the stack without deleting the element
* Empty stack operation: Returning stack is empty or not


# Stack class
class Stack:
    def __init__(self):
        self.st = []
    
    # checking stack is empty or not 
    def isempty(self):
        """
        Return true if all empty list is empty.

        Args:
            self: (todo): write your description
        """
        return self.st == []
    
    # Inserting an element in the list
    def push(self):
        """
        Pushes element to the element.

        Args:
            self: (todo): write your description
        """
        self.st.append(element)

    # Removing the last element from the list
    def pop(self):
        """
        Remove and return the last element.

        Args:
            self: (todo): write your description
        """
        if self.isempty():
            return - 1
        else:
            self.st.pop()

    # Returning the topmost element from the list
    def peek(self):
        """
        Return the next item from the queue.

        Args:
            self: (todo): write your description
        """
        num = len(self.st)
        return self.st[num - 1]


    # Searching an element in the list and return its index position
    def search(self, element):
        """
        Returns the first occurrence.

        Args:
            self: (todo): write your description
            element: (todo): write your description
        """
        if self.isempty():
            return -1
        else:
            try:
                num = self.st.index(element)
                return len(self.st) - num
            except valueError:
                return 2

    # Display the operations 
    def display(self):
        """
        Display the display as a string.

        Args:
            self: (todo): write your description
        """
        return self.st


#### This is a basic Stack data structure usin OOP programming in python.
A stack is a data structure which uses a LIFO(Last In First Out) order to preform operations.
Last In First Out means that the last item to be added to the stack will be the first one to be taken out
It is used in many cases. For example internet search history and creating programming languages.
This program is a bare bones version but can be improved and added to
Python implements a Stack by using a list. 
The list contains all the information held in the stack and we use python list functions within our stack methods.
# Example 2
class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, arg):
        """
        Push an argument to the list.

        Args:
            self: (todo): write your description
            arg: (str): write your description
        """
        self.l.append(arg)

    def pop(self):
        """
        Remove and return the first element from the list.

        Args:
            self: (todo): write your description
        """
        return self.l.pop()

    def top(self):
        """
        Returns the top row.

        Args:
            self: (todo): write your description
        """
        return self.l[-1]

    def __len__(self):
        """
        Return the length of the length.

        Args:
            self: (todo): write your description
        """
        return len(self.l)

    def is_empty(self):
        """
        Returns true if all : class is empty.

        Args:
            self: (todo): write your description
        """
        return len(self) == 0

