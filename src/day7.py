import sys


def part1(lines: list[str]) -> int:
    valid_sum = 0
    for line in lines:
        parts = line.split(":")
        target = int(parts[0])
        numbers = list(map(lambda num: int(num), parts[1].strip().split(" ")))
        if equation_true(target, numbers):
            valid_sum = valid_sum + target
    return valid_sum


def equation_true(target: int, numbers: list[int]) -> bool:
    if len(numbers) == 1 and target == numbers[0]:
        return True
    elif (len(numbers) == 1) and target != numbers[0]:
        return False
    else:
        return equation_true(
            target, [numbers[0] * numbers[1]] + numbers[2:]
        ) or equation_true(target, [numbers[0] + numbers[1]] + numbers[2:])


def part2(lines: list[str]) -> int:
    valid_sum = 0
    for line in lines:
        parts = line.split(":")
        target = int(parts[0])
        numbers = list(map(lambda num: int(num), parts[1].strip().split(" ")))
        if concat_equation_true(target, numbers):
            valid_sum = valid_sum + target
    return valid_sum


def concat_equation_true(target: int, numbers: list[int]) -> bool:
    if len(numbers) == 1 and target == numbers[0]:
        return True
    elif (len(numbers) == 1) and target != numbers[0]:
        return False
    else:
        return (
            concat_equation_true(target, [numbers[0] * numbers[1]] + numbers[2:])
            or concat_equation_true(target, [numbers[0] + numbers[1]] + numbers[2:])
            or concat_equation_true(
                target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:]
            )
        )
