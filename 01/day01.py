#!/usr/bin/env python3

import sys
from collections import deque


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        numbers = [int(x) for x in input.readlines()]

    sliding_window(numbers, window_size=1)
    sliding_window(numbers, window_size=3)


def sliding_window(numbers, window_size):
    if len(numbers) <= window_size:
        return

    count = 0
    window = deque(numbers[0:window_size])
    previous = sum(window)

    for number in numbers[window_size:]:
        window.popleft()
        window.append(number)

        current = sum(window)

        if current > previous:
            count += 1

        previous = current

    print(f"Sliding Window Size: {window_size}\tSum: {count}")


if __name__ == "__main__":
    main()
