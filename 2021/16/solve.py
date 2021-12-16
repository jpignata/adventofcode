import sys
from math import prod


class Reader(object):
    def __init__(self, s):
        self.s = s
        self.pointer = 0

    def read(self, size):
        segment = self.s[self.pointer:self.pointer+size]
        self.pointer += size
        return segment

    def read_decimal(self, size):
        return int(''.join(self.read(size)), 2)


def parse(reader):
    versions = reader.read_decimal(3)
    type = reader.read_decimal(3)

    if type == 4:
        literal = ""

        while (segment := reader.read(5)):
            literal += segment[1:]

            if segment[0] == '0':
                break

        return (versions, int(''.join(literal), 2))

    decoded = []
    literals = []

    if reader.read_decimal(1):
        for _ in range(reader.read_decimal(11)):
            decoded.append(parse(reader))
    else:
        bits_to_read = reader.read_decimal(15)
        start = reader.pointer

        while reader.pointer - start < bits_to_read:
            decoded.append(parse(reader))

    for version, literal in decoded:
        versions += version
        literals.append(literal)

    return (versions, operations[type](literals))


bits = [bin(int(c, 16))[2:].zfill(4) for c in sys.stdin.readline().strip()]
operations = {
    0: lambda literals: sum(literals),
    1: lambda literals: prod(literals),
    2: lambda literals: min(literals),
    3: lambda literals: max(literals),
    5: lambda literals: int(literals[0] > literals[1]),
    6: lambda literals: int(literals[0] < literals[1]),
    7: lambda literals: int(literals[0] == literals[1])}
versions, result = parse(Reader(''.join(bits)))

print('Part 1:', versions)
print('Part 2:', result)
