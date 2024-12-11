import sys
import functools


def part1(lines: list[str]) -> int:
    stones = parse_stones(lines[0])
    return blink(stones, 25)


def parse_stones(line: str) -> list[int]:
    return list(map(lambda stone: int(stone), line.split(" ")))


def blink(stones: list[int], blink_times: int) -> list[int]:
    stone_count = 0
    for stone in stones:
        stone_count = stone_count + blink_stone(stone, blink_times)

    return stone_count


@functools.cache
def blink_stone(stone: int, blink_times: int) -> int:
    if blink_times == 0:
        return 1

    if stone == 0:
        return blink_stone(1, blink_times - 1)
    elif len(str(stone)) % 2 == 0:
        stone_string = str(stone)
        stone_split_index = int(len(stone_string) / 2)
        return blink_stone(
            int(stone_string[:stone_split_index]), blink_times - 1
        ) + blink_stone(int(stone_string[stone_split_index:]), blink_times - 1)

    return blink_stone(stone * 2024, blink_times - 1)


def part2(lines: list[str]) -> int:
    stones = parse_stones(lines[0])
    return blink(stones, 75)
