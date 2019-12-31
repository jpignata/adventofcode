import sys
from heapq import heappush, heappop
from operator import add
from string import ascii_lowercase, ascii_uppercase
from itertools import product, cycle


def find(grid, robot, keys, target):
    heap = [[0, 0, robot, keys]]
    seen = set()

    while heap:
        steps, _, position, keys = heappop(heap)

        yield(steps, position, keys)

        for direction in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = tuple(map(add, position, direction))
            cell = grid[ny][nx]
            is_in_bounds = 0 <= nx < len(grid[0]) and 0 <= ny < len(grid)
            is_passage = cell in ascii_lowercase or cell == '.'
            is_open_door = cell in ascii_uppercase and cell.lower() in keys
            was_seen = ((nx, ny), frozenset(keys)) in seen

            if is_in_bounds and (is_passage or is_open_door) and not was_seen:
                next_keys = keys.copy()

                if cell in ascii_lowercase:
                    next_keys.add(cell)

                heappush(heap, [steps + 1, target - len(next_keys), (nx, ny),
                                next_keys])

                seen.add(((nx, ny), frozenset(next_keys)))


grid = list()
robots = list()
target = 0
start = (-1, -1)

for y, line in enumerate(sys.stdin):
    row = list()

    for x, char in enumerate(line.strip()):
        if char in ascii_lowercase:
            target += 1
        elif char == '@':
            start = (x, y)
            char = '.'

        row.append(char)

    grid.append(row)

for steps, _, keys in find(grid, start, set(), target):
    if len(keys) == target:
        print('Part 1:', steps)
        break

for delta in product((0, 1, -1), repeat=2):
    nx, ny = tuple(map(add, start, delta))

    if all(abs(c) == 1 for c in delta):
        grid[ny][nx] = '.'
        robots.append((nx, ny))
    else:
        grid[ny][nx] = '#'

steps = 0
keys = set()

for i in cycle(range(len(robots))):
    results = list()

    for nsteps, nposition, nkeys in find(grid, robots[i], keys.copy(), target):
        results.append((target - len(nkeys), nsteps, nposition, nkeys))

    _, wsteps, wposition, wkeys = min(results)

    if len(wkeys) > len(keys):
        keys = wkeys
        steps += wsteps
        robots[i] = wposition

    if len(keys) == target:
        print('Part 2:', steps)
        break
