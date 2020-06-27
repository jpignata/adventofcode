boxes = ARGF.each_line.map do |dimensions|
  dimensions.chomp.split('x').map(&:to_i)
end

paper, ribbon = 0, 0

boxes.each do |length, width, height|
  sides = [length * width, width * height, height * length]
  paper += sides.sum { |side| 2 * side }
  paper += sides.min

  ribbon += [length, width, height].min(2).sum() * 2
  ribbon += length * width * height
end

puts "Part 1: #{paper}"
puts "Part 2: #{ribbon}"