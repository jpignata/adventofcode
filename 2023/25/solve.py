import sys
from random import choice
from networkx import Graph, minimum_cut

graph = Graph()

for line in sys.stdin:
    v1, w = line.strip().split(": ")

    for v2 in w.split():
        graph.add_edge(v1, v2, capacity=1)

nodes = list(graph.nodes())
cut_value = -1

while cut_value != 3:
    cut_value, partition = minimum_cut(graph, choice(nodes), choice(nodes))

print("Part 1:", len(partition[0]) * len(partition[1]))
