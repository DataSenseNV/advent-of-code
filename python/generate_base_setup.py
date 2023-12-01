import os
import json

python_dir = "./"
java_dir = "../java/"

python_file_template = """
# Day {day} - Advent of Code 2023
# https://adventofcode.com/2023/day/{day}

if __name__ == "__main__":
    print("Here I go! Wish me luck!")
"""

java_file_template = """
// Day {format_day} - Advent of Code 2023
// https://adventofcode.com/2023/day/{day}

public class Challenge{format_day} {{
    public static void main(String[] args) {{
        System.out.println("Here I go! Wish me luck!");
    }}
}}
"""


def get_jupyter_template(day) -> dict:
    {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Day {day} - Advent of Code 2023\n",
                    "\n",
                    f"**[Challenge URL](https://adventofcode.com/2023/day/{day})**\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": 4,
                "metadata": {},
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": ["Here I go! Wish me luck!\n"],
                    }
                ],
                "source": ['print("Here I go! Wish me luck!")'],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 2,
    }


# create a list of days 01-02...26
days = [f"i" + str(i) if i < 10 else str(i) for i in range(1, 27)]

for day in range(25):
    day = day + 1
    format_day = "{:02d}".format(day)
    new_python_dir = python_dir + f"{format_day}-12"
    new_java_dir = java_dir + f"{format_day}-12"
    os.makedirs(new_python_dir, exist_ok=True)
    os.makedirs(new_java_dir, exist_ok=True)
    with open(new_python_dir + f"/challenge{format_day}.py", "w") as f:
        f.write(python_file_template.format(day=day, format_day=format_day))
    with open(new_python_dir + f"/challenge{format_day}.ipynb", "w") as f:
        f.write("")
        # json.dump(get_jupyter_template(day=day), f, indent=4)
    with open(new_java_dir + f"/Challenge{format_day}.java", "w") as f:
        f.write(java_file_template.format(day=day, format_day=format_day))
