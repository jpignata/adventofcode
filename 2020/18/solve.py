import re
import sys
from collections import deque
import operator

operations = {'+': operator.add, '*': operator.mul}
order = ['+', '*']
part1, part2 = 0, 0

for line in sys.stdin.readlines():
    expr = re.findall(r'[+*()]|\d+', line)
    output = []
    ops = []

    for token in expr:
        print(output, ops)
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ((op := ops.pop()) != '('):
                output.append(operations[op](output.pop(), output.pop()))
        elif token in operations:
            while (ops and ops[-1] != '(' and order.index(token) >= order.index(ops[-1])):
                output.append(operations[ops.pop()](output.pop(), output.pop()))

            ops.append(token)


    while ops:
        output.append(operations[ops.pop()](output.pop(), output.pop()))

    print(output)
    part1 += output[-1]

print('Part 1:', part1)
