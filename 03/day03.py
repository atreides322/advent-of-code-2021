#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        statuses = input.readlines()

    total = len(statuses)
    bit_width = len(statuses[0].strip())
    bitmask = 0

    for index in range(bit_width):
        bitmask |= 1 << index

    half = total // 2
    bit_count = [0] * bit_width

    for status in statuses:
        for index, bit in enumerate(status.strip()):
            if bit == '1':
                bit_count[index] += 1

    gamma = 0
    for index, count in enumerate(bit_count):
        if count > half:
            gamma |= 1 << (bit_width - index - 1)

    epsilon = ~gamma & bitmask

    print('Gamma:', gamma, 'Epsilon:', epsilon)
    print('Power Consumption:', gamma * epsilon)


if __name__ == "__main__":
    main()
