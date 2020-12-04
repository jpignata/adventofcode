import sys
import re

policy1, policy2 = 0, 0

for line in sys.stdin.readlines():
    lo, hi, char, password = re.split(r'[ -]|: ', line.strip())
    lo, hi = int(lo), int(hi)
    policy1 += lo <= password.count(char) <= hi
    policy2 += (password[lo - 1], password[hi - 1]).count(char) == 1

print('Part 1:', policy1)
print('Part 2:', policy2)
