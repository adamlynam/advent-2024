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


def cost_game(game: ((int, int), (int, int), (int, int))) -> int:
    button_a_x = game[0][0]
    button_a_y = game[0][1]
    button_b_x = game[1][0]
    button_b_y = game[1][1]
    prize_x = game[2][0]
    prize_y = game[2][1]

    a_presses = 0
    b_presses = math.floor(prize_x / button_b_x)
    best_price = None
    while b_presses >= 0:
        # print(b_presses)
        while a_presses * button_a_x + b_presses * button_b_x < prize_x:
            a_presses = a_presses + 1
        if (
            a_presses * button_a_x + b_presses * button_b_x == prize_x
            and a_presses * button_a_y + b_presses * button_b_y == prize_y
        ):
            best_price = a_presses * 3 + b_presses
        b_presses = b_presses - 1

    return 0 if best_price is None else best_price


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
