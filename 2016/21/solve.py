import sys
from collections import deque


def swap_position(password, x, y):
    new_password = list(password)

    new_password[x] = password[y]
    new_password[y] = password[x]

    return ''.join(new_password)


def swap_letter(password, x, y):
    new_password = ''

    for char in password:
        if char == x:
            new_password += y
        elif char == y:
            new_password += x
        else:
            new_password += char

    return new_password


def rotate_position(password, steps, direction='right'):
    d = deque(password)

    if direction == 'left':
        steps *= -1

    d.rotate(steps)

    return ''.join(d)


def rotate_letter(password, letter):
    index = password.index(letter)
    steps = index + (index >= 4) + 1

    return rotate_position(password, steps)


def rotate_letter_backwards(password, letter):
    position = password.index(letter)

    if position == 0:
        steps = 1
    elif position % 2 == 1:
        steps = position // 2 + 1
    else:
        steps = position // 2 + 5

    return rotate_position(password, steps, 'left')


def reverse_positions(password, x, y):
    return password[:x] + ''.join(reversed(password[x:y+1])) + password[y+1:]


def move_positions(password, x, y):
    new_password = list(password)

    del new_password[x]
    new_password.insert(y, password[x])

    return ''.join(new_password)


def scramble(password, instructions):
    for instruction in instructions:
        tokens = instruction.strip().split(' ')

        if tokens[0] == 'swap' and tokens[1] == 'position':
            password = swap_position(password, int(tokens[2]), int(tokens[5]))
        elif tokens[0] == 'swap' and tokens[1] == 'letter':
            password = swap_letter(password, tokens[2], tokens[5])
        elif tokens[0] == 'rotate' and tokens[1] in ('left', 'right'):
            password = rotate_position(password, int(tokens[2]), tokens[1])
        elif tokens[0] == 'rotate' and tokens[3] == 'position':
            password = rotate_letter(password, tokens[6])
        elif tokens[0] == 'reverse':
            start, end = int(tokens[2]), int(tokens[4])
            password = reverse_positions(password, start, end)
        elif tokens[0] == 'move':
            password = move_positions(password, int(tokens[2]), int(tokens[5]))

    return password


def unscramble(password, instructions):
    for instruction in reversed(instructions):
        tokens = instruction.strip().split(' ')

        if tokens[0] == 'swap' and tokens[1] == 'position':
            password = swap_position(password, int(tokens[2]), int(tokens[5]))
        elif tokens[0] == 'swap' and tokens[1] == 'letter':
            password = swap_letter(password, tokens[2], tokens[5])
        elif tokens[0] == 'rotate' and tokens[1] in ('left', 'right'):
            direction = 'left' if tokens[1] == 'right' else 'right'
            password = rotate_position(password, int(tokens[2]), direction)
        elif tokens[0] == 'rotate' and tokens[3] == 'position':
            password = rotate_letter_backwards(password, tokens[6])
        elif tokens[0] == 'reverse':
            start, end = int(tokens[2]), int(tokens[4])
            password = reverse_positions(password, start, end)
        elif tokens[0] == 'move':
            password = move_positions(password, int(tokens[5]), int(tokens[2]))

    return password


instructions = sys.stdin.readlines()

print('Part 1:', scramble('abcdefgh', instructions))
print('Part 2:', unscramble('fbgdceah', instructions))
