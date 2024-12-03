from day3 import part1, part2

example1: str = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

example2: str = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1("".join(lines)) == 161


def test_part1_real_input():
    f = open("input/day3.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1("".join(lines)) == 163931492


def test_part2_example():
    lines = example2.split("\n")
    assert part2("".join(lines)) == 48


def test_part2_real_input():
    f = open("input/day3.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2("".join(lines)) == 76911921
