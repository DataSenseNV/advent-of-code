# Day 7 - Advent of Code 2023
# https://adventofcode.com/2023/day/7

from collections import Counter


def calc_hand_score(hand, card_list):
    uniques = len(Counter(hand))
    s1 = 0
    max_identical = 0
    if uniques == 5:
        s1 = 1  # high card
    elif uniques == 4:
        s1 = 2  # one pair
    elif uniques == 3:
        if max(hand.count(item) for item in set(hand)) == 2:
            s1 = 3  # two pair
        else:
            s1 = 4  # three of a kind
    elif uniques == 2:
        if max(hand.count(item) for item in set(hand)) == 3:
            s1 = 5  # full house
        else:
            s1 = 6  # four of a kind
    else:
        s1 = 7  # five of a kind
    s1 = f"{s1:02}"

    s2 = ""
    for c in hand:
        score = card_list.index(c)
        s2 += f"{score:02}"

    score = int(s1 + s2)
    print("Score: {}".format(score))
    return score


if __name__ == "__main__":
    input = "python/07-12/input.txt"
    card_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    hand_list = []
    total_winnings = 0

    with open(input) as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]

    for l in lines:
        hand = l.split()[0]
        bid = l.split()[1]
        score = calc_hand_score(hand, card_list)
        print("Score: {}".format(score))
        print("Hand: {}".format(hand))
        print("Bid: {}".format(bid))

        hand_list.append([hand, bid, score])
        sorted_hand_list = sorted(hand_list, key=lambda x: x[2])
        print("Sorted by score: {}".format(sorted_hand_list))

    for i, hand in enumerate(sorted_hand_list):
        total_winnings += int(hand[1]) * (i + 1)
    print("Total winnings: {}".format(total_winnings))
