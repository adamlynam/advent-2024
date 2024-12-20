from day20 import part1, part2

example1: str = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines, 1) == 44


def test_part1_real_input():
    f = open("input/day20.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines, 100) == 1441


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines, 50) == 285


def test_part2_real_input():
    f = open("input/day20.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines, 100) == 999
