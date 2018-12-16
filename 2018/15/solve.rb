Unit = Struct.new(:team, :x, :y, :hit_points) do
  def hit!(attack)
    self.hit_points -= attack
  end

  def dead?
    hit_points <= 0
  end

  def elf?
    team == "E"
  end
end

Position = Struct.new(:x, :y, :map) do
  def paths
    adjacent.select(&:open?)
  end

  def adjacent
    [
      [x, y - 1],
      [x, y + 1],
      [x - 1, y],
      [x + 1, y]
    ].reject { |coords|
      coords.any?(&:negative?)
    }.sort { |a, b|
      a.reverse <=> b.reverse
    }.map { |coords|
      Position.new(*coords, map)
    }
  end

  def open?
    map[y][x]
  end
end

units = []

map = ARGF.readlines.map.with_index do |line, y|
  line.chars.map.with_index { |object, x|
    case object
    when "." then true
    when "#" then false
    when "E", "G"
      units << Unit.new(object, x, y, 200)
      true
    end
  }.compact
end

def run(map, units, elf_attack_power: 3, debug: true, halt_on_death: false)
  debug("Initial", map, units) if debug
  rounds = 0

  loop do
    units.sort! { |a, b| [a.y, a.x] <=> [b.y, b.x] }

    units.each do |unit|
      next if unit.dead?

      targets = units.select { |u| u.team != unit.team }.reject(&:dead?)

      if targets.none?
        units.reject!(&:dead?)
        debug("Final", map, units) if debug
        puts "Rounds: #{rounds}"
        puts "Hit Points: #{units.sum(&:hit_points)}"
        puts "Outcome: #{rounds * units.sum(&:hit_points)}"
        return true
      end

      curr = map.map(&:dup)
      units.reject(&:dead?).each { |u| curr[u.y][u.x] = false }
      positions = curr.map.with_index do |row, y|
        row.map.with_index do |open, x|
          Position.new(x, y, curr)
        end
      end

      source = positions[unit.y][unit.x]

      if targets.none? { |t| positions[t.y][t.x].adjacent.include?(source) }
        visited = []
        queue = []
        route_to = {}

        visited << source
        queue << source

        while queue.any?
          current_position = queue.shift
          current_position.paths.each do |position|
            next if visited.include?(position)
            visited << position
            queue << position
            route_to[position] = current_position
          end
        end

        candidates = targets.flat_map { |target|
          positions[target.y][target.x].paths.map do |candidate|
            next unless visited.include?(candidate)
            target = candidate
            path = []

            while target != source
              path.unshift(target)
              target = route_to[target]
            end

            [path.size, path.first]
          end
        }.compact.sort { |a,b| [a[0],a[1].y,a[1].x] <=> [b[0], b[1].y, b[1].x] }

        if candidates.size > 0
          unit.x, unit.y = candidates[0][1].x, candidates[0][1].y
        end
      end

      opponent = targets.select { |target|
        positions[unit.y][unit.x].adjacent.include?(positions[target.y][target.x])
      }.sort_by(&:hit_points).first

      if opponent
        opponent.hit!(unit.elf? ? elf_attack_power : 3)
 
        if halt_on_death && opponent.elf? && opponent.dead?
          puts "An elf died; bailing..."
          return false
        end
      end
    end

    rounds += 1

    units.reject!(&:dead?)

    debug("After #{rounds}", map, units) if debug
  end
end

def debug(msg, map, units)
  puts msg + ": \n\n"

  map.each.with_index do |row, y|
    row.each.with_index do |cell, x|
      unit = units.detect { |u|u.x == x && u.y == y }

      if unit
        print unit.team
      elsif cell
        print "."
      else
        print "#"
      end
    end

    print "   "

    print units.select { |u| u.y == y }.sort_by(&:x).map { |u|
      "#{u.team}(#{u.hit_points})"
    }.join(", ")

    print "\n"
  end

  puts
end

puts "Part 1"

run(map, units.map(&:dup), debug: false)

puts

puts "Part 2"

lowest_winning = (4..100).bsearch do |attack_points|
  puts "> Trying #{attack_points} attack points"
  run(map, units.map(&:dup), elf_attack_power: attack_points, halt_on_death: true, debug: false)
end
