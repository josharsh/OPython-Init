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

def factorial_iterative(number = 1):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

factorial_iterative(5) # 1*2*3*4*5 = 120


#############################################################

def factorial_recursive(number = 1):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number*factorial_recursive(number - 1)

factorial_recursive(5) # 5*4*3*2*1 = 120


#############################################################
