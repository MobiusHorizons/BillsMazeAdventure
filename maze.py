# Adapted from code found at http://rosettacode.org/wiki/Maze_generation#Python

from random import shuffle, randrange
def print_config(config):
    print('┌' + ('─' * len(config[0])) + '┐')
    for row in config:
        print('│', end='')
        for cell in row:
            if (cell == 1):
                print('#', end='')
            else:
                print(' ', end='')
        print('│')
    print('└' + ('─' * len(config[0]) * 2) + '┘')
 
def make_maze(w = 16, h = 8):
    visited = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)] 
    # ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    ver = [[[1,0]] * w + [[1]] for _ in range(h)] + [[]]
    # hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    hor = [[[1,1]] * w + [[1]] for _ in range(h + 1)]


    def walk(x, y):
        visited[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if visited[yy][xx]: continue
            if xx == x: 
                hor[max(y, yy)][x] = [1,0]

            if yy == y: 
                ver[y][max(x, xx)] = [0,0]

            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
    config = []
    for (a, b) in zip(hor, ver):
        if len(a) > 0: config.append([item for pair in a for item in pair])
        if len(b) > 0: config.append([item for pair in b for item in pair])

    config[0][1] = 2  # start
    config[-1][-2] = 3 # end
    return config


#main
# maze = Maze(10,10)
# c = maze.config


