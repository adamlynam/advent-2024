import sys
import functools


def part1(lines: list[str], robot_pads: int) -> int:
    lines = list(filter(lambda line: line != "", lines))
    return functools.reduce(
        lambda sum, line: sum + score_code(line, robot_pads), lines, 0
    )


def score_code(code: str, robot_pads: int) -> int:
    code_value = int(code.replace("A", ""))
    code_length = enter_code(code, robot_pads)
    return code_value * code_length


def enter_code(code: str, robot_pads: int) -> int:
    inputs = enter_code_on_numeric_pad_bot(code)
    return enter_code_on_bot_pad(inputs, robot_pads)


@functools.cache
def enter_code_on_numeric_pad_bot(code: str) -> str:
    current_numeric_key = "A"
    inputs = ""
    for key in code:
        inputs = inputs + enter_key_on_numeric_pad(key, current_numeric_key)
        current_numeric_key = key
    return inputs


@functools.cache
def enter_code_on_bot_pad(code: str, robot_pads: int) -> int:
    if robot_pads == 0:
        return len(code)

    current_key = "A"
    sum = 0
    for key in code:
        inputs = enter_key_on_directional_pad(key, current_key)
        sum = sum + enter_code_on_bot_pad(inputs, robot_pads - 1)
        current_key = key

    return sum


def enter_key_on_numeric_pad(target_key: str, current_numeric_key: str) -> str:
    if target_key == "0":
        if current_numeric_key == "0":
            return "A"
        elif current_numeric_key == "1":
            return ">vA"
        elif current_numeric_key == "2":
            return "vA"
        elif current_numeric_key == "3":
            return "<vA"
        elif current_numeric_key == "4":
            return ">vvA"
        elif current_numeric_key == "5":
            return "vvA"
        elif current_numeric_key == "6":
            return "<vvA"
        elif current_numeric_key == "7":
            return ">vvvA"
        elif current_numeric_key == "8":
            return "vvvA"
        elif current_numeric_key == "9":
            return "<vvvA"
        elif current_numeric_key == "A":
            return "<A"
    if target_key == "1":
        if current_numeric_key == "0":
            return "^<A"
        elif current_numeric_key == "1":
            return "A"
        elif current_numeric_key == "2":
            return "<A"
        elif current_numeric_key == "3":
            return "<<A"
        elif current_numeric_key == "4":
            return "vA"
        elif current_numeric_key == "5":
            return "<vA"
        elif current_numeric_key == "6":
            return "<<vA"
        elif current_numeric_key == "7":
            return "vvA"
        elif current_numeric_key == "8":
            return "<vvA"
        elif current_numeric_key == "9":
            return "<<vvA"
        elif current_numeric_key == "A":
            return "^<<A"
    if target_key == "2":
        if current_numeric_key == "0":
            return "^A"
        elif current_numeric_key == "1":
            return ">A"
        elif current_numeric_key == "2":
            return "A"
        elif current_numeric_key == "3":
            return "<A"
        elif current_numeric_key == "4":
            return "v>A"
        elif current_numeric_key == "5":
            return "vA"
        elif current_numeric_key == "6":
            return "<vA"
        elif current_numeric_key == "7":
            return "vv>A"
        elif current_numeric_key == "8":
            return "vvA"
        elif current_numeric_key == "9":
            return "<vvA"
        elif current_numeric_key == "A":
            return "<^A"
    if target_key == "3":
        if current_numeric_key == "0":
            return "^>A"
        elif current_numeric_key == "1":
            return ">>A"
        elif current_numeric_key == "2":
            return ">A"
        elif current_numeric_key == "3":
            return "A"
        elif current_numeric_key == "4":
            return "v>>A"
        elif current_numeric_key == "5":
            return "v>A"
        elif current_numeric_key == "6":
            return "vA"
        elif current_numeric_key == "7":
            return "vv>>A"
        elif current_numeric_key == "8":
            return "vv>A"
        elif current_numeric_key == "9":
            return "vvA"
        elif current_numeric_key == "A":
            return "^A"
    if target_key == "4":
        if current_numeric_key == "0":
            return "^^<A"
        elif current_numeric_key == "1":
            return "^A"
        elif current_numeric_key == "2":
            return "<^A"
        elif current_numeric_key == "3":
            return "<<^A"
        elif current_numeric_key == "4":
            return "A"
        elif current_numeric_key == "5":
            return "<A"
        elif current_numeric_key == "6":
            return "<<A"
        elif current_numeric_key == "7":
            return "vA"
        elif current_numeric_key == "8":
            return "<vA"
        elif current_numeric_key == "9":
            return "<<vA"
        elif current_numeric_key == "A":
            return "^^<<A"
    if target_key == "5":
        if current_numeric_key == "0":
            return "^^A"
        elif current_numeric_key == "1":
            return "^>A"
        elif current_numeric_key == "2":
            return "^A"
        elif current_numeric_key == "3":
            return "<^A"
        elif current_numeric_key == "4":
            return ">A"
        elif current_numeric_key == "5":
            return "A"
        elif current_numeric_key == "6":
            return "<A"
        elif current_numeric_key == "7":
            return "v>A"
        elif current_numeric_key == "8":
            return "vA"
        elif current_numeric_key == "9":
            return "<vA"
        elif current_numeric_key == "A":
            return "<^^A"
    if target_key == "6":
        if current_numeric_key == "0":
            return "^^>A"
        elif current_numeric_key == "1":
            return "^>>A"
        elif current_numeric_key == "2":
            return "^>A"
        elif current_numeric_key == "3":
            return "^A"
        elif current_numeric_key == "4":
            return ">>A"
        elif current_numeric_key == "5":
            return ">A"
        elif current_numeric_key == "6":
            return "A"
        elif current_numeric_key == "7":
            return "v>>A"
        elif current_numeric_key == "8":
            return "v>A"
        elif current_numeric_key == "9":
            return "vA"
        elif current_numeric_key == "A":
            return "^^A"
    if target_key == "7":
        if current_numeric_key == "0":
            return "^^^<A"
        elif current_numeric_key == "1":
            return "^^A"
        elif current_numeric_key == "2":
            return "<^^A"
        elif current_numeric_key == "3":
            return "<<^^A"
        elif current_numeric_key == "4":
            return "^A"
        elif current_numeric_key == "5":
            return "<^A"
        elif current_numeric_key == "6":
            return "<<^A"
        elif current_numeric_key == "7":
            return "A"
        elif current_numeric_key == "8":
            return "<A"
        elif current_numeric_key == "9":
            return "<<A"
        elif current_numeric_key == "A":
            return "^^^<<A"
    if target_key == "8":
        if current_numeric_key == "0":
            return "^^^A"
        elif current_numeric_key == "1":
            return "^^>A"
        elif current_numeric_key == "2":
            return "^^A"
        elif current_numeric_key == "3":
            return "<^^A"
        elif current_numeric_key == "4":
            return "^>A"
        elif current_numeric_key == "5":
            return "^A"
        elif current_numeric_key == "6":
            return "<^A"
        elif current_numeric_key == "7":
            return ">A"
        elif current_numeric_key == "8":
            return "A"
        elif current_numeric_key == "9":
            return "<A"
        elif current_numeric_key == "A":
            return "<^^^A"
    if target_key == "9":
        if current_numeric_key == "0":
            return "^^^>A"
        elif current_numeric_key == "1":
            return "^^>>A"
        elif current_numeric_key == "2":
            return "^^>A"
        elif current_numeric_key == "3":
            return "^^A"
        elif current_numeric_key == "4":
            return "^>>A"
        elif current_numeric_key == "5":
            return "^>A"
        elif current_numeric_key == "6":
            return "^A"
        elif current_numeric_key == "7":
            return ">>A"
        elif current_numeric_key == "8":
            return ">A"
        elif current_numeric_key == "9":
            return "A"
        elif current_numeric_key == "A":
            return "^^^A"
    if target_key == "A":
        if current_numeric_key == "0":
            return ">A"
        elif current_numeric_key == "1":
            return ">>vA"
        elif current_numeric_key == "2":
            return "v>A"
        elif current_numeric_key == "3":
            return "vA"
        elif current_numeric_key == "4":
            return ">>vvA"
        elif current_numeric_key == "5":
            return "vv>A"
        elif current_numeric_key == "6":
            return "vvA"
        elif current_numeric_key == "7":
            return ">>vvvA"
        elif current_numeric_key == "8":
            return "vvv>A"
        elif current_numeric_key == "9":
            return "vvvA"
        elif current_numeric_key == "A":
            return "A"


