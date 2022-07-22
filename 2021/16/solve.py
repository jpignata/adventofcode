import sys

from io import StringIO
from math import prod
from operator import lt, gt, eq


def parse(reader):
    literals = []
    versions = [int(reader.read(3), 2)]
    packet_type = int(reader.read(3), 2)

    def decode():
        version, literal = parse(reader)
        versions.extend(version)
        literals.append(literal)

    if packet_type == 4:
        literal = ""

        while segment := reader.read(5):
            literal += segment[1:]

            if not int(segment[0]):
                return versions, int(literal, 2)

    if int(reader.read(1)):
        for _ in range(int(reader.read(11), 2)):
            decode()
    else:
        read_to = int(reader.read(15), 2) + reader.tell()

        while reader.tell() != read_to:
            decode()

    return versions, operations[packet_type](literals)


operations = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: gt(*x),
    6: lambda x: lt(*x),
    7: lambda x: eq(*x),
}
bits = "".join(bin(int(c, 16))[2:].zfill(4) for c in sys.stdin.read().strip())
versions, result = parse(StringIO(bits))

print("Part 1:", sum(versions))
print("Part 2:", result)
