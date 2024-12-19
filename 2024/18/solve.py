import sys
from collections import deque
from re import findall


def find(visited):
    q = deque([(0, 0, 0)])

    while q:
        t, x, y = q.popleft()

        if (x, y) == (maxx, maxy):
            return t

        if (x, y) in visited:
            continue

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= (nx := x + dx) <= maxx and 0 <= (ny := y + dy) <= maxy:
                q.append((t + 1, nx, ny))

        visited.add((x, y))

    return -1


bytes_ = [tuple(map(int, findall(r"\d+", line))) for line in sys.stdin]
dropped = 1024 if len(bytes_) > 1024 else 12
maxx, maxy = max(x for x, _ in bytes_), max(y for _, y in bytes_)
lo, hi = dropped, len(bytes_)

while lo < hi:
    mid = (lo + hi) // 2

    if find(set(bytes_[:mid])) == -1:
        hi = mid
    else:
        lo = mid + 1

print("Part 1:", find(set(bytes_[:dropped])))
print("Part 2:", ",".join(map(str, bytes_[mid - 1])))
