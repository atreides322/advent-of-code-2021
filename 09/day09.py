#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        topography = [[int(x) for x in line.strip()]
                      for line in input.readlines()]

    max_i = len(topography)
    max_j = len(topography[0])

    risk = 0

    for i, row in enumerate(topography):
        for j, value in enumerate(row):
            local_min = True

            if i - 1 >= 0:
                local_min &= value < topography[i-1][j]

            if local_min and j - 1 >= 0:
                local_min &= value < topography[i][j-1]

            if local_min and i + 1 < max_i:
                local_min &= value < topography[i+1][j]

            if local_min and j + 1 < max_j:
                local_min &= value < topography[i][j+1]

            if local_min:
                risk += 1 + value

    print('Risk:', risk)


if __name__ == "__main__":
    main()
