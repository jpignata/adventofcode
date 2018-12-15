require 'set'

size = 1000
grid = size.times.map { |_| size.times.map { [] } }
candidates = Set.new

ARGF.readlines.each do |line|
  pattern = /#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)/
  captures = pattern.match(line).captures.map(&:to_i)
  id, x, y, w, h = captures

  candidates << id

  y.upto(y + h - 1) do |yi|
    x.upto(x + w - 1) do |xi|
      grid[yi][xi] << id

      if grid[yi][xi].count > 1
        candidates.subtract(grid[yi][xi])
      end
    end
  end
end

puts grid.inject(0) { |acc, row|
  acc += row.count { |cell| cell.count > 1 }
}

puts candidates.to_a
