from day8 import part1, part2

example1: str = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

example2: str = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 14


def test_part1_real_input():
    f = open("input/day8.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 396


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 34


def test_part2_real_input():
    f = open("input/day8.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 1200
