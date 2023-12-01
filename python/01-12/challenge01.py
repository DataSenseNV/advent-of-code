# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1
if __name__ == "__main__":
    file = open("python/01-12/Calibrations", "r")
    total_number_list = []
    int_to_string_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for line in file.readlines():
        number_flag = 0
        number_list = []
        number_string = ""
        for char in line[::1]:
            if char.isnumeric() and number_flag < 1:
                number_flag = number_flag + 1
                number_list.append(char)
            elif number_flag < 1:
                number_string = number_string + str(char)
                for key in int_to_string_dict:
                    if key in number_string:
                        number_list.append(int_to_string_dict.get(key))
                        number_flag += 1
        number_flag = 0
        number_string = ""
        for char in line[::-1]:
            if char.isnumeric() and number_flag < 1:
                number_flag = number_flag + 1
                number_list.append(char)
            elif number_flag < 1:
                number_string = str(char) + number_string
                for key in int_to_string_dict:
                    if key in number_string:
                        number_list.append(int_to_string_dict.get(key))
                        number_flag += 1
        number_flag = 0
        number = str(number_list[0]) + str(number_list[1])
        number_list = []
        number_string = ""
        total_number_list.append(number)
        number = 0
    total = 0
    for numbers in total_number_list:
        total = total + int(numbers)
    print(total)
