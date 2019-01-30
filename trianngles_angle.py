
def calculate_angle(f1, f2=0):
    if f2 is 0:
        f2 = 90

    return 180 - (f1 + f2)


print(calculate_angle(50, 60))
print(calculate_angle(60))
