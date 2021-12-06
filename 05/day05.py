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
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        dx = x2 - x1
        dy = y2 - y1

        dx_inc = 1 if dx >= 0 else -1
        dy_inc = 1 if dy >= 0 else -1

        if x1 == x2 or y1 == y2:
            for y in range(y1, y2 + dy_inc, dy_inc):
                for x in range(x1, x2 + dx_inc, dx_inc):
                    sums[y][x] += 1
        elif abs(dx) == abs(dy):
            for offset in range(0, abs(dx)+1):
                x = x1 + dx_inc * offset
                y = y1 + dy_inc * offset
                sums[y][x] += 1

    for row in sums:
        for value in row:
            print(('.' if value == 0 else value), end='')
        print()

    print('Overlaps:', len([x for x in chain.from_iterable(sums) if x > 1]))


if __name__ == "__main__":
    main()
