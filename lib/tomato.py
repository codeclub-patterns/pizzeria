from lib.decorators import AbstractSupplement


class TomatoSupplement(AbstractSupplement):

    def __init__(self, pizza):
        super().__init__(pizza)

    def __str__(self):
        return f'{self._pizza} с томатами'

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 25.5
