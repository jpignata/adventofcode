import sys

banks = [line.strip() for line in sys.stdin]


def total(digits):
    def find(bank, digits):
        if digits == 1:
            return max(bank)

        next_digit = max(bank[: -digits + 1])
        next_index = bank.index(next_digit)

        return next_digit + find(bank[next_index + 1 :], digits - 1)

    return sum(int(find(bank, digits)) for bank in banks)


print("Part 1:", total(2))
print("Part 2:", total(12))
