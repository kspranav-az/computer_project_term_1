num = int(input(" Enter the number :"))
count = 1

if num < 0:
    print("Factorial not possible")
else:
    while num > 0:
        count = count * num
        num = num - 1
    print(count)
