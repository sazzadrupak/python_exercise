# TIE-02106 Introduction to Programming
# Lecture example: One dice game
# Version 1: the number of players is fixed to two and the whole program is
# implemented using this logic.

# UNFINISHED! We will continue from here in the next lecture by for example
# adding the dice pictures.

from tkinter import *
import random


WINPOINTS = 50

PLAYER_1 = 1
PLAYER_2 = 2


class Dicegame:
    def __init__(self):
        # Creating the window and the components
        self.__window = Tk()
        self.__window.title("Dicegame")
        self.__window.option_add("*Font", "Verdana 14")

        self.__dice_label = Label(self.__window, font="Verdana 72 bold",
                                  width=1, borderwidth=6, relief=RAISED)

        self.__throw_button \
            = Button(self.__window, text="throw", command=self.throw)
        self.__hand_over_button \
            = Button(self.__window, text="hand over", command=self.hand_over)
        self.__new_game_button \
            = Button(self.__window, text="new game", command=self.new_game)
        self.__quit_button \
            = Button(self.__window, text="quit", command=self.quit)

        self.__player1_points_title_label \
            = Label(self.__window, text="Player 1 points:")
        self.__player2_points_title_label \
            = Label(self.__window, text="Player 2 points:")
        self.__points_accumulated_title_label \
            = Label(self.__window, text="Accumulated points:")
        self.__instructions_label = Label(self.__window, anchor=E, text="@")

        self.__player1_points_label = Label(self.__window, width=3, anchor=E)
        self.__player2_points_label = Label(self.__window, width=3, anchor=E)
        self.__points_accumulated_label = Label(self.__window, width=3, anchor=E)

        # Placing the components
        self.__dice_label.grid(row=0, column=1, rowspan=3, sticky=N + E + S + W)

        self.__throw_button.grid(row=0, column=0, sticky=E + W)
        self.__hand_over_button.grid(row=1, column=0, sticky=E + W)
        self.__new_game_button.grid(row=2, column=0, sticky=E + W)
        self.__quit_button.grid(row=3, column=0, sticky=E + W)

        self.__player1_points_title_label.grid(row=0, column=2, sticky=E)
        self.__player2_points_title_label.grid(row=1, column=2, sticky=E)
        self.__points_accumulated_title_label.grid(row=2, column=2, sticky=E)

        self.__instructions_label.grid(row=3, column=1, columnspan=3, sticky=E + W)
        self.__player1_points_label.grid(row=0, column=3, sticky=E)
        self.__player2_points_label.grid(row=1, column=3, sticky=E)
        self.__points_accumulated_label.grid(row=2, column=3, sticky=E)

        self.new_game()

        # Start the userinterface
        self.__window.mainloop()

    def new_game(self):
        self.__player1_points = 0
        self.__player2_points = 0
        self.__accumulated_points = 0
        self.__number_of_turns = 0
        self.__whose_turn = PLAYER_1
        self.update_ui()

    def update_ui(self):
        self.__player1_points_label["text"] = self.__player1_points
        self.__player2_points_label["text"] = self.__player2_points
        self.__points_accumulated_label["text"] = self.__accumulated_points
        self.__instructions_label["text"] = "Player "+str(self.__whose_turn)+\
                                            " throw the dice or hand over the turn"

    def throw(self):
        dice = random.randint(1, 6)
        self.__dice_label["text"] = dice

        if dice == 1:
            self.__accumulated_points = 0
            if self.__whose_turn == PLAYER_1:
                self.__whose_turn = PLAYER_2
            else:
                self.__whose_turn = PLAYER_1
        else:
            self.__accumulated_points += dice
        self.update_ui()

    def hand_over(self):
        if self.__whose_turn == PLAYER_1:
            self.__player1_points += self.__accumulated_points
            self.__whose_turn = PLAYER_2
        else:
            self.__player2_points += self.__accumulated_points
            self.__whose_turn = PLAYER_1

        self.__accumulated_points = 0
        self.update_ui()

    def quit(self):
        self.__window.destroy()


def main():
    game = Dicegame()


main()