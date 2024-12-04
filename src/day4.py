import sys


def part1(lines: list[str]) -> int:
    xmases = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if (lines[x][y] == "X"):
                xmases += find_xmases(x, y, lines)
    return xmases

def find_xmases(x: int, y: int, lines: list[str]) -> int:
    return look_up(x, y, lines) \
        + look_down(x, y, lines) \
        + look_left(x, y, lines) \
        + look_right(x, y, lines) \
        + look_up_left(x, y, lines) \
        + look_up_right(x, y, lines) \
        + look_down_left(x, y, lines) \
        + look_down_right(x, y, lines)

def look_up(x: int, y: int, lines: list[str]) -> int:
    if (y <= 2):
        return 0
    
    if lines[x][y - 1] == "M" and lines[x][y - 2] == "A" and lines[x][y - 3] == "S":
        return 1
        
    return 0

def look_down(x: int, y: int, lines: list[str]) -> int:
    if (y >= len(lines[0]) - 3):
        return 0
    
    if lines[x][y + 1] == "M" and lines[x][y + 2] == "A" and lines[x][y + 3] == "S":
        return 1
        
    return 0

def look_left(x: int, y: int, lines: list[str]) -> int:
    if (x <= 2):
        return 0
    
    if lines[x - 1][y] == "M" and lines[x - 2][y] == "A" and lines[x - 3][y] == "S":
        return 1
        
    return 0

def look_right(x: int, y: int, lines: list[str]) -> int:
    if (x >= len(lines) - 3):
        return 0
    
    if lines[x + 1][y] == "M" and lines[x + 2][y] == "A" and lines[x + 3][y] == "S":
        return 1
        
    return 0

def look_up_left(x: int, y: int, lines: list[str]) -> int:
    if (y <= 2):
        return 0
    if (x <= 2):
        return 0
    
    if lines[x - 1][y - 1] == "M" and lines[x - 2][y - 2] == "A" and lines[x - 3][y - 3] == "S":
        return 1
        
    return 0

def look_up_right(x: int, y: int, lines: list[str]) -> int:
    if (y <= 2):
        return 0
    if (x >= len(lines) - 3):
        return 0
    
    if lines[x + 1][y - 1] == "M" and lines[x + 2][y - 2] == "A" and lines[x + 3][y - 3] == "S":
        return 1
        
    return 0

def look_down_left(x: int, y: int, lines: list[str]) -> int:
    if (y >= len(lines[0]) - 3):
        return 0
    if (x <= 2):
        return 0
    
    if lines[x - 1][y + 1] == "M" and lines[x - 2][y + 2] == "A" and lines[x - 3][y + 3] == "S":
        return 1
        
    return 0

def look_down_right(x: int, y: int, lines: list[str]) -> int:
    if (y >= len(lines[0]) - 3):
        return 0
    if (x >= len(lines) - 3):
        return 0
    
    if lines[x + 1][y + 1] == "M" and lines[x + 2][y + 2] == "A" and lines[x + 3][y + 3] == "S":
        return 1
        
    return 0

def part2(lines: list[str]) -> int:
    mases = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if (lines[x][y] == "A"):
                mases += find_mases(x, y, lines)
    return mases

def find_mases(x: int, y: int, lines: list[str]) -> int:
    if (x <= 0 or x >= len(lines) - 1):
        return 0
    if (y <= 0 or y >= len(lines[0]) - 1):
        return 0

    if forward_diagonal_mas(x, y, lines) and backwards_diagonal_max(x, y, lines):
        return 1
    
    return 0

def forward_diagonal_mas(x: int, y: int, lines: list[str]):
    if lines[x + 1][y - 1] == "M" and lines[x - 1][y + 1] == "S":
        return True
    elif lines[x + 1][y - 1] == "S" and lines[x - 1][y + 1] == "M":
        return True
    
    return False

def backwards_diagonal_max(x: int, y: int, lines: list[str]):
    if lines[x - 1][y - 1] == "M" and lines[x + 1][y + 1] == "S":
        return True
    elif lines[x - 1][y - 1] == "S" and lines[x + 1][y + 1] == "M":
        return True

    return False
