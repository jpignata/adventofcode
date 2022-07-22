import sys
from itertools import groupby


def checksum(box_ids):
    two_chars = 0
    three_chars = 0

    for box_id in box_ids:
        counts = [len(list(group)) for _, group in groupby(sorted(box_id))]

        if 2 in counts:
            two_chars += 1

        if 3 in counts:
            three_chars += 1

    return two_chars * three_chars


def find_boxes(box_ids):
    for box_id in box_ids:
        for other_box_id in box_ids:
            intersection = ""
            diffs = 0

            for i, char in enumerate(box_id):
                if char == other_box_id[i]:
                    intersection += char
                else:
                    diffs += 1

                    if diffs > 1:
                        break

            if diffs == 1:
                return intersection


box_ids = [line.strip() for line in sys.stdin.readlines()]

print("Part 1:", checksum(box_ids))
print("Part 2:", find_boxes(box_ids))
