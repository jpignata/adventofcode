# frozen_string_literal: true

Wire = Struct.new(:input, :wires) do
  def output
    @output ||= signal
  end

  def reset
    @output = nil
  end

  attr_writer :output

  private

  def signal
    tokens = input.split(' ')

    if tokens.size == 1
      get(tokens[0])
    else
      case tokens.detect { |token| token =~ /[A-Z]/ }
      when 'NOT'
        2**16 - get(tokens[1]) - 1
      when 'AND'
        get(tokens[0]) & get(tokens[2])
      when 'OR'
        get(tokens[0]) | get(tokens[2])
      when 'LSHIFT'
        get(tokens[0]) << get(tokens[2])
      when 'RSHIFT'
        get(tokens[0]) >> get(tokens[2])
      end
    end
  end

  def get(token)
    token =~ /[0-9]/ ? token.to_i : wires[token].output
  end
end

lines = ARGF.each_line.map(&:chomp)
instructions = lines.map { |line| line.split(' -> ') }
wires = {}

instructions.each do |input, wire|
  wires[wire] = Wire.new(input, wires)
end

a = wires['a'].output
wires.each_value(&:reset)
wires['b'].output = a

puts "Part 1: #{a}"
puts "Part 2: #{wires['a'].output}"
