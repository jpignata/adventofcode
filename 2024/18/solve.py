import sys
from heapq import heappop, heappush
from re import findall


def find(visited):
    h = [(0, 0, 0)]

    while h:
        t, x, y = heappop(h)

        if (x, y) == (maxx, maxy):
            return t

        if (x, y) in visited:
            continue

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= (nx := x + dx) <= maxx and 0 <= (ny := y + dy) <= maxy:
                heappush(h, (t + 1, nx, ny))

        visited.add((x, y))

    return -1


dropped = 1024
bytes_ = [tuple(map(int, findall(r"\d+", line))) for line in sys.stdin]
maxx, maxy = max(x for x, y in bytes_), max(y for x, y in bytes_)
lo, hi = dropped, len(bytes_)

while lo < hi:
    mid = (lo + hi) // 2

    if find(set(bytes_[:mid])) == -1:
        hi = mid
    else:
        lo = mid + 1

print("Part 1:", find(set(bytes_[:dropped])))
print("Part 2:", ",".join(map(str, bytes_[mid - 1])))
