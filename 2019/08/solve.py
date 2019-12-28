import sys

digits = [int(d) for d in sys.stdin.readline().strip()]
min_layer = min([digits[i:i + 150] for i in range(0, len(digits), 150)],
                key=lambda l: l.count(0))
chunks = [digits[i:i + 25] for i in range(0, len(digits), 25)]
layers = [chunks[i:i + 6] for i in range(0, len(chunks), 6)]
image = layers[0].copy()

for i in range(1, len(layers)):
    for j in range(len(layers[0])):
        for k in range(len(layers[0][0])):
            if image[j][k] == 2:
                image[j][k] = layers[i][j][k]

print('Part 1:', min_layer.count(1) * min_layer.count(2))
print('Part 2:')

for row in image:
    for pixel in row:
        if pixel == 1:
            sys.stdout.write('█')
        else:
            sys.stdout.write(' ')

    print()
