#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        directions = input.readlines()

    horizontal = find_horizontal(directions)
    vertical = find_vertical(directions)

    print(horizontal * vertical)


def find_vertical(directions):
    return filter_steps(directions, positive='down', negative='up')


def find_horizontal(directions):
    return filter_steps(directions, positive='forward', negative='backward')


def filter_steps(directions, positive, negative):
    filtered = [x for x in directions
                if x.startswith(positive) or x.startswith(negative)]
    filtered = [int(x.split()[1]) * (1 if x.startswith(positive) else -1)
                for x in filtered]

    return(sum(filtered))


if __name__ == "__main__":
    main()
