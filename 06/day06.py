#!/usr/bin/env python3

import argparse
from itertools import groupby


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='days', type=int, help='days', default=80)
    parser.add_argument('-v', dest='verbosity', help='increase verbosity',
                        default=0, action='count')
    parser.add_argument('input', help='input file name')
    parser.parse_args()
    args = parser.parse_args()

    with open(args.input) as input:
        fish = [int(x) for x in input.readline().split(',')]

    fish = {k: len(list(v)) for k, v in groupby(sorted(fish))}

    if args.verbosity:
        print('Initial State:', fish_str(fish, args))

    for day in range(args.days):
        new_fish = fish.get(0, 0)
        fish = {(k-1): v for k, v in fish.items() if k > 0}

        if new_fish:
            fish[6] = fish.get(6, 0) + new_fish
            fish[8] = new_fish

        if args.verbosity:
            print(f'Day {day+1}: {fish_str(fish, args)}')

    print(count_fish(fish))


def fish_str(fish, args):
    if args.verbosity > 1:
        return ', '.join([f'{v}({k} days)' for k, v in fish.items()])
    else:
        return str(count_fish(fish))


def count_fish(fish):
    return sum([v for k, v in fish.items()])


if __name__ == '__main__':
    main()
