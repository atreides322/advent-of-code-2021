#!/usr/bin/env python3

import sys
from itertools import groupby


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        statuses = input.readlines()

    find_power_ratings(statuses)
    find_life_support_rating(statuses)


def find_power_ratings(statuses):
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
        if count >= half:
            gamma |= 1 << (bit_width - index - 1)

    epsilon = ~gamma & bitmask

    print('Gamma:', gamma, 'Epsilon:', epsilon)
    print('Power Consumption:', gamma * epsilon)


def find_life_support_rating(statuses):
    o2 = find_o2_rating(statuses)
    co2 = find_co2_rating(statuses)

    print('O2:', o2, 'CO2:', co2)
    print('Life Support:', o2 * co2)


def find_o2_rating(statuses):
    return find_gas_rating(statuses, choose_larger=True)


def find_co2_rating(statuses):
    return find_gas_rating(statuses, choose_larger=False)


def find_gas_rating(statuses, choose_larger):
    split_statuses = [list(x.strip()) for x in statuses]
    return find_gas_rating_recurse(split_statuses, choose_larger)


def find_gas_rating_recurse(statuses, choose_larger):
    if not statuses or not statuses[0]:
        return 0

    groups = groupby(sorted(statuses, key=msb_key), key=msb_key)
    groups = {k: list(v) for k, v in groups}
    groups.setdefault('0', [])
    groups.setdefault('1', [])

    zero_count = len(groups['0'])
    one_count = len(groups['1'])

    larger = groups['1']
    smaller = groups['0']

    if zero_count > one_count:
        larger = groups['0']
        smaller = groups['1']

    if not larger:
        larger = smaller

    if not smaller:
        smaller = larger

    chosen = larger if choose_larger else smaller
    value = find_gas_rating_recurse([x[1:] for x in chosen], choose_larger)
    msb = int(chosen[0][0])
    bit_count = len(chosen[0])

    return value | msb << (bit_count - 1)


def msb_key(bits):
    return bits[0]


if __name__ == "__main__":
    main()
