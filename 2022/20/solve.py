import sys
from collections import deque


def solve():
    numbers = [int(number.strip()) for number in sys.stdin]

    print("Part 1:", sum(coordinates(decrypt(numbers))))
    print("Part 2:", sum(coordinates(decrypt(numbers, key=811589153, times=10))))


def decrypt(numbers, *, key=1, times=1):
    wheel = deque((i, number * key) for i, number in enumerate(numbers))

    for _ in range(times):
        for i in range(len(wheel)):
            while i != wheel[0][0]:
                wheel.rotate(-1)

            _, number = wheel.popleft()
            wheel.rotate(number * -1)
            wheel.appendleft((i, number))
            wheel.rotate(number)

    return [number for _, number in wheel]


def coordinates(numbers):
    return [numbers[(numbers.index(0) + i) % len(numbers)] for i in (1000, 2000, 3000)]


if __name__ == "__main__":
    solve()
