def halfValue(value):
    return value/2

print(halfValue(20))


#############################################################

def doubleString(phrase):            #Frozen came here
    double = phrase + "+" + phrase   #went through double
    return double                    #this return double(from above) back to doubleString(below) and then

String_2x = doubleString("Frozen")
print(String_2x)                     #it get print


#############################################################

def schedule(period1, period2):
    thisSchedule = period1 + " before " + period2
    return thisSchedule

studentSchedule = schedule("maths", "chem")
print(studentSchedule)

######################################################

def add_num(num_1 = 10):
    return num_1 + num_1
print(add_num(100))

#################################################

def add_numbers(num_1, num_2 = 10):
    return num_1 + num_2
print(add_numbers(100))

###########################################

def low_case(words_in): 
      return words_in.lower()
words_lower = low_case("Return THIS lower")
print(words_lower)

    