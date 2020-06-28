DIRECTIONS = ARGF.read.chomp
MOVES = { '(' => 1, ')' => -1 }

def find(floor)
  current = 0

  DIRECTIONS.each_char.with_index do |direction, index|
    current += MOVES[direction]

    return index + 1 if current == floor
  end
end

destination = DIRECTIONS.count('(') - DIRECTIONS.count(')')

puts "Part 1: #{destination}"
puts "Part 2: #{find(-1)}"