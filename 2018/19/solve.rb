Program = Struct.new(:instructions, :ip)

class Device
  attr_accessor :ip
  attr_reader :registers

  def initialize(input = Array.new(6, 0))
    @registers = input.dup
  end

  def run(program, halt_at: -1)
    i = 0
    ip = registers[program.ip]
    instruction = program.instructions.first

    loop do
      break if ip >= program.instructions.length
      break if halt_at > 0 && i > halt_at

      instruction = program.instructions[ip]
      registers[program.ip] = ip
      start = registers.dup
      send(instruction[0], instruction[1..-1])
      ip = registers[program.ip] + 1
      i += 1
    end
  end

  private

  def addr((a, b, c))
    registers[c] = registers[a] + registers[b]
  end

  def addi((a, b, c))
    registers[c] = registers[a] + b
  end

  def mulr((a, b, c))
    registers[c] = registers[a] * registers[b]
  end

  def muli((a, b, c))
    registers[c] = registers[a] * b
  end

  def banr((a, b, c))
    registers[c] = registers[a] & registers[b]
  end

  def bani((a, b, c))
    registers[c] = registers[a] & b
  end

  def borr((a, b, c))
    registers[c] = registers[a] | registers[b]
  end

  def bori((a, b, c))
    registers[c] = registers[a] | b
  end

  def setr((a, b, c))
    registers[c] = registers[a] 
  end

  def seti((a, b, c))
    registers[c] = a
  end

  def gtir((a, b, c))
    registers[c] = a > registers[b] ? 1 : 0
  end

  def gtri((a, b, c))
    registers[c] = registers[a] > b ? 1 : 0
  end

  def gtrr((a, b, c))
    registers[c] = registers[a] > registers[b] ? 1 : 0
  end

  def eqir((a, b, c))
    registers[c] = a == registers[b] ? 1 : 0
  end

  def eqri((a, b, c))
    registers[c] = registers[a] == b ? 1 : 0
  end

  def eqrr((a, b, c))
    registers[c] = registers[a] == registers[b] ? 1 : 0
  end
end

instructions = []
ip = 0

ARGF.readlines.each do |line|
  if line.start_with?("#ip")
    ip = line.scan(/\d+/).first.to_i
  else
    instruction = line.chomp.split
    instructions << [instruction[0], *instruction[1..-1].map(&:to_i)]
  end
end

device = Device.new
program = Program.new(instructions, ip)
device.run(program)

puts device.registers[0]

[0, 1].each do |register|
  device = Device.new([register, 0, 0, 0, 0, 0])
  program = Program.new(instructions, ip)
  device.run(program, halt_at: 20)
  num = device.registers[4]

  puts 1 + num + (2..Math.sqrt(num)).
    select { |i| num % i == 0 }.
    sum { |i| [i, num / i].uniq.sum }
end
