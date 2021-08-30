word1="Joining"
word2="Text"


"""Using "+" operator for text formatting, this operator can be used for joining multiple strings together"""


print(word1+word2)

#Returns JoiningText

print(word1+" "+word2)

#Returns Joining Text

word3=word1+word2
print(word3)

#Returns JoiningText


"""Using join() method we can also join two Strings"""


print("".join([word1,word2]))

#Returns JoiningText

print(" ".join([word1, word2]))

#Returns Joining Text

c=(" ".join([word1, word2]))
print(c)


"""Using %operator for formatting string, it can also be used for concatenation of string"""


print("%s %s" % (word1, word2))

#Returns Joining Text

c=("%s %s" % (word1, word2))
print(c)

#Returns Joining Text


"""Using format() function  is one of the string formatting methods in Python"""


print("{} {}".format(word1, word2))

#Returns Joining Text

c = "{} {}".format(word1, word2)
print(c)

#Returns Joining Text


"""Using ","(comma) for string formatting it can be easily used if we want to unclude a single whitespace"""


print(word1, word2)

#Returns Joining Text
