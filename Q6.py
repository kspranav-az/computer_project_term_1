import random

lst = []

# creating random list
for i in range(10):
    lst.append(random.randint(10, 99))

# slicing list
lst1 = lst[0:5]
lst2 = lst[5:10]

# Displaying original & sliced list
print(lst)
print(lst1)
print(lst2)
