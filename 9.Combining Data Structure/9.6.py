# TIE-02100 Johdatus ohjelmointiin
# Dancing Queen


def read_file(filename):
    # reads the played songs and their scores from the file

    try:
        fileobject = open(filename, "r")

        # TODO: initialize your data structure here
        name_dict = {}
        # loop over fileobject row by row
        for row in fileobject:
            parts = row.strip().split(";")
            player = parts[0]  # name of the player
            if player in name_dict:
                pass
            else:
                name_dict[player] = list()
            songs = parts[1:]  # songs

            # TODO: make a data structure for this single
            song_dict = {}
            #       player that includes his/her songs and scores

            # loop over this player's songs
            for song in songs:
                parts = song.split(":")
                results = parts[1].split(",")
                name = parts[0]  # name of the song
                # list of presses, all integer
                results = [int(luku) for luku in results]

                # TODO: connect these results to the song
                song_dict[name] = results

            # TODO: add this player's data structure into the
            #       main data structure
            name_dict[player].append(song_dict)

        return name_dict  # TODO return the main data structure

    except IOError:
        print("Error! The file could not be read.")
        return None


def get_score(items, coefficients):
    score_by_player = sum([a * b for a, b in zip(items, coefficients)])
    max_score_of_song = sum(items) * 5
    percentage_ratio = float(score_by_player / max_score_of_song) * 100
    return percentage_ratio


def main():
    coefficients = [5, 4, 2, 0, -6, -12]

    filename = input("Enter the name of the file: ")
    score_dict = read_file(filename)
    # print(score_dict)
    # TODO : print ...
    for key, value in sorted(score_dict.items()):
        print("{}:".format(key))
        songs = value
        for item in sorted(songs[0].keys()):
            print("- {}: {:0.2f}%".format(item, get_score(songs[0][item], coefficients)))


main()
