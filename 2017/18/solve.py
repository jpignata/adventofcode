import queue
import sys
from collections import defaultdict
from threading import Thread


class Tablet:
    def __init__(self, instructions, *, id=0):
        self.instructions = instructions
        self.ip = 0
        self.sent = 0
        self.sound = None
        self.inq = queue.Queue()
        self.registers = defaultdict(int)
        self.registers['p'] = id

    def solo(self):
        while 0 <= self.ip < len(instructions):
            instruction, *args = instructions[self.ip]

            if instruction == 'rcv':
                if self.registers[args[0]]:
                    return self.sound

                self.ip += 1
            elif instruction == 'snd':
                self.sound = self.registers[args[0]]
                self.ip += 1
            else:
                self.ip += getattr(self, instruction)(*args) or 1

    def duet(self, outq):
        while 0 <= self.ip < len(instructions):
            ip = 0
            instruction, *args = instructions[self.ip]

            if instruction == 'rcv':
                try:
                    self.registers[args[0]] = self.inq.get(timeout=0.001)
                except queue.Empty:
                    break

                self.ip += 1
            elif instruction == 'snd':
                outq.put(self.registers[args[0]])

                self.sent += 1
                self.ip += 1
            else:
                self.ip += getattr(self, instruction)(*args) or 1

    def add(self, x, y):
        if isdigit(y):
            self.registers[x] += int(y)
        else:
            self.registers[x] += self.registers[y]

    def set(self, x, y):
        if isdigit(y):
            self.registers[x] = int(y)
        else:
            self.registers[x] = self.registers[y]

    def mul(self, x, y):
        self.registers[x] *= int(y)

    def jgz(self, x, y):
        if (isdigit(x) and int(x) > 0) or self.registers[x] > 0:
            if isdigit(y):
                return int(y)
            else:
                return self.registers[y]

    def mod(self, x, y):
        if isdigit(y):
            self.registers[x] %= int(y)
        else:
            self.registers[x] %= self.registers[y]


def isdigit(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


instructions = [line.strip().split(' ') for line in sys.stdin]
p0 = Tablet(instructions, id=0)
p1 = Tablet(instructions, id=1)
t0 = Thread(target=p0.duet, args=[p1.inq])
t1 = Thread(target=p1.duet, args=[p0.inq])

t0.start()
t1.start()
t0.join()
t1.join()

print('Part 1:', Tablet(instructions).solo())
print('Part 2:', p1.sent)
