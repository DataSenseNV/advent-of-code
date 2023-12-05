# Day 5 - Advent of Code 2023
# https://adventofcode.com/2023/day/5

if __name__ == "__main__":
    input = "python/05-12/input.txt"
    with open(input) as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]

    seed_dict = {}
    instruction = 0
    for l in lines[1:]:
        if len(l) == 0:
            continue
        elif not l[0].isdigit():
            instruction += 1
            print("Instruction: {}".format(instruction))
            continue

        x_0 = int(l.split(" ")[0])
        x_1 = int(l.split(" ")[1])
        x_2 = int(l.split(" ")[2])

        for seed in lines[0].split(" ")[1:]:
            print("Seed: {}".format(seed))
            if seed not in seed_dict:
                seed_dict[seed] = [seed]
            if len(seed_dict[seed]) < instruction + 1:
                seed_dict[seed].append(seed_dict[seed][-1])
            if x_1 <= int(seed_dict[seed][-2]) < (x_1 + x_2):
                new_instr = str(x_0 + int(seed_dict[seed][-2]) - x_1)
                print("Instruction found: {}".format(new_instr))
                seed_dict[seed][-1] = new_instr
    print(seed_dict)

    print("Nearest loc: {}".format(min(sublist[-1] for sublist in seed_dict.values())))
