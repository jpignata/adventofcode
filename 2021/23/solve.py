import sys
from collections import defaultdict
from copy import deepcopy
from heapq import heappush, heappop
from math import inf
from string import ascii_uppercase


def freeze(grid):
    return ''.join(''.join(row) for row in grid)


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def heuristic(grid):
    score = 0

    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            if space in ascii_uppercase:
                room = rooms[ord(space) - 65]
                spaces = [row[room] for row in grid
                          if row[room] in ascii_uppercase]

                if y == 1 and x != room:
                    score += distance((x, y), (room, 1))
                elif y != 1 and (x != room or len(set(spaces)) > 1):
                    score += distance((x, y), (room, 1)) + 1

    return score


def moves(grid, x, y):
    valid = (1, 2, 4, 6, 8, 10, 11)
    cost = energy[ord(grid[y][x]) - 65]
    destination = rooms[ord(grid[y][x]) - 65]

    if x == destination and y == 3:
        return
    elif x == destination and y == 2 and grid[3][x] == grid[y][x]:
        return

    if y == 1:
        for dx in (1, -1):
            nx = x

            while grid[y][nx + dx] == '.':
                if nx + dx == destination:
                    room = [grid[ny][nx + dx] for ny in range(y, len(grid))
                            if grid[ny][nx + dx] in ascii_uppercase]

                    if all(space == grid[y][x] for space in room) or not room:
                        ny = len(grid) - len(room) - 2
                        next_grid = deepcopy(grid)
                        next_grid[ny][nx + dx] = grid[y][x]
                        next_grid[y][x] = '.'

                        yield distance((x, y), (nx + dx, ny)) * cost, next_grid

                nx += dx
    else:
        ny = y

        while grid[ny - 1][x] == '.':
            ny -= 1

        if ny == 1:
            nx = x

            for dx in (1, -1):
                while grid[ny][nx + dx] == '.':
                    if nx + dx in valid:
                        next_grid = deepcopy(grid)
                        next_grid[ny][nx + dx] = grid[y][x]
                        next_grid[y][x] = '.'

                        yield distance((x, y), (nx + dx, ny)) * cost, next_grid

                    nx += dx


def search(grid):
    visited = defaultdict(lambda: inf)
    visited[freeze(grid)] = 0
    q = [(0, 0, grid)]

    while q:
        _, total, grid = heappop(q)
        visited[freeze(grid)] = total

        for i, amphipod in enumerate(amphipods):
            if grid[2][rooms[i]] != amphipod or grid[3][rooms[i]] != amphipod:
                break
        else:
            return total

        for y, row in enumerate(grid):
            for x, space in enumerate(row):
                if space in ascii_uppercase:
                    for cost, next_grid in moves(grid, x, y):
                        if total + cost < visited[freeze(next_grid)]:
                            score = heuristic(next_grid)
                            heappush(q, (score, total + cost, next_grid))


grid = [[c for c in line.rstrip()] for line in sys.stdin]
second_grid = deepcopy(grid)
second_grid.insert(3, list('  #D#B#A#C#'))
second_grid.insert(3, list('  #D#C#B#A#'))
amphipods = ('A', 'B', 'C', 'D')
energy = [1, 10, 100, 1000]
rooms = (3, 5, 7, 9)

print('Part 1:', search(grid))
print('Part 2:', search(second_grid))
