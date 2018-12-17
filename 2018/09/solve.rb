Player = Struct.new(:score)
Marbles = Struct.new(:list) do
  def rotate(n)
    if n > 0
      n.times { list.unshift(list.pop) }
    else
      n.abs.times { list.append(list.shift) }
    end
  end

  def add(marble)
    list.unshift(marble)
  end

  def take
    list.shift
  end
end

marbles = Marbles.new([0])
next_marble = 1
number_of_players, last_marble = *ARGV.map(&:to_i)
players = number_of_players.times.map { Player.new(0) }
turn = players.cycle

loop do
  player = turn.next

  if next_marble % 23 == 0
    player.score += next_marble
    marbles.rotate(-7)
    player.score += marbles.take
    marbles.rotate(1)
  else
    marbles.rotate(1)
    marbles.add(next_marble)
  end

  break if next_marble == last_marble

  next_marble += 1
end
  
puts players.map(&:score).max
