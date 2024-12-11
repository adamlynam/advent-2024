from day11 import part1, part2

example1: str = """125 17
"""

example2: str = """example"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 55312


def test_part1_real_input():
    f = open("input/day11.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 229043


def test_part2_real_input():
    f = open("input/day11.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 272673043446478
