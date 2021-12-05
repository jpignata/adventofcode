import sys

boards = []
part1, part2 = None, None

for line in sys.stdin:
    if ',' in line:
        balls = [int(number) for number in line.split(',')]
    elif line == '\n':
        boards.append([])
    else:
        boards[-1].append([int(number) for number in line.split()])

for ball in balls:
    winners = set()

    for i, board in enumerate(boards):
        for y, row in enumerate(board):
            for x, num in enumerate(row):
                if num == ball:
                    board[y][x] = None

                    if not any(board[y]) or not any(list(zip(*board))[x]):
                        score = sum(num for row in board
                                    for num in row if num) * ball
                        part1 = part1 or score
                        part2 = score
                        winners.add(i)

    boards = [board for i, board in enumerate(boards) if i not in winners]

print('Part 1:', part1)
print('Part 2:', part2)
