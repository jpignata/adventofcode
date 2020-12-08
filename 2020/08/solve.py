import sys


class Handheld:
    pointer = 0
    accumulator = 0

    def nop(self, arg):
        self.pointer += 1

    def acc(self, arg):
        self.accumulator += arg
        self.pointer += 1

    def jmp(self, arg):
        self.pointer += arg

    def run_until_loop(self, instructions):
        seen = set()

        while self.pointer < len(instructions):
            if self.pointer in seen:
                return False

            cmd, arg = instructions[self.pointer]

            seen.add(self.pointer)
            getattr(self, cmd)(arg)

        return True

    def run(self, instructions):
        self.run_until_loop(instructions)
        return self.accumulator


instructions = [(cmd, int(arg)) for cmd, arg in
                [tuple(line.strip().split(' '))
                 for line in sys.stdin.readlines()]]
part2 = None

for i, instruction in enumerate(instructions):
    if instruction[0] in ('jmp', 'nop'):
        handheld = Handheld()
        modified = instructions[:]
        cmd = modified[i][0]
        modified[i] = ('jmp' if cmd == 'nop' else 'nop', modified[i][1])

        if handheld.run_until_loop(modified):
            part2 = handheld.accumulator
            break

print('Part 1:', Handheld().run(instructions))
print('Part 2:', part2)
