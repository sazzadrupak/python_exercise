def get_input_lines():

    lines = ""
    que = " "

    while que != '':
        que = input()
        lines = lines + que + " "

    return lines


def get_single_line(words, line_length):

    line = ""
    words_rest = []
    words_rest += words

    for item in words:

        if len(line)+len(item) <= line_length:
            line = line + " " + item
            words_rest.remove(item)

        else:
            final_line = line[1:len(line)]
            return final_line, words_rest

        if words_rest is []:

            final_line = line[1:len(line)]
            return final_line, words_rest


def get_lines_list(words, line_length):

    EMPTY = []
    lines_list = []

    while words != EMPTY:

        line, words = get_single_line(words, line_length)
        lines_list.append(line)

    return lines_list


def insert_extra_spaces(line, extra_spaces):

    line_words_list = line.split()
    no_of_space_positions = len(line_words_list)-1
    new_line = ""
    total_space = extra_spaces + no_of_space_positions
    no_of_loop = total_space//no_of_space_positions

    if total_space % no_of_space_positions > 0:
        no_of_loop += 1

    for loop in range(no_of_loop):

        for index in range(no_of_space_positions):

            if total_space != 0:
                line_words_list[index] += " "
                total_space -= 1

    for item in line_words_list:
        new_line += item

    return new_line


def find_length_of_longest_word (words):

    words_length = []

    for item in words:

        words_length.append(len(item))
    longest_word = max(words_length)

    return longest_word


def print_lines(lines_list, line_length):

    for index in range(len(lines_list)-1):

        line = lines_list[index]
        current_length = len(line)
        extra_spaces = line_length - current_length
        line = insert_extra_spaces(line, extra_spaces)
        print(line)

    print(lines_list[len(lines_list)-1])


def main():

    print("Enter text rows. Quit by entering an empty row.")
    lines = get_input_lines()
    lines = lines.strip()

    words = lines.split()
    line_length = int(input("Enter the number of characters per line: "))
    lines_list = get_lines_list(words, line_length)
    print(lines_list)
    # print_lines(lines_list, line_length)


main()
