import sys

import networkx as nx

graph = nx.Graph()
cliques = 0
largest = ""

for line in sys.stdin:
    graph.add_edge(*line.strip().split("-"))

for clique in nx.enumerate_all_cliques(graph):
    password = ",".join(sorted(clique))

    if len(clique) == 3 and any(node.startswith("t") for node in clique):
        cliques += 1

    if len(password) > len(largest):
        largest = password

print("Part 1:", cliques)
print("Part 2:", largest)
