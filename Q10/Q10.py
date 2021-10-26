# function for checking character type
def ch_check(str1):
    if "a" <= str1 <= "z":
        return "Lower"
    elif "A" <= str1 <= "Z":
        return "Upper"
    elif "0" <= str1 <= "9":
        return "Digit"
    else:
        return None


# opening file
fob = open(input("Enter the file name :")+".txt","r")
str1 = fob.read().split()
lower = 0
upper = 0
digit = 0

# checking character type for each letter
for i in str1:
    lst1 = list(i.strip("\n").strip())
    for j in lst1:
        typ = ch_check(j)
        if typ == "Lower":
            lower += 1
        elif typ == "Upper":
            upper += 1
        elif typ == "Digit":
            digit += 1
        else:
            pass

print("Total Uppercase =", upper)
print("Total Lowercase =", lower)
print("Total digits =", digit)