import sys
from itertools import groupby

policy_1_valid = policy_2_valid = 0

for passphrase in [line.strip() for line in sys.stdin.readlines()]:
    tokens = sorted(passphrase.split(' '))
    sorted_tokens = sorted(map(sorted, tokens))

    group_counts = [len(list(group)) for _, group in groupby(tokens)]
    sorted_group_counts = [len(list(group)) for _, group
                           in groupby(sorted_tokens)]

    policy_1_valid += max(group_counts) == 1
    policy_2_valid += max(sorted_group_counts) == 1

print('Part 1:', policy_1_valid)
print('Part 2:', policy_2_valid)
