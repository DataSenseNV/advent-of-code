# Day 7 - Advent of Code 2023
# https://adventofcode.com/2023/day/7

from collections import Counter
from itertools import product


def calc_hand_score(original_hand, new_hand, card_list):
    uniques = len(Counter(new_hand))
    s1 = 0
    max_identical = 0
    if uniques == 5:
        s1 = 1  # high card
    elif uniques == 4:
        s1 = 2  # one pair
    elif uniques == 3:
        if max(new_hand.count(item) for item in set(new_hand)) == 2:
            s1 = 3  # two pair
        else:
            s1 = 4  # three of a kind
    elif uniques == 2:
        if max(new_hand.count(item) for item in set(new_hand)) == 3:
            s1 = 5  # full house
        else:
            s1 = 6  # four of a kind
    else:
        s1 = 7  # five of a kind
    s1 = f"{s1:02}"

    s2 = ""
    for c in original_hand:
        score = card_list.index(c)
        s2 += f"{score:02}"

    score = int(s1 + s2)
    # print("Score: {}".format(score))
    return score


def generate_hands(hand, card_list):
    joker_positions = [i for i, card in enumerate(hand) if card == "J"]

    hands = []
    for new_hand in product(card_list, repeat=len(joker_positions)):
        current_hand = list(hand)
        for i, replacement in zip(joker_positions, new_hand):
            current_hand[i] = replacement
        hands.append("".join(current_hand))

    if len(hands) == 0:
        hands = [hand]

    return hands


if __name__ == "__main__":
    input = "python/07-12/input.txt"
    card_list = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    hand_list = []
    total_winnings = 0

    with open(input) as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]

    for l in lines:
        hand = l.split()[0]
        bid = l.split()[1]
        all_hands = generate_hands(hand, card_list[1:])
        print("-" * 30)
        print("Hand: {}".format(hand))

        max_score = 0
        for new_hand in all_hands:
            score = calc_hand_score(
                original_hand=hand, new_hand=new_hand, card_list=card_list
            )
            if score > max_score:
                best_hand = new_hand
                max_score = score
        print("Best hand: {}, score: {}".format(best_hand, max_score))

        hand_list.append([hand, bid, max_score])

    sorted_hand_list = sorted(hand_list, key=lambda x: x[2])
    print("Sorted by score: {}".format(sorted_hand_list))

    for i, hand in enumerate(sorted_hand_list):
        total_winnings += int(hand[1]) * (i + 1)
    print("Total winnings: {}".format(total_winnings))

# 252145696 too high
# 252137472
