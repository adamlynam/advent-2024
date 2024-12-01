from day1 import part1, part2

example1: str = """3   4
4   3
2   5
1   3
3   9
3   3"""

example2: str = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_day1_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 11


def test_day1_part1_real_input():
    f = open("input/day1.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 1660292


def test_day1_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 31


def test_day1_part2_real_input():
    f = open("input/day1.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 22776016
