import sys
from collections import deque, defaultdict
from itertools import count
from math import lcm

kinds = defaultdict(lambda: "-")
edges = defaultdict(list)
states = defaultdict(int)
lasts = defaultdict(dict)
cycles = {}
pulses = [0, 0]

for line in sys.stdin:
    module, dests = line.strip().split(" -> ")
    dests = dests.split(", ")

    if module[0] in "%&":
        kind, module = module[0], module[1:]
        kinds[module] = kind

    for dest in dests:
        edges[module].append(dest)
        lasts[dest][module] = 0

    # [lk, fn, fh, hh] -> nc -> rx
    if "nc" in dests:
        cycles[module] = 0

for i in count(1):
    q = deque([("broadcaster", "button", 0)])

    while q:
        module, from_module, pulse = q.popleft()

        if i <= 1000:
            pulses[pulse] += 1

        if module == "nc" and pulse:
            cycles[from_module] = i

        if all(cycles.values()):
            print("Part 1:", pulses[0] * pulses[1])
            print("Part 2:", lcm(*cycles.values()))
            exit()

        match kinds[module]:
            case "%":
                if pulse:
                    continue

                states[module] = 0 if states[module] else 1
                next_pulse = states[module]
            case "&":
                lasts[module][from_module] = pulse
                next_pulse = 0 if all(lasts[module].values()) else 1
            case "-":
                next_pulse = pulse

        for dest in edges[module]:
            q.append((dest, module, next_pulse))
