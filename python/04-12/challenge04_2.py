# Day 4 - Advent of Code 2023
# https://adventofcode.com/2023/day/4

count = 0

amount = []
current_number = 0
with open("input.txt") as file:
    for line in file:
        amount.append(1)
with open("input.txt") as file:
    for line in file:
        matching = 0
        data = line.strip().split(":")
        winning = list(filter(None, data[1].split("|")[0].split(" ")))
        owned = list(filter(None, data[1].split("|")[1].split(" ")))
        for number in owned:
            if number in winning:
                matching += 1
        for x in range(matching):
            amount[current_number + x + 1] += amount[current_number]

        current_number += 1
print(sum(amount))
