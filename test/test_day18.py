from day18 import part1, part2

example1: str = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines, 12, 6) == 22


def test_part1_real_input():
    f = open("input/day18.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines, 1024, 70) == 382


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines, 6) == "6,1"


def test_part2_real_input():
    f = open("input/day18.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines, 70) == "6,36"
