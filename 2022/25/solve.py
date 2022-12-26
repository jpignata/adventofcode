import sys


def solve():
    total = 0

    for line in sys.stdin:
        total += to_decimal(line.strip())

    print("Part 1:", to_snafu(total))


def to_decimal(snafu):
    decimal = 0

    for i, char in enumerate(snafu[::-1]):
        multiplicand = max(1, 5**i)

        match char:
            case "0" | "1" | "2":
                multiplier = int(char)
            case "-":
                multiplier = -1
            case "=":
                multiplier = -2

        decimal += multiplicand * multiplier

    return decimal


def to_snafu(decimal):
    if not decimal:
        return ""

    match decimal % 5:
        case 0 | 1 | 2:
            return to_snafu(decimal // 5) + str(decimal % 5)
        case 3:
            return to_snafu(decimal // 5 + 1) + "="
        case 4:
            return to_snafu(decimal // 5 + 1) + "-"


if __name__ == "__main__":
    solve()
