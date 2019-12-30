from intcode import Computer, Input

computer = Computer.load(filename='input.txt')

while not computer.halted:
    try:
        computer.tick()
    except Input:
        computer.print_screen()
        computer.execute(input())

# Required items: hypercube, prime number, mouse, wreath
