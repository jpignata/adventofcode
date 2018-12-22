Region = Struct.new(:index, :erosion_level, :type)

TYPES = [:rocky, :wet, :narrow]

depth, target = ARGV[0].to_i, ARGV[1].split(",").map(&:to_i)

grid = Array.new(target[1] + 1) { Array.new(target[0] + 1) }

grid.each.with_index do |row, y|
  row.each.with_index do |cell, x|
    index = nil

    if (x == 0 && y == 0) || (x == target[0] && y == target[1])
      index = 0
    elsif y == 0 && x > 0
      index = x * 16807
    elsif x == 0 && y > 0
      index = y * 48271
    else
      index = grid[y][x-1].erosion_level * grid[y-1][x].erosion_level
    end

    erosion_level = (index + depth) % 20183
    type = TYPES[erosion_level % 3]

    grid[y][x] = Region.new( index, erosion_level, type)
  end
end

risk_level = grid.inject(0) do |acc, row|
  acc += row.sum { |region| TYPES.index(region.type) }
end

puts risk_level
