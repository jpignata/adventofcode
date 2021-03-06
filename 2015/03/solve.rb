# frozen_string_literal: true

require 'set'

DIRECTIONS = ARGF.read.chomp
MOVES = { '^' => [0, -1], 'v' => [0, 1], '>' => [1, 0], '<' => [-1, 0] }.freeze

Santa = Struct.new(:x, :y) do
  def position
    [x, y]
  end

  def move(delta)
    self.x += delta[0]
    self.y += delta[1]
  end
end

def deliver(number_of_santas = 1)
  santas = number_of_santas.times.map { Santa.new(0, 0) }.cycle
  visited = Set.new([[0, 0]])

  DIRECTIONS.each_char do |direction|
    santa = santas.next

    santa.move(MOVES[direction])
    visited.add(santa.position)
  end

  visited.size
end

puts "Part 1: #{deliver}"
puts "Part 2: #{deliver(2)}"
