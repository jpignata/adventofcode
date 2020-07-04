# frozen_string_literal: true

require 'set'

lines = ARGF.each_line.map(&:chomp)
cities = Set.new
routes = Set.new
connections = {}

lines.each do |line|
  from, _, to, _, distance = line.split(' ')
  distance = distance.to_i

  cities.add(from)
  cities.add(to)

  connections[from] ||= {}
  connections[to] ||= {}

  connections[from][to] = distance
  connections[to][from] = distance
end

stack = cities.map { |city| [city] }

until stack.empty?
  route = stack.pop
  current = route[-1]

  if route.size == cities.size
    distances = route[1..].map.with_index do |city, index|
      connections[route[index]][city]
    end
    routes.add(distances.sum)

    next
  end

  next unless connections.keys.include?(current)

  destinations = connections[current].keys - route

  destinations.each do |destination|
    stack.push(route + [destination])
  end
end

puts "Part 1: #{routes.min}"
puts "Part 1: #{routes.max}"
