from lib.components import AbstractPizza


class ItalianPizza(AbstractPizza):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self) -> str:
        return f'Итальянская пицца: {self._name}'

    @property
    def name(self):
        return self._name

    def get_cost(self) -> float:
        return 129.50
