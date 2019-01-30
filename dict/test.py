def print_ints(n, k=1, sep=" "):
    if k > 0:
        if n < 0:
            k = -k
            range_value = n
        else:
            range_value = n + 1
        print(*range(0, range_value, k,), sep=sep)
    else:
        print("Illegal parameter k = %d!" % k)


print_ints(4, 2, "#")
