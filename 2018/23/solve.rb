require 'z3'

def distance_between(p1, p2)
  (p1[0] - p2[0]).abs + (p1[1] - p2[1]).abs + (p1[2] - p2[2]).abs
end

def z3_distance_between(p1, p2)
  abs = -> x { Z3.IfThenElse(x >= 0, x, -x) }
  abs.call(p1[0] - p2[0]) + abs.call(p1[1] - p2[1]) + abs.call(p1[2] - p2[2])
end

Nanobot = Struct.new(:x, :y, :z, :radius) do
  def in_range(nanobots)
    nanobots.select { |nanobot| distance_from(nanobot) <= radius }
  end

  def distance_from(nanobot)
    distance_between(position, nanobot.position)
  end

  def position
    [x, y, z]
  end
end

nanobots = ARGF.readlines.map do |line|
  matches = /pos=<(-?\d*),(-?\d*),(-?\d*)>, r=(\d*)/.match(line)
  Nanobot.new(matches[1].to_i, matches[2].to_i, matches[3].to_i, matches[4].to_i)
end

puts nanobots.max_by(&:radius).in_range(nanobots).count

optimizer = Z3::Optimize.new 
x, y, z = Z3.Int('x'), Z3.Int('y'), Z3.Int('z')
bots_in_range = 0
distance_from_origin = z3_distance_between([0, 0, 0], [x, y, z])

nanobots.each do |nanobot|
  expr = z3_distance_between([x, y, z], nanobot.position) <= nanobot.radius
  bots_in_range += Z3.IfThenElse(expr, 1, 0)
end

optimizer.maximize(bots_in_range)
optimizer.minimize(distance_from_origin)
optimizer.check

model = optimizer.model

puts distance_between([0, 0, 0], [model[x].to_i, model[y].to_i, model[z].to_i])
