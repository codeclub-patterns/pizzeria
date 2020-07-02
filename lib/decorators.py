from abc import ABC, abstractmethod
from lib.components import AbstractPizza


class AbstractSupplement(ABC):

    def __init__(self, pizza: AbstractPizza):
        self._pizza = pizza

    @abstractmethod
    def get_cost(self) -> float:
        pass
