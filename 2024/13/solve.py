import re
import sys


def calculate(machines, offset=0):
    costs = []

    for (ax, ay), (bx, by), (prizex, prizey) in machines:
        prizex += offset
        prizey += offset
        b = abs(prizex * ay - prizey * ax) / abs(bx * ay - by * ax)
        a = (prizex - bx * b) / ax

        if a == round(a) and b == round(b):
            costs.append(a * 3 + b)

    return int(sum(costs))


def main():
    machines = [[]]

    for line in sys.stdin:
        if line.strip():
            machines[-1].append(tuple(map(int, re.findall(r"\d+", line))))
        else:
            machines.append([])

    print("Part 1:", calculate(machines))
    print("Part 2:", calculate(machines, 10000000000000))


if __name__ == "__main__":
    main()
