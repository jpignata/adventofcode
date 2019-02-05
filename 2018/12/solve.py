import sys


def parse(lines):
    generation = set()
    rules = []

    for line in lines:
        if 'initial state:' in line:
            initial_state = line.strip().split(': ')[1]

            for i, char in enumerate(initial_state):
                if char == '#':
                    generation.add(i)
        elif '=> #' in line:
            group = list(line.strip().split(' => ')[0])
            rules.append(group)

    return generation, rules


def generate(previous, rules):
    generation = set()

    for i in range(min(previous) - 2, max(previous) + 4):
        group = ['#' if i + delta in previous else '.'
                 for delta in (-2, -1, 0, 1, 2)]

        if group in rules:
            generation.add(i)

    return generation


def total(generation, rules, *, to):
    last = 0
    deltas = [0]

    for i in range(to):
        generation = generate(generation, rules)
        total = sum(generation)

        deltas.append(total - last)

        if len(set(deltas[-3:])) == 1:
            period = i - 3
            frequency = deltas[-1]
            previous = sum(deltas[:-3])

            return ((to - period - 1) * frequency) + previous

        last = total

    return last


generation, rules = parse(sys.stdin.readlines())

print('Part 1:', total(generation, rules, to=20))
print('Part 2:', total(generation, rules, to=50000000000))
