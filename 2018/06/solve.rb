coords = ARGF.readlines.map { |line| line.split(", ").map(&:to_i) }

grid = (0..coords.map(&:last).max).map do
  (0..coords.map(&:first).max + 1).map { [] }
end

coords.each.with_index do |(x, y), i|
  grid.each.with_index do |row, yi|
    row.each.with_index do |cell, xi|
      distance = (x - xi).abs + (y - yi).abs
      cell.push([i, distance])
    end
  end
end

regions = grid.map do |row|
  row.map do |cell|
    next cell unless cell.respond_to?(:min_by)

    a, b = cell.min_by(2, &:last)
    next if a[1] == b[1]
    a[0]
  end
end

candidates = regions.flatten.uniq

regions.each.with_index { |row, ri|
  if ri == 0 || ri == regions.length - 1
    row.each { |cell| candidates.delete(cell) }
  else
    candidates.delete(row[0])
    candidates.delete(row[-1])
  end
}

areas = candidates.map { |candidate|
  regions.inject(0) { |acc, row|
    acc += row.count(candidate)
  }
}

puts areas.max

all = grid.map do |row|
  row.map { |cell| cell.sum(&:last) }
end

puts all.sum { |row|
  row.count { |cell| cell < 10000 }
}
