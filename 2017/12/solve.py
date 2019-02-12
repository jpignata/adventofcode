import sys
from collections import deque


def nodes(start, graph):
    q = deque([start])
    nodes = []

    while q:
        program = q.popleft()

        for other_program in graph[program]:
            if other_program not in nodes:
                nodes.append(other_program)
                q.append(other_program)

    return nodes


def components(graph):
    visited = {}
    components = 0

    for program in graph:
        if program not in visited:
            components += 1

            for node in nodes(program, graph):
                visited[node] = True

    return components


graph = {int(program): list(map(int, programs.split(', ')))
         for program, programs in [line.strip().split(' <-> ')
         for line in sys.stdin.readlines()]}

print('Part 1:', len(nodes(0, graph)))
print('Part 2:', components(graph))
