import sys
import datetime as dt
import re
from collections import defaultdict, Counter

log = defaultdict(Counter)
on_duty = None
asleep = None

for line in sorted(sys.stdin.readlines()):
    isotime, rest = line.strip().split("] ")
    timestamp = dt.datetime.fromisoformat(isotime[1:])

    if rest.startswith("Guard"):
        on_duty = int(re.search(r"(\d+)", rest)[1])
    elif rest.startswith("falls"):
        asleep = timestamp
    elif rest.startswith("wakes"):
        while asleep != timestamp:
            log[on_duty][asleep.minute] += 1
            asleep += dt.timedelta(minutes=1)

strategy_1 = max(
    (sum(counts.values()), counts.most_common(1)[0][0], guard_id)
    for guard_id, counts in log.items()
)
strategy_2 = max(
    (*tuple(reversed(counts.most_common(1)[0])), guard_id)
    for guard_id, counts in log.items()
)

print("Part 1:", strategy_1[1] * strategy_1[2])
print("Part 2:", strategy_2[1] * strategy_2[2])
