# Linked list implementation using OOP

# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        """
        Initialize data.

        Args:
            self: (todo): write your description
            data: (todo): write your description
        """
        self.data = data  # Assign data
        self.next = None  # Initialize
                          # next as null

# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        """
        Initialize the head.

        Args:
            self: (todo): write your description
        """
        self.head = None
    # Here self.head is basically initialised with a null value
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        """
        Print a list of the buffer.

        Args:
            self: (todo): write your description
        """
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Three nodes have been created.
    # We have references to these three blocks as head,
    # second and third

    llist.head.next = second # Link first node with second
    second.next = third # Link second node with the third node
    llist.printList()
