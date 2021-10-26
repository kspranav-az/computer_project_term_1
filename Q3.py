# creating required lists
L = list(map(int, eval(input("enter the list 1 :"))))
M = list(map(int, eval(input("enter the list 2 :"))))
N = []

# adding & appending into N
for i in range(len(L)):
    N.append(L[i]+M[i])

# printing final list N
print(N)

