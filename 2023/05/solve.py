import sys


def parse():
    seeds = [
        int(number)
        for number in sys.stdin.readline().strip().split(": ")[-1].split()
    ]
    maps = []

    for line in sys.stdin:
        if not line.strip():
            maps.append([])
        elif line[0].isdigit():
            maps[-1].append([int(number) for number in line.strip().split()])

    return seeds, maps


def part1(seeds, maps):
    lowest = sys.maxsize

    for seed in seeds:
        for map in maps:
            for dest_start, src_start, jump in map:
                src_end = src_start + jump

                if src_start <= seed <= src_end:
                    seed = (seed - src_start) + dest_start
                    break

        lowest = min(lowest, seed)

    return lowest


def part2(seeds, maps):
    seed_ranges = [
        (start, start + jump) for start, jump in zip(seeds[::2], seeds[1::2])
    ]
    candidates = [[] for _ in range(len(maps))]

    for range_start, range_end in seed_ranges:
        ranges = [(range_start, range_end)]

        for i, map in enumerate(maps):
            while ranges:
                range_start, range_end = ranges.pop()

                for dest_start, src_start, jump in map:
                    src_end = src_start + jump
                    offset = dest_start - src_start

                    if src_end <= range_start or range_end <= src_start:
                        continue

                    if range_start < src_start:
                        ranges.append((range_start, src_start))
                        range_start = src_start

                    if src_end < range_end:
                        ranges.append((src_end, range_end))
                        range_end = src_end

                    range_start += offset
                    range_end += offset

                    break

                candidates[i].append((range_start, range_end))

            ranges = candidates[i]

    return min(candidates[-1])[0]


if __name__ == "__main__":
    seeds, maps = parse()

    print("Part 1:", part1(seeds, maps))
    print("Part 2:", part2(seeds, maps))
