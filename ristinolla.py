# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template


class RepeatError(Exception):
    pass


game_board = [[".", ".", "."],
              [".", ".", "."],
              [".", ".", "."]]


def show_game_board():
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            print(game_board[j][i], end="")
        print()


def check_board(j, i):
    if game_board[j][0] == game_board[j][1] == game_board[j][2] or game_board[0][i] == game_board[1][i] == game_board[2][i]\
            or (game_board[0][0] == game_board[1][1] == game_board[2][2] != "." and game_board[0][0] == game_board[1][1] == game_board[2][2]) \
            or (game_board[0][2] == game_board[1][1] == game_board[2][0] != "." and game_board[0][2] == game_board[1][1] ==game_board[2][0]):
        return True
    else:
        return False


def main():
    # TODO: implement the datastructure for storing the board
    show_game_board()
    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            # TODO: implement the turn of one player here

            if 0 < x > 2 or 0 < y > 2:
                raise IndexError
            elif game_board[x][y] != '.':
                raise RepeatError("Error: a mark has already been placed on this square.")
            else:
                turns += 1
                game_board[x][y] = mark
                show_game_board()
                win_draw = check_board(x, y)

                if win_draw is True:
                    print("The game ended, the winner is %s" % mark)
                    break
                else:
                    if turns == 9 and win_draw is False:
                        print("Draw!")
                        break
                    else:
                        continue
        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
                print("Error: coordinates must be between 0 and 2.")

        except RepeatError as e:
            print(e)


main()
