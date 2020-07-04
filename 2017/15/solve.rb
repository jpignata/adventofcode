# frozen_string_literal: true

def generator(factor, value, multiple = 0)
  Enumerator.new do |e|
    loop do
      value = value * factor % 2_147_483_647
      next if multiple.positive? && value % multiple != 0

      e << value
    end
  end
end

def judge(factors, values, pairs, multiples = [0, 0])
  a = generator(factors[0], values[0], multiples[0])
  b = generator(factors[1], values[1], multiples[1])
  total = 0

  1.upto(pairs) do
    total += 1 if a.next & 0xFFFF == b.next & 0xFFFF
  end

  total
end

values = ARGF.each_line.map { |line| line.split[-1].to_i }

puts "Part 1: #{judge([16_807, 48_271], values, 40_000_000)}"
puts "Part 2: #{judge([16_807, 48_271], values, 5_000_000, [4, 8])}"
