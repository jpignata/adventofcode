import sys


def size_of(data, v2=False):
    count = 0
    i = 0

    while i < len(data):
        if data[i] == "(":
            marker = ""
            i += 1

            while data[i] != ")":
                marker += data[i]
                i += 1

            num_chars, reps = map(int, marker.split("x"))

            if v2:
                count += size_of(data[i + 1 : i + num_chars + 1], v2) * reps
            else:
                count += num_chars * reps

            i += num_chars
        else:
            count += 1

        i += 1

    return count


data = sys.stdin.readline().strip()

print("Part 1:", size_of(data))
print("Part 2:", size_of(data, True))
