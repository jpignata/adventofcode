area = ARGF.readlines.map { |line| line.chomp.chars }
values = []

0.upto(1000) do |i|
  next_area = area.map(&:dup)

  area.each.with_index do |row, y|
    row.each.with_index do |char, x|
      adjacent = [-1, 1, 0].product([-1, 1, 0]).map { |(dx, dy)|
        ax = x - dx
        ay = y - dy

        next if ax == x && ay == y
        next if ax < 0 || ax > area[0].length - 1
        next if ay < 0 || ay > area.length - 1

        area[ay][ax]
      }

      case char
      when "." then next_area[y][x] = "|" if adjacent.count("|") >= 3
      when "|" then next_area[y][x] = "#" if adjacent.count("#") >= 3
      when "#"
        if adjacent.include?("|") && adjacent.include?("#")
          next_area[y][x] = "#"
        else
          next_area[y][x] = "."
        end
      end
    end
  end

  area = next_area
  values[i] = area.sum { |r| r.count("#") } * area.sum { |r| r.count("|") }
end

puts values[9]

deltas = values.reverse.map.with_index { |value, i|
  values.reverse[i+1..-1].find_index { |other_value|
    value == other_value
  }
}.compact
period = deltas.max_by { |delta| deltas.count(delta) }
frequency = 1000000000 % period

puts values.reverse.detect.with_index { |value, i|
  (values.length - i) % period == frequency
}
