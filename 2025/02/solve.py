import sys


def halves_equal(number):
    first, last = number[: len(number) // 2], number[len(number) // 2 :]

    return first == last


def chunks_repeating(number):
    for i in range(1, (len(number) // 2) + 1):
        chunks = [number[j : j + i] for j in range(0, len(number), i)]

        if len(set(chunks)) == 1:
            return True

    return False


def total(start, end, helper):
    return sum(number for number in range(start, end + 1) if helper(str(number)))


def main():
    ranges = []

    for _range in sys.stdin.readline().strip().split(","):
        start, end = _range.split("-")
        ranges.append((int(start), int(end)))

    print("Part 1:", sum(total(start, end, halves_equal) for start, end in ranges))
    print("Part 2:", sum(total(start, end, chunks_repeating) for start, end in ranges))


if __name__ == "__main__":
    main()
