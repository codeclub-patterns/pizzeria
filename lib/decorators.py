from abc import ABC, abstractmethod


class AbstractSupplement(ABC):

    @abstractmethod
    def get_cost(self) -> float:
        pass
