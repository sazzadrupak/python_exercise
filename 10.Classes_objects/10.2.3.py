"""
TIE-02100 Introduction to programming
MÃ¶lkky
"""


# TODO: Implement the class Player here
class Player:
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__round_counter = 0
        self.__number_of_zero = 0

    def get_name(self):
        return self.__name

    def add_points(self, points):
        if points == 0:
            self.__number_of_zero += 1

        self.__points += points
        self.__round_counter += 1
        if self.__points > 50:
            print("{} gets penalty points!".format(self.__name))
            self.__points = 25
        elif 40 <= self.__points <= 49:
            print("{} needs only {} points. It's better to avoid knocking down the pins with higher points.".format(
                self.__name, 50 - self.__points))
        else:
            if points > float(self.__points / self.__round_counter):
                print("Cheers {}!".format(self.__name))

    def has_won(self):
        if self.__points == 50:
            return True
        else:
            return False

    def get_points(self):
        return self.__points

    def success_percentage(self):
        if self.__round_counter > 0:  # check if this is the first round, if not then enter in to "if"
            if self.__number_of_zero > 0:  # if number of zero enter more than zero, then enter this "if" to check
                if self.__round_counter == 1:  # if this is the first round and entered point is zero, then success rate
                    # is zero also
                    return '0'
                else:  # if this is not first round
                    return float(((self.__round_counter - self.__number_of_zero) * 100) / self.__round_counter)
            else:
                return '100'
        else:  # if this is the first round, then success percentage will be 0
            return '0'


def main():

    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        in_turn.add_points(pts)
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p, hit percentage", round(float(player1.success_percentage()), 1))
        print(player2.get_name() + ":", player2.get_points(), "p, hit percentage", round(float(player2.success_percentage()), 1))
        print("")

        throw += 1


main()
