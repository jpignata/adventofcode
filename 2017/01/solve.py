import sys

digits = list(map(int, list(sys.stdin.readline().strip())))
total_next = 0
total_middle = 0

for i, digit in enumerate(digits):
    if digit == digits[(i + 1) % len(digits)]:
        total_next += digit

    if digit == digits[(i + len(digits) // 2) % len(digits)]:
        total_middle += digit

print("Part 1:", total_next)
print("Part 2:", total_middle)
