def generate(data, size):
    a, b = data, ['0' if c == '1' else '1' for c in reversed(data)]
    output = a + '0' + ''.join(b)

    if len(output) >= size:
        return output[:size]
    else:
        return generate(output, size)


def checksum(data):
    output = ['0' if int(data[i]) + int(data[i + 1]) == 1 else '1'
              for i in range(0, len(data), 2)]

    if len(output) % 2 != 0:
        return ''.join(output)
    else:
        return checksum(''.join(output))


print('Part 1:', checksum(generate('11110010111001001', 272)))
print('Part 2:', checksum(generate('11110010111001001', 35651584)))
