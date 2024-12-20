import sys
import functools


def part1(lines: list[str], picoseconds_saved: int) -> int:
    lines = list(filter(lambda line: line != "", lines))
    start = find_start(lines)
    end = find_end(lines)
    picoseconds_from_start = find_picoseconds_for_path(lines, start, end)
    cheats = find_cheats(picoseconds_from_start)
    # print(cheats)
    return functools.reduce(
        lambda sum, cheat: sum if cheat[0] < picoseconds_saved else sum + cheat[1],
        cheats.items(),
        0,
    )


def find_start(lines: list[str]) -> (int, int):
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "S":
                return x, y

    raise ValueError


def find_end(lines: list[str]) -> (int, int):
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "E":
                return x, y

    raise ValueError


def find_picoseconds_for_path(
    lines: list[str], start: (int, int), end: (int, int)
) -> dict[((int, int), int)]:
    picoseconds_from_start = dict()
    current = start
    previous = None
    picoseconds_passed = 0
    while current != end:
        picoseconds_from_start[str(current)] = (current, picoseconds_passed)

        right = (current[0] + 1, current[1])
        left = (current[0] - 1, current[1])
        down = (current[0], current[1] + 1)
        up = (current[0], current[1] - 1)
        if lines[right[0]][right[1]] != "#" and right != previous:
            previous = current
            current = right
        elif lines[left[0]][left[1]] != "#" and left != previous:
            previous = current
            current = left
        elif lines[down[0]][down[1]] != "#" and down != previous:
            previous = current
            current = down
        elif lines[up[0]][up[1]] != "#" and up != previous:
            previous = current
            current = up
        picoseconds_passed = picoseconds_passed + 1

    picoseconds_from_start[str(end)] = (end, picoseconds_passed)
    return picoseconds_from_start


def find_cheats(picoseconds_from_start: dict[((int, int), int)]) -> dict[int]:
    cheats = dict()
    for key, (node, picoseconds) in picoseconds_from_start.items():
        # top_left = str((node[0] - 1, node[1] - 1))
        # if top_left in picoseconds_from_start:
        #     cheat_saves = picoseconds_from_start[top_left][1] - picoseconds - 2
        #     if cheat_saves in cheats:
        #         cheats[cheat_saves] = cheats[cheat_saves] + 1
        #     else:
        #         cheats[cheat_saves] = 1
        top_mid = str((node[0], node[1] - 2))
        if top_mid in picoseconds_from_start:
            cheat_saves = picoseconds_from_start[top_mid][1] - picoseconds - 2
            if cheat_saves in cheats:
                cheats[cheat_saves] = cheats[cheat_saves] + 1
            else:
                cheats[cheat_saves] = 1
        # top_right = str((node[0] + 1, node[1] - 1))
        # if top_right in picoseconds_from_start:
        #     cheat_saves = picoseconds_from_start[top_right][1] - picoseconds - 2
        #     if cheat_saves in cheats:
        #         cheats[cheat_saves] = cheats[cheat_saves] + 1
        #     else:
        #         cheats[cheat_saves] = 1
        left = str((node[0] - 2, node[1]))
        if left in picoseconds_from_start:
            cheat_saves = picoseconds_from_start[left][1] - picoseconds - 2
            if cheat_saves in cheats:
                cheats[cheat_saves] = cheats[cheat_saves] + 1
            else:
                cheats[cheat_saves] = 1
        right = str((node[0] + 2, node[1]))
        if right in picoseconds_from_start:
            cheat_saves = picoseconds_from_start[right][1] - picoseconds - 2
            if cheat_saves in cheats:
                cheats[cheat_saves] = cheats[cheat_saves] + 1
            else:
                cheats[cheat_saves] = 1
        # bottom_left = str((node[0] - 1, node[1] + 1))
        # if bottom_left in picoseconds_from_start:
        #     cheat_saves = picoseconds_from_start[bottom_left][1] - picoseconds - 2
        #     if cheat_saves in cheats:
        #         cheats[cheat_saves] = cheats[cheat_saves] + 1
        #     else:
        #         cheats[cheat_saves] = 1
        bottom_mid = str((node[0], node[1] + 2))
        if bottom_mid in picoseconds_from_start:
            cheat_saves = picoseconds_from_start[bottom_mid][1] - picoseconds - 2
            if cheat_saves in cheats:
                cheats[cheat_saves] = cheats[cheat_saves] + 1
            else:
                cheats[cheat_saves] = 1
        # bottom_right = str((node[0] + 1, node[1] + 1))
        # if bottom_right in picoseconds_from_start:
        #     cheat_saves = picoseconds_from_start[bottom_right][1] - picoseconds - 2
        #     if cheat_saves in cheats:
        #         cheats[cheat_saves] = cheats[cheat_saves] + 1
        #     else:
        #         cheats[cheat_saves] = 1
    return cheats


def part2(lines: list[str], picoseconds_saved: int) -> int:
    return 0
