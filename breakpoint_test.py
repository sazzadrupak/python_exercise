# TIE-02106 Introduction to Programming
# Program code template for testing the use of a debugger

def is_adult(year_of_birth):
    age = 2015 - year_of_birth
    if age >= 18:
        return True
    else:
        return False


def main():

    wills_birth = 1947
    emilys_birth = 1999

    will_adult = is_adult(wills_birth)
    emily_adult = is_adult(emilys_birth)

    print("Will:", will_adult)
    print("Emily:", emily_adult)

main()