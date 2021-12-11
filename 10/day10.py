#!/usr/bin/env python3

import sys


def main():
    group = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }

    compiler_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    autocomplete_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        subsystems = input.readlines()

    illegal = []
    autocomplete = []

    for subsystem in subsystems:
        stack = []
        corrupt = False
        for symbol in subsystem.strip():
            if symbol in group.keys():
                stack.append(symbol)
            elif stack and group[stack[-1]] == symbol:
                stack.pop()
            else:
                illegal.append(symbol)
                corrupt = True
                break

        if not corrupt:
            score = 0
            for symbol in reversed(stack):
                score *= 5
                score += autocomplete_points[group[symbol]]

            if score:
                autocomplete.append(score)

    print('Compiler:', sum(compiler_points[symbol] for symbol in illegal))
    print('Autocomplete:', sorted(autocomplete)[len(autocomplete)//2])


if __name__ == "__main__":
    main()
