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


######################################################

def greetings(msg):# Default argument
    "Good Morning, " + msg

print(greetings("Monica")) # Good Morning, Monica
