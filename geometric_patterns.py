# Introduction to Programming
# Geometry
from math import pi


# square function will take the required dimension from user,
# and check if it is greater than zero or not,
# and which then prints the circumference
# and area of the shape to two decimal places.
def square():
    dimension = 0
    while dimension < 1:
        dimension = float(input("Enter the length of the square's side: "))

    print('The total circumference is %.2f' % (4 * dimension))
    print('The surface area is %.2f' % (dimension * dimension))
    return


# rectangle function will take the required dimensions from user,
# and check if it is greater than zero or not,
# and which then prints the circumference
# and area of the shape to two decimal places.
def rectangle():
    dimension_1 = 0
    dimension_2 = 0

    while dimension_1 < 1:
        dimension_1 = float(input("Enter the length of the rectangle's side 1: "))

    while dimension_2 < 1:
        dimension_2 = float(input("Enter the length of the rectangle's side 2: "))

    print('The total circumference is %.2f' % (2 * (dimension_1 + dimension_2)))
    print('The surface area is %.2f' % (dimension_1 * dimension_2))
    return


# circle function will take the required radius from user,
# and check if it is greater than zero or not,
# and which then prints the circumference
# and area of the shape to two decimal places.
def circle():
    radius = float(input("Enter the circle's radius: "))

    print('The total circumference is %.2f' % (2 * pi * radius))
    print('The surface area is %.2f' % (pi * (radius**2)))
    return


def menu():
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            square()  # call square function

        elif answer == "r":
            rectangle()  # call rectangle function

        elif answer == "c":
            circle()  # call circle function

        elif answer == "q":
            return  # return to main function

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


main()
