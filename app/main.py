from lib.american import AmericanPizza

if __name__ == '__main__':
    american = AmericanPizza('American', 32)
    print(f'{american}\nPrice: {american.get_cost()} uah')
