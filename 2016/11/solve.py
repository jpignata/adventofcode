from collections import namedtuple
from itertools import combinations
import heapq


def hash(floor, floors):
    key = str(floor)

    for floor, items in enumerate(floors):
        types = [item.type for item in items]
        types.sort()
        key += str(floor) + ''.join(types)

    return key


def safe(items):
    generators = filter(lambda i: i.type == 'generator', items)
    generator_elements = set(map(lambda i: i.element, generators))

    if len(generator_elements) == 0:
        return True

    for microchip in filter(lambda i: i.type == 'microchip', items):
        if microchip.element not in generator_elements:
            return False

    return True


def moves(floor, floors):
    for direction in (1, -1):
        next_floor = floor + direction

        if next_floor < 0 or next_floor >= len(floors):
            continue

        items = list(combinations(floors[floor], 1))
        items += list(combinations(floors[floor], 2))

        for i in items:
            yield (next_floor, list(i))


def search(floors):
    total = sum([len(floor) for floor in floors])
    costs = {hash(0, floors): 0}
    q = [(0, 0, 0, floors)]

    while q:
        _, floor, cost, floors = heapq.heappop(q)

        if floor == len(floors) - 1 and len(floors[-1]) == total:
            return cost

        for next_floor, items in moves(floor, floors):
            next_floors = floors.copy()
            next_floors[floor] = [i for i in next_floors[floor]
                                  if i not in items]
            next_floors[next_floor] = next_floors[next_floor].copy() + items
            key = hash(next_floor, next_floors)
            next_cost = cost + 1

            if not safe(next_floors[floor]) or \
               not safe(next_floors[next_floor]):
                continue

            if key not in costs or costs[key] > next_cost:
                costs[key] = next_cost
                weight = (-len(next_floors[-1]), cost)
                heapq.heappush(q, (weight, next_floor, next_cost, next_floors))

        costs[hash(floor, floors)] = cost


item = namedtuple('item', ['type', 'element'])
floors1 = [[item('generator', 'thulium'), item('microchip', 'thulium'),
            item('generator', 'plutonium'), item('generator', 'strontium')],
           [item('microchip', 'plutonium'), item('microchip', 'strontium')],
           [item('generator', 'promethium'), item('microchip', 'promethium'),
            item('generator', 'ruthenium'), item('microchip', 'ruthenium')],
           []]
floors2 = [[item('generator', 'thulium'), item('microchip', 'thulium'),
            item('generator', 'plutonium'), item('generator', 'strontium'),
            item('generator', 'elerium'), item('microchip', 'elerium'),
            item('generator', 'dilithium'), item('microchip', 'dilithium')],
           [item('microchip', 'plutonium'), item('microchip', 'strontium')],
           [item('generator', 'promethium'), item('microchip', 'promethium'),
            item('generator', 'ruthenium'), item('microchip', 'ruthenium')],
           []]

print('Part 1:', search(floors1))
print('Part 2:', search(floors2))
