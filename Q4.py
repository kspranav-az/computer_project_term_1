# creating required lists
lst = list(map(int, eval(input("enter the list :"))))
even = []
odd = []

# sorting for even & odd
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# assigning & printing nested list
nst_list = [even, odd]
print(nst_list)
