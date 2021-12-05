#!/usr/bin/env python3

import sys
from itertools import chain


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        lines = input.readlines()

    lines = [[[
        int(coord) for coord in endpoint.split(',')]
        for endpoint in line.split('->')]
             for line in lines]

    max_x = 0
    max_y = 0

    for line in lines:
        for endpoint in line:
            max_x = max(max_x, endpoint[0])
            max_y = max(max_y, endpoint[0])

    sums = [[0] * (max_x+1) for x in range(max_y+1)]

    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            from_x = min(line[0][0], line[1][0])
            to_x = max(line[0][0], line[1][0])
            from_y = min(line[0][1], line[1][1])
            to_y = max(line[0][1], line[1][1])

            for y in range(from_y, to_y+1):
                for x in range(from_x, to_x+1):
                    sums[y][x] += 1

    for row in sums:
        for value in row:
            print(('.' if value == 0 else value), end='')
        print()

    print('Overlaps:', len([x for x in chain.from_iterable(sums) if x > 1]))


if __name__ == "__main__":
    main()
