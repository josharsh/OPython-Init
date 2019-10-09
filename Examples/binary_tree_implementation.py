"""
A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

A Binary Tree node contains following parts:
1. Data
2. Pointer to left child
3. Pointer to right child

More details about binary tree can be found on https://www.geeksforgeeks.org/binary-tree-data-structure/
"""


class node():
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        self.height = 0

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = node(value)
                else:
                    self.right.insert(value)
            else:
                self.value = value

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.value, end=" ")

    def print_preorder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()


    def print_nth_row(self, n):
        if n==1:
            print(self.value, end=" ")
        self.left.print_nth_row(n-1)
        self.right.print_nth_row(n-1)




a = [6, 7, 9, 4, 1, 3, 15, 17, 5, 2]

head = node(a[0])

for i in range(1, len(a)):
    head.insert(a[i])

head.print_preorder()
