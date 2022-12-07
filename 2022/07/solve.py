import sys
from collections import defaultdict


dirs = defaultdict(int)
current = ["root"]

for line in sys.stdin:
    match line.strip().split():
        case ["$", "cd", "/"]:
            current = ["root"]
        case ["$", "cd", ".."]:
            current.pop()
        case ["$", "cd", name]:
            current.append(name)
        case ["$", "ls"] | ["dir", _]:
            continue
        case [size, _]:
            for segment in current:
                dirs[segment] += int(size)

total = sum(size for size in dirs.values() if size <= 100_000)
smallest = min(size for size in dirs.values() if size >= dirs["root"] - 40_000_000)

print("Part 1:", total)
print("Part 2:", smallest)
