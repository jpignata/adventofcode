class Cart
  DIRS = [:<, :^, :>, :v]

  attr_accessor :x, :y, :direction, :turn

  def initialize(x, y, direction)
    self.x = x
    self.y = y
    self.direction = direction.to_sym
    self.turn = [-1, 0, 1].cycle
  end

  def go!(grid)
    case direction
    when :< then self.x -= 1
    when :> then self.x += 1
    when :^ then self.y -= 1
    when :v then self.y += 1
    end

    flip = [:<, :>].include?(self.direction) ? -1 : 1
    index = DIRS.index(direction)

    case grid[y][x]
    when "+"
      self.direction = DIRS[(index + turn.next) % DIRS.size]
    when "/"
      self.direction = DIRS[(index + 1) * flip % DIRS.size]
    when "\\"
      self.direction = DIRS[(index - 1) * flip]
    end
  end
end

carts = []
grid = ARGF.readlines.map.with_index do |line, y|
  line.split("").map.with_index do |character, x|
    case character
    when "^", "v", ">", "<"
      carts << Cart.new(x, y, character)
      ["v", "^"].include?(character) ? "|" : "-"
    when "|", "-", "/", "\\", "+"
      character
    end
  end
end

loop do
  carts.each do |cart|
    cart.go!(grid)

    carts.each do |other|
      next if cart == other

      if [cart.x, cart.y] == [other.x, other.y]
        puts "Boom @ #{[cart.x, cart.y]}"
        carts -= [cart, other]
      end
    end
  end

  if carts.size == 1
    puts "Last Cart @ #{[carts[0].x, carts[0].y]}"
    break
  end
end
