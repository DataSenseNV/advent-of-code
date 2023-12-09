# Day 8 - Advent of Code 2023
# https://adventofcode.com/2023/day/8

with open("python/08-12/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def part_1(instructions, nodes, current_node_name, amount_of_steps=0):
    while current_node_name != "ZZZ":
        instruction = instructions.pop(0)
        current_node_name = nodes.get(current_node_name).get(instruction)
        amount_of_steps += 1
        instructions.append(instruction)
    return amount_of_steps


if __name__ == "__main__":
    part_1 = part_1(
        instructions=list(lines[0]),
        current_node_name=lines[2][:3],
        nodes=dict(
            (line[:3], {"L": line[7:10], "R": line[-4:-1]}) for line in lines[2:]
        ),
    )
    print(part_1)
