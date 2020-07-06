from lib.components import AbstractPizza


class AmericanPizza(AbstractPizza):

    def __init__(self, name, size):
        super().__init__(name, size)

    def __str__(self):
        return f'Name: {self._name}\nSize: {self._size} sm'

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    def get_cost(self):
        return 100.25

