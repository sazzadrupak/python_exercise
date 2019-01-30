def sharing_expenses():
    filename = input('Enter the name of the file: ')
    try:
        f = open(filename, "r")
        individual_total_pay = {}
        individual_pay_list = dict()
        total_expense = 0
        for line in f:
            if ':' in line:
                split_row = line.split(":")
                key = split_row[0]
                if split_row[1] != '':
                    try:
                        value = float(split_row[1])
                        total_expense = float(total_expense) + value
                        if key in individual_total_pay:
                            individual_total_pay[key] += value
                            individual_pay_list[key].append(value)
                        else:
                            individual_total_pay[key] = value
                            individual_pay_list[key] = [value]

                    except (ValueError, TypeError):
                        print("Error: there was an erroneous line in the file.")
                        individual_total_pay = {}
                        break
                else:
                    print("Error: there was an erroneous line in the file.")
                    individual_total_pay = {}
                    break

            else:
                print("Error: there was an erroneous line in the file.")
                individual_total_pay = {}
                break
    except IOError:
        print("Error: file %s cannot be read." % filename)
    else:
        if len(individual_total_pay) > 0:
            print("Total costs: {0:0.2f}e\n".format(total_expense))
            i = 1
            for key, value in sorted(individual_total_pay.items()):
                individual = individual_pay_list[key]
                print("{0} has paid {1:0.2f} in the following amounts: {2}".format(key, value, ', '.join(['{0:0.2f}'.format(v) for v in individual])))
                average_cost = float(total_expense / len(individual_total_pay))
                temp = average_cost - value
                if temp == 0 or abs(temp) <= 0.05:
                    print("No transfers needed.")
                elif temp > 0:
                    print("{0} needs to pay {1:0.2f}e.".format(key, temp))
                elif temp < 0:
                    print("{0} needs to receive  {1:0.2f}e.".format(key, abs(temp)))
                if i < len(individual_total_pay):
                    print()
                i += 1


def main():
    sharing_expenses()


main()
