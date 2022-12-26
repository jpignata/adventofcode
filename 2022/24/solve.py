import sys
from itertools import count


def solve():
    grid = [line.strip()[1:-1] for line in sys.stdin.readlines()[1:-1]]
    begin = 0, -1
    end = len(grid[0]) - 1, len(grid)
    begin_to_end = simulate(grid, begin, end)
    back_to_begin = simulate(grid, end, begin, begin_to_end)
    back_to_end = simulate(grid, begin, end, back_to_begin)

    print("Part 1:", begin_to_end)
    print("Part 2:", back_to_end)


def simulate(grid, begin, end, start=1):
    maxx, maxy = len(grid[0]), len(grid)
    positions = {begin}

    def move_valid(x, y, step):
        if (x, y) in (begin, end):
            return True

        if not (0 <= nx < maxx and 0 <= ny < maxy):
            return False

        return (
            grid[y][(x - step) % maxx] != ">"
            and grid[y][(x + step) % maxx] != "<"
            and grid[(y - step) % maxy][x] != "v"
            and grid[(y + step) % maxy][x] != "^"
        )

    for step in count(start):
        next_positions = set()

        for x, y in positions:
            for dx, dy in ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy

                if (nx, ny) == end:
                    return step

                if move_valid(nx, ny, step):
                    next_positions.add((nx, ny))

        positions = next_positions


if __name__ == "__main__":
    solve()
