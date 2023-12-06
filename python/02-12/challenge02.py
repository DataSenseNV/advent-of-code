# Day 2 - Advent of Code 2023
# https://adventofcode.com/2023/day/2

from collections import defaultdict

with open("python/02-12/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines() if len(line.strip()) > 0]

part_1 = 0
part_2 = 0

for line in lines:
    proceed = True
    id_, line = line.split(":")
    value_dict = defaultdict(int)
    for event in line.split(";"):
        for balls in event.split(","):
            ball_num, ball_colour = balls.split()
            value_dict[ball_colour] = max(value_dict[ball_colour], int(ball_num))
            if int(ball_num) > {"red": 12, "green": 13, "blue": 14}.get(ball_colour, 0):
                proceed = False
    score = 1
    for value in value_dict.values():
        score *= value
    part_2 += score
    if proceed:
        part_1 += int(id_.split()[-1])

if __name__ == "__main__":
    print(part_1)
    print(part_2)
