import csv

fob = open("books.csv", "w+", newline="")

# creating writer
writer = csv.writer(fob)

writer.writerow([" Accession No.", "Book Name", "Author's Name"])

n = int(input("Enter the number of Entries :"))
records = []

# taking entries
for i in range(n):
    acc = int(input(str(i + 1) + ") Enter the Accession No.:"))
    bkn = input("   Enter the Book Name    :")
    atn = input("   Enter the Author's Name:")
    records.append([acc, bkn, atn])

writer.writerows(records)

fob.close()

# opening once again for reading
print("\n\n")
with open("books.csv","r") as fob1:
    reader = csv.reader(fob1)
    for row in reader:
        print(row)
