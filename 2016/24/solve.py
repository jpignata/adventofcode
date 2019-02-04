import sys
from itertools import permutations
from collections import defaultdict, deque


def fewest_steps(grid, *, return_home=False):
    distances = defaultdict(dict)
    locations = []
    vertices = dict()

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isdigit():
                locations.append(char)
                vertices[char] = (x, y)

    for start, target in permutations(locations, 2):
        if target not in distances[start]:
            cost = bfs(grid, vertices[start], vertices[target])
            distances[start][target] = cost
            distances[target][start] = cost

    min_distance = float('inf')
    locations.remove('0')

    for path in permutations(locations, len(locations)):
        distance = 0
        prev = '0'

        for location in path:
            distance += distances[prev][location]
            prev = location

        if return_home:
            distance += distances[prev]['0']

        min_distance = min(min_distance, distance)

    return min_distance


def bfs(grid, start, target):
    costs = {start: 0}
    q = deque([start])

    while q:
        x, y = q.popleft()

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            new_cost = costs[(x, y)] + 1

            if (nx, ny) == target:
                return new_cost

            if grid[ny][nx] != '#':
                if (nx, ny) not in costs or costs[(nx, ny)] > new_cost:
                    q.append((nx, ny))
                    costs[(nx, ny)] = new_cost


grid = [list(line.strip()) for line in sys.stdin.readlines()]

print('Part 1:', fewest_steps(grid))
print('Part 2:', fewest_steps(grid, return_home=True))
