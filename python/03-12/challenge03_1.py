# Day 3 - Advent of Code 2023
# https://adventofcode.com/2023/day/3
import re
import numpy as np


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
                    ):
                        parts.append((int(matched_int)))

    return parts


if __name__ == "__main__":
    puzzle_input = read_puzzle_input("python/03-12/puzzle_input.txt")
    print(sum(decode_schematic(puzzle_input)))
