from abc import ABC, abstractmethod


class AbstractPizza(ABC):
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @abstractmethod
    def get_cost(self) -> float:
        pass