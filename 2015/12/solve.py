import json
import re
import sys


def tally(element, total=0):
    if isinstance(element, list):
        for e in element:
            total += tally(e)
    elif isinstance(element, dict):
        if 'red' not in element.keys() and 'red' not in element.values():
            total += tally(list(element.values()))
    elif isinstance(element, int):
        total += element

    return total


doc = sys.stdin.readline().strip()

print('Part 1:', sum(map(int, re.findall(r'-?[\d]+', doc))))
print('Part 2:', tally(json.loads(doc)))
