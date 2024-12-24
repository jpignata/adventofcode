import sys
from collections import deque
from operator import and_, or_, xor


def get(wires, letter):
    wires = sorted(
        (wire_name, wire_value)
        for wire_name, wire_value in wires.items()
        if wire_name[0] == letter
    )
    bits = [wire_value for _, wire_value in wires]

    return sum(bit << i for i, bit in enumerate(bits))


def run(wires, gates):
    operators = {"AND": and_, "OR": or_, "XOR": xor}
    wires = wires.copy()
    gates = deque(gates)

    while gates:
        left, operation, right, output = gates.popleft()

        if left in wires and right in wires:
            wires[output] = operators[operation](wires[left], wires[right])
        else:
            gates.append((left, operation, right, output))

    return wires


def main():
    wires = {}
    gates = []

    for line in sys.stdin:
        if ":" in line:
            wire, value = line.strip().split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            operation, output = line.strip().split(" -> ")
            gates.append([*operation.split(), output])

    initial = run(wires, gates)

    print("Part 1:", get(initial, "z"))


if __name__ == "__main__":
    main()
