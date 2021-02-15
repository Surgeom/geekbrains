from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.title = self.__class__.__name__
        self.size = size

    @abstractmethod
    def tissue_consumption(self):
        return f'Расход материала для {self.title} равен {self.size}'


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def tissue_consumption(self):
        return f'Расход материала для {self.title} равен {self.size / 6.5 + 0.5}'


class Suit(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def tissue_consumption(self):
        return f'Расход материала для {self.title} равен {2 * self.size + 0.3}'


a = Coat(6.5)
b = Suit(0.35)
print(a.tissue_consumption)
print(b.tissue_consumption)