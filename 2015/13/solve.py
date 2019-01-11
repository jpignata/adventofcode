import re
import sys
from itertools import permutations


class Attendee:
    def __init__(self, name):
        self.name = name
        self.combinations = dict()

    def add(self, guest, units):
        self.combinations[guest] = units

    def happiness_units(self, left, right):
        return self.combinations.get(left, 0) + self.combinations.get(right, 0)


class Table:
    def __init__(self, attendees):
        self.attendees = attendees

    def total_change(self):
        total_change = 0

        for i, attendee in enumerate(self.attendees):
            left = self.attendees[(i-1) % len(self.attendees)].name
            right = self.attendees[(i+1) % len(self.attendees)].name
            total_change += attendee.happiness_units(left, right)

        return total_change


attendees = dict()
pattern = r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'

for line in sys.stdin.readlines():
    matches = re.match(pattern, line)
    guest1, guest2, change = matches.group(1, 4, 2)
    units = int(matches.group(3))

    if guest1 not in attendees:
        attendees[guest1] = Attendee(guest1)

    if change == 'lose':
        units = units * -1

    attendees[guest1].add(guest2, units)

attendees_with_me = attendees.copy()
attendees_with_me['Me'] = Attendee('Me')

changes = [Table(attendees).total_change()
           for attendees in permutations(attendees.values())]
changes_with_me = [Table(attendees).total_change()
                   for attendees in permutations(attendees_with_me.values())]

print('Part 1:', max(changes))
print('Part 2:', max(changes_with_me))
