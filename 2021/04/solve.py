import sys

boards, marks = [], []
part1, part2 = None, None
winners = set()

for line in sys.stdin:
    if ',' in line:
        balls = [int(number) for number in line.split(',')]
    elif line == '\n':
        boards.append([])
        marks.append([])
    else:
        row = [int(number) for number in line.split()]
        boards[-1].append(row)
        marks[-1].append([False] * len(row))

for ball in balls:
    for bi, board in enumerate(boards):
        if bi in winners:
            continue

        for ri, row in enumerate(board):
            for ni, number in enumerate(row):
                if number == ball:
                    marks[bi][ri][ni] = True
                    rotated = list(zip(*marks[bi][::-1]))

                    if all(marks[bi][ri]) or all(rotated[ni]):
                        unmarked = sum(number for ri, row in enumerate(board)
                                       for ni, number in enumerate(row)
                                       if not marks[bi][ri][ni])

                        if part1 is None:
                            part1 = unmarked * ball

                        part2 = unmarked * ball
                        winners.add(bi)

print('Part 1:', part1)
print('Part 2:', part2)
