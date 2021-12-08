#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        positions = [int(x) for x in input.readline().split(',')]

    first = min(positions)
    last = max(positions)

    best = sys.maxsize
    target = None

    for destination in range(first, last):
        fuel = 0
        for sub in positions:
            distance = abs(sub - destination)
            if distance:
                fuel += (distance * (distance + 1))//2

        if fuel < best:
            best = fuel
            target = destination

    print('Move subs to', target, 'using', best, 'fuel.')


if __name__ == "__main__":
    main()
