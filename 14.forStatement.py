wordo = "Ironman is awesome"

for ltr in wordo:
    print(ltr)
    
print()

for ltr in wordo[::-1]:
    print(ltr)
    
print()

student_name = "iteration"
count = 0
for letter in student_name:
    if letter.lower() == "e":
        print(count)
    count += 1
    