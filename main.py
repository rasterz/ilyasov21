from store import Store
from shop import Shop
from request import Request
from courier import Courier
from exceptions import RequestError

store = Store(
    items={
        'киви': 25,
        'манго': 25,
        'груша': 25,
        'персик': 5,
        'дыня': 5,
        'арбуз': 1
    }
)

shop = Shop(
    items={
        'киви': 2,
        'манго': 2,
        'груша': 2,
        'персик': 1,
        'дыня': 1
    }
)

storages = {
    'магазин': shop,
    'склад': store
}

def main():
    print('Добрый день!\n')
    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n{storages[storage_name].get_items()}')
            print(
                f'Свободно {storages[storage_name].get_free_space()} мест из '
                f'{storages[storage_name].get_capacity()}\n'
            )

        user_input = input(
            'Введите запрос в формате "доставить 3 яблоко из склад в магазин". '
            'Введите "стоп" или "stop", чтобы завершить программу\n'
        ).lower()

        if user_input in ('стоп', 'stop'):
            break

        try:
            request = Request(request_text=user_input, storage_list=storages)
        except (RequestError) as error:
            print(error.message)
            continue


        courier = Courier(request, storages)
        courier.route()


if __name__ == '__main__':
    main()