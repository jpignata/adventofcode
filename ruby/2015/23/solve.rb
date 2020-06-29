# frozen_string_literal: true

class Computer
  def initialize(instructions, register_a = 0)
    @instructions = instructions
    @registers = { 'a' => register_a, 'b' => 0 }
    @pointer = 0
  end

  def run
    tick while pointer < instructions.size
    registers['b'] 
  end

  def tick
    command, operands = instructions[pointer]

    case command
    when 'hlf'
      registers[operands[0]] /= 2
    when 'tpl'
      registers[operands[0]] *= 3
    when 'inc'
      registers[operands[0]] += 1
    when 'jmp'
      return @pointer += operands[0]
    when 'jie'
      return @pointer += operands[1] if registers[operands[0]].even?
    when 'jio'
      return @pointer += operands[1] if registers[operands[0]] == 1
    end

    @pointer += 1
  end

  private

  attr_reader :registers, :instructions, :pointer
end

instructions = ARGF.each_line.map do |instruction|
  tokens = instruction.chomp.split(/,? /)
  command = tokens[0]
  operands = tokens[1..].map { |token| token =~ /[0-9]/ ? token.to_i : token }
  
  [command, operands]
end

puts "Part 1: #{Computer.new(instructions).run}"
puts "Part 2: #{Computer.new(instructions, 1).run}"
