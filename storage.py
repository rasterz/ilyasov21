from abc import ABC, abstractmethod
from typing import Dict

class Storage(ABC):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    # @property
    # @abstractmethod
    # def items(self):
    #     pass
    #
    # @property
    # @abstractmethod
    # def capacity(self):
    #     pass

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
