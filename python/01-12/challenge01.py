# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1

import os

if __name__ == "__main__":
    print(os.getcwd())

    with open("python/01-12/input.txt") as f:
        lines = f.readlines()

    # Count
    lines_dig = []
    for l in lines:
        lines_dig.append([i for i in l if i.isdigit()])

    # Count first and last digits
    print(lines_dig)
    sum = 0
    for l in lines_dig:
        first_last = l[0] + l[-1]
        print(first_last)
        sum += int(first_last)

    print(sum)
