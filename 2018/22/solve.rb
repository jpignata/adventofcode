require 'set'

Region = Struct.new(:x, :y, :index, :erosion_level, :type)
Edge = Struct.new(:from, :to, :weight, :start_equipment, :end_equipment)
Visit = Struct.new(:region, :equipment, :minutes)

TYPES = [:rocky, :wet, :narrow]

EQUIPMENT = {
  rocky: [:climbing_gear, :torch],
  wet: [:climbing_gear, :neither],
  narrow: [:torch, :neither]
}

depth, target = ARGV[0].to_i, ARGV[1].split(",").map(&:to_i)

grid = Array.new(target[1] * 2) { Array.new(target[0] * 2) }

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

edges = grid.map.with_index do |row, y|
  row.map.with_index do |region, x|
    adjacent = [[-1, 0], [1, 0], [0, -1], [0, 1]].map { |xdiff, ydiff|
      coords = [x + xdiff, y + ydiff]

      next if coords.any?(&:negative?)
      next if coords[0] > grid[0].length - 1
      next if coords[1] > grid.length - 1

      grid[coords[1]][coords[0]]
    }.compact

    adjacent.map { |other|
      EQUIPMENT[region.type].product(EQUIPMENT[other.type]).map do |eq1, eq2|
        weight = 1
        weight += 7 if eq1 != eq2
        Edge.new(region, other, weight, eq1, eq2)
      end
    }.flatten
  end
end

queue = []
routes = Hash.new(Float::INFINITY)

queue << Visit.new(grid[0][0], :torch, 0)

while queue.any?
  visit = queue.sort_by!(&:minutes).shift

  if visit.region == grid[target[1]][target[0]] && visit.equipment == :torch
    puts visit.minutes
    break
  end

  edges[visit.region.y][visit.region.x].each do |edge|
    next unless edge.start_equipment == visit.equipment

    distance = visit.minutes + edge.weight

    if routes[edge] > distance
      queue << Visit.new(edge.to, edge.end_equipment, distance)
      routes[edge] = distance
    end
  end
end

