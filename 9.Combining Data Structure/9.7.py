"""
TIE-02100 Johdatus ohjelmointiin, kevÃ¤t 2018
TIE-02106 Introduction to Programming, Spring 2018
A tool program for analyzing friendship networks
Firstname Lastname, StudentId
"""
# TODO: Update your name and student id in the initial comment.


DEFAULT_FILENAME = "friendships.txt"


def read_friendship_network(filename):
    """
    Read a friendship network description file which must contain
    lines in the following format:

        name;friend_1;friend_2;...;friend_n

    At least one friend (i.e. friend_1) must be present on every line
    of the file, but there is no upper limit to how many friends a line
    can contain.

    :param str filename: Name of the friendship network file to be read.
    :return: The data structure containing the friendship network
             information or None in the case of an error.
    """

    # TODO: Initialize a variable named "network" here.
    #       It will be the variable which contains all the
    #       relevant information concerning the friendships
    #       when used later in the program.
    network = list()

    ###################################################
    #  Ã„LÃ„ MUUTA TÃ„TÃ„ FUNKTIOTA TÃ„MÃ„N RIVIN JÃ„LKEEN!  #
    #  DO NOT MODIFY THIS FUNCTION AFTER THIS LINE!   #
    ###################################################

    try:
        with open(filename, mode="r") as fileobj:
            for line in fileobj:
                line = line.strip()

                # Any line in the input file which begins with # is
                # considered a comment line and is skipped.  You can
                # therefore add # characters in the beginning of the
                # lines to temporarily ignore some lines for testing
                # purposes.
                if len(line) > 0 and line[0] == "#":
                    continue

                fields = line.split(";")

                if len(fields) < 2:
                    print(f"Fatal Error: line '{line}' has too few fields.")
                    return None

                for name in fields:
                    if not name.isalpha():
                        print(f"Fatal Error: '{name}' is not a valid name.")
                        return None

                who = fields[0]
                for friend in fields[1:]:
                    # Remember: add_friendship automatically records the
                    # friendships in two ways: <friend> will be <who>'s friend,
                    # and <who> will be <friend>'s friend.
                    add_friendship(network, who, friend)

        return network

    except IOError:
        print(f"Fatal Error: opening '{filename}' failed.")
        return None


def user_interface(network):
    """
    Implements a simple user interface for the friendship network analyzer.

    The errors resulting from faulty user inputs are not fatal errors
    and the program will continue working after printing an error message.
    Most of the error messages are printed in the command functions as this
    leaves the user interface function very clear and easy to understand.

    :param ??? network: The data structure containing the information about
                        who is friends with whom.
    :return: None
    """

    ##################################
    #  Ã„LÃ„ MUUTA TÃ„TÃ„ FUNKTIOTA!     #
    #  DO NOT MODIFY THIS FUNCTION!  #
    ##################################

    while True:
        print()
        print("Enter one of the commands "
              "[Pp]rint/[Aa]dd/[Ff]riends/[Cc]ommon/[Qq]uit")
        print("followed by one or more names if needed.")
        fields = input("Enter command: ").strip().split()

        if len(fields) == 0:
            print("Error: an empty line is not a valid command.")
            continue

        command = fields[0]
        rest = fields[1:]

        if command in ["P", "p"]:
            print_command(network, rest)

        elif command in ["A", "a"]:
            add_command(network, rest)

        elif command in ["F", "f"]:
            friends_command(network, rest)

        elif command in ["C", "c"]:
            common_friends_command(network, rest)

        elif command in [ "Q", "q" ]:
            print("Farewell cruel world...")
            return

        else:
            print(f"Error: unknown command '{command}'.")


