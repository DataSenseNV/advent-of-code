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


def count_winning_numbers(winning_numbers: list[int], my_numbers: list[int]) -> int:
    count_winning_numbers = 0

    for number in winning_numbers:
        if number in my_numbers:
            count_winning_numbers += 1

    return count_winning_numbers


if __name__ == "__main__":
    print("Here I go! Wish me luck!")
    input = read_puzzle_input("python/04-12/puzzle_input.txt")

    ticket_dict = {}

    for ticket in input:
        card_number = string_with_numbers_to_list(ticket.split("|")[0].split(":")[0])[0]
        winning_numbers = string_with_numbers_to_list(
            ticket.split("|")[0].split(":")[1]
        )
        my_numbers = string_with_numbers_to_list(ticket.split("|")[1])

        ticket_dict[card_number] = {
            "winning_numbers": winning_numbers,
            "my_numbers": my_numbers,
            "amount": 1,
        }

    for ticket_number, ticket_details in ticket_dict.items():
        for extra_ticket in range(
            1,
            count_winning_numbers(
                winning_numbers=ticket_details["winning_numbers"],
                my_numbers=ticket_details["my_numbers"],
            )
            + 1,
        ):
            if ticket_number + extra_ticket <= len(ticket_dict):
                ticket_dict[ticket_number + extra_ticket]["amount"] += (
                    1 * ticket_details["amount"]
                )

    print(sum(ticket["amount"] for ticket in ticket_dict.values()))
