import re

with open("input.txt", "r") as f:
    lines = f.readlines()

card_amounts, card_matches = dict((f"Card {i+1}", 1) for i in range(len(lines))), {}
for index, line in enumerate(lines):
    card_matches[f"Card {index+1}"] = len(set([int(v) for v in re.findall("\d+", line.split("|")[0].split(":")[1])]).intersection(set([int(v) for v in re.findall("\d+", line.split("|")[1])])))
    for next_up in range(card_matches[f"Card {index+1}"]):
        card_amounts[f"Card {index+next_up+2}"] += card_amounts[f"Card {index+1}"] if index+next_up+2 <= len(lines) else 0
print(sum(card_amounts.values()))