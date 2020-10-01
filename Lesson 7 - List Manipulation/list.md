# List Manipulation Basics Using Python

(Source: [https://www.tutorialspoint.com/python/python_lists.htm](https://www.tutorialspoint.com/python/python_lists.htm))

Lists are the most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.

## Create a List

```
ll = ["user1", "user2", 2020, "covid", [2050, "future"]]
```


## Find length of list
```
age = [10, 20, 14]
n2 = len(age)
print(f"Length of age is {n2}")
```

## Access Values in List using Indexing
```
age = [10, 20, 14]
l = age[0]
l1 = age[-1]

print(f"The Fist element is {l} and Last element is {l1}")
```

## updating List
```
age = [10, 20, 14]
age[0] = 100
print(age)

```