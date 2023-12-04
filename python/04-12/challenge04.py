# Day 4 - Advent of Code 2023
# https://adventofcode.com/2023/day/4

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


def count_card_winnings(winning_numbers: list[int], my_numbers: list[int]) -> int:
    winnings = 0

    for number in winning_numbers:
        if number in my_numbers:
            if winnings > 0:
                winnings = winnings * 2
            else:
                winnings = 1

    return winnings


if __name__ == "__main__":
    print("Here I go! Wish me luck!")
    input = read_puzzle_input("python/04-12/puzzle_input.txt")

    total_winnings = 0

    for ticket in input:
        winning_numbers = string_with_numbers_to_list(
            ticket.split("|")[0].split(":")[1]
        )
        my_numbers = string_with_numbers_to_list(ticket.split("|")[1])

        total_winnings += count_card_winnings(
            winning_numbers=winning_numbers, my_numbers=my_numbers
        )

    print(total_winnings)
