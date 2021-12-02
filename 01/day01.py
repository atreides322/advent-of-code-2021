#!/usr/bin/env python3

import sys
from collections import deque


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        numbers = [int(x) for x in input.readlines()]

    single_increase(numbers)
    sliding_window(numbers)


def single_increase(numbers):
    if not numbers:
        return

    count = 0
    previous = numbers[0]

    for number in numbers[1:]:
        if number > previous:
            count += 1
        previous = number

    print(f"Single: {count}")


def sliding_window(numbers):
    if len(numbers) < 4:
        return

    count = 0
    window = deque(numbers[0:3])
    previous = sum(window)

    for number in numbers[3:]:
        window.popleft()
        window.append(number)

        current = sum(window)

        if current > previous:
            count += 1

        previous = current

    print(f"Sliding Window: {count}")


if __name__ == "__main__":
    main()
