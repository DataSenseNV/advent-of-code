# Day 3 - Advent of Code 2023
# https://adventofcode.com/2023/day/3
import numpy as np


def find_digits_and_symbols(two_d_array):
    # 1 = digit, -1 = symbol, -2 = gear, 0 = nothing
    mask = np.zeros((two_d_array.shape[0], two_d_array.shape[1]))
    for i, row in enumerate(two_d_array):
        for j, element in enumerate(row):
            if element.isdigit():
                mask[i][j] = 1
            elif element != ".":
                mask[i][j] = -1

            if element == "*":
                mask[i][j] = -2

    return mask


def find_number_size(two_d_array):
    # 1,2,3,4,... = len of number, -1 = symbol, 0 = nothing
    mask = np.zeros((two_d_array.shape[0], two_d_array.shape[1]))
    for i, row in enumerate(two_d_array):
        for j, element in enumerate(row):
            if element == 1:  # if digit
                end = False
                c = 0
                while not end:  # go to the right and find end of number
                    c += 1
                    if j + c + 1 > two_d_array.shape[1]:  # out of border
                        end = True
                    elif two_d_array[i][j + c] in (0, -1):  # if end of number
                        end = True
                    if end:
                        for x in range(0, c):
                            mask[i][j + x] = c
            if element == -1:
                mask[i][j] = -1
            elif element == -2:
                mask[i][j] = -2

    return mask


def find_adjacent_coordinates(two_d_array, list_of_coordinates):
    adj_coord_list = []
    for c in list_of_coordinates:
        for i in range(c[0] - 1, c[0] + 2):
            for j in range(c[1] - 1, c[1] + 2):
                if (
                    i >= 0
                    and i < two_d_array.shape[0]
                    and j >= 0
                    and j < two_d_array.shape[1]
                ):  # if coord is valid
                    adj_coord_list.append([i, j])

    # Remove duplicates and original coordinates
    indices_to_remove = []
    unique_adj_coord_list = []
    for c in adj_coord_list:
        if c not in unique_adj_coord_list:
            unique_adj_coord_list.append(c)
    for i, c in enumerate(unique_adj_coord_list):
        if c in list_of_coordinates:
            indices_to_remove.append(i)
    adj_coord_list = [
        e for i, e in enumerate(unique_adj_coord_list) if i not in indices_to_remove
    ]

    return adj_coord_list


if __name__ == "__main__":
    input = "python/03-12/input.txt"
    with open(input) as f:
        lines = f.readlines()

    # Initialize 2D array
    row = list(lines[0].strip("\n"))
    engine = np.array([row])

    # Vstack 2D array
    for l in lines[1:]:
        new_row = list(l.strip("\n"))
        engine = np.vstack((engine, np.array([new_row])))
    print(engine)

    # mask for all digits and symbols
    engine_mask_digits_symbols = find_digits_and_symbols(engine)
    print(engine_mask_digits_symbols)

    # mask for number sizes and symbols
    engine_mask_number_size = find_number_size(engine_mask_digits_symbols)
    print(engine_mask_number_size)

    # # mask to keep track of adjacent numbers to gears
    # engine_gear_count = np.zeros((engine.shape[0], engine.shape[1]))

    # dict to keep track of numbers near gear
    gear_dict = {}

    # Loop through mask and check if symbol is adjacent
    skip_cols = 0
    for i, row in enumerate(engine_mask_number_size):
        for j, element in enumerate(row):
            if element > 0:  # if digit
                if skip_cols > 0:  # if digit is already analyzed
                    skip_cols -= 1
                    continue

                number = str(engine[i][j])  # start creating number
                number_coord = [[i, j]]
                c = 0
                end = False
                while not end:  # go to the right and find end of number
                    c += 1
                    if j + c + 1 > engine.shape[1]:  # out of border
                        end = True
                    elif engine_mask_number_size[i][j + c] <= 0:  # if end of number
                        end = True

                    if not end:
                        number += engine[i][j + c]
                        number_coord.append([i, j + c])

                    if end:
                        skip_cols = c - 1

                number = int(number)
                adj_coord = find_adjacent_coordinates(engine, number_coord)

                # Check if gear is adjacent
                near_gear = False
                for c in adj_coord:
                    # print(engine_mask_digits_symbols[c[0], c[1]])
                    if engine_mask_digits_symbols[c[0], c[1]] == -2:
                        near_gear = True
                        if tuple(c) in gear_dict:
                            gear_dict[tuple(c)].append(number)
                        else:
                            gear_dict[tuple(c)] = [number]

                print("Number: {}".format(number))
                print("Coordinates: {}".format(number_coord))
                print("Adj. coordinates: {}".format(adj_coord))
                print("Near gear: {}".format(near_gear))

    print("Gear dict: {}".format(gear_dict))

    sum_of_gear_ratios = 0
    for key, item in gear_dict.items():
        if len(item) == 2:
            sum_of_gear_ratios += item[0] * item[1]

    print("Sum of gear ratios: {}".format(sum_of_gear_ratios))

    # digit_coord = np.where(engine_mask_digits_symbols == 1)
    # digit_coord_list = []
    # for x, y in zip(digit_coord[0], digit_coord[1]):
    #     digit_coord_list.append([x, y])
    # x = find_adjacent_coordinates(engine, digit_coord_list)
    # print(x)
