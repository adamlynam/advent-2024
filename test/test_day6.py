from day6 import part1, part2

example1: str = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

example2: str = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 41


def test_part1_real_input():
    f = open("input/day6.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 4696


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 6


def test_part2_real_input():
    f = open("input/day6.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 1443
