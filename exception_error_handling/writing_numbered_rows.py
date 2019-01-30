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
    filename = input("Enter the name of the file: ")
    try:
        f = open(filename, "w+")
        print("Enter rows of text. Quit by entering an empty row.")
        msg = read_message()
        i = 1
        for message in msg:
            f.write("%d %s\n" % (i, message))
            i += 1
        f.close()
        print("File %s has been written." % filename)
    except FileNotFoundError:
        print("Writing the file %s was not successful." % filename)


main()
