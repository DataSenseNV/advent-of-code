# Day 8 - Advent of Code 2023
# https://adventofcode.com/2023/day/8

from math import lcm

with open("python/08-12/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

nodes = dict((line[:3], {"L": line[7:10], "R": line[-4:-1]}) for line in lines[2:])


def get_steps_to_Z(starting_node, amount_of_steps=0):
    instructions = list(lines[0])
    while not starting_node.endswith("Z"):
        instruction = instructions.pop(0)
        starting_node = nodes.get(starting_node).get(instruction)
        instructions.append(instruction)
        amount_of_steps += 1
    return amount_of_steps


print("Part 1:", get_steps_to_Z("AAA"))
len_to_Z = {node: get_steps_to_Z(node) for node in nodes if node.endswith("A")}
print("Part 2:", lcm(*len_to_Z.values()))
