# frozen_string_literal: true

Item = Struct.new(:name, :cost, :damage, :armor)

Player = Struct.new(:hit_points, :damage, :armor) do
  def alive?
    hit_points.positive?
  end

  def damage!(hit_points)
    self.hit_points -= [hit_points - armor, 0].max
  end
end

def combinations
  shop = {
    weapons: [
      Item.new('Dagger', 8, 4, 0),
      Item.new('Shortsword', 10, 5, 0),
      Item.new('Warhammer', 25, 6, 0),
      Item.new('Longsword', 40, 7, 0),
      Item.new('Greataxe', 74, 8, 0)
    ],

    armor: [
      Item.new('Leather', 13, 0, 1),
      Item.new('Chainmail', 31, 0, 2),
      Item.new('Splintmail', 53, 0, 3),
      Item.new('Bandedmail', 75, 0, 4),
      Item.new('Platemail', 102, 0, 5)
    ],

    rings: [
      Item.new('Damage +1', 25, 1, 0),
      Item.new('Damage +2', 50, 2, 0),
      Item.new('Damage +3', 100, 3, 0),
      Item.new('Defense +1', 20, 0, 1),
      Item.new('Defense +2', 40, 0, 2),
      Item.new('Defense +3', 80, 0, 3)
    ]
  }

  Enumerator.new do |enum|
    shop[:weapons].each do |weapon|
      enum << [weapon]

      shop[:armor].each do |armor|
        enum << [weapon, armor]

        shop[:rings].each do |ring|
          enum << [weapon, ring]
          enum << [weapon, armor, ring]
        end

        shop[:rings].combination(2).each do |rings|
          enum << [weapon, *rings]
          enum << [weapon, armor, *rings]
        end
      end
    end
  end
end

min_cost = Float::INFINITY
max_cost = 0

combinations.each do |equipment|
  cost = equipment.sum(&:cost)
  damage = equipment.sum(&:damage)
  armor = equipment.sum(&:armor)

  boss = Player.new(104, 8, 1)
  me = Player.new(100, damage, armor)

  while boss.alive? && me.alive?
    boss.damage!(me.damage)
    me.damage!(boss.damage) if boss.alive?
  end

  if me.alive?
    min_cost = [cost, min_cost].min
  else
    max_cost = [cost, max_cost].max
  end
end

puts "Part 1: #{min_cost}"
puts "Part 2: #{max_cost}"
