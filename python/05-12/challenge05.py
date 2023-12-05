# Day 5 - Advent of Code 2023
# https://adventofcode.com/2023/day/5

data = []
dict_list = []
dict = []
line_counter = 2
sub_line_counter = 1
current_number = 0
next_number = 0
all_locations = []

with open("input.txt") as file:
    for line in file:
        data.append(line.strip())
    seed_numbers = list(filter(None, data[0].split(":")[1].split(" ")))
    while line_counter + sub_line_counter < len(data):
        if data[line_counter + sub_line_counter] == "":
            line_counter += sub_line_counter + 2
            dict_list.append(dict)
            dict = []
            sub_line_counter = 0
        line_data = data[line_counter + sub_line_counter].split(" ")
        dict.append(line_data)
        sub_line_counter += 1
    line_counter += sub_line_counter + 2
    dict_list.append(dict)
    dict = {}
    sub_line_counter = 0
    for seed in seed_numbers:
        current_number = int(seed)
        for dict in dict_list:
            for line_data in dict:
                if current_number >= int(line_data[1]) and current_number < int(
                    line_data[1]
                ) + int(line_data[2]):
                    next_number = current_number - int(line_data[1]) + int(line_data[0])
                    break
                else:
                    next_number = current_number
            current_number = next_number
        all_locations.append(current_number)

print(min(all_locations))