def add_friendship(network, name1, name2):
    """
    Adds a friendship between name1 and name2.

    There are two situations which are not considered as errors
    but the function just doesn't do anything:

    - name1 is the same as name2
    - name1 and name2 are already friends.

    If name1 or name2 is not a name (i.e. it contains other
    characters than letters) an error message is printed and
    network is not modified.

    The friendship relation is always a two way relation:
    name1 will be registered as a friend of name2, and name2
    will be registered as a friend of name1.

    :param network: Data structure containing the friendship network.
                    This parameter will be modified to include the
                    new two way friendship.
    :param str name1: Person 1's name
    :param str name2: Person 2's name
    :return: None
    """

    # This error check is not necessary here since both
    # read_friendship_network and add_command functions (i.e. the only two
    # functions who call this function) already make sure that names only
    # contain letters.  It won't hurt anything to keep this check here
    # anyway, just in case.
    for name in [name1, name2]:
        if not name.isalpha():
            print("Error: '{name}' is not a valid name: friendship not added.")
            return

    # TODO: Implement a sanity check here to make sure no one
    #       can be added as his or her own friend.
    if name1 == name2:
        # print("Error: '{name1}' can not be his own friend.")
        return
    # TODO: Add information about <name1> being <name2>'s friend and
    #       <name2> being <name1>'s friend into the parameter data
    #       structure <network>.  Note: if <name1> and <name2> are
    #       already known to be friends, nothing needs to be done.
    if (name1, name2) in network or (name2, name1) in network:
        pass
    else:
        network.append((name1, name2))


def print_command(network, namelist):
    """
    The function neatly prints out the friendship network.
    All the names and friends' names are printed in alphabetical order.
    Friends' names are printed under the name of the person whose friends
    they are. In front of the every friend's name there is "- "
    (minus and space) character combination.

    The parameter namelist must be an empty list, otherwise an error message
    will be printed and function will return back to user interface which
    will continue normally.

    :param ??? network: Contains the friendship network to be printed.
    :param list namelist: This parameter should be an empty list since
                          print command doesn't require any names after it.
                          It is passed as a parameter only for error checking
                          purposes.
    :return: None
    """
    # print(network)
    # return
    if len(namelist) != 0:
        print("Error: there was extra text after [Pp]rint command.")
        return

    # TODO: Print the information of all friendships in the order
    #       and format shown in the project instructions.
    # get the unique name from tuple list network
    names = set(j for i in network for j in i)

    for name in sorted(names):
        temp1 = filter(lambda tup: name in tup, network)  # get the friends list of a person
        friends = list(set(j for i in temp1 for j in i))  # get the list of unique friends name
        friends.remove(name)  # remove the person name from the friends list
        print(name)
        print("\n".join('- {}'.format(friend) for friend in (sorted(friends))))


def add_command(network, namelist):
    """
    Adds a friendship between the first element of the namelist
    and the rest of its elements.

    The friendships are automatically considered to be a two way relationship,
    therefore, if A has B added as his friend, B will also have A added
    as her friend.

    Any errors happening during a call to this functions are not fatal
    errors.  The function will print an error message and return back
    to the user interface which will continue normally.

    In case of any error, network will be left unmodified.

    :param ??? network: The friendship network data structure which will
                        be modified as a result of the call to this function.
    :param list(str) namelist: This list must have at least two elements.
                               The first one is the name of the person to
                               whom we want to add friends.  The rest of the
                               elements are the names of the friends to be
                               added.
    :return: None
    """

    ##################################
    #  Ã„LÃ„ MUUTA TÃ„TÃ„ FUNKTIOTA!     #
    #  DO NOT MODIFY THIS FUNCTION!  #
    ##################################

    if len(namelist) < 2:
        print("Error: [Aa]dd command requires minimum two names.")
        return

    for name in namelist:
        if not name.isalpha():
            print(f"Error: '{name}' is not a valid name.")
            return

    for friend in namelist[1:]:
        # Remember, add_friendship function is supposed to automatically
        # add a two way relationship.  Therefore one call to it is enough.
        add_friendship(network, namelist[0], friend)


