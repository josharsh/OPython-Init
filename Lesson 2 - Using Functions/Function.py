def say(phrase):
    print(phrase)
    
say("Python")

#############################################################

def yello(phrase):
    print(phrase.upper() + "!")
    
yello("Yepp")


#############################################################

def hey(phrase = "Gooden Morden"):
    print(phrase, '!')
    
hey()

#############################################################

def add(a,b):
    return a+b
    
number = add(3,5)
print(number)