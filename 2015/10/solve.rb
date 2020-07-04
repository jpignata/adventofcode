# frozen_string_literal: true

require 'strscan'

def length_of(sequence, iterations = 40)
  1.upto(iterations) do
    scanner = StringScanner.new(sequence)
    next_sequence = []

    until scanner.eos?
      digit = scanner.getch
      occurrences = 1

      while scanner.peek(1) == digit
        occurrences += 1
        scanner.getch
      end

      next_sequence.push(occurrences)
      next_sequence.push(digit)
    end

    sequence = next_sequence.join
  end

  sequence.size
end

sequence = ARGF.read.chomp

puts "Part 1: #{length_of(sequence)}"
puts "Part 2: #{length_of(sequence, 50)}"
