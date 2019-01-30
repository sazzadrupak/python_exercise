class Fraction:
    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator), abs(self.__denominator))

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator), abs(self.__denominator))

    def simplify(self):
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    # def sum_method(self, f1, f2):
        # temp1 = f1.split("/")
        # temp2 = f2.split("/")
        # numerator = int(temp1[0]) + int(temp2[0])
        # denominator = int(temp1[1]) + int(temp2[1])
        # res = Fraction(numerator, denominator)
        # return res.return_string()


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def get_command(error_message="Unknown command!"):
    try:
        command = input("> ")
        if command == 'add' or command == 'print' or command == 'list' or command == '*' or command == 'file' \
                or command == '+' or command == '-' or command == '/' or command == 'quit':
            return command
        else:
            raise ValueError()
    except ValueError:
        print(error_message)
        return get_command(error_message)


def add_method(fraction_dict):
    fraction_input = input("Enter a fraction in the form integer/integer: ")
    fraction_name = input("Enter a name: ")
    split_value = fraction_input.split("/")
    numerator = int(split_value[0])
    denominator = int(split_value[1])
    fraction_object = Fraction(numerator, denominator)
    fraction_dict[fraction_name] = fraction_object


def multiplication_method(operand1, operand2, fraction_dict):
    numerator1, denominator1 = get_numerator_denominator(str(fraction_dict[operand1]))
    numerator2, denominator2 = get_numerator_denominator(str(fraction_dict[operand2]))
    new_fraction = Fraction((numerator1 * numerator2), (denominator1*denominator2))
    print("{} * {} = {}".format(fraction_dict[operand1], fraction_dict[operand2], new_fraction))
    new_fraction.simplify()
    print("simplified {}".format(new_fraction))


def sum_method(operand1, operand2, fraction_dict):
    numerator1, denominator1 = get_numerator_denominator(str(fraction_dict[operand1]))
    numerator2, denominator2 = get_numerator_denominator(str(fraction_dict[operand2]))
    denominator3 = (denominator1 * denominator2)
    temp1 = denominator3 / denominator1
    temp2 = denominator3 / denominator2
    numerator3 = temp1 * numerator1
    numerator4 = temp2 * numerator2
    new_fraction = Fraction(int((numerator3 + numerator4)), denominator3)
    print("{} + {} = {}".format(fraction_dict[operand1], fraction_dict[operand2], new_fraction))
    new_fraction.simplify()
    print("simplified {}".format(new_fraction))


def substract_method(operand1, operand2, fraction_dict):
    numerator1, denominator1 = get_numerator_denominator(str(fraction_dict[operand1]))
    numerator2, denominator2 = get_numerator_denominator(str(fraction_dict[operand2]))
    denominator3 = (denominator1 * denominator2)
    temp1 = denominator3 / denominator1
    temp2 = denominator3 / denominator2
    numerator3 = temp1 * numerator1
    numerator4 = temp2 * numerator2
    new_fraction = Fraction(int((numerator3 - numerator4)), denominator3)
    print("{} - {} = {}".format(fraction_dict[operand1], fraction_dict[operand2], new_fraction))
    new_fraction.simplify()
    print("simplified {}".format(new_fraction))


def devide_method(operand1, operand2, fraction_dict):
    numerator1, denominator1 = get_numerator_denominator(str(fraction_dict[operand1]))
    numerator2, denominator2 = get_numerator_denominator(str(fraction_dict[operand2]))
    new_fraction = Fraction((numerator1 * denominator2), (numerator2 * denominator1))
    print("{} / {} = {}".format(fraction_dict[operand1], fraction_dict[operand2], new_fraction))
    new_fraction.simplify()
    print("simplified {}".format(new_fraction))


def input_operand(fraction_dict):
    try:
        first_operand = input("1st operand: ")
        if first_operand in fraction_dict:
            pass
        else:
            raise Exception("Name {} was not found".format(first_operand))

        second_operand = input("2nd operand: ")
        if second_operand in fraction_dict:
            pass
        else:
            raise Exception("Name {} was not found".format(second_operand))
        return first_operand, second_operand
    except Exception as ex:
        print(ex)
        return False


def get_numerator_denominator(fraction):
    split_value = fraction.split("/")
    numerator = int(split_value[0])
    denominator = int(split_value[1])
    return int(numerator), int(denominator)


def main():
    fraction_dict = {}
    while True:
        command = get_command()
        if command == 'add':
            add_method(fraction_dict)
            continue
        elif command == 'print':
            print_method(fraction_dict)
            continue
        elif command == 'list':
            list_method(fraction_dict)
            continue
        elif command == '*' or command == '+' or command == '-' or command == '/':
            temp = input_operand(fraction_dict)
            if temp is not False:
                f1, f2 = temp
                arithmetic_dict = {'+': lambda f1, f2, fraction_dict: sum_method(f1, f2, fraction_dict),
                                   "-": lambda f1, f2, fraction_dict: substract_method(f1, f2, fraction_dict),
                                   '*': lambda f1, f2, fraction_dict: multiplication_method(f1, f2, fraction_dict),
                                   '/': lambda f1, f2, fraction_dict: devide_method(f1, f2, fraction_dict)}
                if command in arithmetic_dict.keys():
                    func = arithmetic_dict.get(command)
                    temp = func.__call__(f1, f2, fraction_dict)
            continue
        elif command == 'file':
            file_input_method(fraction_dict)
            continue
        elif command == 'quit':
            print("Bye bye!")
            break


main()
