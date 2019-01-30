def number_file_rows():
    filename = input('Enter the name of the file: ')
    f = open(filename, "r")
    i = 1
    for line in f:
        print("%d %s" % (i, line), end="")
        i += 1


def main():
    number_file_rows()


main()
