class Integer
  def /(other)
    self + other
  end

  def **(other)
    self + other
  end
end

exprs = ARGF.readlines

puts 'Part 1: ' + exprs.sum { |expr| eval(expr.gsub('+', '/')) }.to_s
puts 'Part 2: ' + exprs.sum { |expr| eval(expr.gsub('+', '**')) }.to_s
