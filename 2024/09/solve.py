import sys


def defrag_blocks(blocks):
    blocks = blocks[:]
    lo, hi = 0, len(blocks) - 1

    while lo != hi:
        if blocks[lo].isdigit():
            lo += 1
        elif blocks[hi] == ".":
            hi -= 1
        else:
            blocks[lo], blocks[hi] = blocks[hi], blocks[lo]

    return blocks


def defrag_files(blocks):
    blocks = blocks[:]
    groups = []
    pointer = 0

    while pointer < len(blocks):
        current = blocks[pointer]
        start = pointer
        length = 0

        while pointer < len(blocks) and blocks[pointer] == current:
            pointer += 1
            length += 1

        groups.append((current, start, length))

    files = [group for group in groups if group[0] != "."]
    free = [group for group in groups if group[0] == "."]

    while files:
        file_id, file_start, file_length = files.pop()

        for i, (_, free_start, free_length) in enumerate(free):
            if file_start > free_start and file_length <= free_length:
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
    return sum(pos * int(block) for pos, block in enumerate(blocks) if block != ".")


def main():
    diskmap = sys.stdin.read().strip()
    file_id = 0
    blocks = []

    for i, char in enumerate(diskmap):
        if i % 2:
            for _ in range(int(char)):
                blocks.append(str("."))
        else:
            for _ in range(int(char)):
                blocks.append(str(file_id))

            file_id += 1

    print("Part 1:", checksum(defrag_blocks(blocks)))
    print("Part 2:", checksum(defrag_files(blocks)))


if __name__ == "__main__":
    main()
