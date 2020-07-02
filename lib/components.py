from abc import ABC, abstractmethod


class AbstractPizza(ABC):

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_cost(self) -> float:
        pass
