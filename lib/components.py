from abc import ABC, abstractmethod


class AbstractPizza(ABC):

    @abstractmethod
    def get_cost(self) -> float:
        pass
