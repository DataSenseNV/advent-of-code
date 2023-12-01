# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1

def translate_nums(input: str):
    translations = {
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
    numbers = []
    for index in range(len(input)):
        if input[index].isnumeric():
            numbers.append(input[index])
            continue
        for key, value in translations.items():
            if input[index : index + len(key)] == key:
                numbers.append(value)
                continue
    return int(f"{numbers[0]}{numbers[-1]}")

with open("python/01-12/input.txt", "r") as file:
    print(sum([translate_nums(line) for line in file.readlines()]))
