from lib.components import AbstractPizza


class AmericanPizza(AbstractPizza):
    Name = 'American-pizza'

    def __init__(self, size: int, cost):
        self._size = size
        self._cost = cost

    def get_cost(self) -> float:
        return AbstractPizza.get_cost(self._cost)

    def __str__(self):
        return f'Name: {AmericanPizza.Name}. \nSize = {self._size}sm. \nCost = {self._cost} uah. '\
               f'\nComposition: Tomato sauce, marinated chicken, mushrooms, mozzarella, onions, barbecue sauce.'
