num = int(input(" Enter the number :"))
count = 1

if num < 0:
    print("Factorial doesn't exist")
else:
    while num > 0:
        count = count * num
        num = num - 1
    print(count)
