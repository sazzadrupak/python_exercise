def get_command(error_message="Unknown command!"):
    try:
        command = input("> ")
        if command == 'add' or command == 'print' or command == 'list' or command == 'scalarproduct' \
                or command == 'file' or command == 'matrixproduct' or command == 'quit':
            return command
        else:
            raise ValueError()
    except ValueError:
        print(error_message)
        return get_command(error_message)


def print_method(matrics_dict):
    matrics_name = input("Name: ")
    if matrics_name in matrics_dict:
        print(matrics_name, "=", matrics_dict[matrics_name])
    else:
        print("Name {} was not found".format(matrics_name))


def list_method(matrics_dict):
    if len(matrics_dict) > 0:
        for item in sorted(matrics_dict):
            print(item, "=", matrics_dict[item])


def add_method():
    file_name = input("Enter the name of the matrix file: ")
    try:
        matrics_list = []
        f = open(file_name, "r")
        for line in f:
            matrics_list.append([int(x) for x in line.split(' ')])
        return matrics_list
    except IOError:
        print("Error: the file cannot be read.")


def scalarproduct(matrics_list):
    matrics_name = input("Enter the name: ")
    if matrics_name in matrics_list:
        try:
            multiplier = int(input("Enter a multiplier: "))
            multiply = [[elem * multiplier for elem in row] for row in matrics_list[matrics_name]]
            print(multiplier, "*", matrics_list[matrics_name], "\n=", multiply)
        except ValueError:
            return
    else:
        print("Name {} was not found".format(matrics_name))


def matrixproduct(matrics_list):
    try:
        first_operand = input("1st name: ")
        if first_operand in matrics_list:
            pass
        else:
            raise Exception("Name {} was not found".format(first_operand))

        second_operand = input("2nd name: ")
        if second_operand in matrics_list:
            pass
        else:
            raise Exception("Name {} was not found".format(second_operand))

        result = []
        X = matrics_list[first_operand]
        Y = matrics_list[second_operand]
        numrows = len(Y)
        numcols = len(X[0])

        if numcols == numrows:
            result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
            print(X, "\n*", Y, '\n=', result)
        else:
            raise ValueError("Error, the dimensions of the matrices don't match")

    except Exception as ex:
        print(ex)
        return False


def main():
    matrics_list = {}
    while True:
        command = get_command()
        if command == 'add':
            matrics = add_method()
            matrics_name = input("Enter a name for the matrix: ")
            matrics_list[matrics_name] = matrics
            continue
        elif command == 'print':
            print_method(matrics_list)
            continue
        elif command == 'list':
            list_method(matrics_list)
            continue
        elif command == 'scalarproduct':
            scalarproduct(matrics_list)
            continue
        elif command == 'matrixproduct':
            matrixproduct(matrics_list)
            continue
        elif command == 'quit':
            print("Bye bye!")
            break

main()
