import sys


def part1(lines: list[str]) -> int:
    summits = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            summits = summits + len(find_summits(0, x, y, lines))

    return summits


def find_summits(current_height: int, x: int, y: int, lines: list[str]) -> [(int, int)]:
    summits = []
    if current_height == int(lines[y][x]):
        if current_height == 9:
            return [(x, y)]

        if x - 1 >= 0:
            summits = summits + find_summits(current_height + 1, x - 1, y, lines)
        if x + 1 < len(lines[0]):
            summits = summits + find_summits(current_height + 1, x + 1, y, lines)
        if y - 1 >= 0:
            summits = summits + find_summits(current_height + 1, x, y - 1, lines)
        if y + 1 < len(lines):
            summits = summits + find_summits(current_height + 1, x, y + 1, lines)

    return list(set(summits))


def part2(lines: list[str]) -> int:
    summits = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            summits = summits + len(find_paths(0, x, y, lines))

    return summits


def find_paths(current_height: int, x: int, y: int, lines: list[str]) -> [(int, int)]:
    paths = []
    if current_height == int(lines[y][x]):
        if current_height == 9:
            return [(x, y)]

        if x - 1 >= 0:
            paths = paths + find_paths(current_height + 1, x - 1, y, lines)
        if x + 1 < len(lines[0]):
            paths = paths + find_paths(current_height + 1, x + 1, y, lines)
        if y - 1 >= 0:
            paths = paths + find_paths(current_height + 1, x, y - 1, lines)
        if y + 1 < len(lines):
            paths = paths + find_paths(current_height + 1, x, y + 1, lines)

    return paths
