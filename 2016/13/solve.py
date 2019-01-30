import operator
from collections import deque


def isopen(location):
    x, y = location
    num = x*x + 3*x + 2*x*y + y + y*y + 1358

    return x >= 0 and y >= 0 and bin(num).count('1') % 2 == 0


def search(*, start=(1, 1), target=(5000, 5000), count=0):
    q = deque([start])
    costs = {start: 0}

    while q:
        location = q.popleft()

        for delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor = tuple(map(operator.add, location, delta))
            cost = costs[location] + 1

            if isopen(neighbor):
                if neighbor == target:
                    return cost

                if neighbor not in costs or costs[neighbor] > cost:
                    costs[neighbor] = cost
                    q.append(neighbor)

    return len(list(filter(lambda c: c <= count, costs.values())))


print('Part 1:', search(target=(31, 39)))
print('Part 2:', search(count=50))
