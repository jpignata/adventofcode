import sys

raw = [(int(start), int(end)) for start, end in
       [line.strip().split('-') for line in sys.stdin.readlines()]]
raw.sort()
disallowed = [raw[0]]
allowed_count = 0

for start, end in raw[1:]:
    previous_start, previous_end = disallowed[-1]

    if start <= previous_end + 1:
        if end > previous_end:
            disallowed.pop()
            disallowed.append((previous_start, end))
    else:
        allowed_count += start - previous_end - 1
        disallowed.append((start, end))

print('Part 1:', disallowed[0][-1] + 1)
print('Part 2:', allowed_count)
