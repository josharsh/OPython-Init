def say(phrase):
    print(phrase)
    
say("Python")

======================================================

def yello(phrase):
    print(phrase.upper() + "!")
    
yello("Yepp")

======================================================

def hey(phrase = "Gooden Morden"):
    print(phrase, '!')
    
hey()

======================================================

def say_hello(msg): # No default argument 
    return "Hello" + msg

print(say_hello("World")) # Hello World

======================================================

def greetings(msg = "World"):# Default argument
    return "Hello" + msg
print(greetings()) # Hello World
