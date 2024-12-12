import sys
import functools


def part1(lines: list[str]) -> int:
    return cost_fences(find_plots(lines))


def find_plots(lines: list[str]) -> list[(int, int)]:
    found_plots = []
    in_plots: list[(int, int)] = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) not in in_plots:
                plots, fences, plot_nodes = grow_plot(x, y, lines, [])
                found_plots.append((plots, fences))
                in_plots = in_plots + plot_nodes
    return found_plots


def grow_plot(x: int, y: int, lines: list[str], in_plot_already: list[(int, int)]):
    print("exploring")
    print(x, y)
    in_plot_already.append((x, y))
    plot_type = lines[y][x]
    size = 1
    fences = 0

    if x - 1 >= 0 and lines[y][x - 1] == plot_type:
        if (x - 1, y) not in in_plot_already:
            extra_size, extra_fences, extra_plots = grow_plot(
                x - 1, y, lines, in_plot_already
            )
            size = size + extra_size
            fences = fences + extra_fences
    else:
        fences = fences + 1

    if x + 1 < len(lines[0]) and lines[y][x + 1] == plot_type:
        if (x + 1, y) not in in_plot_already:
            extra_size, extra_fences, extra_plots = grow_plot(
                x + 1, y, lines, in_plot_already
            )
            size = size + extra_size
            fences = fences + extra_fences
    else:
        fences = fences + 1

    if y - 1 >= 0 and lines[y - 1][x] == plot_type:
        if (x, y - 1) not in in_plot_already:
            extra_size, extra_fences, extra_plots = grow_plot(
                x, y - 1, lines, in_plot_already
            )
            size = size + extra_size
            fences = fences + extra_fences
    else:
        fences = fences + 1

    if y + 1 < len(lines) and lines[y + 1][x] == plot_type:
        if (x, y + 1) not in in_plot_already:
            extra_size, extra_fences, extra_plots = grow_plot(
                x, y + 1, lines, in_plot_already
            )
            size = size + extra_size
            fences = fences + extra_fences
    else:
        fences = fences + 1

    return (size, fences, in_plot_already)


def cost_fences(plots: list[(int, int)]) -> int:
    return functools.reduce(
        lambda total_cost, plot: total_cost + (plot[0] * plot[1]), plots, 0
    )


def part2(lines: list[str]) -> int:
    return cost_discount_fences(find_plot_nodes(lines))


def find_plot_nodes(lines: list[str]) -> list[[(int, int)]]:
    found_plots = []
    in_plots: list[(int, int)] = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) not in in_plots:
                plots, fences, plot_nodes = grow_plot(x, y, lines, [])
                found_plots.append(plot_nodes)
                in_plots = in_plots + plot_nodes
    return found_plots


def cost_discount_fences(plots: list[(int, int)]) -> int:
    return functools.reduce(
        lambda total_cost, plot: total_cost + cost_plot_discount_fences(plot), plots, 0
    )


def cost_plot_discount_fences(plot: list[(int, int)]) -> int:
    return len(plot) * count_vertexes(plot)


def count_vertexes(plot: list[(int, int)]):
    vertexes = []
    for node in plot:
        x = node[0]
        y = node[1]
        # top left vertex check
        if (x - 1, y) not in plot and (x, y - 1) not in plot:
            vertexes.append((x, y))
        elif (x - 1, y) in plot and (x, y - 1) in plot and (x - 1, y - 1) not in plot:
            vertexes.append((x, y))

        # top right vertex check
        if (x + 1, y) not in plot and (x, y - 1) not in plot:
            vertexes.append((x + 1, y))
        elif (x + 1, y) in plot and (x, y - 1) in plot and (x + 1, y - 1) not in plot:
            vertexes.append((x + 1, y))

        # bottom left vertex check
        if (x - 1, y) not in plot and (x, y + 1) not in plot:
            vertexes.append((x, y + 1))
        elif (x - 1, y) in plot and (x, y + 1) in plot and (x - 1, y + 1) not in plot:
            vertexes.append((x, y + 1))

        # bottom right vertex check
        if (x + 1, y) not in plot and (x, y + 1) not in plot:
            vertexes.append((x + 1, y + 1))
        elif (x + 1, y) in plot and (x, y + 1) in plot and (x + 1, y + 1) not in plot:
            vertexes.append((x + 1, y + 1))

    return len(vertexes)
