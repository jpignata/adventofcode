import re
import sys


class Computer:
    def __init__(self, registers):
        self.registers = registers.copy()
        self.ip = 0
        self.output = []

    def combo(self, operand):
        if operand in range(0, 4):
            return operand

        if operand in range(4, 7):
            key = chr(operand + 61)
            return self.registers[key]

        raise ValueError(f"Invalid operand: {operand}")

    def adv(self, operand):
        self.registers["A"] //= 2 ** self.combo(operand)

    def bxl(self, operand):
        self.registers["B"] ^= operand

    def bst(self, operand):
        self.registers["B"] = self.combo(operand) & 7

    def jnz(self, operand):
        if self.registers["A"]:
            self.ip = operand
            return True

        return False

    def bxc(self, _):
        self.registers["B"] ^= self.registers["C"]

    def out(self, operand):
        self.output.append(self.combo(operand) & 7)

    def bdv(self, operand):
        self.registers["B"] = self.registers["A"] // 2 ** self.combo(operand)

    def cdv(self, operand):
        self.registers["C"] = self.registers["A"] // 2 ** self.combo(operand)

    def run(self, program):
        instructions = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]

        while self.ip < len(program):
            opcode, operand = program[self.ip], program[self.ip + 1]

            if not instructions[opcode](operand):
                self.ip += 2

        return self.output


def main():
    registers = {}
    program = []

    for line in sys.stdin:
        if match := re.search(r"Register ([A-Z]): (\d+)", line):
            registers[match[1]] = int(match[2])
        elif "Program" in line:
            program = list(map(int, re.findall(r"\d+", line)))

    computer = Computer(registers)
    output = computer.run(program)

    print("Part 1:", ",".join(map(str, output)))


if __name__ == "__main__":
    main()
