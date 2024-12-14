import sys
import time


def part1(lines: list[str], grid_x: int, grid_y: int, steps: int) -> int:
    # return calculate_final_positions(lines, grid_x, grid_y), grid_x, grid_y
    return calculate_safety_factor(
        calculate_final_positions(lines, grid_x, grid_y, steps), grid_x, grid_y
    )


def calculate_final_positions(
    lines: list[str], grid_x: int, grid_y: int, steps: int
) -> list[(int, int)]:
    return list(
        map(lambda line: calculate_final_position(line, grid_x, grid_y, steps), lines)
    )


def calculate_final_position(
    line: str, grid_x: int, grid_y: int, steps: int
) -> (int, int):
    x = int(line.split(" ")[0].split(",")[0].replace("p=", ""))
    y = int(line.split(" ")[0].split(",")[1])
    dx = int(line.split(" ")[1].split(",")[0].replace("v=", ""))
    dy = int(line.split(" ")[1].split(",")[1])

    new_x = (x + dx * steps) % grid_x
    new_y = (y + dy * steps) % grid_y

    return (new_x, new_y)


def calculate_safety_factor(
    positions: list[(int, int)], grid_x: int, grid_y: int
) -> int:
    x_mid = (grid_x - 1) / 2
    y_mid = (grid_y - 1) / 2

    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0

    for position in positions:
        x = position[0]
        y = position[1]
        if x < x_mid and y < y_mid:
            top_left = top_left + 1
        if x > x_mid and y < y_mid:
            top_right = top_right + 1
        if x < x_mid and y > y_mid:
            bottom_left = bottom_left + 1
        if x > x_mid and y > y_mid:
            bottom_right = bottom_right + 1

    return top_left * top_right * bottom_left * bottom_right


def part2(lines: list[str], grid_x: int, grid_y: int, steps: int) -> int:
    for step in range(steps):
        # print(63 + 103 * step)
        print_positions(
            calculate_final_positions(lines, grid_x, grid_y, 6243),
            grid_x,
            grid_y,
        )
        time.sleep(0.5)
    return 6243


def print_positions(positions: list[(int, int)], grid_x: int, grid_y: int) -> None:
    print("")
    for y in range(grid_y):
        line = ""
        for x in range(grid_x):
            if (x, y) in positions:
                line = line + " o"
            else:
                line = line + " ."
        print(line)
