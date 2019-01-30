# Fill in all TODOs in this file

from math import sqrt


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
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    if to_fill > tank_size:
        to_fill = tank_size
    else:
        if gas + to_fill > tank_size:
            to_fill = tank_size - gas
    return gas + to_fill


def drive(x1, y1, x2, y2, gas, gas_consumption):
    d = float(distance(x1, y1, x2, y2))
    required_fuel = float(fuel_needed(d, gas_consumption))
    current_fuel = float(gas - required_fuel)
    if current_fuel < 0:
        new_distance = d * gas / required_fuel
        new_required_fuel = float(fuel_needed(new_distance, gas_consumption))
        current_fuel = float(gas - new_required_fuel)
        x2 = x1 + ((x2 - x1) * new_distance) / d
        y2 = y1 + ((y2 - y1) * new_distance) / d

    return current_fuel, x2, y2


def fuel_needed(d, gas_consumption):
    return "%.2f" % (gas_consumption * 0.01 * d)


def distance(x1, y1, x2, y2):
    d = sqrt(abs(float(x2)-float(x1))**2 + abs(float(y2)-float(y1))**2)
    return d


def read_number(prompt, error_message="Incorrect input!"):
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


main()
