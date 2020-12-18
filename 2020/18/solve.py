import operator
import sys


def evaluate(expr, order):
    operators = {'+': operator.add, '*': operator.mul}
    values, ops = [], []

    for token in expr:
        if token.isdigit():
            values.append(int(token))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ((op := ops.pop()) != '('):
                values.append(operators[op](values.pop(), values.pop()))
        elif token in operators:
            while (ops and ops[-1] != '(' and order[token] <= order[ops[-1]]):
                values.append(operators[ops.pop()](values.pop(), values.pop()))

            ops.append(token)

    while ops:
        values.append(operators[ops.pop()](values.pop(), values.pop()))

    return values[0]


exprs = sys.stdin.readlines()

print('Part 1:', sum(evaluate(expr, {'+': 0, '*': 0}) for expr in exprs))
print('Part 2:', sum(evaluate(expr, {'+': 1, '*': 0}) for expr in exprs))
