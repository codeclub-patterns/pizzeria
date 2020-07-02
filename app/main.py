from lib.italian import ItalianPizza
from lib.tomato import TomatoSupplement


if __name__ == '__main__':
    pizza = ItalianPizza('Star')
    pizza = TomatoSupplement(pizza)
    print(f'{pizza} - {pizza.get_cost()}')
