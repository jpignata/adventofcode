require 'pqueue' # gem install pqueue

TYPES = [:rocky, :wet, :narrow]

Region = Struct.new(:x, :y, :index, :erosion_level, :type) do
  def allowed
    {
      rocky: [:climbing_gear, :torch],
      wet: [:climbing_gear, :neither],
      narrow: [:torch, :neither]
    }[type]
  end
end

depth, target = ARGV[0].to_i, ARGV[1].split(",").map(&:to_i)
grid = Array.new(target[1] + 20) { Array.new(target[0] + 20) }

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

    grid[y][x] = Region.new(x, y, index, erosion_level, type)
  end
end

risk_level = grid[0..target[1]].inject(0) do |acc, row|
  acc += row[0..target[0]].sum { |region| TYPES.index(region.type) }
end

puts risk_level

queue = PQueue.new { |a, b| a.last < b.last }
distance_to = Hash.new(Float::INFINITY)
finish = [target[0], target[1], :torch]

queue.push([0, 0, :torch, 0])

until queue.empty?
  x, y, equipment, minutes = *queue.pop
  current = grid[y][x]
  key = [x, y, equipment]

  next if distance_to[key] <= minutes

  if key == finish
    puts minutes
    break
  end

  current.allowed.each do |allowed|
    queue.push([x, y, allowed, minutes + 7]) if equipment != allowed
  end

  [[-1, 0], [1, 0], [0, -1], [0, 1]].each do |xdiff, ydiff|
    nx, ny = x + xdiff, y + ydiff

    next if [nx, ny].any?(&:negative?)
    next if nx > grid[0].length - 1
    next if ny > grid.length - 1

    queue.push([nx, ny, equipment, minutes + 1]) if grid[ny][nx].allowed.include?(equipment)
  end

  distance_to[key] = minutes
end
