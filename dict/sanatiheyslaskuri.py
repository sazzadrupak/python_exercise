def get_lines():
    lines = ""
    que = " "

    while que != '':
        que = input()
        lines = lines + que + " "

    return lines


def word_density_calculator(lines):
    density_dict = {}
    for word in lines.lower().split():
        if word in density_dict:
            pass
        else:
            density_dict[word] = lines.lower().split().count(word)
    return density_dict


def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    lines = get_lines()
    lines = lines.strip()
    density_dict = word_density_calculator(lines)
    for key, val in sorted(density_dict.items()):
        print('{} : {} times'.format(key, val))


main()

