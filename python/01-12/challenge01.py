# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1
import re


def part1():
    with open(
        "/Users/wouterpardon/Documents/advent-of-code/python/01-12/input.txt"
    ) as file:
        lines = file.readlines()
        print(lines)
        total = 0

        for line in lines:
            first_num = -1
            last_num = -1
            for char in line:
                try:
                    if first_num == -1:
                        first_num = int(char)
                    else:
                        last_num = int(char)
                except:
                    continue

            if last_num == -1:
                last_num = first_num

            num = int(str(first_num) + str(last_num))

            total += num

        print(total)


def part2():
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    with open(
        "/Users/wouterpardon/Documents/advent-of-code/python/01-12/input.txt"
    ) as file:
        lines = file.readlines()
        total = 0

        for line in lines:
            first_num = -1
            last_num = -1

            mapped = {}

            for i in range(len(words)):
                word = words[i]

                if word in line:
                    for m in re.finditer(word, line):
                        mapped[m.start()] = i % 10

            first_num = mapped[min(mapped.keys())]
            last_num = mapped[max(mapped.keys())]

            num = int(str(first_num) + str(last_num))
            total += num

        print(total)


if __name__ == "__main__":
    part2()
