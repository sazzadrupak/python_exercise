def print_box(width, height, border_mark='#', inner_mark=' '):
    print()
    for i in range(height):
        for j in range(width):
            if 0 < i < height - 1 and 0 < j < width - 1:
                print(inner_mark, end="")
            else:
                print(border_mark, end="")
        print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(width=6, height=4, border_mark="O", inner_mark=".")


main()
