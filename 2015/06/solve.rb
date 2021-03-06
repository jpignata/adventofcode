# frozen_string_literal: true

RULES = ARGF.each_line.map do |direction|
  tokens = direction.split(' ')

  if tokens[0] == 'toggle'
    command = :toggle
    start_at_token = 1
    end_at_token = 3
  else
    command = tokens[1].to_sym
    start_at_token = 2
    end_at_token = 4
  end

  start_at = tokens[start_at_token].split(',').map(&:to_i)
  end_at = tokens[end_at_token].split(',').map(&:to_i)

  [command, start_at, end_at]
end

def flip
  grid = Array.new(1000).map { Array.new(1000, 0) }

  RULES.each do |command, start_at, end_at|
    (start_at[1]..end_at[1]).each do |y|
      (start_at[0]..end_at[0]).each do |x|
        yield command, grid, x, y
      end
    end
  end

  grid.sum(&:sum)
end

part1 = flip do |command, grid, x, y|
  case command
  when :toggle
    grid[y][x] ^= 1
  when :on
    grid[y][x] = 1
  when :off
    grid[y][x] = 0
  end
end

part2 = flip do |command, grid, x, y|
  case command
  when :toggle
    grid[y][x] += 2
  when :on
    grid[y][x] += 1
  when :off
    grid[y][x] -= 1 if grid[y][x].positive?
  end
end

puts "Part 1: #{part1}"
puts "Part 2: #{part2}"
