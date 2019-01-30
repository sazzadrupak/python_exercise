def calculate_dose(weight, previous_dose_passed_time, total_taken_dose):
    per_dose = weight * 15
    remaining_dose = (4000 - total_taken_dose)
    next_dose = 0

    if previous_dose_passed_time >= 6:
        if total_taken_dose == 4000:
            next_dose = per_dose
        else:
            if remaining_dose > per_dose:
                next_dose = per_dose
            else:
                next_dose = remaining_dose

    return next_dose


def main():
    weight = int(input("Patient's weight (kg): "))
    previous_dose_passed_time = int(input("How much time has passed from the previous dose (full hours): "))
    total_taken_dose = int(input("The total dose for the last 24 hours (mg): "))

    next_dose = calculate_dose(weight, previous_dose_passed_time, total_taken_dose)
    print("The amount of Parasetamol to give to the patient: %s" % next_dose)


main()
