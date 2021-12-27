import sys


class ALU(object):
    def __init__(self, instructions):
        self.instructions = [instruction.strip() .split()
                             for instruction in instructions]

    def run(self, model):
        registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        model = (int(d) for d in list(str(model)))

        for instruction in instructions:
            if len(instruction.split()) == 3:
                operation, a, b = instruction.split()

                if b in ('w', 'x', 'y', 'z'):
                    b = registers[b]
                else:
                    b = int(b)
            elif len(instruction.split()) == 2:
                operation, a = instruction.split()

            match operation:
                case 'inp':
                    registers[a] = next(model)
                case 'add':
                    registers[a] += b
                case 'mul':
                    registers[a] *= b
                case 'div':
                    registers[a] //= b 
                case 'mod':
                    registers[a] %= b
                case 'eql':
                    registers[a] = 1 if registers[a] == b else 0

        return registers['z'] == 0


instructions = [line.strip() for line in open('input.txt')] 

print(ALU(instructions).run(sys.argv[1]))
