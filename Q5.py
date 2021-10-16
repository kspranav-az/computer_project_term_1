from math import pi

# displaying menu
print("Main menu \n Press<1>: Area \n press<2>: Perimeter \n ----->", end="")
key = input()

# checking held key
if key == "1":
    rad = float(eval(input(" Enter the radius of the circle (meters):")))
    # perimeter calculation
    peri = 2 * pi * rad
    print("perimeter = ", round(peri, 2), "meters")
elif key == "2":
    rad = float(eval(input("Enter the radius of the circle (meters):")))
    # area calculation
    area = pi * rad ** 2
    print("Area = ", round(area, 2), "meter.sq")
else:
    print(" Kindly enter a valid key ")
