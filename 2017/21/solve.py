import sys
import numpy as np


def count(grid, rules, iters):
    for _ in range(iters):
        jump = 2 if len(grid) % 2 == 0 else 3
        rows = list()

        for i in range(0, len(grid), jump):
            row = list()

            for j in range(0, len(grid), jump):
                part = grid[i : i + jump, j : j + jump]
                row.append(rules[part.tobytes()])

            rows.append(row)

        grid = np.bmat(rows)

    return np.count_nonzero(grid)


grid = np.mat([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
rules = dict()

for line in sys.stdin:
    pattern_expr, result_expr = line.strip().split(" => ")
    pattern_parts = pattern_expr.split("/")
    result_parts = result_expr.split("/")

    pattern = np.array(
        [list(map(lambda c: 1 if c == "#" else 0, g)) for g in pattern_parts]
    )
    result = np.array(
        [list(map(lambda c: 1 if c == "#" else 0, g)) for g in result_parts]
    )

    for _ in range(4):
        pattern = np.rot90(pattern)
        rules[pattern.tobytes()] = result
        rules[np.fliplr(pattern).tobytes()] = result

print("Part 1:", count(grid, rules, 5))
print("Part 2:", count(grid, rules, 18))
