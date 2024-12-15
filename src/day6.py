import sys


def part1(lines: list[str]) -> int:
    startx, starty = find_start(lines)
    moved_spaces = move_up_spaces(startx, starty, lines)
    return len(list(set(moved_spaces)))


def find_start(lines: list[str]) -> [int, int]:
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "^":
                return x, y


def move_up_spaces(x: int, y: int, lines: list[str]) -> list[(int, int)]:
    moved_spaces = []

    while y >= 0:
        moved_spaces.append((x, y))
        if y - 1 < 0:
            print("off map up")
            print(x, y)
            return moved_spaces
        elif lines[y - 1][x] == "#":
            print("turn right")
            return moved_spaces + move_right_spaces(x, y, lines)
        else:
            print("current location:")
            print(x, y)
            y = y - 1

    return moved_spaces


def move_right_spaces(x: int, y: int, lines: list[str]) -> list[(int, int)]:
    moved_spaces = []
    print("right turn at:")
    print(x, y)

    while x < len(lines[0]):
        moved_spaces.append((x, y))
        if x + 1 >= len(lines[0]):
            print("off map right")
            print(x, y)
            return moved_spaces
        elif lines[y][x + 1] == "#":
            print("turn down")
            return moved_spaces + move_down_spaces(x, y, lines)
        else:
            x = x + 1

    return moved_spaces


def move_down_spaces(x: int, y: int, lines: list[str]) -> list[(int, int)]:
    moved_spaces = []

    while y < len(lines):
        moved_spaces.append((x, y))
        if y + 1 >= len(lines):
            return moved_spaces
        elif lines[y + 1][x] == "#":
            print("turn left")
            return moved_spaces + move_left_spaces(x, y, lines)
        else:
            y = y + 1

    return moved_spaces


def move_left_spaces(x: int, y: int, lines: list[str]) -> list[(int, int)]:
    moved_spaces = []

    while x >= 0:
        moved_spaces.append((x, y))
        if x - 1 < 0:
            return moved_spaces
        elif lines[y][x - 1] == "#":
            print("turn up")
            return moved_spaces + move_up_spaces(x, y, lines)
        else:
            x = x - 1

    return moved_spaces


def part2(lines: list[str]) -> int:
    startx, starty = find_start(lines)
    moved_spaces = list(set(move_up_spaces(startx, starty, lines)))
    loops = 0
    for x, y in moved_spaces:
        extra_obstacle_lines = lines[:]
        extra_obstacle_lines[y] = (
            extra_obstacle_lines[y][:x] + "#" + extra_obstacle_lines[y][x + 1 :]
        )
        if move_up_loop(startx, starty, extra_obstacle_lines, []):
            loops = loops + 1
    return loops


def move_up_loop(
    x: int, y: int, lines: list[str], positions_seen: list[(str, int, int)]
) -> bool:
    if ("up", x, y) in positions_seen:
        return True
    positions_seen.append(("up", x, y))

    while y >= 0:
        if y - 1 < 0:
            # print("off map up")
            # print(x, y)
            return False
        elif lines[y - 1][x] == "#":
            # print("turn right")
            return move_right_loop(x, y, lines, positions_seen)
        else:
            # print("current location:")
            # print(x, y)
            y = y - 1

    return False


def move_right_loop(
    x: int, y: int, lines: list[str], positions_seen: list[(str, int, int)]
) -> bool:
    if ("right", x, y) in positions_seen:
        return True
    positions_seen.append(("right", x, y))

    while x < len(lines[0]):
        if x + 1 >= len(lines[0]):
            # print("off map right")
            # print(x, y)
            return False
        elif lines[y][x + 1] == "#":
            # print("turn down")
            return move_down_loop(x, y, lines, positions_seen)
        else:
            x = x + 1

    return False


def move_down_loop(
    x: int, y: int, lines: list[str], positions_seen: list[(str, int, int)]
) -> bool:
    if ("down", x, y) in positions_seen:
        return True
    positions_seen.append(("down", x, y))

    while y < len(lines):
        if y + 1 >= len(lines):
            return False
        elif lines[y + 1][x] == "#":
            # print("turn left")
            return move_left_loop(x, y, lines, positions_seen)
        else:
            y = y + 1

    return False


def move_left_loop(
    x: int, y: int, lines: list[str], positions_seen: list[(str, int, int)]
) -> bool:
    if ("left", x, y) in positions_seen:
        return True
    positions_seen.append(("left", x, y))

    while x >= 0:
        if x - 1 < 0:
            return False
        elif lines[y][x - 1] == "#":
            # print("turn up")
            return move_up_loop(x, y, lines, positions_seen)
        else:
            x = x - 1

    return False
