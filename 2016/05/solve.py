import hashlib
import itertools


def hashes(door_id):
    for i in itertools.count():
        md5 = hashlib.md5()
        md5.update(bytearray(door_id + str(i), encoding="ASCII"))
        digest = md5.hexdigest()

        if digest[0:5] == "00000":
            yield (digest[5], digest[6])


password1 = []
password2 = [""] * 8

for char1, char2 in hashes("wtnhxymk"):
    if len(password1) < 8:
        password1.append(char1)

    if char1.isdigit():
        index = int(char1)
        if 0 <= index <= 7 and password2[index] == "":
            password2[index] = char2

    if password2.count("") == 0:
        break

print("Part 1:", "".join(password1))
print("Part 2:", "".join(password2))
