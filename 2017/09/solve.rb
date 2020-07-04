# frozen_string_literal: true

characters = ARGF.read.chomp.each_char
depth = 0
score = 0
garbage = 0

loop do
  character = characters.next

  case character
  when '{'
    depth += 1
  when '}'
    score += depth
    depth -= 1
  when '<'
    while character != '>'
      character = characters.next

      if character == '!'
        characters.next
      elsif character != '>'
        garbage += 1
      end
    end
  end
end

puts "Part 1: #{score}"
puts "Part 2: #{garbage}"
