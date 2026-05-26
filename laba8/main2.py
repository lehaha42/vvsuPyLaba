from Chicken import Russian, Belarusian, Moldavian


class Factory:
    def __init__(self):
        self._russian = Russian(15)
        self._russian_count = 40
        self._belarus = Belarusian(12)
        self._belarus_count = 35
        self._moldova = Moldavian(10)
        self._moldova_count = 30
        self._total_count = self._russian_count + self._belarus_count + self._moldova_count
        self._total_eggs = self._russian.get_eggs_per_month() * self._russian_count +\
                           self._belarus.get_eggs_per_month() * self._belarus_count +\
                           self._moldova.get_eggs_per_month() * self._moldova_count

    def get_russian_count(self):
        return self._russian_count

    def get_belarus_count(self):
        return self._belarus_count

    def get_moldova_count(self):
        return self._moldova_count

    def get_total_count(self):
        return self._total_count

    def get_russian_eggs(self):
        return self._russian.get_eggs_per_month()

    def get_belarus_eggs(self):
        return self._belarus.get_eggs_per_month()

    def get_moldova_eggs(self):
        return self._moldova.get_eggs_per_month()

    def get_totall_eggs(self):
        return self._total_eggs


if __name__ == '__main__':
    factory = Factory()
    print(factory.get_russian_count())
    print(factory.get_russian_eggs())
    print(factory.get_belarus_count())
    print(factory.get_belarus_eggs())
    print(factory.get_moldova_count())
    print(factory.get_moldova_eggs())
    print(factory.get_total_count())
    print(factory.get_totall_eggs())
