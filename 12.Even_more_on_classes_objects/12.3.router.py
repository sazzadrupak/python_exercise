class Router:
    """ This class represents one single router """
    def __init__(self, router_name):
        """
        Constructor.
        :param router_name: routers' name
        """
        self.__router_name = router_name
        self.__neighbour = []  # make a list of a routers' objects
        self.__network = ''  # initialize a blank network
        self.__distance = ''  # initialize a blank distance
        self.__networks = []  # initialize a list of networks for a router

    def get_name(self):
        """
        :return the name of a router
        """
        return self.__router_name

    def add_neighbour(self, neighbour):
        """ Add a neighbour to a router
        :param neighbour: neighbour is the another object of the Router class
        :return: None
        """
        self.__neighbour.append(neighbour)

    def add_network(self, network, distance):
        """
        :param network: user given input, int
        :param distance: networks distance, int
        add a network to a router
        """
        self.__network = str(network)
        self.__distance = str(distance)
        network = self.__network + ":" + self.__distance
        self.__networks.append(network)

    def get_neighbour(self):
        """
        :return the list of neighbours of a router
        """
        return self.__neighbour

    def get_network(self):
        """
        :return the network and distance of a router
        """
        if len(self.__networks) > 0:  # check if the router has network
            return self.__networks  # router has network and return it
        else:
            return ''  # router does not have network, so return empty string

    def print_info(self):
        """
        Print all the information(neighbour and network lists) of a router
        :return: None
        """
        print(self.__router_name.rjust(len(self.__router_name) + 2))  # print the router name with 2 spaces before it
        if len(self.get_neighbour()) > 0:  # check if the router has neighbours
            # get all the neighbours of given router name
            neighbours = [x.get_name() for x in self.get_neighbour()]
            neighbours.sort()  # sort neighbours list to show it in order
            print("    N: ", end='')  # print (N)eighbour with four spaces
            print(*neighbours, sep=', ')  # print all neighbours of a router with ',' separator
        else:
            print("    N:")  # no neighbours found, only print "N:" with four space before and 0 space after it

        if len(self.get_network()) > 0:  # check if the router has network
            # print a router network using Router classes get_network method
            print("    R: ", end='')  # print (N)etworks with four spaces
            networks = self.get_network()  # get all the networks a router has
            networks.sort()  # sort the network list to show it orderly
            print(*networks, sep=', ')  # print all networks of a router with ',' separator
        else:
            print("    R:")  # no networks found, only print "R:" with four space before and 0 space after it

    def receive_routing_table(self, neighbour):
        """
        communicate between a router and it's neighbour router
        :param: neighbour
        :return: None
        """
        router_networks = self.get_network()  # get networks of sender router

        if len(router_networks) > 0:  # check if router has networks
            router_networks.sort()  # router has networks and sort the network list

            # split each network from router network list and save data of network and distance in separate list
            sender_router_network, sender_router_distance = list(zip(*(list(s.split(":")) for s in router_networks)))

            neighbour_router_networks = neighbour.get_network()  # get network of a single neighbour router
            neigbour_router_network = ''  # initial an empty variable to store neighbour routers' network

            if len(neighbour_router_networks) > 0:  # check if a neighbour router has networks
                neighbour_router_networks.sort()  # sort the networks of neighbour router

                # get the network(e.g. 100, 200) from neighbour router networks list items and store it in
                # nighbour_router_networks as list
                neigbour_router_network, neighbour_router_distance = list(
                   zip(*(list(s.split(":")) for s in neighbour_router_networks)))

            # compare a base routers network set and neighbour routers' networks set to get not-shared network
            # from router network

            share_networks = (set(sender_router_network) - set(neigbour_router_network))

            # loop through each not-shared network and share it between neighbour router to communicate
            for share_network in share_networks:
                # get the not-shared network info(network and distance) from base router networks list
                sender_router_network_info = [s for s in router_networks if share_network in s]
                # add not-shared network with neighbour router, increase the distance +1
                neighbour.add_network(((sender_router_network_info[0].split(":"))[0]),
                                      str(int(((sender_router_network_info[0].split(":"))[1])) + 1))

    def has_route(self, network_name):
        """
        check certain router has a connection to a certain network.
        :param network_name:
        :return: None
        """
        router_networks = self.get_network()  # get certain routers' all networks

        if len(router_networks) > 0:  # check if router has networks
            # get the network info for param network_name
            check_network = [s for s in router_networks if network_name in s]
            if len(check_network) > 0:  # check if network exists for param network_name
                split_network_info = check_network[0].split(":")  # split network info to get distance
                if int(split_network_info[1]) > 0:  # check the distance is gt 0
                    print("Network {} is {} hops away".format(network_name, split_network_info[1]))
                else:  # distance is zero
                    print("Router is an edge router for the network.")
            else:  # network not found
                print("Route to the network is unknown.")


def new_router_name(router_dict):
    """
    Get the new router name from user and create an object of Router class, push the object to router dictionary
    :param router_dict:
    """
    router_name = input("Enter a new name: ")
    try:
        # check if the given name already exists in router dictionary
        if router_name in router_dict:
            raise NameError
        else:
            object = Router(router_name)  # create an object for given router name

            # add that object to router dictionary as value and router name as key
            router_dict[object.get_name()] = object
    except NameError:
        # print the error message if the router name already used.
        print('Name is taken.')


def print_router_info(router_dict):
    """
    print the information of a specific router from class Routers' print_info method
    :param router_dict:
    :return: None
    """
    router_name = input("Enter router name: ")
    try:
        if router_name not in router_dict:  # check if the given name exists in router dictionary
            raise NameError  # if no name found, then raise an NameError
        else:
            router_dict[router_name].print_info()  # call the print_info method by object
    except NameError:
        print('Router was not found.')


