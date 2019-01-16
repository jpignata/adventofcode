from collections import namedtuple
from itertools import combinations


class Player:
    def __init__(self, hit_points, damage, armor):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

    def hit(self, damage):
        self.hit_points -= max(damage - self.armor, 0)

    def is_alive(self):
        return self.hit_points > 0


def equipment(shop):
    for weapon in shop['weapons']:
        yield [weapon]

        for armor in shop['armor']:
            yield [weapon, armor]

            for ring in shop['rings']:
                yield [weapon, ring]
                yield [weapon, armor, ring]

            for rings in combinations(shop['rings'], 2):
                yield [weapon, *rings]
                yield [weapon, armor, *rings]


def fight(player, boss):
    while boss.is_alive() and player.is_alive():
        boss.hit(player.damage)

        if boss.is_alive():
            player.hit(boss.damage)

    return player.hit_points > boss.hit_points


item = namedtuple('Item', ['cost', 'damage', 'armor'])
shop = dict()
shop['weapons'] = [item(8, 4, 0), item(10, 5, 0), item(25, 6, 0),
                   item(40, 7, 0), item(74, 8, 0)]
shop['armor'] = [item(13, 0, 1), item(31, 0, 2), item(53, 0, 3),
                 item(75, 0, 4), item(102, 0, 5)]
shop['rings'] = [item(25, 1, 0), item(50, 2, 0), item(100, 3, 0),
                 item(20, 0, 1), item(40, 0, 2), item(80, 0, 3)]
min_cost = float('inf')
max_cost = 0

for equipment in equipment(shop):
    damage = sum(e.damage for e in equipment)
    armor = sum(e.armor for e in equipment)
    cost = sum(e.cost for e in equipment)

    if fight(Player(100, damage, armor), Player(103, 9, 2)):
        min_cost = min(cost, min_cost)
    else:
        max_cost = max(cost, max_cost)

print('Part 1:', min_cost)
print('Part 2:', max_cost)
