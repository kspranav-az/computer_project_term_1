# creating file
fob1 = open("volwords.txt", "w")

# taking input sentence & writing
sts = input("Enter the sentence :")
fob1.write(sts)
fob1.close()

# opening file in reading mode
fob2 = open("volwords.txt", "r")

# creating required strings
stsr = fob2.read()
vowels = ["a", "e", "i", "o", "u"]
count = 0

# counting vowels
for i in stsr:
    if i.casefold() in vowels:
        count += 1

print(count)
