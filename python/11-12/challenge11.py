# Day 11 - Advent of Code 2023
# https://adventofcode.com/2023/day/11

with open("python/11-12/input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines() if len(line.strip()) > 0]

row_amount, col_amount = len(lines), len(lines[0])

coords = []
for row_index in range(row_amount):
    for col_index in range(col_amount):
        if lines[row_index][col_index] == "#":
            coords.append((row_index, col_index))

amount_of_galaxies = len(coords)

empty_row = [
    all([lines[i][j] == "." for j in range(col_amount)]) for i in range(row_amount)
]
empty_col = [
    all([lines[i][j] == "." for i in range(row_amount)]) for j in range(col_amount)
]


def distance(coords_galaxy_1, coords_galaxy_2, compressed_space):
    xg1, yg1 = coords_galaxy_1
    xg2, yg2 = coords_galaxy_2

    xg1, xg2 = min(xg1, xg2), max(xg1, xg2)
    yg1, yg2 = min(yg1, yg2), max(yg1, yg2)

    result = 0
    for x in range(xg1, xg2):
        result += 1
        if empty_row[x]:
            result += compressed_space - 1

    for y in range(yg1, yg2):
        result += 1
        if empty_col[y]:
            result += compressed_space - 1

    return result


def calculate_total_distance(compressed_space=2):
    result = 0
    for gal_index in range(amount_of_galaxies):
        for next_gal_index in range(gal_index + 1, amount_of_galaxies):
            dist = distance(coords[gal_index], coords[next_gal_index], compressed_space)
            result += dist

    return result


if __name__ == "__main__":
    print(calculate_total_distance(compressed_space=2))
    print(calculate_total_distance(compressed_space=10**6))
