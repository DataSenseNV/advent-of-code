# Day 2 - Advent of Code 2023
# https://adventofcode.com/2023/day/2

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
import re


def read_puzzle_input(file_name: str) -> str:
    code_list = []
    with open(file_name, "r") as f:
        for line in f:
            code_list.append(line.strip())

    return code_list


def decode_input_string(input: str) -> tuple[int, dict[str, int]]:
    colors = {}

    game_number_string = input.split(":")[0].strip()
    colored_cubes_string = input.split(":")[1].strip()

    game_number = int(re.findall(r"\d+", game_number_string)[0])

    for reveal in colored_cubes_string.split(";"):
        for colored_ball in reveal.split(","):
            ball_count = int(colored_ball.strip().split(" ")[0])
            color = colored_ball.strip().split(" ")[1]
            if color not in colors.keys():
                colors[color] = ball_count
            elif colors[color] < ball_count:
                colors[color] = ball_count

    return game_number, colors


def is_possible_game(
    cubes_available: dict[str, int], game_played: dict[str, int]
) -> bool:
    for color in cubes_available.keys():
        if cubes_available[color] < game_played[color]:
            return False

    return True


if __name__ == "__main__":
    print("Here I go! Wish me luck!")

    cubes_available = {"red": 12, "blue": 14, "green": 13}

    inputs = read_puzzle_input("python/02-12/puzzle_input.txt")

    sum_games = 0
    for input in inputs:
        game_number, colors = decode_input_string(input)

        if is_possible_game(cubes_available=cubes_available, game_played=colors):
            print(game_number, colors)
            print(cubes_available)
            sum_games += game_number

    print(sum_games)
