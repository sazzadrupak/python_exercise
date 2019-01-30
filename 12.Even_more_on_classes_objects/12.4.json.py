# TIE-02106 Introduction to Programming
# Md. Ariful Islam Mahmud, mahmudm@student.tut.fi, Student ID: 281791
# Solution of task 12.4 :
# A program for Getting to know the JSON library

import json


def read_file(filename):
    data_list = []
    try:
        json_file = open(filename, "r")
        dump = json.load(json_file)
        json_file.close()
        for item in dump:
            station_id = item["stationId"]
            station_name = item["name"]
            data_list.append(station_id + ';' + station_name + '\n')
    except IOError:
        print("There was an error in handling the file.")
    return data_list


def write_file(data_array, filename):
    try:
        output_file = open(filename, "w")
        for line in data_array:
            output_file.writelines(line)
        output_file.close()
    except IOError:
        print("There was an error in handling the file.")


def main():
    input_file_name = input("Enter the name of the input file: ")
    output_file_name = input("Enter the name of the output file: ")
    data_array = read_file(input_file_name)
    if len(data_array) > 0:
        write_file(data_array, output_file_name)
        print("Conversion succeeded.")


main()
