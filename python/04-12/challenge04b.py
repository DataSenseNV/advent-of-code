# Day 4 - Advent of Code 2023
# https://adventofcode.com/2023/day/4
import re

if __name__ == "__main__":
    input = "python/04-12/input.txt"
    with open(input) as f:
        lines = f.readlines()

    ticket_dict = {}
    for e, l in enumerate(lines):
        l = l.strip("\n")
        game = l.split(":")[0]
        winning_no = l.split(":")[1].split("|")[0]
        player_no = l.split(":")[1].split("|")[1]
        ticket_dict[e] = {"winning_no": winning_no, "player_no": player_no, "amount": 1}

    total_score = 0
    for ticket in ticket_dict:
        ticket_score = 0
        for w in re.split(r"\s+", ticket_dict[ticket]["winning_no"]):
            if w:  # if not empty string
                for p in re.split(r"\s+", ticket_dict[ticket]["player_no"]):
                    if p == w:
                        ticket_score += 1
        print("Ticket score: {}".format(ticket_score))

        for s in range(1, ticket_score + 1):
            ticket_dict[ticket + s]["amount"] += ticket_dict[ticket]["amount"]

        total_score += ticket_dict[ticket]["amount"]

    print("Total score: {}".format(total_score))
