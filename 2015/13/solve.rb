require 'set'

lines = ARGF.each_line.map(&:chomp)
perferences = {}

lines.each do |line|
  tokens = line.split(' ')
  name = tokens[0]
  points = tokens[3].to_i
  points *= -1 if tokens[2] == 'lose'
  other_name = tokens[-1][0..-2]

  perferences[name] ||= {}
  perferences[name][other_name] = points
end

def optimal(preferences)
  permutations = preferences.keys.permutation
  changes = Set.new

  permutations.each do |guests|
    change = 0  

    guests.each.with_index do |attendee, index|
      left = guests[(index - 1) % guests.size]
      right = guests[(index + 1) % guests.size]

      change += preferences[attendee].fetch(left, 0)
      change += preferences[attendee].fetch(right, 0)
    end

    changes.add(change)
  end

  changes.max
end

puts "Part 1: #{optimal(perferences)}"
perferences['Host'] = {}
puts "Part 2: #{optimal(perferences)}"