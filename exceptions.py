class BaseError(Exception):
    message = NotImplemented

class RequestError(BaseError):
    message = NotImplemented

class CourierError(BaseError):
    message = NotImplemented

class NotEnoughSpace(CourierError):
    message = 'Недостаточно места'

class NotEnoughGoods(CourierError):
    message = 'Недостаточно товара'

class NoGood(CourierError):
    message = 'Нет такого товара'

class TooManyDifferentGoods(CourierError):
    message = 'Слишком много разных видов товаров'

class InvalidRequest(RequestError):
    message = 'Неправильный запрос, попробуйте снова'

class InvalidStorageName(RequestError):
    message = 'Выбран несуществующий склад'