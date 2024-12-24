import sys
from operator import and_, or_, xor


def main():
    wires = {}
    operators = {"AND": and_, "OR": or_, "XOR": xor}

    for line in sys.stdin:
        if ":" in line:
            wire, value = line.strip().split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            operation, wire = line.strip().split(" -> ")
            wires[wire] = operation.split()

    def evaluate(wire):
        match wires[wire]:
            case [left, operation, right]:
                return operators[operation](evaluate(left), evaluate(right))
            case _:
                return wires[wire]

    output = sum(evaluate(wire) << int(wire[1:]) for wire in wires if wire[0] == "z")

    print("Part 1:", output)


if __name__ == "__main__":
    main()
