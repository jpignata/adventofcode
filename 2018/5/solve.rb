polymer = ARGF.readlines.first.chomp
pairs = ("A".."Z").map { |char|
  [char, char.downcase].permutation.map { |c1, c2| "(#{c1}#{c2})" }.join("|")
}.join("|")
pattern = Regexp.new(pairs)
units = {}

def react(polymer, pattern)
  polymer.dup.tap do |polymer|
    while polymer.match(pattern)
      polymer.gsub!(pattern, "")
    end
  end
end

puts react(polymer, pattern).length

("A".."Z").map do |char|
  reacted = react(polymer, /#{char}/i)
  reacted = react(reacted, pattern)
  units[char] = reacted.length
end

puts units.sort_by(&:last).first
