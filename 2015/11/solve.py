from string import ascii_lowercase
from itertools import groupby


def valid(password):
    for b in ('i', 'o', 'l'):
        if b in password:
            return False

    if [len(list(g)) for _, g in groupby(password)].count(2) < 2:
        return False

    for i, char in enumerate(password):
        if i + 2 == len(password):
            return False

        char_index = ascii_lowercase.index(char)
        char1_index = ascii_lowercase.index(password[i + 1])
        char2_index = ascii_lowercase.index(password[i + 2])

        if char1_index - char_index == 1 and char2_index - char1_index == 1:
            break

    return True


def increment(password):
    chars = list(password)

    for i, char in enumerate(reversed(chars)):
        index = ascii_lowercase.index(char) + 1
        chars[((i - len(chars)) * -1) - 1] = ascii_lowercase[index % 26]

        if index < 26:
            break

    return ''.join(chars)


def find(current):
    password = increment(current)

    while not valid(password):
        password = increment(password)

    return password


print('Part 1:', find('hxbxwxba'))
print('Part 2:', find('hxbxxyzz'))
