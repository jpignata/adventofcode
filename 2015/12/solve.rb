# frozen_string_literal: true

require 'json'

document = ARGF.read.chomp
parsed = JSON.parse(document)
numbers = document.scan(/-?[0-9]+/).map(&:to_i)

def sum(object)
  total = 0

  case object
  when Hash
    total += sum(object.values) unless object.values.include?('red')
  when Array
    total += object.map { |item| sum(item) }.sum
  when Integer
    total += object
  end

  total
end

puts "Part 1: #{numbers.sum}"
puts "Part 2: #{sum(parsed)}"
