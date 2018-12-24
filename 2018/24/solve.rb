def index(armies, group)
  armies.each do |army|
    return [army.name, army.groups.index(group) + 1] if army.groups.index(group)
  end
end

def boost(armies, boost)
  clone = armies.map(&:clone)
  clone.detect { |army| army.name == "Immune System" }.boost(boost)
  clone
end

Army = Struct.new(:name, :groups) do
  def alive
    groups.select(&:alive?)
  end

  def selection_order
    alive.sort do |a, b|
      [b.effective_power, b.initiative] <=> [a.effective_power, a.initiative]
    end end

  def alive?
    groups.any?(&:alive?)
  end

  def dead?
    groups.none?(&:alive?)
  end

  def clone
    Army.new(name, groups.map(&:dup))
  end

  def boost(i)
    self.groups = groups.map do |group|
      group.attack_damage += i
      group
    end
  end
end

Group = Struct.new(:units, :hit_points, :weaknesses, :immunities, :attack_damage, :attack_type, :initiative) do
  def alive?
    units > 0
  end

  def effective_power
    [units * attack_damage, 0].max
  end

  def damage_to(group)
    return effective_power * 2 if group.weaknesses.include?(attack_type)
    return 0 if group.immunities.include?(attack_type)

    effective_power
  end
end

armies = []
army = nil

ARGF.readlines.each do |line|
  if line =~ /^([\w ]+):$/
    army = Army.new($1, [])
    armies << army
  elsif line =~ /^(\d+) units each with (\d+) hit points ?(\(([\w,; ]+)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)$/
    units = $1.to_i
    hit_points = $2.to_i
    aspects = $4 || ""
    attack_damage = $5.to_i
    attack_type = $6.to_sym
    initiative = $7.to_i
    weaknesses = []
    immunities = []

    aspects.split("; ").each do |aspect|
      if aspect.start_with?("weak to")
        weaknesses = aspect.gsub("weak to ", "").split(", ").map(&:to_sym)
      elsif aspect.start_with?("immune to")
        immunities = aspect.gsub("immune to ", "").split(", ").map(&:to_sym)
      end
    end

    army.groups << Group.new(units, hit_points, weaknesses, immunities,
                             attack_damage, attack_type, initiative)
  end
end

def run(armies, verbose: false)
  loop do
    if verbose
      armies.each do |army|
        puts "#{army.name}:"
        puts "No groups remain." if army.dead?

        army.alive.each do |group|
          puts "Group #{index(armies, group)[1]} contains #{group.units} units"
        end
      end
    end

    if armies.any?(&:dead?)
      army = armies.detect(&:alive?)

      return [army.name, army.alive.sum(&:units)]
    end

    puts if verbose

    battles = []

    armies.reverse.each do |army|
      other_army = armies.detect { |other| other != army }
      targets = other_army.alive

      army.selection_order.each do |group|
        group_details = index(armies, group)

        candidates = targets.map { |target|
          target_details = index(armies, target)
          damage = group.damage_to(target)
          sort = [damage, target.effective_power, target.initiative]

          if verbose
            puts "#{group_details[0]} group #{group_details[1]} would deal defending group #{target_details[1]} #{damage} damage" 
          end

          [target, sort]
        }.sort_by(&:last)

        if candidates.any?
          damage = candidates[-1][1][0] 
          target = candidates[-1][0]

          if damage > 0
            targets.delete(target)
            battles << [group, target]
          end
        end
      end
    end

    puts if verbose

    battles.sort_by! { |group, _| group.initiative * -1 }

    total_killed = 0

    battles.each do |group, target|
      next unless group.alive?

      group_details = index(armies, group)
      target_details = index(armies, target)

      damage = group.damage_to(target)
      before = target.units
      killed = (damage / target.hit_points).floor
      target.units -= killed
      total_killed += [before, killed].min

      if verbose
        puts "#{group_details[0]} group #{group_details[1]} attacks defending group #{target_details[1]}, killing #{[before, killed].min} units"
      end
    end

    return [] if total_killed == 0

    puts if verbose
  end
end

boost = 0

loop do
  puts "Trying #{boost}..."

  boosted = boost(armies, boost)
  result = run(boosted)

  if boost == 0
    puts "Part 1: #{result[1]}"
  end

  if result[0] == "Immune System"
    puts "Part 2: #{result[1]}"
    exit
  end

  boost += 1
end
