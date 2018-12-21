Program = Struct.new(:instructions, :ip)

class Device
  attr_accessor :ip
  attr_reader :registers

  def initialize(input = Array.new(6, 0))
    @registers = input.dup
  end

  def run(program)
    ip = registers[program.ip]
    instruction = program.instructions.first

    loop do
      break if ip >= program.instructions.length

      instruction = program.instructions[ip]
      registers[program.ip] = ip
      send(instruction[0], instruction[1..-1])
      yield registers[5] if ip == 28 if block_given?
      ip = registers[program.ip] + 1
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

program = Program.new(instructions, ip)
device = Device.new([0, 0, 0, 0, 0, 0])

candidates = []
device.run(program) do |candidate|
  if candidates.include?(candidate)
    puts
    puts "Part 1: #{candidates[0]}"
    puts "Part 2: #{candidates[-1]}"
    exit
  end

  candidates << candidate
  print "."
end
