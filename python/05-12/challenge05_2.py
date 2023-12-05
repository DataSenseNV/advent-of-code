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
seed_numbers = []
temp = []
new_seed_numbers = []


def check_possiblities(seed, dict):
    new_seed_numbers = []
    S1 = seed[0]
    S2 = seed[0] + seed[1] - 1
    line_data = dict[0]
    L0 = line_data[0]
    L1 = line_data[1]
    L2 = line_data[1] + line_data[2] - 1
    if S1 <= S2 < L1 <= L2:
        if len(dict) == 1:
            new_seed_numbers.append(seed)
            return new_seed_numbers
        new_seed_numbers += check_possiblities(seed, dict[1:])
    elif S1 <= L1 <= S2 <= L2:
        if len(dict) == 1:
            new_seed_numbers.append([S1, L1 - S1])
            new_seed_numbers.append([L0, S2 - L1 + 1])
            return new_seed_numbers
        new_seed_numbers += check_possiblities([S1, L1 - S1], dict[1:])
        new_seed_numbers.append([L0, S2 - L1 + 1])
    elif S1 <= L1 <= L2 <= S2:
        if len(dict) == 1:
            new_seed_numbers.append([S1, L1 - S1])
            new_seed_numbers.append([L0, L2 - L1 + 1])
            new_seed_numbers.append([L2, S2 - L2])
            return new_seed_numbers
        new_seed_numbers += check_possiblities([S1, L1 - S1], dict[1:])
        new_seed_numbers.append([L0, L2 - L1 + 1])
        new_seed_numbers += check_possiblities([L2, S2 - L2], dict[1:])
    elif L1 <= S1 <= S2 <= L2:
        if len(dict) == 1:
            new_seed_numbers.append([L0 + S1 - L1, S2 - S1 + 1])
            return new_seed_numbers
        new_seed_numbers.append([L0 + S1 - L1, S2 - S1 + 1])
    elif L1 <= S1 <= L2 <= S2:
        if len(dict) == 1:
            new_seed_numbers.append([L0 + S1 - L1, L2 - S1 + 1])
            new_seed_numbers.append([L2, S2 - L2])
            return new_seed_numbers
        new_seed_numbers.append([L0 + S1 - L1, L2 - S1 + 1])
        new_seed_numbers += check_possiblities([L2, S2 - L2], dict[1:])
    elif L1 <= L2 < S1 <= S2:
        if len(dict) == 1:
            new_seed_numbers.append(seed)
            return new_seed_numbers
        new_seed_numbers += check_possiblities(seed, dict[1:])
    return new_seed_numbers


with open("input.txt") as file:
    for line in file:
        data.append(line.strip())
    seed_numbers_temp = list(filter(None, data[0].split(":")[1].split(" ")))
    for x in range(len(seed_numbers_temp)):
        temp.append(int(seed_numbers_temp[x]))
        if x % 2 == 1:
            seed_numbers.append(temp)
            temp = []
    while line_counter + sub_line_counter < len(data):
        if data[line_counter + sub_line_counter] == "":
            line_counter += sub_line_counter + 2
            dict_list.append(dict)
            dict = []
            sub_line_counter = 0
        line_data = data[line_counter + sub_line_counter].split(" ")
        line_data = [int(x) for x in line_data]
        dict.append(line_data)
        sub_line_counter += 1
    line_counter += sub_line_counter + 2
    dict_list.append(dict)
    dict = {}
    sub_line_counter = 0
    for dict in dict_list:
        for seed in seed_numbers:
            a = check_possiblities(seed, dict)
            for x in a:
                new_seed_numbers.append(x)
        seed_numbers = new_seed_numbers
        new_seed_numbers = []
    for location in seed_numbers:
        all_locations.append(location[0])
print(min(all_locations))
