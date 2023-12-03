# Day 3 - Advent of Code 2023
# https://adventofcode.com/2023/day/3
import re


def read_puzzle_input(file_name: str) -> str:
    input_list = []
    with open(file_name, "r") as f:
        for line in f:
            input_list.append(line.strip())

    return input_list


def decode_schematic(input_list: list[str]):
    parts = []
    for row_index, row_value in enumerate(input_list):
        # search all integers in current engine line useing re.finditer()
        # to account for duplicates and get position in string
        for p in re.finditer(r"\d+", row_value):
            matched_int = p.group(0)
            match_start_index = p.start()  # start position in string
            match_end_index = p.end()  # end position in string

            # search for symbol around part number
            for search_row in range(
                max(row_index - 1, 0), min(row_index + 2, len(row_value))
            ):
                for search_column in range(
                    max(match_start_index - 1, 0),
                    min(match_end_index + 1, len(row_value)),
                ):
                    if (
                        not input_list[search_row][search_column].isdigit()
                        and input_list[search_row][search_column] != "."
                        and input_list[search_row][search_column] == "*"
                    ):
                        gear_loc = (search_row, search_column)
                        parts.append(((int(matched_int)), gear_loc))

    return parts


def gears_to_dict(
    gear_list: list[tuple[int, tuple[int, int]]]
) -> dict[tuple[int, int], list[int]]:
    gear_dict = {}

    for tuple in gear_list:
        if tuple[1] not in gear_dict.keys():
            gear_dict[tuple[1]] = [tuple[0]]
        else:
            gear_dict[tuple[1]].append(tuple[0])

    return gear_dict


if __name__ == "__main__":
    puzzle_input = read_puzzle_input("python/03-12/puzzle_input.txt")
    parts_around_gears = decode_schematic(puzzle_input)
    gear_dict = gears_to_dict(parts_around_gears)

    sum = 0
    for key, value in gear_dict.items():
        if len(value) == 2:
            sum += value[0] * value[1]

    print(sum)
