def read_message():
    user_message_list = []
    while True:
        user_messages = input("")
        if user_messages is not "":
            user_message_list.append(user_messages)
        else:
            break
    return user_message_list


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for message in msg:
        print(message.upper())


main()
