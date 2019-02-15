import sys
import operator


def order(steps):
    done = list()

    while len(done) != len(steps):
        for step, requirements in sorted(steps.items()):
            if step not in done and all(r in done for r in requirements):
                done.append(step)

    return ''.join(done)


def run(steps, worker_count=5):
    workers = [(None, None) for _ in range(worker_count)]
    clock = 0
    done = list()

    while len(done) != len(steps):
        for worker, (current, started) in enumerate(workers):
            if current:
                if started + (ord(current) - 64) + 60 == clock:
                    done.append(current)
                    workers[worker] = (None, None)
                else:
                    continue

            for step, requirements in sorted(steps.items()):
                if (step not in done and
                        step not in map(operator.itemgetter(0), workers) and
                        all(r in done for r in requirements)):
                    workers[worker] = (step, clock)

            if not any(map(operator.itemgetter(0), workers)):
                return clock

        clock += 1


steps = dict()

for line in sys.stdin:
    tokens = line.split(' ')
    requirement, step = tokens[1], tokens[7]

    if step not in steps:
        steps[step] = list()

    if requirement not in steps:
        steps[requirement] = list()

    steps[step].append(requirement)

print('Part 1:', order(steps))
print('Part 2:', run(steps))
