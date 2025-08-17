# 6. Сложное: "Асинхронный продюсер-кансюмер с ограничением"
#
#  Задание:
#  Имплементируйте продюсера, который каждую секунду кладёт в asyncio.Queue случайное число от 1 до 100.
#  Консюмеры (2 шт.) обрабатывают числа (например, выводят их и делают sleep(n/100) секунд).
#  Продюсер должен остановиться после 10 чисел, а консюмеры завершиться корректно.


import asyncio
import time
from random import randint
from q_5 import AsyncTimer


async def producer(queue: asyncio.Queue, number_of_consumers: int):
    for task_count in range(10):
        num = randint(1, 100)
        await queue.put((task_count, num))
        print(f'Таск {task_count} (число {num}) отправлен в очередь...')
        await asyncio.sleep(1)

    for _ in range(number_of_consumers):
        await queue.put(None)


async def consumer(queue: asyncio.Queue, cons_id: int):
    while True:
        task = await queue.get()
        if task is None:
            queue.task_done()
            break

        num_task, num = task
        delay = num / 100
        async with AsyncTimer(name=num_task):
            print(f'Таск {num_task} обрабатывается воркером №{cons_id}!')
            await asyncio.sleep(delay)
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    number_of_consumers = 2

    producer_task = asyncio.create_task(producer(queue, number_of_consumers))
    consumers = [
        asyncio.create_task(consumer(queue, i))
        for i in range(1, number_of_consumers + 1)
    ]
    start_time = time.perf_counter()
    await producer_task
    await queue.join()
    await asyncio.gather(*consumers)
    total_time = time.perf_counter() - start_time
    print(f'ВСЕ ТАСКИ ОБРАБОТАНЫ ЗА {total_time:.4f} СЕКУНД!')

if __name__ == '__main__':
    asyncio.run(main())