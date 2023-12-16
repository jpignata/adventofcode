import sys
from re import split


def _hash(seq):
    val = 0

    for char in seq:
        val += ord(char)
        val *= 17
        val %= 256

    return val


sequences = sys.stdin.read().strip().split(",")
buckets = [[] for _ in range(256)]

for seq in sequences:
    key, value = split(r"[-=]", seq)
    bucket_id = _hash(key)
    bucket = buckets[bucket_id]

    if value:
        for slot in bucket:
            if slot[0] == key:
                slot[1] = value
                break
        else:
            bucket.append([key, value])
    else:
        buckets[bucket_id] = [slot for slot in bucket if slot[0] != key]

power = sum(
    i * j * int(value)
    for i, bucket in enumerate(buckets, 1)
    for j, (_, value) in enumerate(bucket, 1)
)

print("Part 1:", sum(_hash(seq) for seq in sequences))
print("Part 2:", power)
