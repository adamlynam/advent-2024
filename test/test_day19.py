from day19 import part1, part2, possible_with_towels

example1: str = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 6


def test_short_towel_first_example():
    assert possible_with_towels("bada", ["bad", "ba", "da"]) is True


def test_part1_real_input():
    f = open("input/day19.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 355


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 16


def test_part2_real_input():
    f = open("input/day19.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 732978410442050
