import csv


def main():

    input_file = input("Enter the name of the input file: ")
    input_dialect = input("and its dialect: ")
    output_file = input("Enter the name of the output file: ")
    output_dialect = input("and its dialect: ")
    if input_dialect not in csv.list_dialects() or output_dialect not in csv.list_dialects():
        print()
        print("The given dialect is wrong.")
        return
    read_list = []

    try:

        with open(input_file, newline='') as my_input_file:
            input_reader = csv.reader(my_input_file, dialect=input_dialect)
            for row in input_reader:
                read_list.append(row)

        with open(output_file, 'w', newline='') as my_output_file:
            output_writer = csv.writer(my_output_file, dialect=output_dialect)
            for items in read_list:
                output_writer.writerow(items)

        print()
        print("File", input_file, "has been converted into", output_dialect+".")

    except IOError:
        print()
        print("There was an error in handling the file.")


main()
