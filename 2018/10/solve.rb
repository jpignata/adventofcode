require 'curses'

MSG_HEIGHT = 9

Star = Struct.new(:position, :velocity) do
  def <=>(other)
    position.last <=> other.position.last
  end

  def tick
    position[0] += velocity[0]
    position[1] += velocity[1]
  end
end

stars = ARGF.readlines.map do |line|
  pattern = /position=< *(-?[0-9]+), *(-?[0-9]+)> velocity=< *(-?[0-9]+), *(-?[0-9]+)>/
  match = pattern.match(line)

  Star.new([match[1].to_i, match[2].to_i], [match[3].to_i, match[4].to_i]) 
end

1.step do |i|
  stars.each(&:tick)
  stars.sort!
  
  if (stars.first.position.last - stars.last.position.last).abs == MSG_HEIGHT
    y_offset = stars.first.position.last
    x_offset = stars.min_by { |s| s.position.first }.position.first

    stars.each do |star|
      Curses.setpos(star.position.last - y_offset, star.position.first - x_offset)
      Curses.addstr("#")
    end

    Curses.setpos(11, 0)
    Curses.addstr("Received in #{i} seconds")
    Curses.curs_set(0)
    Curses.getch
    Curses.clear

    break
  end
end
