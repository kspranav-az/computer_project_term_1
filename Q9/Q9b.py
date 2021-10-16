# opening required file
fob1 = open("abc.txt", "r")
str1 = fob1.read()
str2 = ""

# converting into required string
for i in str1:
    if i.islower():
        j = i.capitalize()
        str2 += j
    elif i.isupper():
        j = i.lower()
        str2 += j
    else:
        str2 += i
fob1.close()

# writing in xyz
fob2 = open("xyz.txt","w")
fob2.write(str2)
fob2.close()

