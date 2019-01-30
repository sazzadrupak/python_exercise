def longest_substring_in_order(string):
    # holds the ongoing character list
    char1 = ""
    # holds the substring which are ordered
    char2 = ""
    for char in string:
        if char1 == "":
            # initially store the first character to char1
            char1 = char
        elif char1[-1] <= char:
            # if the current character is gte of the previous last character, then append it to char1
            char1 += char
        elif char1[-1] > char:
            # if the current character is lte of the previous last character

            if len(char2) < len(char1):
                # if previously substring length is less than currently achieved substring
                char2 = char1
            char1 = char

    if len(char2) >= len(char1):
        return char2
    else:
        return char1

