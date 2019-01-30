# TIE-02106 Introduction to Programming
# Lecture example: One dice game
# Version 1: the number of players is fixed to two and the whole program is
# implemented using this logic.

from tkinter import *
import random
import time

# These image files have to be in the PyCharmi project folder.
IMAGE_FILES = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]

WINPOINTS = 50

PLAYER_1 = 1
PLAYER_2 = 2


class Dicegame:
    def __init__(self):
        # Creating the window and the components
        self.__window = Tk()
        self.__window.title("Dicegame")
        self.__window.option_add("*Font", "Verdana 14")

        # Create PhotoImage-objects of the image files and store them in a list.
        self.__dice_images = []
        for image_file in IMAGE_FILES:
            new_image = PhotoImage(file=image_file)
            self.__dice_images.append(new_image)

        # Empty PhotoImage-object, that is used as the initial value of the
        # self.__dice when a new game begins. All the dice images are
        # 86x86 pixels, so we make the initial value the same size.
        self.__empty_image = PhotoImage(width=86, height=86)

        self.__dice_label = Label(self.__window, anchor=N)
        self.__dice_label.grid(row=0, column=1, rowspan=3, padx=10, \
                               sticky=W + E + S + N)

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
        self.__whose_turn = PLAYER_1
        self.__dice_label["image"] = self.__empty_image
        self.update_ui()

        # Activate the buttons that can be deactivated
        self.__throw_button.configure(state=NORMAL)
        self.__hand_over_button.configure(state=NORMAL)


    def update_ui(self):
        self.__player1_points_label["text"] = self.__player1_points
        self.__player2_points_label["text"] = self.__player2_points
        self.__points_accumulated_label["text"] = self.__accumulated_points
        self.__instructions_label["text"] = "Player "+str(self.__whose_turn)+\
                                            " throw the dice or hand over the turn"

    def throw(self):
        dice = 0

        # To create an impression of throwing the dice we will create 10
        # random numbers and update the dice image according to them as the
        # image of self.__dice_label.
        for i in range(10):
            dice = random.randint(1, 6)
            self.__dice_label["image"] = self.__dice_images[dice-1]

            # Normally the GUI components are updated on screen in the mainloop.
            # To create this "animation" we need to get them updated faster,
            # this is done using the update_idletasks -method.
            self.__window.update_idletasks()

            # Time interval 0.05 seconds to make the animation look better.
            time.sleep(0.05)

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


        # NOTE! The game over is tested only after the turn of player 2, but
        # the condition has to be PLAYER_1 because the value of
        # self.__whose_turn has already been changed.
        if self.__whose_turn == PLAYER_1:
            if self.is_over():
                return


    def is_over(self):
        if self.__player1_points>= WINPOINTS \
                or self.__player2_points >= WINPOINTS:
            if self.__player1_points > self.__player2_points:
              self.__instructions_label.configure(text="Player 1 won!")
            elif self.__player2_points > self.__player1_points:
              self.__instructions_label.configure(text="Player 2 won!")
            else:
              self.__instructions_label.configure(text="Draw!")

            # Deactivate buttons that can not be used when game is over.
            self.__throw_button.configure(state=DISABLED)
            self.__hand_over_button.configure(state=DISABLED)

            return True
        else:
            return False


    def quit(self):
        self.__window.destroy()


def main():
    game = Dicegame()


main()