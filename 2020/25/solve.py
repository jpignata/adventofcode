def find(number):
    result = 1
    loop_size = 0

    while result != number:
        result *= 7
        result %= 20201227
        loop_size += 1

    return loop_size


def calculate(loop_size, number):
    result = 1

    for _ in range(loop_size):
        result *= number
        result %= 20201227

    return result


public_keys = [10212254, 12577395]
loop_sizes = [find(key) for key in public_keys]

print('Part 1:', calculate(loop_sizes[0], public_keys[1]))
