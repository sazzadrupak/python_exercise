def main():
    print("Give 5 numbers:")
    element_list = []
    for i in range(0, 5, 1):
        number = int(input("Next number: "))
        element_list.append(number)

    print("The numbers you entered, in reverse order:")
    for element in element_list[::-1]:
        print(element)


main()
