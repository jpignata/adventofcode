import sys
from collections import Counter
from itertools import product


def search(word, dirs):
    maxx, maxy = len(grid[0]), len(grid)
    starts = [(x, y) for y in range(maxy) for x in range(maxx) if grid[y][x] == word[0]]
    matches = []

    def dfs(x, y, dir_, path):
        if 0 <= (nx := x + dir_[0]) < maxx and 0 <= (ny := y + dir_[1]) < maxy:
            if grid[ny][nx] == word[1:][len(path) - 1]:
                if grid[ny][nx] == word[-1]:
                    matches.append(path + [(nx, ny)])
                else:
                    dfs(nx, ny, dir_, path + [(nx, ny)])

    for x, y in starts:
        for dir_ in dirs:
            dfs(x, y, dir_, [(x, y)])

    return matches


grid = [list(line.strip()) for line in sys.stdin]
all_dirs = [(x, y) for x, y in product((-1, 0, 1), repeat=2) if x or y]
diagonals = list(product((-1, 1), repeat=2))
part1 = len(search("XMAS", all_dirs))
part2 = sum(c == 2 for c in Counter(m[1] for m in search("MAS", diagonals)).values())

print("Part 1:", part1)
print("Part 2:", part2)
