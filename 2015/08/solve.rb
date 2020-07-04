# frozen_string_literal: true

require 'strscan'

code = 0
values = 0
encoded = 0

ARGF.each_line.map(&:chomp).each do |line|
  scanner = StringScanner.new(line)
  encoded += 2

  while scanner.rest?
    case scanner.getch
    when '"'
      code += 1
      encoded += 2
    when '\\'
      next_character = scanner.peek(1)

      if next_character == '"'
        scanner.getch
        code += 2
        values += 1
        encoded += 4
      elsif next_character == 'x'
        3.times { scanner.getch }
        code += 4
        values += 1
        encoded += 5
      elsif next_character == '\\'
        scanner.getch
        code += 2
        values += 1
        encoded += 4
      end
    else
      code += 1
      values += 1
      encoded += 1
    end
  end
end

puts "Part 1: #{code - values}"
puts "Part 2: #{encoded - code}"
