# Day 3 - Advent of Code 2023
# https://adventofcode.com/2023/day/3

numbers = "0123456789"
count = 0
data = []
fake_data = []
fake_count = 0
fake_values = []
temp = "0"
valid = False

test = []
with open("input.txt") as file:
    for line in file:
        data.append([char for char in line.strip()])
    for x in range(len(data)):
        fake_data.append([])
        if valid:
            count += int(temp)
            fake_values.append(int(temp))
            fake_count += 1
        temp = "0"
        for y in range(len(data[x])):
            if data[x][y] in numbers:
                temp += data[x][y]
                for hor in [-1, 0, 1]:
                    for vert in [-1, 0, 1]:
                        if 0 <= x + hor < len(data) and 0 <= y + vert < len(data[x]):
                            if (
                                data[x + hor][y + vert] not in numbers
                                and data[x + hor][y + vert] != "."
                            ):
                                valid = True
            elif valid:
                count += int(temp)
                fake_values.append(int(temp))
                temp = "0"
                valid = False
                fake_count += 1
            else:
                if temp != "0":
                    fake_values.append(int(temp))
                    fake_count += 1
                temp = "0"
                valid = False
            if data[x][y] in numbers:
                fake_data[x].append(fake_count)
            elif data[x][y] == "*":
                fake_data[x].append(data[x][y])
            else:
                fake_data[x].append(".")
count = 0
for x in range(len(fake_data)):
    for y in range(len(fake_data[x])):
        if fake_data[x][y] == "*":
            values = []
            for hor in [-1, 0, 1]:
                for vert in [-1, 0, 1]:
                    if 0 <= x + hor < len(fake_data) and 0 <= y + vert < len(
                        fake_data[x]
                    ):
                        if (
                            fake_data[x + hor][y + vert] != "*"
                            and fake_data[x + hor][y + vert] != "."
                        ):
                            values.append(fake_data[x + hor][y + vert])
            values = list(set(values))
            if len(values) == 2:
                count += int(fake_values[values[0]]) * int(fake_values[values[1]])
print(count)
