import sys


def solve():
    buffer = sys.stdin.readline().strip()

    print("Part 1:", marker(buffer, 4))
    print("Part 2:", marker(buffer, 14))


def marker(buffer, window):
    for i in range(len(buffer) - window):
        if len(set(buffer[i : i + window])) == window:
            return i + window

    return -1


if __name__ == "__main__":
    solve()
