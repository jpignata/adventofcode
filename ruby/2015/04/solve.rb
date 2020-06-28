# frozen_string_literal: true

require 'digest'

input = ARGF.read.chomp

def find(key, number_of_zeroes)
  zeroes = '0' * number_of_zeroes

  ('1'..).each do |number|
    md5 = Digest::MD5.new
    md5 << key + number

    return number if md5.hexdigest.start_with?(zeroes)
  end
end

puts "Part 1: #{find(input, 5)}"
puts "Part 2: #{find(input, 6)}"
