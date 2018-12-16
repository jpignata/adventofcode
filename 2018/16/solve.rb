opcodes = %i(addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr
              eqir eqri eqrr)

class Device
  attr_reader :registers

  def initialize(input = Array.new(4, 0))
    @registers = input.dup
  end

  def addr((op, a, b, c))
    registers[c] = registers[a] + registers[b]
  end

  def addi((op, a, b, c))
    registers[c] = registers[a] + b
  end

  def mulr((op, a, b, c))
    registers[c] = registers[a] * registers[b]
  end

  def muli((op, a, b, c))
    registers[c] = registers[a] * b
  end

  def banr((op, a, b, c))
    registers[c] = registers[a] & registers[b]
  end

  def bani((op, a, b, c))
    registers[c] = registers[a] & b
  end

  def borr((op, a, b, c))
    registers[c] = registers[a] | registers[b]
  end

  def bori((op, a, b, c))
    registers[c] = registers[a] | b
  end

  def setr((op, a, b, c))
    registers[c] = registers[c] = registers[a] 
  end

  def seti((op, a, b, c))
    registers[c] = registers[c] = a
  end

  def gtir((op, a, b, c))
    registers[c] = a > registers[b] ? 1 : 0
  end

  def gtri((op, a, b, c))
    registers[c] = registers[a] > b ? 1 : 0
  end

  def gtrr((op, a, b, c))
    registers[c] = registers[a] > registers[b] ? 1 : 0
  end

  def eqir((op, a, b, c))
    registers[c] = a == registers[b] ? 1 : 0
  end

  def eqri((op, a, b, c))
    registers[c] = registers[a] == b ? 1 : 0
  end

  def eqrr((op, a, b, c))
    registers[c] = registers[a] == registers[b] ? 1 : 0
  end
end

samples = []
instructions = []
in_sample = false

ARGF.readlines.each do |line|
  case line
  when /^Before: +\[([0-9, ]*)\]$/
    in_sample = true
    samples[samples.length] = { before: $1.split(", ").map(&:to_i).freeze }
  when /^After: +\[([0-9, ]*)\]$/
    in_sample = false
    samples[-1][:after] = $1.split(", ").map(&:to_i).freeze
  when /^([0-9 ]+)$/
    instruction = $1.split(" ").map(&:to_i).freeze

    if in_sample
      samples[-1][:instruction] = instruction
    else
      instructions << instruction
    end
  end
end

tests = samples.map { |sample|
  0.upto(opcodes.size-1).inject(Array.new) do |acc, idx|
    device = Device.new(sample[:before])
    device.send(opcodes[idx], sample[:instruction])

    acc << opcodes[idx] if device.registers == sample[:after]
    acc
  end
}
  
puts tests.count { |result| result.size >= 3 }

counts = Hash.new { |h, k| h[k] = Hash.new(0) }
ordered = []

tests.each.with_index { |test, i|
  test.each { |op| counts[samples[i][:instruction][0]][op] += 1 }
}

until ordered.compact.count == opcodes.size
  counts.each do |code, occurrences|
    next if ordered.include?(code)

    if occurrences.size == 1
      ordered[code] = occurrences.first.first
    else
      ordered.each { |key| occurrences.delete(key) }
    end
  end
end

device = Device.new

instructions.each do |instruction|
  device.send(ordered[instruction[0]], instruction)
end

p device.registers
