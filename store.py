from storage import Storage
from exceptions import NotEnoughSpace, NotEnoughGoods, NoGood


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self._items = items
        self._capacity = capacity
        super().__init__(items, capacity)

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name, quantity):
        if self.get_free_space() > quantity:
            if name not in self._items:
                self._items[name] = 0
            self._items[name] += quantity
        else:
            raise NotEnoughSpace

    def remove(self, name, quantity):
        if name not in self._items:
            raise NoGood
        elif self._items[name] >= quantity:
            self._items[name] -= quantity
        else:
            raise NotEnoughGoods

    def get_free_space(self):
        return self.capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_capacity(self):
        return self._capacity

    def get_unique_items_count(self):
        return len(self._items)
