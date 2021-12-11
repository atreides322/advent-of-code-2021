#!/usr/bin/env python3

import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        topography = [[int(x) for x in line.strip()]
                      for line in input.readlines()]

    calc_risk(topography)
    calc_basins(topography)


def calc_risk(topography):

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


def calc_basins(topography):

    max_i = len(topography)
    max_j = len(topography[0])

    visited = [[False] * max_j for _ in range(max_i)]

    basins = []

    for i, row in enumerate(topography):
        for j, value in enumerate(row):
            basin = find_basin(i, j, max_i, max_j, topography, visited)
            basins.append(basin)

    area = 1
    for x in sorted(basins)[-3:]:
        area *= x

    print('Area:', area)


def find_basin(i, j, max_i, max_j, topography, visited):
    if i < 0 or j < 0 or i >= max_i or j >= max_j \
            or topography[i][j] == 9 or visited[i][j]:
        return 0

    visited[i][j] = True

    return (1
            + find_basin(i - 1, j, max_i, max_j, topography, visited)
            + find_basin(i, j - 1, max_i, max_j, topography, visited)
            + find_basin(i + 1, j, max_i, max_j, topography, visited)
            + find_basin(i, j + 1, max_i, max_j, topography, visited))


if __name__ == "__main__":
    main()
