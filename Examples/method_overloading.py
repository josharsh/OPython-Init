""" 
Method Overloading allows different methods to have the same name,
but different signatures where the signature can differ by the number of
input parameters or type of input parameters, or a mixture of both. 
Method overloading is also known as Compile-time Polymorphism, Static Polymorphism, or Early binding in Java.
In Method overloading compared to parent argument, child argument will get the highest priority. 
Below is an example which demonstrates method overloading
"""


# First product method.
# Takes two argument and print their
# product
def product(a, b):
	p = a * b
	print(p)
	
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error	
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)
