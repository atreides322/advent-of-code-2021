#!/usr/bin/env python3

import argparse


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

    if args.verbosity:
        print('Initial State:', fish_str(fish, args))

    for day in range(args.days):
        new_fish = [8 for x in fish if x == 0]
        fish = [x-1 if x > 0 else 6 for x in fish]
        fish.extend(new_fish)
        if args.verbosity:
            print(f'Day {day+1}: {fish_str(fish, args)}')

    print(len(fish))


def fish_str(fish, args):
    return ', '.join([str(x) for x in fish]) if args.verbosity > 1 else len(fish)


if __name__ == '__main__':
    main()
