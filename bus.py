def get_next_bus_time(bus_time, position):
    next_three = []
    count = 0
    while True:
        count += 1
        if count > 3:
            break
        else:
            next_three.append(bus_time[position])
            position = (position + 1) % len(bus_time)
    return next_three


def main():
    bus_time = [630, 1015, 1415, 1620, 1720, 2000]
    user_given_time = int(input("Enter the time (as an integer): "))
    index = [n for n, i in enumerate(bus_time) if i >= user_given_time]
    if len(index) == 0:
        position = 0
    else:
        position = index[0]
    next_busses = get_next_bus_time(bus_time, position)

    print("The next buses leave:")
    for bus in next_busses:
        print(bus)


main()
