import sys


def marker(buffer, window):
    for i in range(len(buffer) - window):
        if len(set(buffer[i : i + window])) == window:
            return i + window


buffer = sys.stdin.readline().strip()

print("Part 1:", marker(buffer, 4))
print("Part 2:", marker(buffer, 14))
