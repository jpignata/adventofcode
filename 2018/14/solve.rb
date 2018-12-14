input = 556061

answer_size = 10
scores = [3, 7]
elf1 = 0
elf2 = 1

1.upto((input + answer_size) * 100) do
  (scores[elf1] + scores[elf2]).digits.reverse.each { |d| scores << d }
  elf1 = (elf1 + 1 + scores[elf1]) % scores.size
  elf2 = (elf2 + 1 + scores[elf2]) % scores.size
end

puts scores[input...input+answer_size].map(&:to_s).join
puts scores.map(&:to_s).join.index(input.digits.reverse.map(&:to_s).join)
