# Functions in Python


## Brief Introduction:

(Source: [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp))



*   A function is a block of code which only runs when it is called.It performs a specific task.
*   You can pass data, known as parameters, into a function.
*   A function can return data as a result to the calling function.


### Python Sample program to display the use of functions:
```
#This function checks whether the entered number is a multiple of 5 or not:
def check( x ):
    if (x % 5 == 0):
        print "Yes"
    else:
        print "No"
#Driver code
check(2)
check(3)
```

In python we can also assign functions to variables

```
evenOdd = check
#Driver code
evenOdd(2)
evenOdd(3)
#the output will be same as of previous function calls: check(2) , check(3)

```

## Creating a Function

In Python a function is defined using the `def` keyword:


```
def my_function():
  print("I am a Function")
```



## Calling a Function

To call a function, use the function name followed by parenthesis:


```
def my_function():
  print("Hello from a function")

my_function()
```

## Uses of Functions 
Functions are useful because they allow us to reuse pieces of code. For example, consider the following code, to print numbers from 0 to 5: 

```
for i in range(6):
  print(i)
```

What if we wanted to do this for any number n? 

We can write a function that does this for us: 
```
def from_0_to_(n):
  for i in range(n+1):
    print(n)

from_0_to_(6)
from_0_to_(7)
```
#### With this short and crisp refresher on functions in python, the Lesson will now walk you through some in-built functions in python. It is expected that you have preliminary programming knowledge (Iterators, Conditions, Syntax, Semantics, etc.) 


# MODULE 1: CREATING  A REMINDER APP

Before heading further to module 1, It is important to know where the functions of python are stored. Python uses the concept of libraries to store functions and classes (later in this course).


# The Python Standard Library


(Source:[https://docs.python.org/3/library/](https://docs.python.org/3/library/))

While [The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index) describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.


### Task 1: Create a python script to set a reminder in about a fix duration of time that opens a youtube video using the concept of functions in python. 

(This can be used to take a break from long and continuous computer hours)


### Assistance: 



*   Python Standard Library has a module called 'webbrowser'
*   Check on Resources to get the solution 


### TASK 2: There is a message to be decoded. There have been pictures of file format .jpg which have to be renamed in such a way that the digits in the names have to be removed which upon sorting would show a message. There is a folder containing all those images along this lesson. Write a python script to do the needful 

(Wait What??....Yes! This can be playful with your friends.)


### Assistance: 



*   Python Standard Library has a module called 'os'
*   Use listdir function inside the os module
*   Refer to the Internet for complete documentation of os module
*   Check on Resources to get the solution 


# About Used Modules:



*   [https://docs.python.org/2/library/webbrowser.html](https://docs.python.org/2/library/webbrowser.html)
*   [https://docs.python.org/2/library/os.html](https://docs.python.org/2/library/os.html)


Refer to [https://data-flair.training/blogs/python-built-in-functions/](https://data-flair.training/blogs/python-built-in-functions/) for a list of python inbuilt functions and explore their potential.


