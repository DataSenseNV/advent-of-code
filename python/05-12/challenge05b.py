# Day 5 - Advent of Code 2023
# https://adventofcode.com/2023/day/5

import numpy as np
import copy


def find_index_by_value(list, v):
    # list is a range of values
    # value is 1 value to be found in the range
    for i, l in enumerate(list):
        if l[1] >= v >= l[0]:
            return i
    print("niks gevonden maat")


def find_invalid_values(list):
    values_list = []
    for l in list:
        if l[1] < l[0]:
            values_list.append(l)
            print("Removing from list: {}".format(l))
    return values_list


if __name__ == "__main__":
    input = "python/05-12/input.txt"
    with open(input) as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]

    instr_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    for i, seed in enumerate(lines[0].split(" ")[1:]):
        if i % 2 == 0:
            instr_dict[0].append(
                [int(seed), int(seed) + int(lines[0].split(" ")[1:][i + 1]) - 1]
            )

    step = 0
    temp_prev_list = []
    temp_new_list = []
    for l in lines[1:]:
        if len(l) == 0:
            print("")
            continue
        elif not l[0].isdigit():
            instr_dict[step].extend(temp_prev_list)
            instr_dict[step].extend(temp_new_list)

            step += 1

            print("step: {}".format(step))
            temp_prev_list = instr_dict[step - 1].copy()
            temp_new_list = []
            print(instr_dict)
            continue
        else:
            # 50 98 2
            y0 = int(l.split(" ")[0])
            y_min = int(l.split(" ")[1])
            y_max = int(l.split(" ")[1]) + int(l.split(" ")[2]) - 1
            print("New steps: {} {} {}".format(y0, y_min, y_max))

            for z in instr_dict[step - 1]:  # [79, 92]
                print("Previous step range: {}".format(z))

                # for i in temp_prev_list:
                #     if i[1] < i[0]:
                #         print("prev")
                #         print(temp_prev_list)
                #         raise ValueError("y_min must be less than y_max")
                # for i in temp_new_list:
                #     if i[1] < i[0]:
                #         print("new")
                #         print(temp_new_list)
                #         raise ValueError("y_min must be less than y_max")

                if y_min <= z[0]:  # if y_min below range
                    if y_max < z[0]:  # if y_max below range
                        print("case 1: no match")
                        continue
                    elif y_max >= z[1]:  # if y_max above range
                        print("case 2: full overlap")
                        x_min = y0 + z[0] - y_min
                        x_max = x_min + z[1] - z[0]

                        # remove z and add new x
                        temp_prev_list.remove(z)
                        temp_new_list.append([x_min, x_max])
                        print("Prev. list: {}".format(temp_prev_list))
                        print("New list: {}".format(temp_new_list))
                    else:  # if y_max is in range
                        print("case 3: left overlap")
                        x_min = y0 + z[0] - y_min
                        x_max = y0 + y_max - y_min

                        temp_new_list.append([x_min, x_max])
                        # remove left side of z
                        i = find_index_by_value(temp_prev_list, z[0])
                        temp_prev_list[i] = [
                            y_max + 1,
                            temp_prev_list[i][1],
                        ]
                        to_remove = find_invalid_values(temp_prev_list)
                        for r in to_remove:
                            temp_prev_list.remove(r)

                        print("Prev. list: {}".format(temp_prev_list))
                        print("New list: {}".format(temp_new_list))

                elif y_min > z[1]:  # if y_min above range
                    print("case 4: no match")
                    continue
                else:  # if y_min in range
                    if y_max <= z[1]:  # if y_max in range
                        print("case 5: full inside")
                        x_min = y0
                        x_max = y0 + y_max - y_min

                        temp_new_list.append([x_min, x_max])
                        # adjust edges
                        # left edge
                        i = find_index_by_value(temp_prev_list, y_min)
                        i_0 = copy.deepcopy(temp_prev_list[i][0])
                        i_1 = copy.deepcopy(temp_prev_list[i][1])
                        temp_prev_list[i] = [
                            i_0,
                            y_min - 1,
                        ]
                        # right edge
                        temp_prev_list.append([y_max + 1, i_1])

                        to_remove = find_invalid_values(temp_prev_list)
                        for r in to_remove:
                            temp_prev_list.remove(r)

                        print("Prev. list: {}".format(temp_prev_list))
                        print("New list: {}".format(temp_new_list))

                    else:  # if y_max out of range
                        print("case 6: right overlap")
                        x_min = y0
                        x_max = y0 + z[1] - y_min

                        temp_new_list.append([x_min, x_max])
                        # remove right side of z
                        i = find_index_by_value(temp_prev_list, z[1])
                        temp_prev_list[i] = [
                            temp_prev_list[i][0],
                            y_min - 1,
                        ]
                        print("Prev. list: {}".format(temp_prev_list))
                        print("New list: {}".format(temp_new_list))

    instr_dict[step].extend(temp_prev_list)
    instr_dict[step].extend(temp_new_list)

    for key in instr_dict:
        print("Step: {}: {}".format(key, instr_dict[key]))
    nearest_loc = np.inf
    for l in instr_dict[7]:
        if l[0] < nearest_loc and l[0] != -1 and l[0] != 0:
            nearest_loc = l[0]
    print("Nearest location: {}".format(nearest_loc))
