import sys

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
points = [3, 57, 1197, 25137]
score = 0
scores = []

for line in sys.stdin:
    s = []

    for char in line.strip():
        if char in closing:
            index = closing.index(char)

            if s.pop() != opening[index]:
                score += points[index]
                break
        else:
            s.append(char)
    else:
        scores.append(0)

        while s:
            scores[-1] *= 5
            scores[-1] += opening.index(s.pop()) + 1

print('Part 1:', score)
print('Part 2:', sorted(scores)[len(scores) // 2])
