import sys
import functools


def part1(lines: list[str]) -> int:
    lines = list(filter(lambda line: "#" in line, lines))
    start = find_start(lines)
    end = find_end(lines)
    visited_nodes = shortest_path_for_all_nodes(lines, start)
    return find_lowest_score_at_end_node(visited_nodes, end)


def find_start(lines: list[str]) -> (int, int):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "S":
                return (x, y, "east")


def find_end(lines: list[str]) -> (int, int):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "E":
                return (x, y)


def generate_nodes(lines: list[str]) -> dict[(int, list[(int, int, str)])]:
    nodes = dict()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != "#":
                nodes[str((x, y, "east"))] = (None, [])
                nodes[str((x, y, "west"))] = (None, [])
                nodes[str((x, y, "north"))] = (None, [])
                nodes[str((x, y, "south"))] = (None, [])
    return nodes


def shortest_path_for_all_nodes(
    lines: list[str], start: (int, int, str)
) -> dict[(int, list[(int, int, str)])]:
    unvisited_nodes: dict[(int, list[(int, int, str)])] = generate_nodes(lines)
    unvisited_nodes[str(start)] = (0, [start])
    visited_nodes: dict[(int, list[(int, int, str)])] = dict()

    current_node = find_node_with_shortest_path(unvisited_nodes)
    while len(unvisited_nodes) > 0 and current_node is not None:
        current_node = node_from_string(current_node)
        (current_node_path_length, current_seen_nodes) = unvisited_nodes.pop(
            str(current_node)
        )
        current_node_x = current_node[0]
        current_node_y = current_node[1]
        current_node_face = current_node[2]
        visited_nodes[current_node] = (
            current_node_path_length,
            current_seen_nodes,
        )

        west_node = (current_node_x - 1, current_node_y, "west")
        east_node = (current_node_x + 1, current_node_y, "east")
        north_node = (current_node_x, current_node_y - 1, "north")
        south_node = (current_node_x, current_node_y + 1, "south")

        # go west
        if str(west_node) in unvisited_nodes:
            current_west_cost = (
                1 + turn_west_score(current_node_face) + current_node_path_length
            )
            best_west_cost, west_seen_nodes = unvisited_nodes[str(west_node)]
            if best_west_cost is None or best_west_cost > current_west_cost:
                unvisited_nodes[str(west_node)] = (
                    current_west_cost,
                    current_seen_nodes + [current_node],
                )
            elif best_west_cost == current_west_cost:
                unvisited_nodes[str(west_node)] = (
                    current_west_cost,
                    west_seen_nodes + current_seen_nodes + [current_node],
                )
        # go east
        if str(east_node) in unvisited_nodes:
            current_east_cost = (
                1 + turn_east_score(current_node_face) + current_node_path_length
            )
            best_east_cost, east_seen_nodes = unvisited_nodes[str(east_node)]
            if best_east_cost is None or best_east_cost > current_east_cost:
                unvisited_nodes[str(east_node)] = (
                    current_east_cost,
                    current_seen_nodes + [current_node],
                )
            elif best_east_cost == current_east_cost:
                unvisited_nodes[str(east_node)] = (
                    current_east_cost,
                    east_seen_nodes + current_seen_nodes + [current_node],
                )
        # go north
        if str(north_node) in unvisited_nodes:
            current_north_cost = (
                1 + turn_north_score(current_node_face) + current_node_path_length
            )
            best_north_cost, north_seen_nodes = unvisited_nodes[str(north_node)]
            if best_north_cost is None or best_north_cost > current_north_cost:
                unvisited_nodes[str(north_node)] = (
                    current_north_cost,
                    current_seen_nodes + [current_node],
                )
            elif best_north_cost == current_north_cost:
                unvisited_nodes[str(north_node)] = (
                    current_north_cost,
                    north_seen_nodes + current_seen_nodes + [current_node],
                )
        # go south
        if str(south_node) in unvisited_nodes:
            current_south_cost = (
                1 + turn_south_score(current_node_face) + current_node_path_length
            )
            best_south_cost, south_seen_nodes = unvisited_nodes[str(south_node)]
            if best_south_cost is None or best_south_cost > current_south_cost:
                unvisited_nodes[str(south_node)] = (
                    current_south_cost,
                    current_seen_nodes + [current_node],
                )
            elif best_south_cost == current_south_cost:
                unvisited_nodes[str(south_node)] = (
                    current_south_cost,
                    south_seen_nodes + current_seen_nodes + [current_node],
                )

        # explore the next node
        current_node = find_node_with_shortest_path(unvisited_nodes)

    return visited_nodes


