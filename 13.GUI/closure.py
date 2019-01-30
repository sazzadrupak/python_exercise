def create_a_counter():

    counter = 0

    def innerFunction():
        nonlocal counter
        counter += 1
        return counter

    return innerFunction


if __name__ == '__main__':
    first_counter = create_a_counter()
    second_counter = create_a_counter()
    print(first_counter())
    print(second_counter())
    print(first_counter())
    print(first_counter())
    print(second_counter())
