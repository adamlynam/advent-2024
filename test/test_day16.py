from day16 import part1, part2

example1: str = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

example2: str = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

my_example: str = """#################
#...#.#########.#
#.#.#.#########.#
#.#S#...........#
#.###.#########.#
#..E#.#########.#
#################
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 7036


def test_part1_example2():
    lines = example2.split("\n")
    assert part1(lines) == 11048


def test_part1_my_example():
    lines = my_example.split("\n")
    assert part1(lines) == 4010


def test_part1_real_input():
    f = open("input/day16.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 72428


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 45


def test_part2_example2():
    lines = example2.split("\n")
    assert part2(lines) == 64


def test_part2_real_input():
    f = open("input/day16.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 456
