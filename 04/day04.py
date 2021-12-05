#!/usr/bin/env python3

import sys
from copy import deepcopy
from itertools import chain

from colors import color


class Board:
    def __init__(self, numbers):
        self.original = deepcopy(numbers)
        self.rows = deepcopy(numbers)
        self.columns = [list(x) for x in zip(*numbers)]
        self.numbers = list(chain.from_iterable(numbers))
        self.picked = []

    def pulled(self, number):
        self.picked.append(number)

        bingo = False

        for row in self.rows:
            self.safe_remove(row, number)
            bingo = bingo or not row

        for column in self.columns:
            self.safe_remove(column, number)
            bingo = bingo or not column

        self.safe_remove(self.numbers, number)

        if bingo:
            return sum(self.numbers) * number
        else:
            return None

    def __str__(self):
        return '\n'.join(
            ''.join([self.format_number(number) for number in row])
            for row in self.original)

    def format_number(self, number):
        formatted = str(number).rjust(3)
        return (color(formatted, bg='red', style='bold')
                if number in self.picked else formatted)

    @staticmethod
    def safe_remove(alist, item):
        try:
            alist.remove(item)
        except ValueError:
            pass


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        lines = input.readlines()

    number_pulls = [int(x) for x in lines[0].split(',')]

    puzzles = read_puzzles(lines[2:])

    bingo = False
    for number in number_pulls:
        for puzzle in puzzles:
            score = puzzle.pulled(number)

            if score is not None:
                bingo = True
                print(puzzle)
                print('Score:', score)

        if bingo:
            break


def read_puzzles(lines):
    puzzles = []
    puzzle = []
    for line in lines:
        if not line.strip():
            puzzles.append(Board(puzzle))
            puzzle = []
        else:
            puzzle.append([int(x) for x in line.split()])

    puzzles.append(Board(puzzle))

    return puzzles


if __name__ == "__main__":
    main()
