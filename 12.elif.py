guess = input("Enter number: ")

if guess.isdigit() == "False":
    print("Invalid")
elif guess == "1":
    print("No")
elif guess == "2":
    print("Right")
elif guess == "3":
    print("NO")
else:
    print(guess)
    
