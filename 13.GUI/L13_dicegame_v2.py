# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Lecture example: one-dice dicegame
# Version 2, where you can change the number of players by changing the value
# of the constant NR_OF_PLAYERS.

from tkinter import *
import random
import time

# These image files have to be in the PyCharmi project folder.
IMAGE_FILES = ["1S.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]

WIN_POINTS = 20
NR_OF_PLAYERS = 3


class Dicegame:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Dicegame")
        self.__window.option_add("*Font", "Verdana 16")

        # Create PhotoImage-objects of the image files and store them in a list.
        self.__dice_images = []
        for image_file in IMAGE_FILES:
            new_image = PhotoImage(file=image_file)
            self.__dice_images.append(new_image)

        # Empty PhotoImage-object, that is used as the initial value of the
        # self.__dice when a new game begins. All the dice images are
        # 86x86 pixels, so we make the initial value the same size.
        self.__empty_image = PhotoImage(width=86, height=86)

        # Column by column we define the GUI components and place them in
        # their positions using the grid.

        # ======================================================================
        # Column 0: Buttons
        # Why are some of the buttons stored as attributes and some are not?

        self.__throw_button = Button(self.__window, text="throw", command=self.throw)
        self.__throw_button.grid(row=0, column=0, sticky=W + E)

        self.__hand_over_button = Button(self.__window, text="hand over",
                                         command=self.hand_over)
        self.__hand_over_button.grid(row=1, column=0, sticky=W + E)

        Button(self.__window, text="new game", command=self.new_game) \
            .grid(row=2, column=0, sticky=W + E)
        Button(self.__window, text="quit", command=self.__window.destroy)\
            .grid(row=3, column=0, sticky=W + E)

        # ======================================================================
        # Column 1: Dice image and the instructions labels

        # The content of self.__dice will be set later in the new_game -method
        # and it will also be modified in the throw-method.
        self.__dice_label = Label(self.__window, anchor=N)
        self.__dice_label.grid(row=0, column=1, rowspan=3, padx=10, \
                               sticky=W + E + S + N)

        self.__instructions_label = Label(self.__window, anchor=E)
        self.__instructions_label.grid(row=NR_OF_PLAYERS + 1, column=1, \
                                       columnspan=3, sticky=E + W)

        # ======================================================================
        # Column 2: Text labels for the scores that are in the following column

        for i in range(NR_OF_PLAYERS):
            Label(self.__window, text="Player " + str(i + 1) + " points:") \
            .grid(row=i, column=2, sticky=E)
        Label(self.__window, text="Accumulated points:")\
            .grid(row=NR_OF_PLAYERS, column=2, sticky=E)

        # ======================================================================
        # Column 3: Labels where the scores are displayed.

        self.__point_labels = []

        for i in range(NR_OF_PLAYERS):
            new_point_label = Label(self.__window, width=3, anchor=E)
            new_point_label.grid(row=i, column=3, sticky=E)
            self.__point_labels.append(new_point_label)

        self.__accumulated_points_label = Label(self.__window, width=3, anchor=E)
        self.__accumulated_points_label.grid(row=NR_OF_PLAYERS, column=3, sticky=E)

        # ======================================================================

        self.new_game()
        self.__window.mainloop()


    # Method that initiates the values of all attributes. Is called both in
    # the constructor and when the button "new game" is clicked.
    def new_game(self):
        # Initial values for the attributes
        self.__points = [0] * NR_OF_PLAYERS
        self.__accumulated_points = 0
        self.__whose_turn = 0
        self.__instructions = "Player " + str(self.__whose_turn + 1) + \
                              " throw the dice or hand over the turn"

        self.update_gui_texts()
        self.__dice_label.configure(image=self.__empty_image)

        #Activate the buttons that can be deactivated
        self.__throw_button.configure(state=NORMAL)
        self.__hand_over_button.configure(state=NORMAL)


    # Method that updates the texts in the GUI components
    def update_gui_texts(self):
        for i in range(NR_OF_PLAYERS):
            self.__point_labels[i].configure(text=self.__points[i])
        self.__accumulated_points_label.configure(text=self.__accumulated_points)
        self.__instructions_label.configure(text=self.__instructions)


    # Method tied to the button "throw"
    def throw(self):
        dice = 0

        for i in range(0, 10):
            dice = random.randint(1, 6)
            self.__dice_label["image"] = self.__dice_images[dice - 1]
            self.__window.update_idletasks()

            time.sleep(0.05)

        if dice == 1:
            self.change_turn()
        else:
            self.__accumulated_points += dice
        self.update_gui_texts()


    # Method tied to the button "hand over"
    def hand_over(self):
        self.__points[self.__whose_turn] += self.__accumulated_points
        self.change_turn()


    # This method is called when you have dice 1 or when the player hands over
    # the turn.
    def change_turn(self):
        if self.__whose_turn == NR_OF_PLAYERS - 1:
            if self.is_over():
                return

        self.__whose_turn = (self.__whose_turn + 1) % NR_OF_PLAYERS
        self.__instructions = "Player " + str(self.__whose_turn + 1) + \
                                   " throw the dice or hand over the turn"
        self.__accumulated_points = 0
        self.update_gui_texts()


    # Method checks if the game is over and finds out and declares the winner(s).
    def is_over(self):
        winners = []
        for i in range(len(self.__points)):
            if self.__points[i] >= WIN_POINTS:
                winners.append(i)

        if len(winners) == 0:
            return False
        elif len(winners) == 1:
            self.__instructions = "Player " + str(winners[0] + 1) + " won!"
        else:
            self.__instructions = "Draw!"
        self.update_gui_texts()

        # Disable the buttons that should not be clicked when the game is over.
        self.__throw_button.configure(state=DISABLED)
        self.__hand_over_button.configure(state=DISABLED)
        return True


def main():
    Dicegame()


main()