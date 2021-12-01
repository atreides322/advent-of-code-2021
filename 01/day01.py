#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        numbers = [int(x) for x in input.readlines()]

    if not numbers:
        return

    count = 0
    previous = numbers[0]

    for number in numbers[1:]:
        if number > previous:
            count += 1
        previous = number

    print(count)


if __name__ == "__main__":
    main()
