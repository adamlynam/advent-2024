import sys
import itertools


def part1(lines: list[str]) -> int:
    towers = parse_towers(lines)
    # return towers
    antinodes = set(parse_antinodes(lines, towers))
    # return antinodes
    return len(antinodes)


def parse_towers(lines: list[str]) -> dict[str : list[(int, int)]]:
    towers: dict[str : list[(int, int)]] = {}

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != ".":
                tower_type = lines[y][x]
                if tower_type in towers:
                    towers[tower_type].append((x, y))
                else:
                    towers[tower_type] = [(x, y)]

    return towers


def parse_antinodes(
    lines: list[str], towers: dict[str : list[(int, int)]]
) -> list[(int, int)]:
    antinodes: list[(int, int)] = []

    for tower_type, locations in towers.items():
        antinodes = antinodes + parse_antinodes_for_tower_type(lines, locations)

    return antinodes


def parse_antinodes_for_tower_type(
    lines: list[str], locations: list[(int, int)]
) -> list[(int, int)]:
    antinodes: list[(int, int)] = []

    # print(list(itertools.permutations(locations, 2)))

    for first_location, second_location in itertools.permutations(locations, 2):
        antinodes = antinodes + parse_antinodes_for_locations(
            lines, first_location, second_location
        )

    return antinodes


def parse_antinodes_for_locations(
    lines: list[str], location_one: (int, int), location_two: (int, int)
) -> list[(int, int)]:
    antinodes: list[(int, int)] = []

    location_one_x = location_one[0]
    location_one_y = location_one[1]
    location_two_x = location_two[0]
    location_two_y = location_two[1]

    x_diff = abs(location_one_x - location_two_x)
    y_diff = abs(location_one_y - location_two_y)

    if location_one_x < location_two_x:
        if location_one_y < location_two_y:
            # location one is top left
            if location_one_x - x_diff >= 0 and location_one_y - y_diff >= 0:
                antinodes.append((location_one_x - x_diff, location_one_y - y_diff))
            if location_two_x + x_diff < len(
                lines[0]
            ) and location_two_y + y_diff < len(lines):
                antinodes.append((location_two_x + x_diff, location_two_y + y_diff))
        else:
            # location one is bottom left
            if location_one_x - x_diff >= 0 and location_one_y + y_diff < len(lines):
                antinodes.append((location_one_x - x_diff, location_one_y + y_diff))
            if location_two_x + x_diff < len(lines[0]) and location_two_y - y_diff >= 0:
                antinodes.append((location_two_x + x_diff, location_two_y - y_diff))

    else:
        if location_one_y < location_two_y:
            # location one is top right
            if location_one_x + x_diff < len(lines[0]) and location_one_y - y_diff >= 0:
                antinodes.append((location_one_x + x_diff, location_one_y - y_diff))
            if location_two_x - x_diff >= 0 and location_two_y + y_diff < len(lines):
                antinodes.append((location_two_x - x_diff, location_two_y + y_diff))

        else:
            # location one is bottom right
            if location_one_x + x_diff < len(
                lines[0]
            ) and location_one_y + y_diff < len(lines):
                antinodes.append((location_one_x + x_diff, location_one_y + y_diff))
            if location_two_x - x_diff >= 0 and location_two_y - y_diff >= 0:
                antinodes.append((location_two_x - x_diff, location_two_y - y_diff))

    return antinodes


def part2(lines: list[str]) -> int:
    towers = parse_towers(lines)
    antinodes = set(parse_antinodes2(lines, towers))
    print(antinodes)
    return len(antinodes)


def parse_antinodes2(
    lines: list[str], towers: dict[str : list[(int, int)]]
) -> list[(int, int)]:
    antinodes: list[(int, int)] = []

    for tower_type, locations in towers.items():
        antinodes = antinodes + parse_antinodes_for_tower_type2(lines, locations)

    return antinodes


def parse_antinodes_for_tower_type2(
    lines: list[str], locations: list[(int, int)]
) -> list[(int, int)]:
    antinodes: list[(int, int)] = []

    # print(list(itertools.permutations(locations, 2)))

    for first_location, second_location in itertools.permutations(locations, 2):
        antinodes = antinodes + parse_antinodes_for_locations2(
            lines, first_location, second_location
        )

    return antinodes


def parse_antinodes_for_locations2(
    lines: list[str], location_one: (int, int), location_two: (int, int)
) -> list[(int, int)]:
    antinodes: list[(int, int)] = []

    location_one_x = location_one[0]
    location_one_y = location_one[1]
    location_two_x = location_two[0]
    location_two_y = location_two[1]

    x_diff = abs(location_one_x - location_two_x)
    y_diff = abs(location_one_y - location_two_y)

    if location_one_x < location_two_x:
        if location_one_y < location_two_y:
            # location one is top left
            current_x = location_one_x
            current_y = location_one_y
            while current_x >= 0 and current_y >= 0:
                antinodes.append((current_x, current_y))
                current_x = current_x - x_diff
                current_y = current_y - y_diff
            current_x = location_one_x
            current_y = location_one_y
            while current_x < len(lines[0]) and current_y < len(lines):
                antinodes.append((current_x, current_y))
                current_x = current_x + x_diff
                current_y = current_y + y_diff
        else:
            # location one is bottom left
            current_x = location_one_x
            current_y = location_one_y
            while current_x < len(lines[0]) and current_y >= 0:
                antinodes.append((current_x, current_y))
                current_x = current_x + x_diff
                current_y = current_y - y_diff
            current_x = location_one_x
            current_y = location_one_y
            while current_x >= 0 and current_y < len(lines):
                antinodes.append((current_x, current_y))
                current_x = current_x - x_diff
                current_y = current_y + y_diff
    else:
        if location_one_y < location_two_y:
            # location one is top right
            current_x = location_one_x
            current_y = location_one_y
            while current_x < len(lines[0]) and current_y >= 0:
                if location_one == (5, 2) and location_two == (4, 4):
                    print(location_one)
                    print(location_two)
                    print(current_x, current_y)
                antinodes.append((current_x, current_y))
                current_x = current_x + x_diff
                current_y = current_y - y_diff
            current_x = location_one_x
            current_y = location_one_y
            while current_x >= 0 and current_y < len(lines):
                antinodes.append((current_x, current_y))
                current_x = current_x - x_diff
                current_y = current_y + y_diff
        else:
            # location one is bottom right
            current_x = location_one_x
            current_y = location_one_y
            while current_x >= 0 and current_y >= 0:
                antinodes.append((current_x, current_y))
                current_x = current_x - x_diff
                current_y = current_y - y_diff
            current_x = location_one_x
            current_y = location_one_y
            while current_x < len(lines[0]) and current_y < len(lines):
                antinodes.append((current_x, current_y))
                current_x = current_x + x_diff
                current_y = current_y + y_diff
    return antinodes
