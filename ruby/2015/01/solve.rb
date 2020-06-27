input = File.read('input.txt')
destination = input.count('(') - input.count(')')

puts "Part 1: #{destination}"

floor = 0

input.each_char.with_index do |direction, index|
  if direction == '('
    floor += 1
  else
    floor -= 1
  end

  if floor == -1
    puts "Part 2: #{index + 1}"
    break
  end
end