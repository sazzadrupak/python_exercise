def get_vowels(user_input):
    vowel_counter = 0
    for i in user_input:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowel_counter += 1
    return vowel_counter


def main():
    user_input = input("Enter a word: ")
    vowel_counter = get_vowels(user_input)
    print("The word {} contains {} vowels and {} consonants".format(user_input, vowel_counter, len(user_input) -
                                                                    vowel_counter))


main()
