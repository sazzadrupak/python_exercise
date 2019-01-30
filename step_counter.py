import math
# define a global list to store the user input steps
# this can be accessed from anywhere of the project
amount_of_steps_list = []

# number_of_measurements() gives the number of measurements represented by '#'
def number_of_measurements(steps_range):
    return len([1 for i in amount_of_steps_list if (steps_range <= int(i) < (steps_range + 4000))])


# graphical_presentation() shows the graphical presentation of steps information
def graphical_presentation():
    # get the length of maximum item in the steps list
    if max(amount_of_steps_list) < 5000:
        measurement_number = number_of_measurements(1000)

        if measurement_number > 0:
            print("{} {}".format(1000, measurement_number * '#'))
        else:
            print("{}".format(1000))

        print()
        print("Steps taken during most of the days: over {} but under {} steps".format(1000, 5000))

    else:
        max_item_length = len(str(max(amount_of_steps_list)))

        # get the number of steps of lowest and highest point
        number_of_between_steps = math.ceil(max(amount_of_steps_list) / 4000)

        initial_highest_steps = 0
        most_measurements_list = []
        # show the graphical presentation via loop
        for step in range(0, number_of_between_steps, 1):
            range_value = str((1000 + (step * 4000))).rjust(max_item_length)
            measurement_number = number_of_measurements((1000 + (step * 4000)))

            if measurement_number > initial_highest_steps:
                most_measurements_list = []
                initial_highest_steps = measurement_number
                most_measurements_list.append(1000 + (step * 4000))
                most_measurements_list.append((1000 + (step * 4000)) + 4000)

            if measurement_number > 0:
                print("{} {}".format(range_value, measurement_number * '#'))
            else:
                print("{}".format(range_value))

        print()
        if most_measurements_list[1] > max(amount_of_steps_list):
            print("Steps taken during most of the days: over {} steps".format(most_measurements_list[0]))
        else:
            print("Steps taken during most of the days: over {} but under {} steps".format(most_measurements_list[0],
                                                                                           most_measurements_list[1]))


# shows the rejected number of steps which are under 1000 steps/day
def rejected_steps():
    rejected = len([1 for i in amount_of_steps_list if int(i) < 1000])
    if int(rejected) > 0:
        print("Rejected {} results of under 1000 steps/day.".format(rejected))
    else:
        pass
    return rejected


def main():
    print("Enter the amount of steps/day, one day per line.")
    print("End by entering an empty row.")

    while True:
        amount_of_steps = input("")
        if amount_of_steps is not "":
            amount_of_steps_list.append(int(amount_of_steps))
        else:
            break

    if len(amount_of_steps_list) > 0:
        print("Information related to the period of measurement (%d days):" % len(amount_of_steps_list))

    # To check if all steps are under rejected or not
    count_rejected_steps = rejected_steps()
    if len(amount_of_steps_list) != count_rejected_steps:
        print()
        # if all steps are not rejected, then show the graphical presentation
        print("Graphical representation of information:")
        graphical_presentation()

        # information about days with over 9000 steps taken
        print("Days with over 9000 steps taken: {} days".format(len([1 for i in amount_of_steps_list if int(i) > 9000])))

        # information about longest distance walked
        print("Longest distance walked during a day: {:.2f} km".format((max(amount_of_steps_list) * 1.5) / 2500))

        # information about total consumed calories over 1000 thousands steps
        consumed_calories = int(((sum([int(i) for i in amount_of_steps_list if int(i) > 1000]) * 1.5) / 2500) * 50)
        print("Total calories consumed by walking: {} kcal".format(consumed_calories))


main()
