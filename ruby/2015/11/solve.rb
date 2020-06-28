# frozen_string_literal: true

def valid?(password)
  return false unless straight?(password)
  return false if password =~ /[iol]/
  return false unless password =~ /.*([a-z])\1.*([a-z])\2.*/

  true
end

# Passwords must include one increasing straight of at least three letters,
# like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd
# doesn't count.
def straight?(password)
  password[1..-2].each_char.with_index do |character, index|
    return true if password[index].next == character && character.next == password[index + 2]
  end

  false
end

def find(password)
  loop do
    password = password.next

    return password if valid?(password)
  end
end

password = ARGF.read.chomp
next_password = find(password)

puts "Part 1: #{next_password}"
puts "Part 2: #{find(next_password)}"
