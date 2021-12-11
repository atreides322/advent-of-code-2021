#!/usr/bin/env python3

import sys


debug = False
iterations = 100


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        octopodes = [[int(x) for x in line.strip()]
                     for line in input.readlines()]

    if debug:
        print_octopodes(octopodes)

    flashes = 0

    for _ in range(iterations):
        octopodes = run_step(octopodes)

        flashes += len([octopus for row in octopodes
                        for octopus in row if octopus == 0])

        if debug:
            print()
            print_octopodes(octopodes)

    print('Flashes:', flashes)


def run_step(octopodes):
    new_octopodes = [[octopus + 1 for octopus in row] for row in octopodes]

    while True:
        made_changes = False

        if debug:
            print()
            print_octopodes(new_octopodes, width=3)

        for i, row in enumerate(new_octopodes):
            for j, octopus in enumerate(row):

                if octopus > 9:
                    made_changes = True

                    new_octopodes[i][j] = 0

                    # index + 1 (for next) + 1 (because range end exclusive)
                    for i_prime in range(max(i-1, 0), min(i + 1 + 1, 10)):
                        for j_prime in range(max(j-1, 0), min(j + 1 + 1, 10)):
                            if new_octopodes[i_prime][j_prime] != 0:
                                new_octopodes[i_prime][j_prime] += 1

        if not made_changes:
            break

    return new_octopodes


def print_octopodes(octopodes, width=0):
    for row in octopodes:
        for octopus in row:
            print(str(octopus).rjust(width), end='')
        print()


if __name__ == "__main__":
    main()
