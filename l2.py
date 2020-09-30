from abc import ABC, abstractmethod
import math

class Dress(ABC):
    def __init__(self, model):
        self.model = model
    @abstractmethod
    def expenditure(self):
        pass

class Coat(Dress):
    def __init__(self, model, v):
        super().__init__(model)
        self.v = v
    @property
    def expenditure(self):
        return math.ceil(self.v / 6.5 + 0.5)

class Сlothes(Dress):
    def __init__(self, model, h):
        super().__init__(model)
        self.h = h
    @property
    def expenditure(self):
        return math.ceil(2 * self.h + 0.3)

coat = Coat('Осень2020', 52)
clothes = Сlothes('Смокинг', 180)
print(coat.expenditure)
print(clothes.expenditure)