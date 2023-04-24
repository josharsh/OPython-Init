'''
Beginning with Python programming:

Finding an Interpreter:

Before we start Python programming, we need to have an interpreter to interpret and run our programs. 
There are certain online interpreters like http://ideone.com/ or http://codepad.org/  that can be used to start Python 
without installing an interpreter.

Windows:There are many interpreters available freely to run Python scripts like IDLE ( Integrated Development Environment ) 
which is installed when you install the python software from http://python.org/

Linux:For Linux, Python comes bundled with the linux.

'''
#first program in Python
# Script Begins 
  
print("Hello!!") 
  
# Scripts Ends 
'''
OUTPUT
Hello!!
'''
'''
NOTE
In a Python script to print something on the console print() function is used – it simply prints out a line ( and also 
includes a newline unlike in C ). One difference between Python 2 and Python 3 is the print statement. In Python 2, the “print” 
atement is not a function, and therefore can be invoked without a parenthesis. However, in Python 3, it is a function, and must 
invoked with parentheses.
'''
'''
A suggestion would be to visit the documentation page of Python and study the keywords, functions, classes before actually
going ahead with python programming.
'''

# Variables
x = 5
y = "John"
print(x)
print(y)

# String Operations
a = "Hello"
b = "World"
print(a+b)

# For loop travesing a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# For loop iterating 6 times
for i in range(6):
  print(i)

# For loop parameters
for i in range(start=10, stop=20, step=2): # In every iteration i value will be increased by 2.
  print(i)
  
# Summing first 5 digits
sum=0
for i in range(5):
  sum += i
  
# Binary Addition
a = int("1010", 2) # 10 in decimal
b = int("110", 2) # 6 in decimal
print(a+b)

# Bitwise Operations
a = 5
b = 2

print(a<<2) # 20 (Left Shift)
print(a^b) # 7 (XOR) 
print(~a) # Two's complement of a
