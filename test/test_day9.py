from day9 import part1, part2

example1: str = """2333133121414131402
"""

example2: str = """2333133121414131402
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 1928


def test_part1_real_input():
    f = open("input/day9.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 6435922584968


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 2858


def test_part2_real_input():
    f = open("input/day9.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 6469636832766
