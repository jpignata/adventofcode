# frozen_string_literal: true

class Reindeer
  attr_reader :distance, :score

  def initialize(speed, fly_duration, rest_duration)
    @speed = speed
    @durations = { fly: fly_duration, rest: rest_duration }
    @states = %i[fly rest].cycle
    @distance = 0
    @score = 0

    next_state!
  end

  def tick!
    @distance += @speed if flying?
    @timer -= 1

    next_state! if @timer.zero?
  end

  def award!
    @score += 1
  end

  private

  def flying?
    @state == :fly
  end

  def next_state!
    @state = @states.next
    @timer = @durations[@state]
  end
end

lines = ARGF.each_line.map(&:chomp)
reindeer = lines.map do |line|
  tokens = line.split(' ')
  speed = tokens[3].to_i
  fly_duration = tokens[6].to_i
  rest_duration = tokens[13].to_i

  Reindeer.new(speed, fly_duration, rest_duration)
end

1.upto(2503) do
  reindeer.each(&:tick!)

  max = reindeer.map(&:distance).max
  winners = reindeer.select { |r| r.distance == max }

  winners.each(&:award!)
end

puts "Part 1: #{reindeer.map(&:distance).max}"
puts "Part 2: #{reindeer.map(&:score).max}"
