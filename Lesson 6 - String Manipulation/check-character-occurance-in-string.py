count = 0

my_string = input("Enter string ")
my_char = input("Enter character ")

for i in my_string:
    if i == my_char:
        count += 1

print(my_char +" is present in "+ my_string +" " + str(count)+" times")
