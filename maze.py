from numpy.random import shuffle
import numpy as np


def generate(width=31, height=31):
    if width < 5:
        raise Exception('Maze width must be >= 5')

    if width % 2 == 0:
        raise Exception('Maze weight must be odd')

    if height < 5:
        raise Exception('Maze height must be >= 5')

    if height % 2 == 0:
        raise Exception('Maze height must be odd')

    grid = np.full((height, width), True, dtype=bool)

    forest = []
    for row in range(1, height - 1, 2):
        for col in range(1, width - 1, 2):
            forest.append([(row, col)])
            grid[row][col] = False

    edges = []
    for row in range(2, height - 1, 2):
        for col in range(1, width - 1, 2):
            edges.append((row, col))

    for row in range(1, height - 1, 2):
        for col in range(2, width - 1, 2):
            edges.append((row, col))

    shuffle(edges)

    while len(forest) > 1:
        ce_row, ce_col = edges[0]
        edges = edges[1:]

        tree1 = -1
        tree2 = -1

        if ce_row % 2 == 0:  # even-numbered row: vertical wall
            tree1 = sum([
                i if (ce_row - 1, ce_col) in j else 0
                for i, j in enumerate(forest)
            ])
            tree2 = sum([
                i if (ce_row + 1, ce_col) in j else 0
                for i, j in enumerate(forest)
            ])
        else:  # odd-numbered row: horizontal wall
            tree1 = sum([
                i if (ce_row, ce_col - 1) in j else 0
                for i, j in enumerate(forest)
            ])
            tree2 = sum([
                i if (ce_row, ce_col + 1) in j else 0
                for i, j in enumerate(forest)
            ])

        if tree1 != tree2:
            new_tree = forest[tree1] + forest[tree2]
            temp1 = list(forest[tree1])
            temp2 = list(forest[tree2])
            forest = [x for x in forest if x != temp1]
            forest = [x for x in forest if x != temp2]
            forest.append(new_tree)
            grid[ce_row][ce_col] = False

    plan = list(grid.reshape(width * height))
    plan[1] = False

    return width, height, plan
