import sys


def part1(lines: list[str]) -> int:
    schematics = parse_schematics(lines)
    locks = schematics_to_tuples(list(filter(is_lock, schematics)))
    keys = schematics_to_tuples(list(filter(is_key, schematics)))
    return locks_fitting_keys(locks, keys)


def parse_schematics(lines: list[str]) -> list[list[str]]:
    schematics = []

    i = 0
    while i < len(lines):
        schematics.append(lines[i : i + 7])
        i = i + 8

    return schematics


def is_lock(schematic: list[str]) -> bool:
    if schematic[0] == "#####":
        return True
    return False


def is_key(schematic: list[str]) -> bool:
    if schematic[6] == "#####":
        return True
    return False


def schematics_to_tuples(
    schematics: list[list[str]],
) -> list[(int, int, int, int, int)]:
    return list(map(schematic_to_tuple, schematics))


def schematic_to_tuple(schematic: list[str]) -> (int, int, int, int, int):
    pin_one = len([line for line in schematic if line[0] == "#"])
    pin_two = len([line for line in schematic if line[1] == "#"])
    pin_three = len([line for line in schematic if line[2] == "#"])
    pin_four = len([line for line in schematic if line[3] == "#"])
    pin_five = len([line for line in schematic if line[4] == "#"])

    return (pin_one, pin_two, pin_three, pin_four, pin_five)


def locks_fitting_keys(
    locks: list[(int, int, int, int, int)], keys: list[(int, int, int, int, int)]
) -> int:
    fits = 0
    for key in keys:
        for lock in locks:
            if (
                key[0] + lock[0] <= 7
                and key[1] + lock[1] <= 7
                and key[2] + lock[2] <= 7
                and key[3] + lock[3] <= 7
                and key[4] + lock[4] <= 7
            ):
                fits = fits + 1

    return fits


def part2(lines: list[str]) -> int:
    return 0
