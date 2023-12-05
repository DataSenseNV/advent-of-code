# Day 5 - Advent of Code 2023
# https://adventofcode.com/2023/day/5

import numpy as np


def find_index_by_value(list, v):
    # list is a range of values
    # value is 1 value to be found in the range
    print("Looking for {} in {}".format(v, list))
    for i, l in enumerate(list):
        if l[1] >= v >= l[0]:
            return i
    print("niks gevonden maat")


if __name__ == "__main__":
    input = "python/05-12/test_input.txt"
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
    for l in lines[1:]:
        if len(l) == 0:
            print("")
            continue
        elif not l[0].isdigit():
            step += 1

            print("step: {}".format(step))
            instr_dict[step] = instr_dict[step - 1].copy()
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

                if y_min <= z[0]:  # if y_min below range
                    if y_max < z[0]:  # if y_max below range
                        print("case 1: no match")
                        continue
                    elif y_max >= z[1]:  # if y_max above range
                        print("case 2: full overlap")
                        x_min = y0 + z[0] - y_min
                        x_max = x_min + z[1] - z[0]

                        # remove z and add new x
                        instr_dict[step].remove(z)
                        instr_dict[step].append([x_min, x_max])
                        print(instr_dict)

                    else:  # if y_max is in range
                        print("case 3: left overlap")
                        x_min = y0 + z[0] - y_min
                        x_max = y0 + y_max - y_min

                        instr_dict[step].append([x_min, x_max])
                        # remove left side of z
                        i = find_index_by_value(instr_dict[step], z[0])
                        instr_dict[step][i] = [
                            y_max + 1,
                            instr_dict[step][i][1],
                        ]
                        print(instr_dict)

                elif y_min > z[1]:  # if y_min above range
                    print("case 4: no match")
                    continue
                else:  # if y_min in range
                    if y_max <= z[1]:  # if y_max in range
                        print("case 5: full inside")
                        x_min = y0
                        x_max = y0 + y_max - y_min

                        instr_dict[step].append([x_min, x_max])
                        # adjust edges
                        # left edge
                        i = find_index_by_value(instr_dict[step], y_min)
                        instr_dict[step][i] = [
                            instr_dict[step][i][0],
                            y_min - 1,
                        ]
                        # right edge
                        instr_dict[step].append([y_max + 1, instr_dict[step][i][1]])
                        print(instr_dict)

                    else:  # if y_max out of range
                        print("case 6: right overlap")
                        x_min = y0
                        x_max = y0 + z[1] - y_min

                        instr_dict[step].append([x_min, x_max])
                        # remove right side of z
                        i = find_index_by_value(instr_dict[step], z[1])
                        instr_dict[step][i] = [
                            instr_dict[step][i][0],
                            y_min - 1,
                        ]
                        print(instr_dict)

    nearest_loc = np.inf
    for l in instr_dict[7]:
        if l[0] < nearest_loc and l[0] != -1 and l[0] != 0:
            nearest_loc = l[0]
    print("Nearest location: {}".format(nearest_loc))
