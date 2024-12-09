import sys
from itertools import groupby


def defrag_blocks(blocks):
    lo, hi = 0, len(blocks) - 1

    while lo != hi:
        if blocks[lo] != ".":
            lo += 1
        elif blocks[hi] == ".":
            hi -= 1
        else:
            blocks[lo], blocks[hi] = blocks[hi], blocks[lo]

    return blocks


def defrag_files(blocks):
    files = []
    free = []
    start = 0

    for current, group in groupby(blocks):
        length = len(list(group))

        if current == ".":
            free.append((current, start, length))
        else:
            files.append((current, start, length))

        start += length

    while files:
        file_id, file_start, file_length = files.pop()

        for i, (_, free_start, free_length) in enumerate(free):
            if file_start < free_start:
                break

            if file_length <= free_length:
                for j in range(file_start, file_start + file_length):
                    blocks[j] = "."

                for j in range(free_start, free_start + file_length):
                    blocks[j] = file_id

                if free_length == file_length:
                    del free[i]
                else:
                    free[i] = (".", free_start + file_length, free_length - file_length)

                break

    return blocks


def checksum(blocks):
    return sum(pos * block for pos, block in enumerate(blocks) if block != ".")


def main():
    blocks = []
    file_id = 0

    for i, char in enumerate(sys.stdin.read().strip()):
        if not i % 2:
            blocks.extend([file_id] * int(char))
            file_id += 1
        else:
            blocks.extend(["."] * int(char))

    print("Part 1:", checksum(defrag_blocks(blocks[:])))
    print("Part 2:", checksum(defrag_files(blocks[:])))


if __name__ == "__main__":
    main()
