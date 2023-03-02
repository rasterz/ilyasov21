from store import Store
from exceptions import TooManyDifferentGoods

class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        if self.get_unique_items_count() >= 5 and name not in self.get_items():
            raise TooManyDifferentGoods
        super().add(name, quantity)
