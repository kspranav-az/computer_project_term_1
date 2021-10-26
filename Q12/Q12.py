# opening & reading main file
fob = open("main.txt", "r")
lines = fob.readlines()
fob.close()

# opening copy file
fob1 = open("copy.txt", "w", newline="")
cline = []

# checking for T character
for line in lines:
    if line[0].casefold() == "t":
        cline.append(line)

# writing in copy file
fob1.writelines(cline)
fob1.close()
