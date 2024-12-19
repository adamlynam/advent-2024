import sys
import re
import functools


def part1(lines: list[str]) -> int:
    towels = lines[0].split(", ")
    patterns = list(filter(lambda line: line != "" and "," not in line, lines))
    return len(
        list(filter(lambda pattern: possible_with_towels(pattern, towels), patterns))
    )


def possible_with_towels(pattern: str, towels: list[str]) -> bool:
    towel_regex = "^(" + "|".join(towels) + ")*$"
    match = re.search(towel_regex, pattern)
    if match:
        return True

    return False


def part2(lines: list[str]) -> int:
    towels = lines[0].split(", ")
    patterns = list(filter(lambda line: line != "" and "," not in line, lines))
    return functools.reduce(
        lambda sum, pattern: sum + combinations_with_towels(pattern, tuple(towels)),
        patterns,
        0,
    )


@functools.cache
def combinations_with_towels(pattern: str, towels: list[str]) -> int:
    if pattern == "":
        return 1
    return functools.reduce(
        lambda sum, towel: sum
        + (
            combinations_with_towels(pattern.replace(towel, "", 1), towels)
            if pattern.startswith(towel)
            else 0
        ),
        towels,
        0,
    )
