from math import pi


def area(r):
    # area calculation
    ar = pi * r ** 2
    print("Area = ", round(ar, 2), "meter.sq")


def perimeter(r):
    # perimeter calculation
    peri = 2 * pi * r
    print("perimeter = ", round(peri, 2), "meters")


# displaying menu
print("Main menu \n Press<1>: Area \n press<2>: Perimeter \n ----->", end="")
key = input()

# checking held key
if key == "1":
    rad = float(input(" Enter the radius of the circle (meters):"))
    area(rad)
elif key == "2":
    rad = float(input("Enter the radius of the circle (meters):"))
    perimeter(rad)
else:
    print(" Kindly enter a valid key ")
