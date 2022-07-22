import sys
from string import hexdigits as hex


def validate(passport):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def fields_present(p):
        return set(p.keys()) & required == required

    def byr(v):
        return v.isdigit() and 1920 <= int(v) <= 2002

    def iyr(v):
        return v.isdigit() and 2010 <= int(v) <= 2020

    def eyr(v):
        return v.isdigit() and 2020 <= int(v) <= 2030

    def hgt(v):
        if v[-2:] == "cm":
            return v[:-2].isdigit() and 150 <= int(v[:-2]) <= 193
        elif v[-2:] == "in":
            return v[:-2].isdigit() and 59 <= int(v[:-2]) <= 76
        else:
            return False

    def hcl(v):
        return len(v) == 7 and v[0] == "#" and all(c in hex for c in v[1:])

    def ecl(v):
        return v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def pid(v):
        return v.isdigit() and len(v) == 9

    if not fields_present(passport):
        return (False, False)

    for field in required:
        value = passport[field]

        if not locals()[field](value):
            return (True, False)

    return (True, True)


passport = {}
part1, part2 = 0, 0

for line in [line.strip() for line in sys.stdin.readlines()] + [""]:
    if len(line):
        for attr in line.strip().split(" "):
            field, value = attr.split(":")
            passport[field] = value
    else:
        fields_present, valid = validate(passport)
        passport = {}
        part1 += fields_present
        part2 += valid

print("Part 1:", part1)
print("Part 2:", part2)
