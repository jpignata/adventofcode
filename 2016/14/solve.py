import hashlib
import re
from itertools import count


def search(salt, *, stretch=0):
    def gethash(i):
        for j in range(len(hashes), i+1):
            input = salt + str(j)

            for _ in range(stretch + 1):
                md5 = hashlib.md5()
                md5.update(bytearray(input, encoding='ASCII'))
                input = md5.hexdigest()

            hashes.append(md5.hexdigest())

        return hashes[i]

    def findmatch(hash, char, num):
        match = re.findall('(' + char + ')' + r'\1' * (num - 1), hash)

        if match:
            return match[0][0]

    hashes = list()
    keys = 0

    for i in count(0):
        char = findmatch(gethash(i), '.', 3)

        if char:
            for j in range(1, 1001):
                if findmatch(gethash(i+j), char, 5):
                    keys += 1

                    if keys == 64:
                        return i


print('Part 1:', search('zpqevtbw'))
print('Part 2:', search('zpqevtbw', stretch=2016))
