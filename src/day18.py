import sys


def part1(lines: list[str], bytes: int, grid_length: int) -> int:
    early_bytes = [
        (int(lines[i].split(",")[0]), int(lines[i].split(",")[1])) for i in range(bytes)
    ]
    return to_exit_steps(early_bytes, grid_length, (0, 0), (grid_length, grid_length))


def to_exit_steps(
    early_bytes: list[(int, int)], grid_length: int, start: (int, int), end: (int, int)
) -> int:
    unvisted: dict[(int, int), int] = find_available_nodes(early_bytes, grid_length)
    unvisted[str(start)] = ((0, 0), 0)
    visited: dict[(int, int), int] = dict()

    current_node = find_node_with_shortest_path(unvisted)
    while len(unvisted) > 0 and current_node is not None:
        node_coords, path_length = unvisted[str(current_node)]
        visited[str(current_node)] = (node_coords, path_length)
        unvisted.pop(current_node)

        west_node = (node_coords[0] + 1, node_coords[1])
        east_node = (node_coords[0] - 1, node_coords[1])
        south_node = (node_coords[0], node_coords[1] + 1)
        north_node = (node_coords[0], node_coords[1] - 1)

        if str(west_node) in unvisted:
            unvisted[str(west_node)] = (west_node, path_length + 1)
        if str(east_node) in unvisted:
            unvisted[str(east_node)] = (east_node, path_length + 1)
        if str(south_node) in unvisted:
            unvisted[str(south_node)] = (south_node, path_length + 1)
        if str(north_node) in unvisted:
            unvisted[str(north_node)] = (north_node, path_length + 1)

        current_node = find_node_with_shortest_path(unvisted)

    return visited[str(end)][1]


def find_available_nodes(
    early_bytes: list[(int, int)], grid_length: int
) -> dict[(int, int), int]:
    nodes: dict[(int, int), int] = dict()

    for x in range(grid_length + 1):
        for y in range(grid_length + 1):
            node = (x, y)
            if node not in early_bytes:
                nodes[str(node)] = ((x, y), None)

    return nodes


def find_node_with_shortest_path(unvisted: dict[(int, int), int]):
    node_with_shortest_path = None
    shortest_path = None

    for node_key in unvisted.keys():
        node_coords, path_length = unvisted[node_key]
        if path_length is not None:
            if shortest_path is None or path_length < shortest_path:
                node_with_shortest_path = node_key
                shortest_path = path_length

    return node_with_shortest_path


def part2(lines: list[str], grid_length: int) -> str:
    lines = list(filter(lambda line: line != "", lines))
    bytes_seen = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]
    previous_byte = None
    for byte in reversed(bytes_seen):
        print(len(bytes_seen))
        try:
            to_exit_steps(bytes_seen, grid_length, (0, 0), (grid_length, grid_length))
            return f"{previous_byte[0]},{previous_byte[1]}"
        except KeyError:
            previous_byte = byte
            bytes_seen.remove(byte)

    return ""
