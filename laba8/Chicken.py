
class Chicken:
    def __init__(self, productivity):
        self._productivity = productivity

    def get_eggs_per_month(self):
        return self._productivity

    def __str__(self):
        return "Я курица"


class Russian(Chicken):
    def __init__(self, productivity):
        super().__init__(productivity)

    def __str__(self):
        return super().__str__() + f". Моя страна - Россия. Я несу {super().get_eggs_per_month()} яиц в месяц"


class Belarusian(Chicken):
    def __init__(self, productivity):
        super().__init__(productivity)

    def __str__(self):
        return super().__str__() + f". Моя страна - Белорусь. Я несу {super().get_eggs_per_month()} яиц в месяц"


class Moldavian(Chicken):
    def __init__(self, productivity):
        super().__init__(productivity)

    def __str__(self):
        return super().__str__() + f". Моя страна - Молдова. Я несу {super().get_eggs_per_month()} яиц в месяц"