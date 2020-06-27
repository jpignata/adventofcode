directions = ARGF.read
destination = directions.count('(') - directions.count(')')

floor = 0
basement = 0

directions.each_char.with_index do |direction, index|
  floor += {'(' => 1, ')' => -1}[direction]

  if floor == -1
    basement = index + 1
    break
  end
end


puts "Part 1: #{destination}"
puts "Part 2: #{basement}"