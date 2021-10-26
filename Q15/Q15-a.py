import pickle


def write(data):
    global studat
    studat.append(data)


# creating data file
fob = open("studat.dat", "wb")
studat = []

n = int(input("Enter the number of entries :"))

for i in range(n):
    name = input(str(i + 1) + ") Enter name :")
    roll = int(input("   Enter Roll no. :"))
    marks = float(input("   Enter Marks :"))
    data = [roll, name, marks]
    write(data)

pickle.dump(studat, fob)
fob.close()
