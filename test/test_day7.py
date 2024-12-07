from day7 import part1, part2, equation_true, concat_equation_true

example1: str = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

example2: str = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 3749


def test_part1_190_truth():
    assert equation_true(190, [10, 19]) is True


def test_part1_3267_truth():
    assert equation_true(3267, [81, 40, 27]) is True


def test_part1_292_truth():
    assert equation_true(292, [11, 6, 16, 20]) is True


def test_part1_real_input():
    f = open("input/day7.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 7710205485870


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 11387


def test_part2_190_truth():
    assert concat_equation_true(190, [10, 19]) is True


def test_part2_3267_truth():
    assert concat_equation_true(3267, [81, 40, 27]) is True


def test_part2_292_truth():
    assert concat_equation_true(292, [11, 6, 16, 20]) is True


def test_part2_156_truth():
    assert concat_equation_true(156, [15, 6]) is True


def test_part2_7290_truth():
    assert concat_equation_true(7290, [6, 8, 6, 15]) is True


def test_part2_192_truth():
    assert concat_equation_true(192, [17, 8, 14]) is True


def test_part2_real_input():
    f = open("input/day7.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 20928985450275
