import numpy as np
from matplotlib import pyplot as plt

import maze


def build_labyrinth(width, height, plan):
    # Implement the body of the function
    lab = np.zeros((height, width), dtype = 'uint8')
    i = 0
    for x in range(0, height):
        for y in range(0, width):
            if plan[i]:
                lab[x][y] = 1
            else:
                lab[x][y] = 0
            i += 1
    lab[0][1] = 2
    lab[-2][-2] = 4
    return lab


'''
PATH     = 0  # The cell contains a passageway
WALL     = 1  # The cell contains a wall
THESEUS  = 2  # Theseus is in this cell
THREAD   = 3  # The cell contains Ariadne's thread
MINOTAUR = 4  # The Minotaur is in this cell
VISITED  = 5  # Special marker for the cells visited by Theseus'''


def slay(lab, y, x):
    # it should be, if it is unvisited and a path, go left, then right, or middle
    # if all of those are visited or a wall, turn around (pop up the recursive stack)

    # Base case here
    if lab[y][x] == 1 or lab[y][x] == 5:
        return False
    elif lab[y][x] == 4:
        return True
    lab[y][x] = 5

    # Recursive calls here
    if slay(lab, y, x+1):  # to the right
        lab[y][x] = 3
        return True
    elif slay(lab, y+1, x):  # down
        lab[y][x] = 3
        return True
    elif slay(lab, y, x-1):  # to the left
        lab[y][x] = 3
        return True
    elif slay(lab, y-1, x):  # up
        lab[y][x] = 3
        return True
    return False  # Replace this and implement the function


if __name__ == '__main__':
    width, height, plan = maze.generate()
    labyrinth = build_labyrinth(width, height, plan)
    plt.imshow(labyrinth)
    slay(labyrinth, 0, 1)
    plt.imshow(labyrinth)