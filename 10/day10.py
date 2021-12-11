#!/usr/bin/env python3

import sys


def main():
    group = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }

    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        subsystems = input.readlines()

    illegal = []

    for subsystem in subsystems:
        stack = []
        for symbol in subsystem.strip():
            if symbol in group.keys():
                stack.append(symbol)
            elif stack and group[stack[-1]] == symbol:
                stack.pop()
            else:
                illegal.append(symbol)
                break

    print(sum(score[symbol] for symbol in illegal))


if __name__ == "__main__":
    main()
