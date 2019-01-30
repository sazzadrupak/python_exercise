def factorial(value):
    if value is 0:
        return 1
    else:
        return value * factorial(value - 1)


def foo(lottery_balls, drawn_balls):
    return int((factorial(lottery_balls)) / ((factorial(lottery_balls - drawn_balls)) * factorial(drawn_balls)))


def main():
    lottery_balls = input("Enter the total number of lottery balls: ")
    drawn_balls = input("Enter the number of the drawn balls: ")

    if (int(lottery_balls) < 0) or (int(drawn_balls) < 0):
        print('The number of balls must be a positive number.')
    elif int(lottery_balls) <= (int(drawn_balls)):
        print('At most the total number of balls can be drawn.')
    else:
        print("The probability of guessing all %s" % drawn_balls, "balls correctly is 1/%s" % foo(int(lottery_balls), int(drawn_balls)))


main()
