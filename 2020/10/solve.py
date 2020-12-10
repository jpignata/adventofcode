import sys
from collections import defaultdict

diffs = defaultdict(int)
diffs[3] = 1
memo = defaultdict(int)
memo[0] = 1
prev = 0

for adapter in sorted([int(line) for line in sys.stdin.readlines()]):
    diffs[adapter - prev] += 1
    memo[adapter] = memo[adapter-1] + memo[adapter-2] + memo[adapter-3]
    prev = adapter

print('Part 1:', diffs[1] * diffs[3])
print('Part 2:', memo[max(memo)])
