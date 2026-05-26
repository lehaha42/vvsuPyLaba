
class Animal:
    def __init__(self, name, gender, age, species):
        self.name = name
        self.gender = gender
        self.age = age
        self.species = species

    def move(self):
        print(f"{self.name} moves around")

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")


class Mammal(Animal):
    def __init__(self, name, gender, age, species, fur_length, fur_color):
        super().__init__(name, gender, age, species)
        self.fur_length = fur_length
        self.fur_color = fur_color

    def feed_milk(self):
        print(f"{self.name} feeds babies")


class Bird(Animal):
    def __init__(self, name, gender, age, species, beak_size, wingspan):
        super().__init__(name, gender, age, species)
        self.beak_size = beak_size
        self.wingspan = wingspan

    def build_nest(self):
        print(f"{self.name} makes a nest")

    def lay_eggs(self):
        print(f"{self.name} lays eggs")

    def fly(self):
        print(f"{self.name} flyes")


class Tiger(Mammal):
    def __init__(self, name, gender, age, species, fur_length, fur_color, stripe_pattern, hunting_skill):
        super().__init__(name, gender, age, species, fur_length, fur_color)
        self.stripe_pattern = stripe_pattern
        self.hunting_skill = hunting_skill

    def roar(self):
        print(f"{self.name} roars")

    def hunt(self):
        print(f"{self.name} hunts (hunting skill: {self.hunting_skill}).")


if __name__ == '__main__':
    pass
