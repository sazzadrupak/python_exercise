def number_series(range_value):
    for i in range_value:
        print(i)
    return


def main():
    number_series(range(0, 100+1, 2))
    number_series(range(100, 0-1, -2))


main()
