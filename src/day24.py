import sys


def part1(lines: list[str]) -> int:
    initial_wires = parse_initial_wires(lines)
    gates = parse_gates(lines)
    solved_wires = solve_gates(initial_wires, gates)
    return read_wires(solved_wires, "z")


def parse_initial_wires(lines: list[str]) -> dict[bool]:
    initial_lines = filter(lambda line: ":" in line, lines)
    return dict(
        map(
            lambda line: (line.split(":")[0], line.split(":")[1] == " 1"), initial_lines
        )
    )


def parse_gates(lines: list[str]) -> list[(str, str, str, str)]:
    initial_gates = filter(lambda line: ">" in line, lines)
    return list(map(parse_gate, initial_gates))


def parse_gate(line: str) -> (str, str, str, str):
    parts = line.split(" ")
    input_one = parts[0]
    input_two = parts[2]
    gate_operation = parts[1]
    output = parts[4]
    return (input_one, input_two, gate_operation, output)


def solve_gates(
    initial_wires: dict[bool], gates: list[(str, str, str, str)]
) -> dict[bool]:
    solved_wires = initial_wires
    while len(gates) > 0:
        for gate in gates:
            input_one = gate[0]
            input_two = gate[1]
            gate_operation = gate[2]
            output = gate[3]
            try:
                solved_wires[output] = solve_gate(
                    solved_wires[input_one], solved_wires[input_two], gate_operation
                )
            except KeyError:
                continue
            gates.remove(gate)
    return solved_wires


def solve_gate(input_one: bool, input_two: bool, gate_operation: str) -> bool:
    if gate_operation == "AND":
        return input_one and input_two
    if gate_operation == "OR":
        return input_one or input_two
    if gate_operation == "XOR":
        return input_one ^ input_two


def read_wires(wires: dict[str], wire_type: str) -> int:
    wire_keys = sorted(
        filter(lambda wire_key: wire_type in wire_key, wires.keys()),
        reverse=True,
    )
    wire_bools = list(
        map(
            lambda wire_key: "1" if wires[wire_key] else "0",
            wire_keys,
        )
    )
    decimal_number = "".join(wire_bools)
    return int(decimal_number, base=2)


def part2(lines: list[str], output_swaps: list[(str, str)]) -> int:
    initial_wires = parse_initial_wires(lines)
    gates = swap_gates(parse_gates(lines), output_swaps)
    solved_wires = solve_gates(initial_wires, gates)
    first_number = read_wires(solved_wires, "x")
    second_number = read_wires(solved_wires, "y")
    answer = read_wires(solved_wires, "z")
    print("expected:")
    print(f"{first_number} + {second_number} = {answer}")
    print(
        f"{"{0:b}".format(first_number)} + {"{0:b}".format(second_number)} = {"{0:b}".format(first_number + second_number)}"
    )
    print("calculated:")
    print(
        f"{"{0:b}".format(first_number)} + {"{0:b}".format(second_number)} = {"{0:b}".format(answer)}"
    )
    return first_number + second_number == answer


def swap_gates(
    gates: list[(str, str, str, str)], swaps: list[(str, str)]
) -> list[(str, str, str, str)]:
    swapped_gates = gates[:]

    for swap in swaps:
        swapped_gates = list(map(lambda gate: swap_gate(gate, swap), swapped_gates))

    return swapped_gates


# 1101011111100011011001011001110100101001010010
# 1101100011100011011001011001110100101001010010 - 6 swaps
# 1101100011100101011001011001110100101001010010 - 4 swaps
# 1101100011100101011001011001110101001001010010 - 2 swaps
# 1101100011100101011001011001110101001010010010 - 0 swaps
def swap_gate(gate: (str, str, str, str), swap: (str, str)):
    if gate[3] == swap[0]:
        print(f"swapping: {swap[0]}")
        return (gate[0], gate[1], gate[2], swap[1])
    elif gate[3] == swap[1]:
        print(f"swapping: {swap[1]}")
        return (gate[0], gate[1], gate[2], swap[0])
    return gate
