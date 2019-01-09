from collections import deque


def look_and_say(numbers, times):
    numbers = deque(numbers)
    output = []

    while numbers:
        number = numbers.popleft()
        count = 1

        while numbers and number == numbers[0]:
            numbers.popleft()
            count += 1

        output.append(f'{count}{number}')

    if times - 1 == 0:
        return ''.join(output)
    else:
        return look_and_say(''.join(output), times - 1)


print('Part 1:', len(look_and_say('1113122113', 40)))
print('Part 2:', len(look_and_say('1113122113', 50)))