# v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A
#    <   A > A   <   AA  v <   AA >>  ^ A  v  AA ^ A  v <   AAA >  ^ A
#        ^   A       ^^        <<       A     >>   A        vvv      A
#            3                          7          9                 A


# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#    <   A > A  v <<   AA >  ^ AA > A  v  AA ^ A   < v  AAA >  ^ A
#        ^   A         <<      ^^   A     >>   A        vvv      A
#            3                      7          9                 A


# v<<A>>^AvA^Av<A<AA>>^AAvA<^A>AAvA^Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A
#    <   A > A  v <<   AA >  ^ AA > A  v  AA ^ A  v <   AAA >  ^ A
#        ^   A         <<      ^^   A     >>   A        vvv      A
#            3                      7          9                 A


# 3 to 7
# v<<A>>^AAv<A<A>>^AAvAA^<A>
# <vA<AA>>^AAvA<^A>AAvA^A
def enter_key_on_directional_pad(target_key: str, current_key: str) -> str:
    if target_key == "<":
        if current_key == "<":
            return "A"
        elif current_key == "v":
            return "<A"
        elif current_key == ">":
            return "<<A"
        elif current_key == "^":
            return "v<A"
        elif current_key == "A":
            return "v<<A"
    elif target_key == "v":
        if current_key == "<":
            return ">A"
        elif current_key == "v":
            return "A"
        elif current_key == ">":
            return "<A"
        elif current_key == "^":
            return "vA"
        elif current_key == "A":
            return "<vA"
    elif target_key == ">":
        if current_key == "<":
            return ">>A"
        elif current_key == "v":
            return ">A"
        elif current_key == ">":
            return "A"
        elif current_key == "^":
            return "v>A"
        elif current_key == "A":
            return "vA"
    elif target_key == "^":
        if current_key == "<":
            return ">^A"
        elif current_key == "v":
            return "^A"
        elif current_key == ">":
            return "<^A"
        elif current_key == "^":
            return "A"
        elif current_key == "A":
            return "<A"
    elif target_key == "A":
        if current_key == "<":
            return ">>^A"
        elif current_key == "v":
            return "^>A"
        elif current_key == ">":
            return "^A"
        elif current_key == "^":
            return ">A"
        elif current_key == "A":
            return "A"


def part2(lines: list[str]) -> int:
    return part1(lines, 25)