def friends_command(network, namelist):
    """
    Print out, in aplhabetical order, all the friends of the person whose
    name is the only element in the namelist parameter.

    An error message is printed if the namelist doesn't contain exactly
    one element which is a string of letters.

    An error message is also printed if the name in the namelist does not
    exist in the friendship network.

    These error conditions are not fatal errors. The program will continue
    normally after printing an error message and returning to the
    user interface.

    :param ??? network: Data structure containing the friendship information.
    :param list(str) namelist: List containing one element: the name of the
                               person whose friends are we interested in
                               printing.
    :return: None
    """

    if len(namelist) != 1:
        print("Error: [Ff]riends command requires exactly one name.")
        return

    name = namelist[0]

    if not name.isalpha():
        print(f"Error: {name} is not a valid name.")
        return

    # TODO: Check if <name> is an unknown person. If so print an error
    #       message and stop.  The error message should be printed as follows:
    #
    #           print(f"Error: '{name}' is an unknown name.")
    names = set(j for i in network for j in i)
    if name not in names:
        print(f"Error: '{name}' is an unknown name.")
        return

    # TODO: Print <name>'s friends in alphabetical order as
    #       described in the project instructions.
    temp1 = filter(lambda tup: name in tup, network)  # get the friends list of a person
    friends = list(set(j for i in temp1 for j in i))  # get the list of unique friends name

    friends.remove(name)  # remove the person name from the friends list
    print(*(sorted(friends)), sep="\n")


def common_friends_command(network, namelist):
    """
    Prints, in alphabetical order, the common friends of the two persons whose
    names are in the namelist.

    The following error conditions are possible:

    - There are more or less than two names in the namelist.
    - Either of the names in the namelist contains some other
      characters than letters.
    - Either of the names in namelist does not exist in the network.

    All these errors cause an error message to printed but they are not
    fatal errors: the program will return to user interface and continue
    normally after printing the error message.

    :param ??? network: Data structure containing the friendship information.
    :param list(str) namelist: A list containing exactly two names.
    :return: None
    """
    names = set(j for i in network for j in i)

    if len(namelist) != 2:
        print("[Cc]ommon command requires exactly two names.")
        return

    for name in namelist:
        if not name.isalpha():
            print(f"Error: {name} is not a valid name.")
            return

    for name in namelist:
        # TODO: Check if <name> is an unknown person. If so print
        #       an error message and stop.  The error message should
        #       be printed as follows:
        #
        #           print(f"Error: '{name}' is an unknown name.")
        if name not in names:
            print(f"Error: '{name}' is an unknown name.")
            return
        pass

    name1 = namelist[0]
    name2 = namelist[1]

    # TODO: Just as a matter of common sense, let's agree that a person
    #       does not have common friends with him/herself.  Check this
    #       and if so print a message and stop.  The message should
    #       be printed in the following format:
    #
    #           print(f"{name1} has no common friends with him/herself.")
    if name1 == name2:
        print(f"{name1} has no common friends with him/herself.")
        return

    # TODO: Find the common friends of <name1> and <name2>
    #       and print them on the screen in an alphabetical order.
    #       If <name1> and <name2> do not have common friends,
    #       print instead an error message:
    #
    #         print(f"{name1} and {name2} have no common friends.")
    temp1 = filter(lambda tup: name1 in tup, network)  # get the friends list of a person
    friends1 = list(set(j for i in temp1 for j in i))  # get the list of unique friends name
    friends1.remove(name1)  # remove the person name from the friends list

    temp2 = filter(lambda tup: name2 in tup, network)  # get the friends list of a person
    friends2 = list(set(j for i in temp2 for j in i))  # get the list of unique friends name
    friends2.remove(name2)  # remove the person name from the friends list

    commons = sorted(list(set(friends1).intersection(friends2)))
    if len(commons) > 0:
        print(*commons, sep="\n")
    else:
        print(f"{name1} and {name2} have no common friends.")


def main():
    ##################################
    #  Ã„LÃ„ MUUTA TÃ„TÃ„ FUNKTIOTA!     #
    #  DO NOT MODIFY THIS FUNCTION!  #
    ##################################

    filename = input("Enter the name of the input file: ")

    # If the user inputs an empty filename let's use the default file.
    if filename == "":
        filename = DEFAULT_FILENAME

    net = read_friendship_network(filename)

    if net is None:
        return
    else:
        print(f"File {filename} successfully read.")

    user_interface(net)


main()