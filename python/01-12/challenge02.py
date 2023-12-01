# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1

numbers = "0123456789"
dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
values = []

with open("input.txt") as file:
    for item in file:
        first = ""
        last = ""
        print(item)
        for x in dict.keys():
            if x in item:
                item = item.replace(x, x + dict[x] + x)
        print(item)
        for char in item:
            if char in numbers:
                if first == "":
                    first = char
                last = char
        values.append(int(first + last))
        print(sum(values))
