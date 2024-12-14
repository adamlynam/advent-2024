from day13 import part1, part2, cost_game

example1: str = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

example2: str = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 480


def test_part1_example1():
    assert cost_game(((94, 34), (22, 67), (8400, 5400))) == 280


def test_part1_example2():
    assert cost_game(((26, 66), (67, 21), (12748, 12176))) == 0


def test_part1_example3():
    assert cost_game(((17, 86), (84, 37), (7870, 6450))) == 200


def test_part1_example4():
    assert cost_game(((69, 23), (27, 71), (18641, 10279))) == 0


# def test_part1_example_mine1():
#     assert cost_game(((10, 10), (20, 20), (10, 10))) == 3


# def test_part1_example_mine2():
#     assert cost_game(((80, 80), (20, 20), (160, 160))) == 6


def test_part1_example_mine4():
    assert cost_game(((90, 17), (35, 92), (3055, 2541))) == 98


def test_part1_real_input():
    f = open("input/day13.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 25629


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 875318608908


def test_part2_example1():
    assert cost_game(((94, 34), (22, 67), (10000000008400, 10000000005400))) == 0


def test_part2_example2():
    assert (
        cost_game(((26, 66), (67, 21), (10000000012748, 10000000012176)))
        == 459236326669
    )


def test_part2_example3():
    assert cost_game(((17, 86), (84, 37), (10000000007870, 10000000006450))) == 0


def test_part2_example4():
    assert (
        cost_game(((69, 23), (27, 71), (10000000018641, 10000000010279)))
        == 416082282239
    )


def test_part2_real_input():
    f = open("input/day13.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 107487112929999
