
class Animal:
    def __init__(self, name, age, breed, sound, tamed):
        self._name = name
        self._age = age
        self._breed = breed
        self._sound = sound
        self._tamed = tamed

    def sound(self):
        return f"{self._name} makes sound '{self._sound}'"

    def pat(self):
        if self._tamed:
            return f"you patted {self._name}"
        return f"{self._name} bited your hand"

    def feed(self, food):
        return f"{self._name} ate {food}"


class Glass:
    def __init__(self, volume, fluid, amount, transparent, material):
        self._volume = volume
        self._fluid = fluid
        self._amount = amount
        self._transparent = transparent
        self._material = material

    def puor_in(self, fluid, amount):
        if self._fluid:
            if fluid != self._fluid:
                return
            if amount + self._amount > self._volume:
                self._amount = self._volume
            else:
                self._amount += amount
        self._fluid = fluid
        self._amount = amount

    def pour_out(self, amount):
        if amount < self._amount:
            self._amount -= amount
        else:
            self._amount = 0
            self._fluid = None

    def observe(self):
        if self._fluid:
            return f"glass of {self._fluid} made of {self._material} is {self._amount/self._volume * 100}% filled"
        return f"glass made of {self._material}"


if __name__ == "__main__":
    pass
