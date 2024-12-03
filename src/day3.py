import sys
import re
import functools


def part1(input: str) -> int:
    return functools.reduce(lambda a, b: a+b, muls_to_product(match_muls(input)))

def match_muls(line: str) -> list[str]:
    return re.findall(r'mul\([0-9]*,[0-9]*\)', line)

def muls_to_product(muls: list[str]) -> list[int]:
    return list(map(mul_product, muls))

def mul_product(mul: str) -> int:
    # print (mul)
    numbers = mul.replace("mul(", "").replace(")", "").split(",")
    return int(numbers[0]) * int(numbers[1])

def part2(input: str) -> int:
    # return match_instructions(input)
    return eval_instructions(match_instructions(input))

def match_instructions(line: str) -> list[str]:
    return re.findall(r'mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)', line)

def eval_instructions(instructions: list[str]) -> int:
    sum = 0
    active = True
    for instruction in instructions:
        if (instruction == "do()"):
            active = True
        elif (instruction == "don't()"):
            active = False
        else:
            if (active):
                sum += mul_product(instruction)
            
    return sum
