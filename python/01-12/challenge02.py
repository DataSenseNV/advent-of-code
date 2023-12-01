# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1

import os
import re

if __name__ == "__main__":
    with open("python/01-12/input.txt") as f:
        lines = f.readlines()

    # Create dummy and fill digits on correct positions
    new_lines = []
    for l in lines:
        l = l.replace(" ", "")
        dummy = "x" * (len(l))
        i = -1
        for x in l:
            i += 1
            # copy original line
            if i == 0:
                new_line = dummy
            # check if x is digit and replace dummy if so
            if x.isdigit():
                new_line = new_line[:i] + x + new_line[i + 1 :]

        new_lines.append(new_line)

    written_digs = {
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

    # Find all written numbers and replace in dummy
    for i, l in enumerate(lines):
        l = l.replace(" ", "")
        for k, v in written_digs.items():
            occurences = [m.start() for m in re.finditer(k, l)]
            for o in occurences:
                index = o
                new_lines[i] = new_lines[i][:o] + str(v) + new_lines[i][o + 1 :]

    sum = 0
    for l in new_lines:
        l = l.replace("x", "")
        first_last = l[0] + l[-1]
        print(first_last)
        sum += int(first_last)

    print(sum)
