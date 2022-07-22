from collections import deque

steps = 343
buffer = deque([0])

for i in range(1, 2018):
    buffer.rotate(-steps - 1)
    buffer.appendleft(i)

num = 0
index = 0

for i in range(1, 50_000_000):
    index = (index + steps) % i

    if index == 0:
        num = i

    index += 1

print("Part 1:", buffer[1])
print("Part 2:", num)
