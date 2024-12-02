from day2 import part1, part2

example1: str = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

example2: str = """1 1 2 3"""


def test_day2_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 2


def test_day2_part1_real_input():
    f = open("input/day2.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 246


def test_day2_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 4


def test_day2_part2_first_item_test():
    lines = example2.split("\n")
    assert part2(lines) == 1


def test_day2_part2_real_input():
    f = open("input/day2.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 318
