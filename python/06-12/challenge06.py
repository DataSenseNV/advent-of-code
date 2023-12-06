# Day 6 - Advent of Code 2023
# https://adventofcode.com/2023/day/6

times = []
distances = []
line_count = 1
total_possibilities = 1
with open("input.txt") as file:
    for line in file:
        if line_count == 1:
            for time in line.strip().split(" ")[1:]:
                if time != "":
                    times.append(int(time))
            line_count += 1
        else:
            for distance in line.strip().split(" ")[1:]:
                if distance != "":
                    distances.append(int(distance))

    for index in range(len(times)):
        temp_possibilities = 0
        time = times[index]
        for x in range(1, time + 1):
            distance = x * (time - x)
            if distance > distances[index]:
                temp_possibilities += 1
        total_possibilities *= temp_possibilities
print(total_possibilities)
