def main():
    filename = input('Enter the name of the score file: ')
    try:
        f = open(filename, "r")
        score = {}
        for line in f:
            if ' ' in line:
                split_row = line.split(" ")
                key = split_row[0]
                try:
                    value = int(split_row[1])
                    if key in score:
                        score[key] += value
                    else:
                        score[key] = value
                except (ValueError, TypeError):
                    print("There was an erroneous score in the file:")
                    print(split_row[1])
                    score = {}
                    break
            else:
                print("There was an erroneous line in the file:")
                print(line)
                score = {}
                break
    except IOError:
        print("There was an error in reading the file.")
    else:
        if len(score) > 0:
            print("Contestant score:")
            for key, value in sorted(score.items()):
                print("%s %d" % (key, value))


main()
