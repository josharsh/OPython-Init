def say(phrase):
    print(phrase)
    
say("Python")

#############################################################

def yello(phrase):
    print(phrase.upper() + "!")
    
yello("Yepp")


#############################################################
#Creating a function that takes keyword arguments
def hey(phrase = "Gooden Morden"):
    print(phrase, '!')
    
hey()

#############################################################
# Creating a function that takes a variable number of positional arguments
def varargs(*args):
    return(args)

arguments = varargs('argument1', 'argument2', 'argument3')
print(arguments[0])
print(arguments[1])
print(arguments[2])

#############################################################
# Creating a function that takes a variable number of positional arguments
# and keyword arguments
def both_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

args = (1, 2, 3, 4, 5, 6)
kwargs = {"A": 7, "B": 8}
both_the_args(*args)
both_the_args(**kwargs)
both_the_args(*args, **kwargs)