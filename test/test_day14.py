from day14 import part1, part2, calculate_final_position

example1: str = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines, 11, 7, 100) == 12


def test_part1_example_5_steps():
    assert calculate_final_position("p=2,4 v=2,-3", 11, 7, 5) == (1, 3)


def test_part1_real_input():
    f = open("input/day14.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines, 101, 103, 100) == 222901875


def test_part2_example_5_steps():
    assert part2(["p=2,4 v=2,-3"], 11, 7, 5) == 6243


def test_part2_real_input():
    f = open("input/day14.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines, 101, 103, 1) == 6243
