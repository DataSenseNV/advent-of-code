# Day 1 - Advent of Code 2023
# https://adventofcode.com/2023/day/1

# combining the first digit and the last digit (in that order) to form a single two-digit number.

import re


def find_digits_in_string(string: str) -> list:
    return re.findall(r"\d", string)


def decode_calibration_code(code: str) -> int:
    digits = find_digits_in_string(code)
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)


def read_puzzle_input(file_name: str) -> str:
    code_list = []
    with open(file_name, "r") as f:
        for line in f:
            code_list.append(line.strip())

    return code_list


if __name__ == "__main__":
    print("Here I go! Wish me luck!")

    puzzle_input = read_puzzle_input(
        "/workspaces/advent-of-code/python/01-12/puzzle_input.txt"
    )

    testcases = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    sum = 0
    for testcase in testcases:
        print(decode_calibration_code(testcase))
        sum += decode_calibration_code(testcase)

    print(sum)

    sum = 0
    for input in puzzle_input:
        print(decode_calibration_code(input))
        sum += decode_calibration_code(input)

    print(sum)
