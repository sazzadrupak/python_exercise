def count_abbas(string):
    abba_count = 0
    counter = 0
    for i in string:
        if i == 'a':
            if string[counter:(counter + 4)] == 'abba':
                abba_count += 1
        counter += 1
    return abba_count

