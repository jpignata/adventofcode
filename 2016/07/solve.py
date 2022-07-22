import sys
import re

ips = [line.strip() for line in sys.stdin.readlines()]
abba = re.compile(r"(?!([a-z])\1)([a-z])([a-z])\3\2")
aba_bab = re.compile(r"(?=(([a-z])(?!\2)[a-z]\2))")
tls = set()
ssl = set()

for ip in ips:
    sequences = re.findall(r"\[?[a-z]+\]?", ip)
    supernet_sequences = list(filter(lambda s: s[0] != "[", sequences))
    hypernet_sequences = list(filter(lambda s: s[0] == "[", sequences))
    has_abba = any(map(lambda s: abba.search(s), sequences))
    has_abba_in_hypernet_sequence = any(
        map(lambda s: abba.search(s), hypernet_sequences)
    )

    if has_abba and not has_abba_in_hypernet_sequence:
        tls.add(ip)

    for sn_sequence in supernet_sequences:
        matches = aba_bab.findall(sn_sequence)
        for match in matches:
            bab = "".join((match[0][1], match[0][0], match[0][1]))
            for hn_sequence in hypernet_sequences:
                if bab in hn_sequence:
                    ssl.add(ip)

print("Part 1:", len(tls))
print("Part 2:", len(ssl))
