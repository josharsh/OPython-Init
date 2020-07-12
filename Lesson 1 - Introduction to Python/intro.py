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

# While loop traversing a list
i = 0
while i < len(fruits) :
    print(fruits[i])
    i = i + 1     #or i+=1

# While loop iterating 6 times
i = 0 
while i < 6 :
	print(i)
	i = i + 1

# If - Else statements 
i = 0
if i == 0 :
	print(" i is equal 0")
else :
	print(" i is not equal to 0")

# Use of elif 
i = 1
if i == 0 :
	print(" i is equal 0")
elif i == 1 :
	print(" i is equal 1")
else :
	print(" i is neither 0 nor 1")