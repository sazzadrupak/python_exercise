def number_file_rows():
    filename = input('Enter the name of the file: ')
    try:
        f = open(filename, "r")
        i = 1
        for line in f:
            print("%d %s" % (i, line), end="")
            i += 1
    except FileNotFoundError:
        print("There was an error in reading the file.")


def main():
    number_file_rows()


main()
