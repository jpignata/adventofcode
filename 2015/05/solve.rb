# frozen_string_literal: true

def rulebook1(string)
  return unless %w[a e i o u].sum { |vowel| string.count(vowel) } >= 3
  return unless string =~ /.*([a-z])\1.*/
  return unless %w[ab cd pq xy].none? { |item| string.include?(item) }

  true
end

def rulebook2(string)
  return unless string =~ /.*([a-z][a-z]).*\1.*/
  return unless string =~ /.*([a-z])[a-z]\1.*/

  true
end

strings = ARGF.each_line.map(&:chomp)
part1 = 0
part2 = 0

strings.each do |string|
  part1 += 1 if rulebook1(string)
  part2 += 1 if rulebook2(string)
end

puts "Part 1: #{part1}"
puts "Part 2: #{part2}"
