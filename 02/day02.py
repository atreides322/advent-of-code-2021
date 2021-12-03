#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        directions = input.readlines()

    aim = 0
    vertical = 0
    horizontal = 0

    for direction, magnitude in [x.split() for x in directions]:
        magnitude = int(magnitude)

        if direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude
        elif direction == 'forward':
            horizontal += magnitude
            vertical += magnitude * aim
        else:
            raise ValueError(f'Invalid direction {direction}')

    print(vertical * horizontal)


if __name__ == "__main__":
    main()
