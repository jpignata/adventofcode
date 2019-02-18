def cook(scores=[3, 7], elf1=0, elf2=1):
    while True:
        total = scores[elf1] + scores[elf2]

        if total >= 10:
            digits = divmod(total, 10)
        else:
            digits = (total,)

        for digit in digits:
            scores.append(digit)

            if scores[-6:] == [5, 5, 6, 0, 6, 1]:
                return scores

        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)


scores = cook()

print('Part 1:', ''.join(map(str, scores[556061:556061+10])))
print('Part 2:', len(scores) - 6)
