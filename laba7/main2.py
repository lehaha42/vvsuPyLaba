class Character:
    def __init__(self, name, hp, mp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.abilities = []
        self.items = []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        damage = damage / (1 + self.defense/20)
        if damage < self.hp:
            self.hp -= damage
            print(f"{self.name} gets {damage} points of damamge; HP: ({self.hp}/{self.max_hp})")
        else:
            self.hp = 0
            print(f"{self.name} died")

    def restore_hp(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} restores {amount} HP; HP: ({self.hp}/{self.max_hp})")

    def restore_mp(self, amount):
        self.mp = min(self.max_mp, self.mp + amount)
        print(f"{self.name} restores {amount} MP; MP: ({self.mp}/{self.max_mp})")

    def __str__(self):
        return f"{self.name} (HP:{self.hp}/{self.max_hp}, MP:{self.mp}/{self.max_mp})"


class Ability:
    def __init__(self, caster, name, damage=0, cost=0, effect=""):
        self.caster = caster
        self.name = name
        self.damage = damage
        self.cost = cost
        self.effect = effect

    def use(self, target):
        if self.caster.mp < self.cost:
            print(f"{self.caster.name} not enough MP for {self.name}")
            return
        print(f"{self.caster.name} uses {self.name}")

        self.caster.mp -= self.cost
        if self.damage > 0:
            target.take_damage(self.damage)
        else:
            target.restore_hp(-self.damage)
        if self.effect:
            print(f"{self.effect}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=120, mp=20, attack=18, defense=15)
        self.abilities = [
            Ability(self, "Punch", damage=15, cost=5),
            Ability(self, "Sword slash", damage=55, cost=10)
        ]


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=70, mp=80, attack=10, defense=5)
        self.abilities = [
            Ability(self, "Fireball", damage=80, cost=20),
            Ability(self, "Frost arrow", damage=45, cost=10),
            Ability(self, "Regeneration spell", damage=-50, cost=15)
        ]


class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, mp=50, attack=15, defense=8)
        self.abilities = [
            Ability(self, "Punch", damage=30, cost=10),
            Ability(self, "Stealth", effect=f"{name} became invivbls", cost=15)
        ]


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, mp=60, attack=14, defense=12)
        self.abilities = [
            Ability(self, "Divine punch", damage=30, cost=15),
            Ability(self, "Divine heal", damage=-40, cost=20),
            Ability(self, "Divine protection", effect=f"{name} усиливает защиту", cost=10)
        ]


class Enemy(Character):
    def __init__(self, name, hp, mp, attack, defense):
        super().__init__(name, hp, mp, attack, defense)


class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, hp=40, mp=10, attack=8, defense=4)
        self.abilities = [
            Ability(self, "Punch", damage=10, cost=10)
        ]


class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, hp=70, mp=20, attack=14, defense=8)
        self.abilities = [
            Ability(self, "Punch", damage=20, cost=10)
        ]


class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name, hp=150, mp=100, attack=22, defense=16)
        self.abilities = [
            Ability(self, "Fire Breathing", damage=40, cost=25),
            Ability(self, "Tail kick", damage=30, cost=15)
        ]


class Battle:
    def __init__(self):
        self.heroes = {
            "Gendalf": Mage("Gendalf"),
            "George": Rogue("George"),
            "Alexandr": Paladin("Alexandr")
        }
        self.enemies = {
            "Sauron": Dragon("Sauron"),
            "Grug": Orc("Grug"),
            "Kerk": Goblin("Kerk")
        }

    def start(self):
        for hero in self.heroes.values():
            print(hero)
        for enemy in self.enemies.values():
            print(enemy)
        self.heroes["Gendalf"].abilities[0].use(self.enemies["Sauron"])
        self.heroes["George"].abilities[0].use(self.enemies["Sauron"])
        self.heroes["Alexandr"].abilities[0].use(self.enemies["Sauron"])

        self.enemies["Sauron"].abilities[0].use(self.heroes["Gendalf"])
        self.enemies["Grug"].abilities[0].use(self.heroes["Alexandr"])
        self.enemies["Kerk"].abilities[0].use(self.heroes["George"])

        self.heroes["Gendalf"].abilities[2].use(self.heroes["Gendalf"])
        self.heroes["George"].abilities[0].use(self.enemies["Sauron"])
        self.heroes["Alexandr"].abilities[0].use(self.enemies["Sauron"])

        self.enemies["Sauron"].abilities[1].use(self.heroes["Gendalf"])
        self.enemies["Grug"].abilities[0].use(self.heroes["Alexandr"])
        self.enemies["Kerk"].abilities[0].use(self.heroes["George"])

        self.heroes["Gendalf"].abilities[0].use(self.enemies["Sauron"])
        self.heroes["George"].abilities[0].use(self.enemies["Grug"])
        self.heroes["Alexandr"].abilities[0].use(self.enemies["Grug"])


if __name__ == '__main__':
    Battle().start()
