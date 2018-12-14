require 'curses'

MSG_HEIGHT = 9

Star = Struct.new(:x, :y, :vx, :vy) do
  def tick
    self.x += vx
    self.y += vy
  end
end

stars = ARGF.readlines.map do |line|
  match = line.scan(/-?[0-9]+[>,]+/)
  Star.new(*match.map(&:to_i))
end

1.step do |i|
  stars.each(&:tick)
  stars.sort_by!(&:y)
  
  if (stars.first.y - stars.last.y).abs == MSG_HEIGHT
    y_offset = stars.first.y
    x_offset = stars.map(&:x).min

    stars.each do |star|
      Curses.setpos(star.y - y_offset, star.x - x_offset)
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
