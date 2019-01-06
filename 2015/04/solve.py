import itertools
import hashlib

input = 'yzbqklnj'

def findhash(number_of_zeroes=5):
    for i in itertools.count():
        md5 = hashlib.md5()
        md5.update(bytearray(input + str(i), encoding='ASCII'))

        if md5.hexdigest()[0:number_of_zeroes] == '0' * number_of_zeroes:
            return i

print('Part 1:', findhash())
print('Part 2:', findhash(6))
