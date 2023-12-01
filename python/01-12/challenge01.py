# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1

numbers = "0123456789"
values = []

with open("input.txt") as file:
    for item in file:
        first = ""
        last = ""
        for char in item:
            if char in numbers:
                if first == "":
                    first = char
                last = char
        values.append(int(first + last))
print(sum(values))
