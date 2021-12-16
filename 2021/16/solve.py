import sys
from math import prod


class Reader(object):
    def __init__(self, s):
        self.s = s
        self.pointer = 0
        self.max = len(s) - 1

    def eof(self):
        at_end = self.pointer >= self.max
        no_data_left = all(c == '0' for c in self.s[self.pointer:])
        return at_end or no_data_left

    def read(self, number):
        segment = self.s[self.pointer:self.pointer+number]
        self.pointer += number
        return segment

    def read_decimal(self, number):
        return int(''.join(self.read(number)), 2)


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


bits = [bin(int(char, 16)).replace('0b', '').zfill(4)
        for char in sys.stdin.readline().strip()]
operations = [
    lambda literals: sum(literals),
    lambda literals: prod(literals),
    lambda literals: min(literals),
    lambda literals: max(literals),
    None,
    lambda literals: int(literals[0] > literals[1]),
    lambda literals: int(literals[0] < literals[1]),
    lambda literals: int(literals[0] == literals[1])]
versions, result = parse(Reader(''.join(bits)))

print('Part 1:', versions)
print('Part 2:', result)
