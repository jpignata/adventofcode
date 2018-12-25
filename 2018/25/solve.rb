def distance(a, b)
  (a[0] - b[0]).abs + (a[1] - b[1]).abs + (a[2] - b[2]).abs + (a[3] - b[3]).abs
end

coordinates = ARGF.readlines.map { |line| line.split(",").map(&:to_i) }
constellations = []

coordinates.each do |coords|
  matches = constellations.select { |points|
    points.any? { |point| distance(coords, point) <= 3 }
  }

  if matches.none?
    constellations << [coords]
    next
  end

  matches.each { |match| constellations.delete(match) }

  constellation = matches.inject(:+)
  constellation << coords
  constellations << constellation
end

puts constellations.count
