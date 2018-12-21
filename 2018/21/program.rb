results = []

r5 = 0

loop do
  r4 = r5 | 65536
  r5 = ARGV[0].to_i

  loop do
    r5 = (((r5 + (r4 & 255)) & 16777215) * 65899) & 16777215
    break if r4 < 256
    r4 = r4 / 256
  end

  break if results.include?(r5)
  results.append(r5)
end

puts [results[0], results[-1]]
