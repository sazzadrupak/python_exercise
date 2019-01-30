# Fill in all TODOs in this file

from math import sqrt

# This is a text-based menu. You should ONLY touch TODOs inside the menu.
# TODOs in the menu call functions that you have implemented and take care
# of the return values of the function calls.


def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            # TODO = fill(TODO)
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            drive_data = drive(x, y, new_x, new_y, gas, gas_consumption)
            gas = drive_data[0]
            x = drive_data[1]
            y = drive_data[2]

        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.
def fill(tank_size, to_fill, gas):
    if to_fill > tank_size:
        to_fill = tank_size
    else:
        if gas + to_fill > tank_size:
            to_fill = tank_size - gas
    return gas + to_fill


# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.
def drive(x1, y1, x2, y2, gas, gas_consumption):
    # It might be usefull to make one or two helper functions to help
    # the implementation of this function (drive)
    # TODO
    # get the distance between two axis to drive
    d = distance(x1, y1, x2, y2)

    # get the required fuel to cover the distance
    required_fuel = fuel_needed(d, gas_consumption)

    if gas == 0.0:
        return gas, x1, y1
    elif required_fuel > gas:
        # if there is less fuel then required, then find
        # minimum distance to drive with available fuel
        minimum_distance = (100 * gas) / gas_consumption
        # print(d, minimum_distance, gas)
        if x2 == x1:
            x = x1
        elif (y2 - y1) < 0:
            x = 0.0
        elif minimum_distance < (y2 - y1):
            x = minimum_distance
        else:
            if x1 >= 0 > x2:
                print('1')
                x = float(int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2) - x1))
            elif 0 <= x2 < x1:
                print('2')
                # print("1--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
                x = float(x1 - int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2)))
            elif 0 > x2 < x1:
                print('3')
                # print("2--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
                x = - float(int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2) - x1))
            else:
                print('4')
                x = float(int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2) + x1))
            # if 0 <= x2 < x1:
            #     print("1--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
            #     x = float(x1 - int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2)))
            # elif 0 > x2 < x1:
            #     print("2--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
            #     x = - float(int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2) - x1))
            # else:
            #     print("3--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
            #     x = float(int(sqrt(minimum_distance ** 2 - (y2 - y1) ** 2) + x1))

        if y2 == y1:
            y = y1
        elif (x2 - x1) < 0:
            y = 0.0
        elif minimum_distance < (x2 - x1):
            y = minimum_distance
        else:
            if y1 >= 0 > y2:
                y = float(int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2) - y1))
            if 0 <= y2 < y1:
                # print("4--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
                y = float(y1 - int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2)))
            elif 0 > y2 < y1:
                # print("5--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
                y = - float(int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2) - y1))
            else:
                y = float(int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2) + y1))
            # if 0 <= y2 < y1:
            #     print("4--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
            #     y = float(y1 - int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2)))
            # elif 0 > y2 < y1:
            #     print("5--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
            #     y = - float(int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2) - y1))
            # else:
            #     print("6--", minimum_distance, "--", x2, "--", x1, "--", y1, "--", y2)
            #     y = float(int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2) + y1))
            # y = float(int(sqrt(minimum_distance ** 2 - (x2 - x1) ** 2) + y1))

        gas = 0.0
        return gas, x, y
    else:
        x = x2
        y = y2
        gas = gas - required_fuel
        return gas, x, y


def fuel_needed(d, gas_consumption):
    return gas_consumption * 0.01 * d


def distance(x1, y1, x2, y2):
    x = (x2 - x1)
    y = (y2 - y1)
    d = sqrt(x ** 2 + y ** 2)
    return d


# TODO
# Implement your own functions here. It is required to implement at least
# two functions that take at least one parameter and return at least one
# value.
# The functions have to be used somewhere in the program.


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


main()
