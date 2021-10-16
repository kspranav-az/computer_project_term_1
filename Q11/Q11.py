# opening and reading required file
fob = open("text.txt","r")
lines = fob.readlines()

# checking each word's length
for line in lines:
    for word in line.strip().split():
        if len(word.strip(".")) == 4:
            print(word.strip("."))

fob.close()
