# 5. Сложное: "Асинхронный таймер с контекстным менеджером"
#
#  Задание:
#  Создайте асинхронный контекстный менеджер, который замеряет время выполнения кода внутри него.
#  Пример использования:


import asyncio
import time
from random import randint


class AsyncTimer:
    def __init__(self, name = None):
        self.name = name

    async def __aenter__(self):
        self.start = time.perf_counter()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        name_str = f"' {self.name}'" if self.name is not None else ""
        print(f'Время выполнения{name_str}: {elapsed:.4f} сек.')
        return False

async def async_worker(n: int):
    print(f'Начало обработки задачи {n}...')
    time = n - randint(0, n)
    await asyncio.sleep(time)
    print(f'Готово: {n}, за {time} сек!')


async def main():
    tasks = [asyncio.create_task(async_worker(i)) for i in range(10)]
    async with AsyncTimer() as timer:
       for task in tasks:
           await task

if __name__ == '__main__':
    asyncio.run(main())
