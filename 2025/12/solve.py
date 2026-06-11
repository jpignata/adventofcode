import sys
from functools import cache


def normalize(cells):
    min_x = min(x for x, _ in cells)
    min_y = min(y for _, y in cells)

    return tuple(sorted((x - min_x, y - min_y) for x, y in cells))


def orientations(cells):
    variants = set()

    for x_sign, y_sign, swap in (
        (1, 1, False),
        (1, -1, False),
        (-1, 1, False),
        (-1, -1, False),
        (1, 1, True),
        (1, -1, True),
        (-1, 1, True),
        (-1, -1, True),
    ):
        transformed = []

        for x, y in cells:
            if swap:
                x, y = y, x

            transformed.append((x * x_sign, y * y_sign))

        variants.add(normalize(transformed))

    return tuple(variants)


def parse(lines):
    shapes = []
    regions = []
    current = []

    for line in lines:
        line = line.strip()

        if not line:
            if current:
                shapes.append(tuple(current))
                current = []
            continue

        if line.endswith(":") and line[:-1].isdigit():
            if current:
                shapes.append(tuple(current))
                current = []
            continue

        if "#" in line or "." in line:
            current.append(line)
            continue

        if current:
            shapes.append(tuple(current))
            current = []

        size, counts = line.split(": ")
        width, height = map(int, size.split("x"))
        regions.append((width, height, tuple(map(int, counts.split()))))

    if current:
        shapes.append(tuple(current))

    return shapes, regions


def shape_cells(shape):
    return tuple(
        (x, y)
        for y, row in enumerate(shape)
        for x, cell in enumerate(row)
        if cell == "#"
    )


def placement_masks(shape, width, height):
    masks = []

    for orientation in orientations(shape):
        shape_width = max(x for x, _ in orientation) + 1
        shape_height = max(y for _, y in orientation) + 1

        if shape_width > width or shape_height > height:
            continue

        for y_offset in range(height - shape_height + 1):
            for x_offset in range(width - shape_width + 1):
                mask = 0

                for x, y in orientation:
                    mask |= 1 << ((y + y_offset) * width + x + x_offset)

                masks.append(mask)

    return tuple(sorted(set(masks)))


def fits(shapes, width, height, counts):
    if sum(len(shapes[index]) * count for index, count in enumerate(counts)) > width * height:
        return False

    if (width // 3) * (height // 3) >= sum(counts):
        return True

    placements = tuple(
        placement_masks(shape, width, height)
        for shape in shapes
    )

    @cache
    def search(occupied, remaining):
        if not any(remaining):
            return True

        candidates = []

        for index, count in enumerate(remaining):
            if not count:
                continue

            available = tuple(mask for mask in placements[index] if not occupied & mask)

            if not available:
                return False

            candidates.append((len(available), index, available))

        _, index, available = min(candidates)
        next_remaining = list(remaining)
        next_remaining[index] -= 1
        next_remaining = tuple(next_remaining)

        return any(
            search(occupied | mask, next_remaining)
            for mask in available
        )

    return search(0, counts)


def main():
    raw_shapes, regions = parse(sys.stdin)
    shapes = tuple(shape_cells(shape) for shape in raw_shapes)

    print(
        "Part 1:",
        sum(fits(shapes, width, height, counts) for width, height, counts in regions),
    )


if __name__ == "__main__":
    main()
