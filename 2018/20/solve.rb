Node = Struct.new(:x, :y, :distance) do
  def <=>(other)
    distance <=> other.distance
  end
end

class Map
  def initialize(x=500, y=500)
    @grid = []
    @context = []
    @current = Node.new(x, y, 0)
  end

  def walk(route)
    route.chars.each do |char|
      case char
      when "("
        @context.unshift(@current)
      when ")"
        @current = @context.shift
      when "|"
        @current = @context.first
      when "N"
        move(0, -1)
      when "S"
        move(0, 1)
      when "W"
        move(-1, 0)
      when "E"
        move(1, 0)
      end
    end

    self
  end

  def rooms
    @grid.flatten.compact
  end

  private

  def move(x, y)
    node = get(@current.x + x, @current.y + y)
    node.distance = [node.distance, @current.distance + 1].min
    @current = node
  end

  def get(x, y)
    @grid[y] ||= []
    @grid[y][x] ||= Node.new(x, y, Float::INFINITY)
  end
end

route = ARGF.readline.chomp
map = Map.new.walk(route)

puts map.rooms.max.distance
puts map.rooms.count { |room| room.distance >= 1000 }
