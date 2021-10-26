import pickle

fob = open("student.dat","rb")

studat1 = pickle.load(fob)
fob.close()

Roll = int(input("Enter the roll no to be searched :"))
for dat in studat1:
    if dat[0] == Roll:
        print(dat[1])
        break
    else:
        pass
else:
    print("No record found with the provided Roll no")