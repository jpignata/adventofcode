input = 556061
sequence = input.digits.reverse
answer_size = 10
scores = [3, 7]
elf1 = 0
elf2 = 1
count = scores.size
index = 0

1.step do |i|
  (scores[elf1] + scores[elf2]).digits.reverse.each do |d|
    scores << d
    count += 1
    index = sequence[index] == d ? index + 1 : 0

    if index == sequence.size
      puts count - sequence.size
      puts scores[input...input+answer_size].map(&:to_s).join
      exit
    end
  end

  elf1 = (elf1 + 1 + scores[elf1]) % scores.size
  elf2 = (elf2 + 1 + scores[elf2]) % scores.size
end
