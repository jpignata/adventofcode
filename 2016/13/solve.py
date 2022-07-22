import operator
from collections import deque


def search(*, target=None, count=0):
    q = deque([(1, 1)])
    costs = {(1, 1): 0}

    while q:
        location = q.popleft()

        for delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor = tuple(map(operator.add, location, delta))
            cost = costs[location] + 1

            if neighbor == target:
                return cost

            if neighbor not in costs and isopen(neighbor):
                costs[neighbor] = cost
                q.append(neighbor)

    return len(list(filter(lambda c: c <= count, costs.values())))


def isopen(location):
    x, y = location
    num = x * x + 3 * x + 2 * x * y + y + y * y + 1358

    return x >= 0 and y >= 0 and bin(num).count("1") % 2 == 0


print("Part 1:", search(target=(31, 39)))
print("Part 2:", search(count=50))
