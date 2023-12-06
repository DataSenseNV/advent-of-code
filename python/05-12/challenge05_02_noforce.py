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
    seeds = maps.pop(0)[0]
    seeds_ranges = []
    for seed_range_start, seed_range_length in zip(seeds[0::2], seeds[1::2]):
        seeds_ranges.append((seed_range_start, seed_range_start + seed_range_length))

    for maps_range in maps:
        new_seeds = []

        while len(seeds_ranges) > 0:
            start, end = seeds_ranges.pop(0)
            for destination, source, length in maps_range:
                overlap_start = max(start, source)
                overlap_end = min(end, source + length)

                if overlap_start < overlap_end:
                    new_seeds.append(
                        [
                            overlap_start - source + destination,
                            overlap_end - source + destination,
                        ]
                    )
                    if overlap_start > start:
                        seeds_ranges.append([start, overlap_start])
                    if overlap_end < end:
                        seeds_ranges.append([overlap_end, end])
                    break
            else:
                new_seeds.append([start, end])

        seeds_ranges = new_seeds

    print(min(seeds_ranges)[0])
