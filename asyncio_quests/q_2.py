# Простое: "Параллельные запросы" (мок)
#
# Задание: Создайте 3 корутины, каждая из которых «имитирует» сетевой запрос через asyncio.sleep(n). Запустите их параллельно и выведите время выполнения всей группы.
# Подсказка: можно попробовать воспользоваться asyncio.gather (все зависит от версии питона).

import asyncio
import time

async def async_mok_request(request: int, delay: float):
    print(f'Запрос №{request} начал выполнение, займет {delay} секунд!')
    await asyncio.sleep(delay)
    result = hash(request + delay)
    print(f'Запрос №{request} выполнен!')
    return f'Результат запроса №{request} - {result}'

async def main():
    start_time = time.time()

    results = await asyncio.gather(
        async_mok_request(1, 6.23),
        async_mok_request(2, 3.75),
        async_mok_request(3, 9.13)
    )
    end_time = time.time() - start_time

    print(f'Все запросы завершены за {end_time:.2f}!')
    print('Результаты:', results)

if __name__ == '__main__':
    asyncio.run(main())

