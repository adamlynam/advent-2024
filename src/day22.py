import sys
import functools
import math


def part1(lines: list[str]) -> int:
    lines = list(filter(lambda line: line != "", lines))
    numbers = list(map(lambda line: int(line), lines))
    return functools.reduce(
        lambda sum, number: sum + xth_secret_number(number, 2000), numbers, 0
    )


def xth_secret_number(secret_number: int, count: int):
    for x in range(count):
        secret_number = next_secret_number(secret_number)
    return secret_number


def next_secret_number(secret_number: int) -> int:
    multi_result = next_secret_number_multi(secret_number)
    divide_result = next_secret_number_divide(multi_result)
    multi_2024_result = next_secret_number_2024(divide_result)
    return multi_2024_result


def next_secret_number_multi(secret_number: int) -> int:
    multi_result = secret_number * 64
    mix_result = multi_result ^ secret_number
    prune_result = mix_result % 16777216
    return prune_result


def next_secret_number_divide(secret_number: int) -> int:
    divide_result = math.floor(secret_number / 32)
    mix_result = divide_result ^ secret_number
    prune_result = mix_result % 16777216
    return prune_result


def next_secret_number_2024(secret_number: int) -> int:
    multi_result = secret_number * 2048
    mix_result = multi_result ^ secret_number
    prune_result = mix_result % 16777216
    return prune_result


def part2(lines: list[str]) -> int:
    lines = list(filter(lambda line: line != "", lines))
    buyer_profiles = list(
        map(lambda line: buyer_banana_profile(int(line), 2000), lines)
    )
    return optimal_buy_sequence(buyer_profiles)


def buyer_banana_profile(secret_number: int, count: int) -> list[(int, int)]:
    bananas = secret_number % 10
    secret_numbers = []
    for x in range(count):
        secret_number = next_secret_number(secret_number)
        banana_change = secret_number % 10 - bananas
        bananas = secret_number % 10
        secret_numbers.append((banana_change, bananas))
    return secret_numbers


def optimal_buy_sequence(buyer_profiles: list[list[(int, int)]]) -> list[int]:
    total_buyers = len(buyer_profiles)
    optimal_sum = 0
    for a in reversed(range(-9, 10)):
        for b in reversed(range(-9, 10)):
            for c in reversed(range(-9, 10)):
                for d in reversed(range(-9, 10)):
                    sequence = [a, b, c, d]
                    if (9 + sum(sequence)) * total_buyers <= optimal_sum:
                        continue
                    print(sequence)
                    sequence_sum = functools.reduce(
                        lambda sum, profile: sum
                        + bananas_for_sequence(sequence, profile),
                        buyer_profiles,
                        0,
                    )
                    optimal_sum = max(optimal_sum, sequence_sum)
                    print(optimal_sum)
    return optimal_sum


def bananas_for_sequence(sequence: list[int], buyer_profile: list[(int, int)]) -> int:
    for i, order in enumerate(buyer_profile):
        if (
            i < 1997
            and buyer_profile[i][0] == sequence[0]
            and buyer_profile[i + 1][0] == sequence[1]
            and buyer_profile[i + 2][0] == sequence[2]
            and buyer_profile[i + 3][0] == sequence[3]
        ):
            return buyer_profile[i + 3][1]
    return 0
