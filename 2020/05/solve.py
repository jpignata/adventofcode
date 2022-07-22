import sys


def calculate(spec, lo, hi):
    mid = (hi - lo) // 2

    if lo == hi:
        return lo
    elif spec[0] in "FL":
        return calculate(spec[1:], lo, lo + mid)
    elif spec[0] in "BR":
        return calculate(spec[1:], lo + mid + 1, hi)


seats = {
    calculate(line[:-4], 0, 127) * 8 + calculate(line[-4:-1], 0, 7)
    for line in sys.stdin.readlines()
}

print("Part 1:", max(seats))
print("Part 2:", (set(range(min(seats), max(seats))) - seats).pop())
