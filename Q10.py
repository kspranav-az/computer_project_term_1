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


# taking input & creating required vars
sts = input("Enter the sentence :")
str1 = sts.split()
lower = 0
upper = 0
digit = 0

# checking character type for each letter
for i in str1:
    lst1 = list(i)
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