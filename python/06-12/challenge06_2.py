# Day 6 - Advent of Code 2023
# https://adventofcode.com/2023/day/6

times = ""
distances = ""
line_count = 1
with open("input.txt") as file:
    for line in file:
        if line_count == 1:
            for time in line.strip().split(" ")[1:]:
                if time != "":
                    times += time
            times = int(times)
            line_count += 1
        else:
            for distance in line.strip().split(" ")[1:]:
                if distance != "":
                    distances += distance
            distances = int(distances)
    for x in range(0, times + 1):
        distance = x * (times - x)
        if distance > distances:
            print(times - (x) * 2 + 1)
            break
