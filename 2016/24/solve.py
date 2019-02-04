import sys
from itertools import permutations
from collections import defaultdict, deque


def fewest_steps(grid, *, return_home=False):
    distances = defaultdict(dict)

    for start_location, end_location in permutations(find_locations(grid), 2):
        if end_location not in distances[start_location]:
            cost = bfs(grid, start_location, end_location)
            distances[start_location][end_location] = cost
            distances[end_location][start_location] = cost

    min_distance = float('inf')
    first = min(distances['0'])
    distance = distances['0'][first]

    locations = find_locations(grid)
    locations.remove('0')
    locations.remove(first)

    for path in permutations(locations, len(locations)):
        new_distance = distance
        next = first

        for loc in path:
            new_distance += distances[next][loc]
            next = loc

        if return_home:
            new_distance += distances[next]['0']

        min_distance = min(min_distance, new_distance)

    return min_distance


def find_locations(grid):
    locations = []

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isdigit():
                locations.append(char)

    return locations


def bfs(grid, start_location, end_location):
    start = find_location(grid, start_location)
    target = find_location(grid, end_location)
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


def find_location(grid, location):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == location:
                return (x, y)


grid = [list(line.strip()) for line in sys.stdin.readlines()]

print('Part 1:', fewest_steps(grid))
print('Part 2:', fewest_steps(grid, return_home=True))
