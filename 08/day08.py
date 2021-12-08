#!/usr/bin/env python3

import sys


UNIQUE_SIGNAL_COUNT = {2, 4, 3, 7}


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        puzzles = [parse_line(line) for line in input.readlines()]

    simple_count = [1 for puzzle in puzzles
                    for display in puzzle['current']
                    if len(display) in UNIQUE_SIGNAL_COUNT]

    print(len(simple_count))


def parse_line(line):
    parts = [x.strip().split(' ') for x in line.split('|')]
    return {'all': parts[0], 'current': parts[1]}


if __name__ == "__main__":
    main()
