# TIE-02100 Johdatus ohjelmointiin
# Read genres and tv-series from a file into a dict.
# Print a list of the genres in alphabetical order
# and list tv-series by given genre on user's command.


def read_file(filename):
    # reads and saves the series and their genres from the file

    # TODO initialize a new data structure
    series_dict = {}
    try:
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            for genre in genres:
                if genre in series_dict:
                    series_dict[genre].append(name)
                else:
                    series_dict[genre] = list()
                    series_dict[genre].append(name)

            # TODO add the info to the data structure

        file.close()
        # TODO return the data structure
        return series_dict

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    series_dict = read_file(filename)
    # print(series_dict)

    # TODO print the genres
    print("Available genres are: {}".format(', '.join(['{}'.format(k) for k in sorted(series_dict.keys())])))
    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series ...
        if genre in series_dict:
            print("{}".format('\n'.join(['{}'.format(k) for k in sorted(series_dict[genre])])))


main()
