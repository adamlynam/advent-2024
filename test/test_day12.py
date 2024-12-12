from day12 import part1, part2

example1: str = """AAAA
BBCD
BBCC
EEEC"""

example2: str = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

example3: str = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

example4: str = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

example5: str = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 140


def test_part1_example2():
    lines = example2.split("\n")
    assert part1(lines) == 772


def test_part1_example3():
    lines = example3.split("\n")
    assert part1(lines) == 1930


def test_part1_real_input():
    f = open("input/day12.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 1424472


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 80


def test_part2_example2():
    lines = example2.split("\n")
    assert part2(lines) == 436


def test_part2_example3():
    lines = example3.split("\n")
    assert part2(lines) == 1206


def test_part2_example4():
    lines = example4.split("\n")
    assert part2(lines) == 236


def test_part2_example5():
    lines = example5.split("\n")
    assert part2(lines) == 368


def test_part2_real_input():
    f = open("input/day12.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 870202
