from lib.components import AbstractPizza

#to run the program put this code in "main.py":
# bavarian = BavarianPizza('Bavarian Pizza', 30, 1)
# print(f'\n{bavarian}\n Price: {bavarian.get_cost()} uah')

class BavarianPizza(AbstractPizza):
    #pass

    def __init__(self, size: str, ptype: int, item: int): #def __init__(self, size: str, ptype: str, item1: float, name1: str):
         super().__init__(size, ptype) #super().__init__(psize, ptype, pitem, name, size)
         self._item = item

    def __str__(self) -> str:
        return super().__str__() + f'; \n quantity: = {self._item} it.\n Size: {self._size} sm\n Name: {self.name}'


    def description(self):
        print(' "BavarianPizza" with ingredients: Cheese: Parmesan, Mozarella; '
              'Sausages: Bavarian sausages; '
              'Sauce: BBQ sauce; Additions: BBQ sauce (on top)')

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    def get_cost(self) -> float:
        return 220








