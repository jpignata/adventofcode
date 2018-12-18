require 'set'

class Ground
  attr_reader :clay, :spring, :flowing, :settled, :ymax, :xmax, :visited, :xmin

  def initialize(clay, spring)
    @spring = spring
    @visited = Set.new(clay)
    @clay = Set.new(clay)
    @flowing = Set.new
    @settled = Set.new
    @xmax = clay.map(&:first).max + 1
    @xmin = clay.map(&:first).min
    @ymax = clay.map(&:last).max
  end

  def draw(start = 0, rows = nil)
    (start..(start+(rows || ymax))).each do |y|
      (xmin..xmax).each do |x|
        if spring == [x, y]
          print "+"
        elsif clay.include?([x, y])
          print "#"
        elsif settled.include?([x, y])
          print "~"
        elsif flowing.include?([x, y])
          print "|"
        else
          print "."
        end
      end

      print "\n"
    end

  end

  def fill(x, y)
    return if y > ymax
    return if clay.include?([x, y])

    if clay.include?(below(x, y)) || settled.include?(below(x, y))
      if reservoir?(x, y)
        fill_line(x, y)
        fill(x, y-1)
      else
        i = 0
        found = 0
        direction = 1
        nextpt = [x, y]

        loop do
          break if found == 2

          nextpt = [x + i * direction, nextpt[1]]

          if clay.include?(nextpt)
            found += 1
            direction *= -1
            i = 0
            next
          elsif settled.include?(nextpt)
            return
          elsif !visited.include?(below(*nextpt))
            fill(*nextpt)
            found += 1
            direction *= -1
            i = 0
            next
          elsif flowing.include?(below(*nextpt))
            found += 1
            direction *= -1
            i = 0
            next
          end

          flowing.add(nextpt)
          visited.add(nextpt)

          i += 1
        end

        if reservoir?(x, y)
          fill_line(x, y)
          fill(x, y-1)
        end
      end
    else
      flowing.add([x, y])
      visited.add([x, y])
      fill(*below(x, y))
    end
  end

  def fill_line(x, y)
    settled.add([x, y])
    flowing.delete([x, y])
    visited.add([x, y])

    i = 0
    found = 0
    direction = 1

    loop do
      break if x + i * direction  > xmax

      nextpt = [x + i * direction, y]

      if clay.include?(nextpt)
        found += 1
        direction *= -1
        i = 0
        next
      end

      settled.add(nextpt)
      flowing.delete(nextpt)
      visited.add(nextpt)

      i += 1

      return if found == 2
    end
  end

  def reservoir?(x, y)
    i = 0
    found = 0
    direction = 1

    loop do
      break if x + i * direction > xmax

      candidate = [x + i * direction, y]

      break unless visited.include?(below(*candidate))

      if clay.include?(candidate)
        found += 1
        direction *= -1
        i = 0
        next
      end

      i += 1

      return true if found == 2
    end

    false
  end

  def below(x, y)
    [x, y+1]
  end

  def above(x, y)
    [x, y-1]
  end

  def water
    (flowing + settled)
  end
end

spring = [500, 0]

clay = ARGF.readlines.map { |line|
  line.chomp.split(", ").sort.map { |part|
    val = part[2..-1]
    val.include?(".") ? Range.new(*val.split("..").map(&:to_i)) : val.to_i
  }
}.flat_map { |coords|
  Array(coords[0]).product(Array(coords[1])).map { |x, y| [x, y] }
}

ymin = clay.map(&:last).min

ground = Ground.new(clay, spring)
ground.fill(spring[0], spring[1]+ymin)
ground.draw

p [ground.water.count, ground.settled.count]
