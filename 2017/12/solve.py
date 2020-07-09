import sys


def dfs(programs, program):
    visited = set()
    s = [program]

    while s:
        if (program := s.pop()) not in visited:
            visited.add(program)
            s.extend(programs[program])

    return visited


def components(programs):
    visited = set()
    components = 0

    for program in programs:
        if program not in visited:
            visited.update(dfs(programs, program))
            components += 1

    return components


programs = {int(program): [int(p) for p in programs.split(',')]
            for program, programs in [line.strip().split(' <-> ')
            for line in sys.stdin.readlines()]}

print('Part 1:', len(dfs(programs, 0)))
print('Part 2:', components(programs))
