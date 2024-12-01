import sys


def part1(lines: list[str]) -> int:
    list1, list2 = build_lists(lines)
    list1.sort()
    list2.sort()
    difference = 0
    for index, number in enumerate(list1):
        difference += abs(list2[index] - number)
    return difference


def part2(lines: list[str]) -> int:
    list1, list2 = build_lists(lines)
    similarity = 0
    for index, number in enumerate(list1):
        similarity += number * len(list(filter(lambda x: number == x, list2)))
    return similarity


def build_lists(lines: list[str]) -> (list[int], list[int]):
    list1 = []
    list2 = []
    for line in lines:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))
    return (list1, list2)
