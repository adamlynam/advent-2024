from day22 import part1, part2, xth_secret_number, buyer_banana_profile

example1: str = """1
10
100
2024
"""

example2: str = """1
2
3
2024
"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 37327623


def test_part1_next_secret_123():
    assert xth_secret_number(123, 1) == 15887950


def test_part1_2nd_secret_123():
    assert xth_secret_number(123, 2) == 16495136


def test_part1_3rd_secret_123():
    assert xth_secret_number(123, 3) == 527345


def test_part1_4th_secret_123():
    assert xth_secret_number(123, 4) == 704524


def test_part1_5th_secret_123():
    assert xth_secret_number(123, 5) == 1553684


def test_part1_6th_secret_123():
    assert xth_secret_number(123, 6) == 12683156


def test_part1_7th_secret_123():
    assert xth_secret_number(123, 7) == 11100544


def test_part1_8th_secret_123():
    assert xth_secret_number(123, 8) == 12249484


def test_part1_9th_secret_123():
    assert xth_secret_number(123, 9) == 7753432


def test_part1_10th_secret_123():
    assert xth_secret_number(123, 10) == 5908254


def test_part1_2000th_secret_1():
    assert xth_secret_number(1, 2000) == 8685429


def test_part1_2000th_secret_10():
    assert xth_secret_number(10, 2000) == 4700978


def test_part1_2000th_secret_100():
    assert xth_secret_number(100, 2000) == 15273692


def test_part1_2000th_secret_2024():
    assert xth_secret_number(2024, 2000) == 8667524


def test_part1_real_input():
    f = open("input/day22.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 19822877190


# 15887950: 0 (-3)
# 16495136: 6 (6)
#   527345: 5 (-1)
#   704524: 4 (-1)
#  1553684: 4 (0)
# 12683156: 6 (2)
# 11100544: 4 (-2)
# 12249484: 4 (0)
#  7753432: 2 (-2)
def test_banana_list_123():
    buyer_profile = buyer_banana_profile(123, 10)
    assert buyer_profile[0] == (-3, 0)
    assert buyer_profile[1] == (6, 6)
    assert buyer_profile[2] == (-1, 5)
    assert buyer_profile[3] == (-1, 4)
    assert buyer_profile[4] == (0, 4)
    assert buyer_profile[5] == (2, 6)
    assert buyer_profile[6] == (-2, 4)
    assert buyer_profile[7] == (0, 4)
    assert buyer_profile[8] == (-2, 2)


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 23


def test_part2_real_input():
    f = open("input/day22.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 25
