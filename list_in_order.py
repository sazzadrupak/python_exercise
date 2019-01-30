def is_the_list_in_order(list_item):
    result = False
    if len(list_item) == 0 or len(list_item) == 1:
        return True
    else:
        for i in range(len(list_item)-1):
            if list_item[i] < list_item[i + 1]:
                result = True
            else:
                result = False
                break
    return result


def main():
    print(is_the_list_in_order([42, 37, 43]))


main()
