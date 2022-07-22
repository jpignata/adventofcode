import random


class Player:
    def __init__(self, hit_points, damage, armor, mana):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.mana = mana

    def deal(self, damage):
        self.hit_points -= max(damage - self.armor, 1)

    def heal(self, hit_points):
        self.hit_points += hit_points

    def lose(self, hit_points):
        self.hit_points -= hit_points

    def fortify(self, armor):
        self.armor += armor

    def weaken(self, armor):
        self.armor -= armor

    def recharge(self, mana):
        self.mana += mana

    def cast(self, mana):
        self.mana -= mana

    def alive(self):
        return self.hit_points > 0


class Spell:
    def __init__(
        self,
        cost,
        *,
        on_cast=[lambda p, b: None],
        on_apply=lambda p, b: None,
        on_end=lambda p, b: None,
        turns=0
    ):
        self.cost = cost
        self.on_cast = on_cast
        self.on_apply = on_apply
        self.on_end = on_end
        self.turns = turns
        self.timer = 0

    def apply(self):
        self.on_apply(self.player, self.boss)
        self.timer -= 1

        if not self.active():
            self.on_end(self.player, self.boss)

    def cast(self, player, boss):
        self.player = player
        self.boss = boss
        self.timer = self.turns
        player.cast(self.cost)

        for effect in self.on_cast:
            effect(self.player, self.boss)

        return self.cost

    def active(self):
        return self.timer > 0


class Spells:
    def __init__(self, spells):
        for spell in spells:
            spell.player = spell.boss = None
            spell.timer = 0

        self.spells = spells

    def select(self, mana):
        castable = filter(lambda s: not s.active(), self.spells)
        affordable = filter(lambda s: s.cost <= mana, castable)
        candidates = list(affordable)

        if len(candidates) == 0:
            return None

        return random.choice(candidates)

    def apply(self):
        for spell in filter(lambda s: s.active(), self.spells):
            spell.apply()


def fight(player, boss, spells, difficulty=0):
    spent = 0

    while player.alive() and boss.alive():
        player.lose(difficulty)

        if player.alive():
            spells.apply()

            if boss.alive():
                spell = spells.select(player.mana)

                if spell:
                    spent += spell.cast(player, boss)
                else:
                    return float("inf")

            if boss.alive():
                spells.apply()

            if boss.alive():
                player.deal(boss.damage)

    if not player.alive():
        return float("inf")

    return spent


magic_missle = Spell(53, on_cast=[lambda p, b: b.deal(4)])
drain = Spell(73, on_cast=[lambda p, b: b.deal(2), lambda p, b: p.heal(2)])
shield = Spell(
    113, on_cast=[lambda p, b: p.fortify(7)], on_end=lambda p, b: p.weaken(7), turns=6
)
poison = Spell(173, on_apply=lambda p, b: b.deal(3), turns=6)
recharge = Spell(229, on_apply=lambda p, b: p.recharge(101), turns=5)
lowest_cost = float("inf")
lowest_cost_on_hard = float("inf")

for i in range(10000):
    player = Player(50, 0, 0, 500)
    boss = Player(55, 8, 0, 0)
    spells = Spells([magic_missle, drain, shield, poison, recharge])
    cost = fight(player, boss, spells)
    lowest_cost = min(cost, lowest_cost)

for i in range(100000):
    player = Player(50, 0, 0, 500)
    boss = Player(55, 8, 0, 0)
    spells = Spells([magic_missle, drain, shield, poison, recharge])
    cost = fight(player, boss, spells, difficulty=1)
    lowest_cost_on_hard = min(cost, lowest_cost_on_hard)

print("Part 1:", lowest_cost)
print("Part 2:", lowest_cost_on_hard)
