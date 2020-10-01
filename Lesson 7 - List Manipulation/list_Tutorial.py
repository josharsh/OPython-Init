# List operation in Python


# Creating Empty List
empty = []
print(empty)
# output => []


# Creating List of ages
age = [10, 20, 14]
print(age)
# output => [10, 20, 14]

# It can have values of different datatypes

ll = ["user1", "user2", 2020, "covid", [2050, "future"]]
# The above list contains string , number and list

# find length of list
n1 = len(empty)
n2 = len(age)
print(f"Length of empty is {n1} and age is {n2}")
# output => Length of empty is 0 and age is 3

# Access Values in List using Indexing
l = age[0]
l1 = age[-1]

print(f"The Fist element is {l} and Last element is {l1}")
# The Fist element is 10 and Last element is 14


# updating List

age[0] = 100
print(age)
# output => [100,20,14]


# delete List Elements

list1 = ['maths', 'school', 1997, 2000]
del(list1[2])
print(f"After deleting value at index 2 : {list1}")
# output  => ['maths','school',2000]


# append elements to list

list2 = ['a', 'b', 'c']
list2.append('d')
print(list2)
# output => ['a','b','c','d']
