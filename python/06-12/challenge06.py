# Day 6 - Advent of Code 2023
# https://adventofcode.com/2023/day/6

import re
from numpy import prod

with open("python/06-12/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines() if len(line.strip()) > 0]


def part_1():
    dist = [int(num) for num in re.findall("\d+", lines.pop())]
    times = [int(num) for num in re.findall("\d+", lines.pop())]

    win_combos = []
    for index in range(len(dist)):
        win_combos.append(
            [
                time
                for time in range(times[index])
                if (times[index] - time) * time > dist[index]
            ]
        )
    return prod([len(cb) for cb in win_combos])


def part_2():
    dist = re.findall("\d+", lines.pop())
    times = re.findall("\d+", lines.pop())

    return len(
        [
            time
            for time in range(int("".join(times)))
            if (int("".join(times)) - time) * time > int("".join(dist))
        ]
    )


if __name__ == "__main__":
    print(part_1())
    print(part_2())