def find_node_with_shortest_path(
    unvisited_nodes: dict[(int, list[(int, int, str)])],
) -> str:
    node_with_shortest_path = None
    shortest_path = None
    for node, (path_length, nodes_in_path) in unvisited_nodes.items():
        if path_length is None:
            continue

        if shortest_path is None or shortest_path > path_length:
            node_with_shortest_path = node
            shortest_path = path_length

    return node_with_shortest_path


def node_from_string(node: str) -> (int, int, str):
    node = node.replace("(", "").replace(")", "").replace("'", "")
    return (int(node.split(", ")[0]), int(node.split(", ")[1]), node.split(", ")[2])


def turn_east_score(face: str) -> int:
    if face == "east":
        return 0
    if face == "west":
        return 2000
    if face == "north":
        return 1000
    if face == "south":
        return 1000


def turn_west_score(face: str) -> int:
    if face == "east":
        return 2000
    if face == "west":
        return 0
    if face == "north":
        return 1000
    if face == "south":
        return 1000


def turn_north_score(face: str) -> int:
    if face == "east":
        return 1000
    if face == "west":
        return 1000
    if face == "north":
        return 0
    if face == "south":
        return 2000


def turn_south_score(face: str) -> int:
    if face == "east":
        return 1000
    if face == "west":
        return 1000
    if face == "north":
        return 2000
    if face == "south":
        return 0


def find_lowest_score_at_end_node(
    visited_nodes: dict[(int, list[(int, int, str)])], end_node: (int, int)
) -> int:
    lowest_score_at_end_node = None
    end_node_east = (end_node[0], end_node[1], "east")
    end_node_west = (end_node[0], end_node[1], "west")
    end_node_north = (end_node[0], end_node[1], "north")
    end_node_south = (end_node[0], end_node[1], "south")
    if end_node_east in visited_nodes:
        east_score, east_nodes = visited_nodes[end_node_east]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > east_score:
            lowest_score_at_end_node = east_score
    if end_node_west in visited_nodes:
        west_score, west_nodes = visited_nodes[end_node_west]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > west_score:
            lowest_score_at_end_node = west_score
    if end_node_north in visited_nodes:
        north_score, north_nodes = visited_nodes[end_node_north]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > north_score:
            lowest_score_at_end_node = north_score
    if end_node_south in visited_nodes:
        south_score, south_nodes = visited_nodes[end_node_south]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > south_score:
            lowest_score_at_end_node = south_score

    return lowest_score_at_end_node


def part2(lines: list[str]) -> int:
    lines = list(filter(lambda line: "#" in line, lines))
    start = find_start(lines)
    end = find_end(lines)
    visited_nodes = shortest_path_for_all_nodes(lines, start)
    return find_nodes_seen_at_end_node(visited_nodes, end)


def find_nodes_seen_at_end_node(
    visited_nodes: dict[(int, list[(int, int, str)])], end_node: (int, int)
) -> int:
    lowest_score_at_end_node = None
    nodes_seen_at_end_node = []
    end_node_east = (end_node[0], end_node[1], "east")
    end_node_west = (end_node[0], end_node[1], "west")
    end_node_north = (end_node[0], end_node[1], "north")
    end_node_south = (end_node[0], end_node[1], "south")
    if end_node_east in visited_nodes:
        east_score, east_nodes = visited_nodes[end_node_east]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > east_score:
            lowest_score_at_end_node = east_score
            nodes_seen_at_end_node = east_nodes
    if end_node_west in visited_nodes:
        west_score, west_nodes = visited_nodes[end_node_west]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > west_score:
            lowest_score_at_end_node = west_score
            nodes_seen_at_end_node = west_nodes
    if end_node_north in visited_nodes:
        north_score, north_nodes = visited_nodes[end_node_north]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > north_score:
            lowest_score_at_end_node = north_score
            nodes_seen_at_end_node = north_nodes
    if end_node_south in visited_nodes:
        south_score, south_nodes = visited_nodes[end_node_south]
        if lowest_score_at_end_node is None or lowest_score_at_end_node > south_score:
            lowest_score_at_end_node = south_score
            nodes_seen_at_end_node = south_nodes

    unique_nodes = set(map(lambda node: (node[0], node[1]), nodes_seen_at_end_node))
    print(sorted(unique_nodes))
    return len(unique_nodes) + 1
