import sys


def calculate(spec, lo, hi):
    mid = (hi - lo) // 2

    if lo == hi:
        return lo
    elif spec[0] in ('F', 'L'):
        return calculate(spec[1:], lo, lo + mid)
    elif spec[0] in ('B', 'R'):
        return calculate(spec[1:], lo + mid + 1, hi)


def find(seats):
    prev = seats[0]

    for seat in seats[1:]:
        if seat - prev == 2:
            return seat - 1

        prev = seat


seats = sorted(calculate(line[:-4], 0, 127) * 8 + calculate(line[-4:-1], 0, 7)
               for line in sys.stdin.readlines())

print('Part 1:', max(seats))
print('Part 2:', find(seats))
