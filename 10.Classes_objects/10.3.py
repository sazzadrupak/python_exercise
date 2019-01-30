def get_second(time_area, day):
    h, m, s = time_area.split(":")
    return int(int(int(h) * 3600 + int(m) * 60 + int(s)) + int(86400 * day))


def convert_time(filename):
    updated_time_format = []
    try:
        f = open(filename, "r")
        i = 1  # use to count the number of line
        prev_hour = 0  # store the information about previous time's hour to compare with current time's hour
        day = 0  # store the information about day counter

        for line in f:  # loop through the every line in the file
            if i != 1:  # skip first line of the file as it is header
                if ';' in line:  # check if the line has ';' character,
                    #  the line has ';' character means input format okay

                    split_row = line.split(";", 1)[0]  # split the line from first appearance of the ';'
                    if ":" in split_row:  # check if the split part has ':' in it
                        # split_row part has ':' in it to get time part only

                        time_area = split_row
                        h, m, s = time_area.split(":")  # split the time part to get hour, minute and second

                        current_hour = int(h)  # put h into current hour variable
                        if int(prev_hour) > current_hour:  # check if the prev time's hour is larger then current hour
                            day += 1  # increment day value by one

                        # format the line for writing in new file
                        updated_time_format.append(str(get_second(time_area, day)) + ";" + str(line.split(";", 1)[1]))
                        prev_hour = current_hour  # assign current hour to prev hour for further row checking
                    else:
                        # split_row has no ':' in it, no data about time in the line
                        print("Error in reading the file!")
                        updated_time_format = []
                        break
                else:
                    # line has no ';' in it, wrong format line
                    print("Error in reading the file!")
                    updated_time_format = []
                    break
            else:
                updated_time_format.append(line)
            i += 1  # increment i for new line in file
    except IOError:
        # raise error if file is not found
        print("Error in reading the file!")
    else:
        return updated_time_format  # if everything goes right, return list to the main function


# read the file name from user
def read_input(message):
    filename = input(message)
    return filename


# write the new temperature file to user given file name
def write_to_file(filename, output_data):
    f = open(filename, "w")
    for line in output_data:
        f.write(line)
    f.close()


def main():
    from_file = read_input("Enter the name of the file to be read: ")
    output_data = convert_time(from_file)
    if len(output_data) > 0:  # check if the return value from convert_time method is empty or not
        to_file = read_input("Enter the name of the file to be written: ")
        write_to_file(to_file, output_data)  # return value from convert_time is not empty, so write value in modified
        # file


main()
