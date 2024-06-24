# Non - Recursive functions

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
# Non - recursive factorial function

def fact(n) :
	f = 1
	for i in range(n, 0, -1) :
		f = f * i
	print(n ," factorial is : ", f)
fact(5)

#############################################################
# Recursive Factorial function

def fact(n) :
	if n == 0 :
		result = 1
	else :
		result = n * fact(n - 1)
	return result
n = 5
print(n ," factorial is : ", fact(n))

##############################################################
# Lambda Function
# Lambda fuctions are the fuctions where the name of function is not required
x = lambda a, b, c : a + b + c
print(x(10, 20 , 30))