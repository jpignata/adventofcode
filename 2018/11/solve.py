import numpy as np


def builder(serial):
    def power_level(y, x):
        rack_id = x + 10
        return ((((y * rack_id) + serial) * rack_id) // 100 % 10) - 5

    def build_grid(y, x):
        return np.array([power_level(y[i], x[i]) for i in range(len(x))])

    return build_grid


def find_largest(index, size):
    largest = 0
    coords = (-1, -1)

    for x in range(0, len(index)):
        if x + size >= len(index):
            continue

        for y in range(0, len(index)):
            if y + size >= len(index):
                continue

            a = index[y, x]
            b = index[y, x+size]
            c = index[y+size, x]
            d = index[y+size, x+size]
            area = d - b - c + a
            largest = max(largest, area)

            if area == largest:
                coords = (x + 1, y + 1)

    return coords, largest


def find_largest_square(index):
    largest = 0
    largest_coords = (-1, -1)
    largest_size = 0

    for size in range(len(index)):
        coords, value = find_largest(index, size)
        largest = max(largest, value)

        if value == largest:
            largest_size = size
            largest_coords = coords

    return ','.join(map(str, largest_coords + (largest_size,)))


grid = np.fromfunction(builder(7347), shape=(300, 300))
index = grid.cumsum(axis=0).cumsum(axis=1)

print('Part 1:', ','.join(map(str, find_largest(index, 3)[0])))
print('Part 2:', find_largest_square(index))
