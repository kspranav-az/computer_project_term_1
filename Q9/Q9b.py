# creating file
fob = open("abc.txt","w")
fob.write("Honesty9 Is The$ Best @Policy")
fob.close()

# reading required file
fob1 = open("abc.txt", "r")
str1 = fob1.read()
str2 = ""
fob1.close()

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

# writing in xyz
fob2 = open("xyz.txt","w")
fob2.write(str2)
fob2.close()

