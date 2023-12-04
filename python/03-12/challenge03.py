
# Day 3 - Advent of Code 2023
# https://adventofcode.com/2023/day/3

import re

with open("python/03-12/test_input.txt", "r") as file:
    lines = [re.sub(r'[^0-9.]', '#', l.strip()) for l in file.readlines()]

def part1(gear_sum = 0):
    num_info, hash_info = {}, {-1: set(), len(lines): set()}
    for index, line in enumerate(lines):
        hash_info[index] = set([symbol.start() for symbol in re.finditer(r'#', line)])
        for number in re.finditer(r'[0-9]+', line): 
            num_info[tuple([index, range(*number.span())])] = int(number.group(0))
    #hash_info = dict(sorted(hash_info.items()))
    for num_pos, num_val in num_info.items():
        symbols_in_area = hash_info[num_pos[0]-1].union(hash_info[num_pos[0]]).union(hash_info[num_pos[0]+1])
        if len(set(range(num_pos[1].start-1, num_pos[1].stop+1)).intersection(symbols_in_area)) >= 1: gear_sum += num_val 
    return gear_sum

print(part1())