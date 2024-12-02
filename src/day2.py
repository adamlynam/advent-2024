import sys


def part1(lines: list[str]) -> int:
    return len(safe_lines(lines))


def part2(lines: list[str]) -> int:
    return len(safe_lines_with_dampener(lines))

def safe_lines(lines: list[str]) -> list[str]:
    return list(filter(lambda line: safe_line(get_levels(line)) , lines))

def safe_line(levels: list[int]) -> bool:
    rising = levels[0] < levels[1]

    if (rising):
        current = levels[0] - 1
        for level in levels:
            if level <= current:
                return False
            if level > current and level - current > 3:
                return False
            current = level
    else:
        current = levels[0] + 1
        for level in levels:
            if level >= current:
                return False
            if level < current and current - level > 3:
                return False
            current = level
        
    return True

def get_levels(line: str) -> list[int]:
    return [int(level) for level in line.split(" ")]

def safe_lines_with_dampener(lines: list[str]) -> list[str]:
    return list(filter(lambda line: safe_line_with_dampener(line) , lines))

def safe_line_with_dampener(line: str) -> bool:
    levels = get_levels(line)
    
    for index,level in enumerate(levels):
        dampened_levels = levels[:]
        del dampened_levels[index]
        if safe_line(dampened_levels):
            return True

    return False
