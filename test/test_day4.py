from day4 import part1, part2

example1: str = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

example2: str = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 18


def test_part1_real_input():
    f = open("input/day4.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 2370


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 9


def test_part2_real_input():
    f = open("input/day4.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 1908
