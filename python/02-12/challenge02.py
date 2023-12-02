# Day 2 - Advent of Code 2023
# https://adventofcode.com/2023/day/2

import re

if __name__ == "__main__":
    # Parameters
    terugleggen = True
    r_max = 12
    g_max = 13
    b_max = 14
    colors = {
        "r": {"max": r_max, "balance": r_max, "min_req_cubes": 0, "name": "red"},
        "g": {"max": g_max, "balance": g_max, "min_req_cubes": 0, "name": "green"},
        "b": {"max": b_max, "balance": b_max, "min_req_cubes": 0, "name": "blue"},
    }
    sum_of_IDs = 0
    sum_of_products = 0

    # Read file
    with open("python/02-12/input.txt") as f:
        lines = f.readlines()

    # Go through lines
    for l in lines:
        # Game ID
        pattern = r"(?<=\s)(.*?)(?=:)"  # All chars between \s and :
        game_id = re.search(pattern, l).group(1)
        print("Game ID: {}".format(game_id))

        # Rounds
        pattern = r"(?=[:;](.*?)(?:;|$))"
        rounds = re.finditer(pattern, l)

        # Go through rounds
        valid_game = True
        for r in rounds:
            print("-" * 10)

            # Go search value for each color
            for c in colors.keys():
                pattern = r"(\d+)\s*{}".format(colors[c]["name"])
                result = re.search(pattern, r.group(1))

                # Update balance
                if result:
                    print("{}: {}".format(c, result.group(1)))
                    colors[c]["balance"] -= int(result.group(1))

                # Update min req cubes
                if result:
                    if int(result.group(1)) > colors[c]["min_req_cubes"]:
                        colors[c]["min_req_cubes"] = int(result.group(1))

            # Check if balance is valid
            for c in colors.keys():
                if colors[c]["balance"] < 0:
                    valid_game = False

            # Reset balance if terugleggen
            if terugleggen:
                for c in colors.keys():
                    colors[c]["balance"] = colors[c]["max"]

        product = 1
        for c in colors.keys():
            product *= colors[c]["min_req_cubes"]
        sum_of_products += product

        # Reset min required cubes
        for c in colors.keys():
            colors[c]["min_req_cubes"] = 0

        if valid_game:
            sum_of_IDs += int(game_id)

    print("Sum of valid game IDs: {}".format(sum_of_IDs))
    print("Sum of products of min cubes: {}".format(sum_of_products))
