# frozen_string_literal: true

def turn_on_corners(grid)
  grid[0][0] = '#'
  grid[0][grid[0].size - 1] = '#'
  grid[grid.size - 1][0] = '#'
  grid[grid.size - 1][grid[0].size - 1] = '#'
end

def generate(grid, *, broken: false, iterations: 100)
  1.upto(iterations) do |_gen|
    turn_on_corners(grid) if broken

    next_grid = Array.new(grid.size) { Array.new(grid[0].size, '.') }

    grid.each.with_index do |row, y|
      row.each.with_index do |cell, x|
        cells = [0, 1, -1].repeated_permutation(2).to_a.map do |deltax, deltay|
          newx = x + deltax
          newy = y + deltay

          next if newx == x && newy == y
          next if newy.negative? || newy >= grid.size
          next if newx.negative? || newx >= grid[0].size

          grid[newy][newx]
        end

        on = cells.compact.count('#')

        if cell == '#'
          next_grid[y][x] = [2, 3].include?(on) ? '#' : '.'
        elsif cell == '.'
          next_grid[y][x] = on == 3 ? '#' : '.'
        end
      end
    end

    grid = next_grid
  end

  turn_on_corners(grid) if broken
  grid.map { |row| row.count('#') }.sum
end

grid = ARGF.each_line.map do |line|
  line.chomp.each_char.to_a
end

puts "Part 1: #{generate(grid)}"
puts "Part 2: #{generate(grid, broken: true)}"
