def main():
    print("Give 5 numbers:")
    element_list = []
    for i in range(0, 5, 2):
        number = int(input("Next number: "))
        if number > 0:
            element_list.append(number)

    print("The numbers you entered that were greater than zero were:")
    for element in element_list:
        print(element)


main()
