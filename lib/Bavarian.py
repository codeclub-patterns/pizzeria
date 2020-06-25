from lib.components import AbstractPizza

class BavarianPizza(AbstractPizza):
    #pass

    def __init__(self, psize: str, ptype: str, pitem: float):
         super().__init__(psize, ptype)
         self._pitem = pitem

    def __str__(self): -> str:
        return super().__str__() + f'; quantity: = {self._pitem} it.'

    def description(self):
        print(' "BavarianPizza" with ingredients: Cheese: Parmesan, Mozarella; '
              'Sausages: Bavarian sausages; '
              'Sauce: BBQ sauce; Additions: BBQ sauce (on top)')








