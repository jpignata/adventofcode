import sys
import intcode

if len(sys.argv) > 1:
    computer = intcode.Computer.load(filename=sys.argv[1])
else:
    computer = intcode.Computer.load()

while not computer.halted:
    try:
        computer.tick()
    except intcode.Input:
        computer.print_screen()

        if (command := input()) == 'dump':
            with open('memory.out', 'w') as f:
                f.write(','.join(str(d) for d in computer.program.values()))

            print('Wrote memory.out.', end='\n\n')
        elif command == 'quit':
            break
        else:
            computer.execute(command)
    except intcode.Halt:
        computer.print_screen()
