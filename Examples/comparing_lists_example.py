# Start with your program from Exercise 4-1. 

favpizzas = ['Gold Ring', 'White Walker', 'Raising Arizona']

# Make a copy of the list of pizzas, and call it friend_pizzas.

friend_pizzas = favpizzas.copy()

#Add a new pizza to the original list.
favpizzas.append('Buffalo 666')

#Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Pig Destroyer')

#Prove that you have two separate lists. 
print(favpizzas)
print(friend_pizzas)

#Print the message My favorite pizzas are:, and then use a for loop to print the first list.

print("My favorite pizzas are: ")
for x in range(len(favpizzas)):
    print(favpizzas[x])

#Print the message My friend’s favorite pizzas are:, 
#and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.

for x in range(len(friend_pizzas)):
    print(friend_pizzas[x])
