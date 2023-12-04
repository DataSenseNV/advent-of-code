# Day 2 - Advent of Code 2023
# https://adventofcode.com/2023/day/2

count = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        dict = {"blue": 0, "red": 0, "green": 0}
        data = line.split(":")
        game_number = data[0].split(" ")[1]
        game_data = data[1].split(";")
        for entry in game_data:
            game_entry = entry.split(",")
            for entry_data in game_entry:
                entry_data = entry_data.split(" ")
                dict[entry_data[2]] = max(dict[entry_data[2]], int(entry_data[1]))
        power = 1
        for number in dict.values():
            power *= number
        count += power

print(count)
