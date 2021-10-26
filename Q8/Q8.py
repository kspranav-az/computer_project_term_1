# creating file
fob = open("sentence.txt", "w")

sts = input(" Enter the sentence :")
fob.write(sts)
fob.close()

# reading created file
fob1 = open("sentence.txt", "r")
stsr = fob1.read()
str1 = stsr.split()

to = 0
the = 0

# checking for to & the
for i in str1:
    if i.casefold() == "to":
        to += 1
    elif i.casefold() == "the":
        the += 1
    else:
        pass

print("Total number of 'to' present =", to)
print("Total number of 'the' present =", the)