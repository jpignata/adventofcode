import sys

part1, part2 = 0, 0

for line in sys.stdin.readlines():
    policy, password = line.strip().split(': ')
    freq, char = policy.split(' ')
    minfreq, maxfreq = [int(f) for f in freq.split('-')]
    index1, index2 = minfreq - 1, maxfreq - 1
    part1 += minfreq <= password.count(char) <= maxfreq
    part2 += (password[index1], password[index2]).count(char) == 1

print('Part 1:', part1)
print('Part 2:', part2)
