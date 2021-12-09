#!/usr/bin/env python3

import sys
from itertools import groupby


UNIQUE_SIGNAL_COUNT = {2, 4, 3, 7}


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        puzzles = [parse_line(line) for line in input.readlines()]

    simple_count = [1 for puzzle in puzzles
                    for display in puzzle['current']
                    if len(display) in UNIQUE_SIGNAL_COUNT]

    print('Unique:',  len(simple_count))

    decoded = [decode(**puzzle) for puzzle in puzzles]
    print('Decoded Sum:', sum(decoded))


def parse_line(line):
    parts = [x.strip().split(' ') for x in line.split('|')]
    return {'sample': parts[0], 'current': parts[1]}


def decode(sample, current):
    grouped = {k: list(v) for k, v in
               groupby((frozenset(signal) for signal in
                        sorted(sample, key=len)), key=len)}

    one = grouped[2][0]
    four = grouped[4][0]
    seven = grouped[3][0]
    eight = grouped[7][0]

    translation = {one: '1', four: '4', seven: '7', eight: '8'}

    standard_a = get_single(seven - one)

    almost_nine = four | seven
    nine = next(x for x in grouped[6] if len(x ^ almost_nine) == 1)
    translation[nine] = '9'

    standard_g = get_single(nine - almost_nine)
    # standard_e = get_single(eight - nine) # Apparently unnecessary?

    bottom_corner = eight - four - seven - one
    almost_zero = bottom_corner | seven
    zero = next(x for x in grouped[6] if len(x ^ almost_zero) == 1)
    translation[zero] = '0'

    standard_b = get_single(zero - almost_zero)
    standard_d = get_single(eight - zero)

    three = frozenset({standard_a, standard_d, standard_g}) | one
    translation[three] = '3'

    six = get_single(set(grouped[6]) - {zero} - {nine})
    translation[six] = '6'

    standard_c = get_single(eight - six)
    standard_f = get_single(one - {standard_c})

    two = frozenset(eight - {standard_b} - {standard_f})
    translation[two] = '2'

    five = frozenset(nine - {standard_c})
    translation[five] = '5'

    return int(''.join([translation.get(frozenset(x), x) for x in current]))


def get_single(the_set):
    return list(the_set)[0]


if __name__ == "__main__":
    main()
