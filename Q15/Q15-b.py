import pickle


def update(rno):
    with open("studat.dat", "rb") as fob:
        data = pickle.load(fob)
        l = len(data)
        for i in range(l):
            if data[i][0] == rno:
                val = input(" what is to be updated(Name/Marks) :")
                if val.casefold() == "name":
                    name = input("Enter new Name :")
                    data[i][1] = name
                    break
                elif val.casefold() == "marks" or "mark":
                    mark = float(input("Enter the new marks :"))
                    data[i][2] = mark
                    break
                else:
                    pass
        else:
            print("No record found with given Roll no.")
    with open("studat.dat", "wb") as fob3:
        pickle.dump(data, fob3)


update(int(input("Enter roll no:")))

