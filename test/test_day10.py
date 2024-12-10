from day10 import part1, part2

example1: str = """0123
1234
8765
9876"""

example2: str = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 1


def test_part1_example2():
    lines = example2.split("\n")
    assert part1(lines) == 36


def test_part1_real_input():
    f = open("input/day10.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 760


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 81


def test_part2_real_input():
    f = open("input/day10.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 1764
