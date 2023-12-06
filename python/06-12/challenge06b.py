# Day 6 - Advent of Code 2023
# https://adventofcode.com/2023/day/6


def fysica_van_het_middelbaar(v, t, a):
    D = v * t + (a * t**2) / 2
    return D


if __name__ == "__main__":
    input = "python/06-12/input.txt"
    with open(input) as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]

    product_of_wins = 1
    number_of_wins = 0
    time = ""
    D_record = ""
    for i, t in enumerate(lines[0].split()[1:]):
        time += t
        D_record += lines[1].split()[1:][i]
    print("Input time: {}".format(time))
    print("Input distance: {}".format(D_record))

    for t0 in range(0, int(time)):
        v = t0  # mm/s
        a = 0  # mm/s^2
        t = int(time) - t0
        D = fysica_van_het_middelbaar(v, t, a)
        # print("Distance: {}".format(D))
        if D > int(D_record):
            number_of_wins += 1

        if t0 % 10e6 == 0:
            print("Iteration: {}".format(t0))

    product_of_wins *= number_of_wins

    print("Result: {}".format(product_of_wins))
