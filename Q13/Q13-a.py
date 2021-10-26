import pickle

fob = open("student.dat", "wb")

studat = []

n = int(input("Enter the number of entries :"))
for i in range(n):
    name = input(str(i + 1) + ") Enter the Name:")
    rollno = int(input("   Enter Roll no :"))
    studat.append([rollno, name])

pickle.dump(studat, fob)

fob.close()
