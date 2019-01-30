def print_ints(n, k=1, sep=" "):
    if k > 0:
        range_number = abs(n) + 1
        for i in range(0, range_number, k):
            if n < 0:
                m = i
                if i == abs(n) - 1:
                    print("%d" % -m, end='')
                else:
                    print("%d" % -m, end=sep)
            else:
                m = i
                if i == abs(n):
                    print("%d" % m, end='')
                else:
                    print("%d" % m, end=sep)
        print()
    else:
        print("Illegal parameter k = %d!" % k)


def main():
    # print_ints(4, 2, "_")
    # print_ints(-5, 2)
    # print_ints(5, sep=" < ")
    # print_ints(2, 0)
    print_ints(7, -5)
    print_ints(10, 2, ' # ')
    print_ints(-10, 3, ' > ')


main()