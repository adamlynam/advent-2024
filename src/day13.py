import sys
import math
import functools


def part1(lines: list[str]) -> int:
    games = parse_games(lines)
    return cost_games(games)


def parse_games(lines: list[str]) -> list[((int, int), (int, int), (int, int))]:
    games = []
    for game_index, line in enumerate(lines):
        if game_index % 4 == 0:
            button_a = lines[game_index]
            button_a_x = int(button_a.split(",")[0].replace("Button A: X+", ""))
            button_a_y = int(button_a.split(",")[1].replace(" Y+", ""))
            button_b = lines[game_index + 1]
            button_b_x = int(button_b.split(",")[0].replace("Button B: X+", ""))
            button_b_y = int(button_b.split(",")[1].replace(" Y+", ""))
            prize = lines[game_index + 2]
            prize_x = int(prize.split(",")[0].replace("Prize: X=", ""))
            prize_y = int(prize.split(",")[1].replace(" Y=", ""))
            games.append(
                ((button_a_x, button_a_y), (button_b_x, button_b_y), (prize_x, prize_y))
            )
    return games


def cost_games(games: list[((int, int), (int, int), (int, int))]) -> int:
    return functools.reduce(lambda cost, game: cost_game(game) + cost, games, 0)


# prize_x = button_a_x * a_presses + button_b_x * b_presses
# prize_y = button_a_y * a_presses + button_b_y * b_presses

# a_presses = (prize_x - button_b_x * b_presses) / button_a_x
# a_presses = (prize_y - button_b_y * b_presses) / button_a_y


# (prize_y - button_b_y * b_presses) / button_a_y = (prize_x - button_b_x * b_presses) / button_a_x
# (prize_y - button_b_y * b_presses) = ((prize_x - button_b_x * b_presses) / button_a_x) * button_a_y
# b_presses = (prize_x * button_a_y - prize_y * button_a_x) / (-button_b_y * button_a_x + button_b_x * button_a_y)
def cost_game(game: ((int, int), (int, int), (int, int))) -> int:
    button_a_x = game[0][0]
    button_a_y = game[0][1]
    button_b_x = game[1][0]
    button_b_y = game[1][1]
    prize_x = game[2][0]
    prize_y = game[2][1]

    b_presses = (prize_x * button_a_y - prize_y * button_a_x) / (
        -button_b_y * button_a_x + button_b_x * button_a_y
    )
    a_presses = (prize_x - b_presses * button_b_x) / button_a_x

    if not b_presses.is_integer() or not a_presses.is_integer():
        return 0

    return int(a_presses * 3 + b_presses)


def part2(lines: list[str]) -> int:
    games = map(
        lambda game: (
            (game[0][0], game[0][1]),
            (game[1][0], game[1][1]),
            (game[2][0] + 10000000000000, game[2][1] + 10000000000000),
        ),
        parse_games(lines),
    )
    return cost_games(games)