def add_neighbour(router_dict):
    """
    create neighbours between two router, user has to give two routers name
    :param router_dict:
    :return:
    """
    first_router = input("Enter 1st router: ")
    second_router = input("Enter 2nd router: ")
    try:
        # check if both router name exists in router dict
        if first_router not in router_dict or second_router not in router_dict:
            raise NameError  # if any of routers not exists, raise NameError
        else:
            # make second router neighbour to first router using Router class's add neighbour method
            router_dict[first_router].add_neighbour(router_dict[second_router])

            # make first router neighbour to second router using Router class's add neighbour method
            router_dict[second_router].add_neighbour(router_dict[first_router])
    except NameError:
        print("Router was not found")


def add_network(router_dict):
    """
    create a new network, user has to give three inputs, Router name, network and distance
    :param router_dict:
    :return:
    """
    router_name = input("Enter router name: ")
    network = int(input("Enter network: "))
    distance = int(input("Enter distance: "))
    try:
        # check if router name exists in router dict
        if router_name not in router_dict:
            raise NameError  # if router does not exists, raise NameError
        else:
            # pass the network and distance as parameter to Router class add_network method by object
            router_dict[router_name].add_network(network, distance)
    except NameError:
        print("Router was not found")


def read_from_file_line(router_dict, f):
    for line in f:  # loop every line in the file
        if '!' in line:  # check if the line has '!'
            line = line.replace("\n", "")  # remove the \n character at the end of each line
            split_row = line.split('!')  # split each line from '!' character
            router_name = split_row[0]  # index 0 value is router name
            if router_name in router_dict:  # check if the router name exists in router dictionary
                pass  # if found, nothing to do
            else:
                object = Router(router_name)  # create an object for given router name

                # add that object to router dictionary as value and router name as key
                router_dict[object.get_name()] = object

            if len(split_row[1]) > 0:  # check if the index 1 has some value
                neighbours = split_row[1].split(";")  # split the index 1 value by ';' to get neighbour routers
                for neighbour_router_name in neighbours:  # loop through each neighbour routers
                    if neighbour_router_name in router_dict:  # if neighbour router name exists in router dictionary
                        pass # if found, nothing to do
                    else:
                        object = Router(neighbour_router_name)  # create an object for given router name

                        # add that object to router dictionary as value and router name as key
                        router_dict[object.get_name()] = object

                        # make second router neighbour to first router using Router class's add neighbour method
                        router_dict[router_name].add_neighbour(router_dict[neighbour_router_name])

                        # make first router neighbour to second router using Router class's add neighbour method
                        router_dict[neighbour_router_name].add_neighbour(router_dict[router_name])

            # check if index 2 has value to get the network and distance info
            if len(split_row[2]) > 0:
                network, distance = split_row[2].split(":")  # split last part of line to network and distance
                # create network by calling Router class objects add_network method, pass network and distance as
                # parameter
                router_dict[split_row[0]].add_network(network, distance)


def print_all(router_dict):
    """
    print all routers information, call the print_info method in Router class
    :param router_dict:
    :return: None
    """
    if len(router_dict) > 0:  # check if router dictionary has some value
        for router in router_dict.values():  # loop through each router name from dictionary values
            router.print_info()  # call Router classes print_info method


def sending_routing_table(router_dict):
    """
    take a router name and create communication with it's neighbour router
    :param router_dict:
    :return: None
    """
    router_name = input("Sending router: ")
    try:
        # check if router name exists in router dict
        if router_name not in router_dict:
            raise NameError  # if router does not exists, raise NameError
        else:
            neighbours = router_dict[router_name].get_neighbour()  # call get_neighbour method of Router class by object
            if len(neighbours) > 0:  # check if the router has neighbours
                for neighbour in neighbours:  # loop through each neighbours
                    # call Route classes receive_routing_table method with neighbour parameter
                    router_dict[router_name].receive_routing_table(neighbour)
    except NameError:
        print("Router was not found")


def check_has_route(router_dict):
    """
    call Router classes has_route method using router object, pass network name as parameter
    :param router_dict:
    :return: None
    """
    router_name = input("Enter router name: ")
    try:
        # check if router name exists in router dict
        if router_name not in router_dict:
            raise NameError  # if router does not exists, raise NameError
        else:
            network_name = input("Enter network name: ")  # input a network name
            # call has_route method of Router class by object, pass network name as parameter
            router_dict[router_name].has_route(network_name)
    except NameError:
        print("Router was not found")


def main():
    routerfile = input("Network file: ")
    router_dict = {}
    try:
        if routerfile != '':
            f = open(routerfile, "r")  # read from file
            read_from_file_line(router_dict, f)  # method to read every line of the input file
        while True:
            command = input("> ")
            command = command.upper()

            if command == "P":
                print_router_info(router_dict)
                continue
            elif command == "PA":
                print_all(router_dict)
                continue

            elif command == "S":
                sending_routing_table(router_dict)
                continue

            elif command == "C":
                add_neighbour(router_dict)
                continue

            elif command == "RR":
                check_has_route(router_dict)
                continue
            elif command == "NR":
                new_router_name(router_dict)
                continue

            elif command == "NN":
                add_network(router_dict)
                continue

            elif command == "Q":
                print("Simulator closes.")
                return

            else:
                print("Erroneous command!")
                print("Enter one of these commands:")
                print("NR (new router)")
                print("P (print)")
                print("C (connect)")
                print("NN (new network)")
                print("PA (print all)")
                print("S (send routing tables)")
                print("RR (route request)")
                print("Q (quit)")
    except IOError:
        print("Error: the file could not be read or there is something wrong with it.")


main()
