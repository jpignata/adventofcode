from intcode import Computer, Input

computer = Computer.load_file('input.txt')

while not computer.halted:
    try:
        computer.tick()
    except Input:
        computer.execute(input())

    computer.print_screen()

# Required items: hypercube, prime number, mouse, wreath
