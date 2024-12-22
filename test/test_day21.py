from day21 import part1, part2, enter_code_on_numeric_pad_bot, enter_code
from day21_online_solution import calc_fewest

example1: str = """029A
980A
179A
456A
379A
"""

example2: str = """example"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines, 2) == 126384


def test_numeric_pad_direct():
    assert len(enter_code_on_numeric_pad_bot("029A")) == len("<A^A>^^AvvvA")


def test_full_chain_029A():
    assert enter_code("029A", 2) == len(
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    )


def test_full_chain_980A():
    assert enter_code("980A", 2) == len(
        "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"
    )


def test_full_chain_179A():
    assert enter_code("179A", 2) == len(
        "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    )


def test_full_chain_456A():
    assert enter_code("456A", 2) == len(
        "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"
    )


def test_full_chain_379A():
    assert enter_code("379A", 2) == len(
        "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    )


def test_online_solver_869A():
    assert calc_fewest("869A", 3) == 70


def test_online_solver_170A():
    assert calc_fewest("170A", 3) == 72


def test_online_solver_319A():
    assert calc_fewest("319A", 3) == 70


def test_online_solver_349A():
    assert calc_fewest("349A", 3) == 72


def test_online_solver_489A():
    assert calc_fewest("489A", 3) == 74


def test_my_solver_869A():
    assert enter_code("869A", 2) == 70


def test_my_solver_170A():
    assert enter_code("170A", 2) == 72


def test_my_solver_319A():
    assert enter_code("319A", 2) == 70


def test_my_solver_349A():
    assert enter_code("349A", 2) == 72


def test_my_solver_489A():
    assert enter_code("489A", 2) == 74


def test_part1_real_input():
    f = open("input/day21.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines, 2) == 156714


# too low
def test_part2_real_input():
    f = open("input/day21.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 191139369248202
