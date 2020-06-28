boxes = ARGF.each_line.map do |dimensions|
  dimensions.chomp.split('x').map(&:to_i)
end

paper, ribbon = 0, 0

boxes.each do |dimensions|
  length, width, height = dimensions
  sides = [length * width, width * height, height * length]

  paper += sides.sum * 2
  paper += sides.min

  ribbon += dimensions.min(2).sum * 2
  ribbon += dimensions.inject(&:*)
end

puts "Part 1: #{paper}"
puts "Part 2: #{ribbon}"