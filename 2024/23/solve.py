import sys

import networkx as nx

graph = nx.Graph(line.strip().split("-") for line in sys.stdin)
cliques = list(nx.enumerate_all_cliques(graph))
found = sum(len(nodes) == 3 and any(n[0] == "t" for n in nodes) for nodes in cliques)
password = ",".join(sorted(cliques[-1]))

print("Part 1:", found)
print("Part 2:", password)
