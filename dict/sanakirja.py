# TIE-02100 Johdatus ohjelmointiin


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print("{} in Spanish is {}".format(word, english_spanish[word]))
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[english_word] = spanish_word

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "P":
            for key, value in sorted(english_spanish.items()):
                print(key, value)

        elif command == 'T':
            sentence = input("Enter the text to be translated into Spanish: ")
            translated_sentence = ' '.join([english_spanish.get(english_word, english_word) for english_word in sentence
                                           .split()])
            print("The text, translated by the dictionary:\n", translated_sentence, sep="")

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
