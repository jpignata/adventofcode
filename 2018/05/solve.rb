polymer = ARGF.readlines.first.chomp

def react(polymer)
  units = [""]

  polymer.chars.each do |char|
    if char != units[-1] && char.downcase == units[-1].downcase
      units.pop
    else
      units.append(char)
    end
  end

  units.join.length
end

puts react(polymer)
puts ("a".."z").map { |t| polymer.gsub(/#{t}/i, "") }.map { |p| react(p) }.min
