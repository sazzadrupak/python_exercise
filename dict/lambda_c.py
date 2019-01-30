def print_in_accordance_of_values(english_spanish):
    for key, value in sorted(english_spanish.items(), key=lambda kv: kv[1]):
        print(value, key)

