class Computer
  def initialize(instructions, c=0)
    @instructions = instructions
    @registers = {'a' => 0, 'b' => 0, 'c' => c, 'd' => 0}
    @ip = 0
  end

  def run    
    send(*@instructions[@ip].split) while @ip < @instructions.size
    @registers['a']
  end

  private

  def cpy(src, dest)
    @registers[dest] = src =~ /[0-9]/ ? src.to_i : @registers[dest] = @registers[src]
    @ip += 1
  end

  def inc(register)
    @registers[register] += 1
    @ip += 1
  end

  def dec(register)
    @registers[register] -= 1
    @ip += 1
  end

  def jnz(src, offset)
    integer = src =~ /[0-9]/ ? src.to_i : @registers[src]

    if integer != 0
      @ip += offset.to_i
    else
      @ip += 1
    end
  end
end

instructions = ARGF.each_line.map(&:chomp)

puts "Part 1: #{Computer.new(instructions).run}"
puts "Part 2: #{Computer.new(instructions, 1).run}"