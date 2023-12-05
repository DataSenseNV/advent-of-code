# Day 5 - Advent of Code 2023
# https://adventofcode.com/2023/day/5

import numpy as np

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

    instruction = 0
    for l in lines[1:]:
        if len(l) == 0:
            continue
        elif not l[0].isdigit():
            instruction += 1

            if instruction > 1:
                for r in remaining_instr:
                    instr_dict[instruction - 1].append(r)
                    print("Remaining instruction added: {}".format(r))
            remaining_instr = instr_dict[instruction - 1].copy()
            print("Instruction: {}".format(instruction))
            # instr_dict[instruction] = instr_dict[instruction - 1]
            continue
        else:
            # 50 98 2
            x_min = int(l.split(" ")[0])
            y_min = int(l.split(" ")[1])
            y_max = int(l.split(" ")[1]) + int(l.split(" ")[2]) - 1
            print("New instructions: {} {} {}".format(x_min, y_min, y_max))

            for prev_instr in instr_dict[instruction - 1]:  # [79, 92]
                print("Previous instruction range: {}".format(prev_instr))

                if y_min < prev_instr[0]:  # if y_min below range
                    if y_max < prev_instr[0]:  # if y_max below range
                        continue
                    elif y_max > prev_instr[1]:  # if y_max above range
                        new_range_min = x_min + prev_instr[0] - y_min
                        new_range_max = new_range_min + prev_instr[1] - prev_instr[0]
                        new_instr_range = [new_range_min, new_range_max]
                        instr_dict[instruction].append(new_instr_range)

                        for x in remaining_instr:
                            if x == prev_instr:
                                remaining_instr.remove(x)

                        print("case 1")
                    else:  # if y_max is in range
                        new_range_min = x_min + prev_instr[0] - y_min
                        new_range_max = x_min + y_max - y_min
                        new_instr_range = [new_range_min, new_range_max]
                        instr_dict[instruction].append(new_instr_range)

                        for i, x in enumerate(remaining_instr):
                            if x[0] <= y_max <= x[1]:
                                if y_max == x[1]:
                                    remaining_instr.remove(x)
                                else:
                                    remaining_instr[i] = [y_max + 1, x[1]]

                        print("case 2")
                elif y_min > prev_instr[1]:  # if y_min above range
                    continue
                else:  # if y_min in range
                    if y_max <= prev_instr[1]:  # if y_max in range
                        new_range_min = x_min
                        new_range_max = x_min + y_max - y_min
                        new_instr_range = [new_range_min, new_range_max]
                        instr_dict[instruction].append(new_instr_range)

                        add = False
                        print(remaining_instr)
                        for i, x in enumerate(remaining_instr):
                            if x[0] <= y_max <= x[1]:
                                if x[0] <= y_min <= x[1]:
                                    if y_min == x[0]:
                                        remaining_instr[i] = [-1, -1]
                                    else:
                                        print("Remaining: {}".format([y_max + 1, x[1]]))
                                        remaining_instr[i] = [y_max + 1, x[1]]
                                    if y_max == x[1]:
                                        to_add = [-1, -1]
                                    else:
                                        to_add = [x[0], y_min - 1]
                                        print("Remaining: {}".format(to_add))
                                        add = True
                        if add:
                            remaining_instr.append(to_add)

                        print("case 3")
                    else:  # if y_max out of range
                        new_range_min = y_min - prev_instr[0] + x_min
                        new_range_max = prev_instr[1] - prev_instr[0] + x_min
                        new_instr_range = [new_range_min, new_range_max]
                        instr_dict[instruction].append(new_instr_range)

                        for i, x in enumerate(remaining_instr):
                            if x[0] <= y_min <= x[1]:
                                if x[1] == y_min:
                                    remaining_instr.remove(x)
                                else:
                                    print("Remaining: {}".format([x[0], y_min - 1]))
                                    remaining_instr[i] = [x[0], y_min - 1]

                        print("case 4")

            print(instr_dict)
    for r in remaining_instr:
        instr_dict[instruction].append(r)
        print("Remaining instruction added: {}".format(r))

    nearest_loc = np.inf
    for l in instr_dict[7]:
        if l[0] < nearest_loc and l[0] != -1 and l[0] != 0:
            nearest_loc = l[0]
    print("Nearest location: {}".format(nearest_loc))
