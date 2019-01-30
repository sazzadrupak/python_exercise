def read_message():
    user_message_list = []
    while True:
        user_messages = input("")
        if user_messages is not "":
            user_message_list.append(user_messages)
        else:
            break
    return user_message_list


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
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for message in msg:
        print(row_encryption(message))


main()
