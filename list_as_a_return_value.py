def input_to_list(how_many_numbers):
    number_list = []
    print("Enter %d numbers:" % int(how_many_numbers))
    for i in range(how_many_numbers):
        number = int(input(""))
        number_list.append(number)
    return number_list


def main():
    how_many_numbers = int(input("How many numbers do you want to process: "))
    number_list = input_to_list(how_many_numbers)

    searched_number = int(input("Enter the number to be searched: "))
    found_count = 0
    for i in number_list:
        if i == searched_number:
            found_count += 1

    if found_count > 0:
        print("%d shows up %d times among the numbers you have entered." % (searched_number, found_count))
    else:
        print("%d is not among the numbers you have entered." % searched_number)


main()
