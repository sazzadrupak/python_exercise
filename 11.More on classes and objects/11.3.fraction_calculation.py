class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

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

    def complement(self):
        return Fraction(-1*self.__numerator, self.__denominator)

    def reciprocal(self):
        swap_numerator, swap_denominator = self.__denominator, self.__numerator
        return Fraction(swap_numerator, swap_denominator)

    def multiply(self, other):
        return Fraction(self.__numerator*other.__numerator, self.__denominator*other.__denominator)

    def divide(self, other):
        return Fraction(self.__numerator*other.__denominator, self.__denominator*other.__numerator)

    def add(self, other):
        multiply_denominator = self.__denominator*other.__denominator
        var1 = self.__numerator*(multiply_denominator//self.__denominator)
        var2 = other.__numerator*(multiply_denominator//other.__denominator)
        return Fraction(var1+var2, multiply_denominator)

    def deduct(self, other):
        multiply_denominator = self.__denominator*other.__denominator
        var1 = self.__numerator*(multiply_denominator//self.__denominator)
        var2 = other.__numerator*(multiply_denominator//other.__denominator)
        return Fraction(var1-var2, multiply_denominator)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a
