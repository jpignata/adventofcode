import sys


def count(row, *, rows=40):
    count = 0

    for row in generate(row, rows):
        count += row.count(True)

    return count


def generate(row, rows):
    width = len(row)
    last = width - 1

    for _ in range(rows):
        next_row = []

        for i in range(width):
            left = True if i == 0 else row[i - 1]
            right = True if i == last else row[i + 1]
            next_row.append(left == right)

        yield row

        row = next_row


row = [c == '.' for c in sys.stdin.readline().strip()]

print('Part 1:', count(row))
print('Part 2:', count(row, rows=400000))
