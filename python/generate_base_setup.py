import os

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
    with open(new_java_dir + f"/Challenge{format_day}.java", "w") as f:
        f.write(java_file_template.format(day=day, format_day=format_day))
