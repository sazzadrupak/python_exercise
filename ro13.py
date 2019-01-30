# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ROT13, program code template


def encrypt(alphabet):
    if alphabet.isalpha():
        regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                         "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                         "w", "x", "y", "z"]

        encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                           "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                           "j", "k", "l", "m"]
        user_alphabet = alphabet.lower()
        index_of_alphabet = regular_chars.index(user_alphabet)
        encrypted_alphabet = encrypted_chars[index_of_alphabet]
        if alphabet.islower():
            alphabet = encrypted_alphabet
        else:
            alphabet = encrypted_alphabet.upper()
    else:
        pass

    return alphabet


def row_encryption(row):
    encrypted_string = ""
    for alphabet in row:
        encrypted_string += encrypt(alphabet)
    return encrypted_string


def main():
    print(row_encryption("Happy, happy, joy, joy!"))


main()
