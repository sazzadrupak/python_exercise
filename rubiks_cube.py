def main():
    i = 1
    performance_time_list = []
    while i <= 5:
        performance_time = float(input("Enter the time for performance %d: " % i))
        performance_time_list.append(performance_time)
        i += 1

    performance_time_list.remove(max(performance_time_list))
    performance_time_list.remove(min(performance_time_list))

    average_performance = float(sum(performance_time_list) / 3)
    print("The official competition score is %.2f seconds." % average_performance)


main()
