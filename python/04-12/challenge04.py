# Day 4 - Advent of Code 2023
# https://adventofcode.com/2023/day/4
import re

if __name__ == "__main__":
    input = "python/04-12/input.txt"
    with open(input) as f:
        lines = f.readlines()

    total_score = 0
    for l in lines:
        l = l.strip("\n")
        game = l.split(":")[0]
        winning_no = l.split(":")[1].split("|")[0]
        player_no = l.split(":")[1].split("|")[1]

        ticket_score = 0
        for w in re.split(r"\s+", winning_no):
            if w:  # if not empty string
                for p in re.split(r"\s+", player_no):
                    if p == w:
                        if ticket_score == 0:
                            ticket_score = 1
                        else:
                            ticket_score *= 2
        total_score += ticket_score
        print("Ticket score: {}".format(ticket_score))

    print("Score: {}".format(total_score))
