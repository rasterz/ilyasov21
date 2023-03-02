from request import Request
from exceptions import CourierError

class Courier():
    def __init__(self, request:Request, storages:dict):
        self.__request = request

        if self.__request.departure in storages:
            self.__departure = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__destination = storages[self.__request.destination]

    def _send(self):
            self.__departure.remove(self.__request.product, self.__request.amount)
            print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}')

    def _move(self):
        print(f'Курьер везет {self.__request.amount} {self.__request.product} из {self.__request.departure} в {self.__request.destination}')

    def _deliver(self):
            self.__destination.add(self.__request.product, self.__request.amount)
            print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')

    def _return(self):
        self.__departure.add(self.__request.product, self.__request.amount)
        print(f'Курьер вернул {self.__request.amount} {self.__request.product} в {self.__request.departure}')

    def route(self):

        try:
            self._send()
            self._move()
        except CourierError as error:
            print(error.message)
            return

        try:
            self._deliver()
        except CourierError as error:
            print(error.message)
            self._return()
