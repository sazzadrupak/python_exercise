# TIE-02106 Introduction to Programming
# Task: Ristinolla game (GUI components in in lists)
# Two players can play this Tic Tac Toe game,
# palyers' turn will move automatically from one player to second player
# if same icon matches in the same row or same column or diagonally, then that player has won the game.
# 9 turns available for a entire game, if total turns reach 9, then the game is drawn
# Current player turn, total turn count info will be shown at the bottom of the gui
# Won player or drawn game info text will be shown
# new game button will start the game from the initial state
# stop button will close the gui window

from tkinter import *

PLAYER_NUMBER = 2
PLAYER_ICON = ['X', 'O']
width, height = 3, 3  # width = button number row wise, height = button number column wise
total_turn = 9  # total turn in a game


class Ristinolla:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Ristinolla")

        self.__turn = 0  # by default X player turns first
        self.__turn_count = 0  # count the total turn, max number is 9
        self.game_board = []  # hold the players turn in a matrix to check win or draw
        self.__game_lock = False  # lock the game after a win, so no click event

        # initialize game board buttons number
        self.__ristinolla_buttons = [[0 for x in range(width)] for y in range(height)]

        Button(self.__window, text="new game", command=self.initialize_game) \
            .grid(row=0, column=5, sticky=W + E + N)
        Button(self.__window, text="stop", command=self.__window.destroy) \
            .grid(row=1, column=5, sticky=W + E + S)

        self.__infoLabel = Label(self.__window)
        self.__infoLabel.grid(row=5, column=0, columnspan=2)

        self.initialize_game()

    def initialize_game(self):
        '''
        Initialize the game from the very beginning state
        :return:
        '''
        self.__turn = 0
        self.__turn_count = 0
        self.__game_lock = False

        # game info label text with current player turn and total turn count
        self.__gamesituationtext = "Player " + PLAYER_ICON[self.__turn] + " turn. \n Total move: " \
                                   + str(self.__turn_count)

        # show the buttons in the gui in a 2D matrix
        for i in range(0, width, 1):
            for j in range(0, height, 1):
                new_button = Button(self.__window, height=4, width=8)
                new_button.grid(row=i, column=j)
                new_button.configure(text='', command=lambda i=i, j=j: self.game_move(i, j))
                self.__ristinolla_buttons[i][j] = new_button

        self.game_board_marks()
        self.update_ui_texts()

    def game_board_marks(self):
        '''
        put the player mark in the game board matrix array,
        initially only "." will be stored
        :return:
        '''
        self.game_board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

    def game_move(self, i, j):
        '''
        after button click, make a move
        :param i:
        :param j:
        :return:
        '''
        if self.__game_lock:
            # if the game is locked, nothing is here
            pass
        else:
            self.__turn_count += 1  # increment the total turn count

            if self.__turn_count >= 9:  # check if the total turn count gte 9
                self.__ristinolla_buttons[i][j].configure(text=PLAYER_ICON[self.__turn], state=DISABLED)  # disable clicked button
                self.game_board[i][j] = PLAYER_ICON[self.__turn]
                win_draw = self.check_board(i, j)  # check the game board for a result
                if win_draw is True:
                    self.__game_lock = True  # final result found and lock the game to disable game state
                    self.__gamesituationtext = "The winner is " + PLAYER_ICON[self.__turn]
                else:
                    self.__gamesituationtext = "Game drawn."

            else:
                self.__ristinolla_buttons[i][j].configure(text=PLAYER_ICON[self.__turn], state=DISABLED)  # disable clicked button
                self.game_board[i][j] = PLAYER_ICON[self.__turn]

                win_draw = self.check_board(i, j)  # check the game board for a result
                if win_draw is True:
                    self.__game_lock = True  # final result found and lock the game to disable game state
                    self.__gamesituationtext = "The winner is " + PLAYER_ICON[self.__turn]
                else:
                    self.__turn = (self.__turn + 1) % PLAYER_NUMBER  # move turn to second player
                    self.__gamesituationtext = "Player " + PLAYER_ICON[self.__turn] + " turn. \n Total move: " \
                                           + str(self.__turn_count)
            self.update_ui_texts()

    def check_board(self, j, i):
        '''
        check the board to match the icons
        :param j:
        :param i:
        :return: True if 3 icons matched, False if not matched
        '''
        if self.game_board[j][0] == self.game_board[j][1] == self.game_board[j][2] or self.game_board[0][i] == \
                self.game_board[1][i] == self.game_board[2][i] \
                or (
                self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != "." and self.game_board[0][0]
                == self.game_board[1][1] == self.game_board[2][2]) \
                or (
                self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != "." and self.game_board[0][2]
                == self.game_board[1][1] == self.game_board[2][0]):
            return True
        else:
            return False

    def update_ui_texts(self):
        self.__infoLabel.configure(text=self.__gamesituationtext)

    def start(self):
        self.__window.mainloop()


def main():
    ui = Ristinolla()
    ui.start()


main()
