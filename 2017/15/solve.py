def gen(start, factor, multiple=0):
    current = start

    while True:
        current *= factor
        current %= 2147483647

        if multiple > 0 and current % multiple != 0:
            continue

        yield current


def count(start, pairs, multiples=(0, 0)):
    a = gen(start[0], 16807, multiples[0])
    b = gen(start[1], 48271, multiples[1])
    total = 0

    for _ in range(pairs):
        total += next(a) & 0xFFFF == next(b) & 0xFFFF

    return total


print('Part 1:', count((679, 771), 40_000_000))
print('Part 2:', count((679, 771), 5_000_000, (4, 8)))
