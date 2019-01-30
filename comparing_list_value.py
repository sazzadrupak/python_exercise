def are_all_members_same(list_item):
    result = False
    if len(list_item) == 0 or len(list_item) == 1:
        return True
    else:
        for i in range(len(list_item)-1):
            if list_item[i] == list_item[i + 1]:
                result = True
            else:
                result = False
                break
    return result


def main():
    print(are_all_members_same([]))


main()
