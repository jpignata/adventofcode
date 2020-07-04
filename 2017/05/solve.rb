# frozen_string_literal: true

def run(offsets)
  offsets = offsets.dup
  pointer = 0
  steps = 0

  while pointer < offsets.size
    next_pointer = pointer + offsets[pointer]
    offsets[pointer] = yield(offsets[pointer])
    pointer = next_pointer
    steps += 1
  end

  steps
end

offsets = ARGF.each_line.map(&:to_i)

part1 = run(offsets) { |offset| offset + 1 }
part2 = run(offsets) { |offset| offset >= 3 ? offset - 1 : offset + 1 }

puts "Part 1: #{part1}"
puts "Part 2: #{part2}"
