# Introduction to the basics of Python.
# If you have not read the Introduction.md file already, be sure to do so.
# Introduction.md will explain why choosing to learn Python is a good choice.
# Also it will help you get started.

'''
... with that said, It is time to cover one of the first things:
    comments
    Comments are strings, that the program will ignore.
        single-line comments:
        A lot of programming languages use: // to initiate a single-line command.
        Python uses: # to initiate a single-line comment as you can see above.
        multi-line comments:
        Again, many programming languages will support the syntax:
        /*
        some comment here
        and a second line following
        */
        However Python did not start out with a multi-line option. It has been added later and is using the syntax:
        """
        some comment here
        and a second line following
        """
        NOTE: you can always replace double quotation marks with single ones and vica-versa.
        NOTE: this entire section is a multi-line comment defined by double quotation marks.
'''

# Let's learn basic Python coding

# 1. One more of the first things: output "Hello World!" to the standard output.

print("Hello World!") # The output of this code will be "Hello World!" written in your standard output

# NOTE: print() is a function, so:  print "Hello World!"  is incorrect. Use parenthesis.

# 2. Variables

one = 1
characterchain = "I am a happy helloworlder!"
decimal = 3.14159
print(one)  # will print the [integer] 1
print(characterchain)  # will print the [string] "I am a happy helloworlder!"
print(decimal)  # will print the [float]ing point number 3.14159

# The option to do such variable assignments is made possible by Python assigning variable types dynamically.
# Sometimes this automatic assignment requires correction, however most of the time It works just fine.

nice_number = 512 # we define a variable
typ = type(nice_number) # getting the variable type of "nice_number"
print(typ) # printing the type of the variable
# then...let's try converting it, so the integer is now interpreted as a string. This operation is also called "casting (the variable)"
nice_number = str(nice_number)
print(type(nice_number)) # printing the result
# you can always embed functions within each other. However IMPORTANT NOTE: this is usually discouraged after a certain number of operations
# for demonstrative purposes...:
print(type(float(nice_number)))

# 3. Strings
# A string is a list of characters. We will talk about lists later.
# I could show you all string operations, but a lot of them are trivial.
string = "A very nice string!"
# demonstration of some trivial operations:
print(string.capitalize()) # prints: "A VERY NICE STRING!"
print(string.find("very")) # prints: index where "very" starts or -1 if "very" iis not a substring
# etc...
# Now we are going to look at one of the most used string operation which is formatting.
# There are several ways to do this, but for simplicity we will keep it down to 1 solution that will work with older Python versions too.
string = "A very nice string created by {}".format("John Doe") # we are using the "format" property of strings.
print(string)
# using the {} braces means something like: "Hey dude, hold this place for something I will pass in later".
# in case you use multiple {}s, you need to expand the parameter list of .format()
# for instance:
number = 2
by = "John"
string = "The number is: {}\nNumber created by: {}\n".format(number, by) # you can use special characters properly escaped, like: "\n" for new line
print(string)

# 4. Loops
# to understand loops, let's move on to data structures...so that it is easier to explain. The two actually make more sense together.

# 5. Data structures & Loops
# There are several data structures in Python. I mostly use 2 of them, so I will stick with those for now.
my_list = [] # list
my_dict = {} # dictionary
# LIST: indexed, can increase or decrease in size, iterable
# DICTIONARY: named indexes, can increase or decrease in size, iterable in several ways. NOTE: {"key":"value"}

second_list = ["random", "words", "written", "in", "a", "list"]
# if we printed our list now, we would literally get: ["random", "words", "written", "in", "a", "list"]
# so obviously we will iterate through it:
i = 0 # set "i" to zero (to start at index: 0). Lists are indexed from 0. So a list containing 5 items will have indexes 0-4
while i < len(second_list):
    print(second_list[i]) # our print statement will print the item at the specified index
    i += 1 # Python does not support the ++ operator, so instead of i++ we use i += 1 to increment the value of "i" by one
# here "i" will refer to the current iteration in the loop
# "second_list" is the iterable we going through item by item

second_dict = {"itemno1":"first", "itemno2":"second"}
# if we printed our dictionary (dict for short) now, we would literally get: {"itemno1":"first", "itemno2":"second"}
# so obviously we will iterate through it obviously with a different loop: FOR
# the FOR loop is a bit different from programming languages like java, c, c++, etc...
for i in second_dict: # this for loop will iterate through ONLY the key values
    print(i)  # so this will print: "itemno1" and "itemno2"
for k in second_dict.keys(): # this is exactly the same as above, using "k" for "keys"
    print(k)
for v in second_dict.values(): # this for loop will get only the values, using "v" for "values"
    print(v) # printing: "first" and "second"
# so now we know how to list the keys and values of our dict
# why not list them both?
for k,v in second_dict.items():
    print(k,v) # prints key and item side by side
# you can always experience further:
for item in second_dict.items(): # we assign both key and value to one variable /iteration
    print(item) # returns with a tuple containing both the key and value
# we will not cover touples here

# so now that we know the contents of our arrays (lists are also called arrays, lists are arrays in Java, C, C++, etc..)
# can we modify these contents? - Sure!

#Add:
second_list.append("to my entertainment")
print(second_list) # this print statement will not be pretty, will it? We will soon work around that ;)
second_dict["newitem"] = "wut?"
print(second_dict)

#Remove:
second_list.pop()
print(second_list)
second_dict.pop("newitem")
print(second_dict)

# now we know the basics
# one more quick thing that is useful with lists (creating an input from a text typed or anything...)
str=""
str = str.join(second_list)
print(str)

"""
I think we covered enough to get you started on your journey with Python. Old snakeboy may seem strange at first,
but it will very soon grow on you.
However do not ever forget how practice makes perfect!
Practice daily, write code, make mistakes, debug them with print statements, get an IDE, debug in a debugger, 
familiarize yourself with libraries, tools, contribute to open-source projects, have fun. The coding community is very supportive.
some useful links:
www.stackoverflow.com
www.medium.com
www.reddit.com
Also some universities offer the video versions of some of their lectures online for FREE. You can make use of those too.
Have fun and welcome!
"""



