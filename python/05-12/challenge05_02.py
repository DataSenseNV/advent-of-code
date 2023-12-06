# Day 5 - Advent of Code 2023
# https://adventofcode.com/2023/day/5
import re


def read_puzzle_input(file_name: str) -> str:
    code_list = []
    with open(file_name, "r") as f:
        for line in f:
            code_list.append(line.strip())

    return code_list


def string_with_numbers_to_list(string_with_numbers: str) -> list[int]:
    numbers = re.findall(r"\d+", string_with_numbers)
    return [int(number) for number in numbers]


def map_input_to_map_list(input_list: list[str]) -> list[list[tuple[int, int, int]]]:
    maps = []
    values_per_section = []

    for line in puzzle_input:
        integers = string_with_numbers_to_list(line)
        if integers:
            values_per_section.append(tuple(integers))
        else:
            if values_per_section:
                maps.append(values_per_section)
            values_per_section = []

    return maps


if __name__ == "__main__":
    puzzle_input = read_puzzle_input("python/05-12/input.txt")
    maps = map_input_to_map_list(puzzle_input)
    seeds_range = maps.pop(0)[0]

    seeds = []

    for seed_range_start, seed_range_length in zip(
        seeds_range[0::2], seeds_range[1::2]
    ):
        for seed in range(seed_range_start, seed_range_start + seed_range_length):
            seeds.append(seed)

    seeds = set(seeds)

    lowest_location = 0
    for seed in seeds:
        for map_ranges in maps:
            for destination_start, source_start, length in map_ranges:
                if source_start <= seed <= source_start + length - 1:
                    seed = destination_start + seed - source_start
                    break
        if lowest_location == 0:
            lowest_location = seed
        else:
            lowest_location = min(lowest_location, seed)

    print(lowest_location)
