import os

from intcode import Computer, Input, Halt

computer = Computer.load(filename=f'./{os.path.dirname(__file__)}/input.txt')

while not computer.halted:
    try:
        computer.tick()
    except Input:
        computer.print_screen()

        if (command := input()) == 'dump':
            with open('memory.out', 'w') as f:
                f.write(','.join(str(d) for d in computer.program.values()))

            print('Wrote memory.out.', end='\n\n')
        else:
            computer.execute(command)
    except Halt:
        computer.print_screen()
