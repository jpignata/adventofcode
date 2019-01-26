import sys
from collections import defaultdict


class Bot:
    def __init__(self):
        self.values = []

    def append(self, value):
        self.values.append(value)
        self.values.sort()

    def instructions(self, lo_dest, lo_num, hi_dest, hi_num):
        self.lo_dest = lo_dest
        self.lo_num = lo_num
        self.hi_dest = hi_dest
        self.hi_num = hi_num

    def run(self):
        if len(self.values) != 2:
            return 0

        self.lo_dest[self.lo_num].append(self.values[0])
        self.hi_dest[self.hi_num].append(self.values[1])
        self.values.clear()

        return 2


bots = defaultdict(Bot)
outputs = defaultdict(list)
moves = -1

for line in sys.stdin.readlines():
    tokens = line.split(' ')

    if tokens[0] == 'value':
        bots[int(tokens[5])].append(int(tokens[1]))
    elif tokens[0] == 'bot':
        lo_dest = outputs if tokens[5] == 'output' else bots
        hi_dest = outputs if tokens[10] == 'output' else bots

        bots[int(tokens[1])].instructions(lo_dest, int(tokens[6]), hi_dest,
                                          int(tokens[11]))

while moves != 0:
    moves = 0

    for num, bot in bots.items():
        if bot.values == [17, 61]:
            print('Part 1:', num)

        moves += bot.run()

print('Part 2:', outputs[0][0] * outputs[1][0] * outputs[2][0])
