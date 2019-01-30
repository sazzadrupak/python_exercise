def read_input(input_string):
    while True:
        try:
            user_input = int(input(input_string))
            if user_input <= 0:
                raise ValueError
        except ValueError:
            continue
        else:
            return user_input


def print_box(width, height, mark):
    height_counter = 0
    print()
    while height_counter < int(height):
        print(mark * int(width))
        height_counter += 1


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print_box(width, height, mark)


main()
