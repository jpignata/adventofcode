DIRECTIONS = ARGF.read.chomp
MOVES = {'(' => 1, ')' => -1}

def find_basement
  floor = 0

  DIRECTIONS.each_char.with_index do |direction, index|
    floor += MOVES[direction]

    return index + 1 if floor == -1
  end
end

destination = DIRECTIONS.count('(') - DIRECTIONS.count(')')

puts "Part 1: #{destination}"
puts "Part 2: #{find_basement}"