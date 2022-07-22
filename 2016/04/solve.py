import sys
import re
from collections import namedtuple, Counter


def parse(room):
    name, sector_id_and_checksum = room.rsplit("-", 1)
    match = re.match(r"(\d*)\[([a-z]*)\]", sector_id_and_checksum)
    sector_id, checksum = match.group(1, 2)
    return Room(name, int(sector_id), checksum)


def checksum(name):
    chars = name.replace("-", "")
    counted = sorted(Counter(chars).items(), key=lambda kv: (-kv[1], kv[0]))
    return "".join(map(lambda c: c[0], counted))[0:5]


def decrypt(name, key):
    decrypted = []
    for char in name:
        if char == "-":
            decrypted.append(" ")
        else:
            decrypted.append(chr(97 + ((ord(char) - 97) + key) % 26))
    return "".join(decrypted)


Room = namedtuple("Room", ["name", "sector_id", "checksum"])
rooms = [parse(line.strip()) for line in sys.stdin.readlines()]
real = [room for room in rooms if checksum(room.name) == room.checksum]

print("Part 1:", sum(map(lambda r: r.sector_id, real)))

for room in rooms:
    if decrypt(room.name, room.sector_id) == "northpole object storage":
        print("Part 2:", room.sector_id)
