# 4. Среднее: "Очередь задач и воркеры"
#
# Задание:
#  Создайте очередь задач asyncio.Queue, заполните её числами от 1 до 10.
#  Запустите 3 асинхронных воркера, которые берут элемент из очереди, ждут n секунд (n = элемент из очереди), и выводят: "Готово: {n}".
#  Очередь должна быть обработана полностью.


import asyncio
from random import randint


async def producer(queue: asyncio.Queue, num_task: int):
    for i in range(num_task):
        task_id = i + 1
        delay = randint(1, 7)
        await queue.put((task_id, delay))
    await queue.put(None)

async def worker(queue: asyncio.Queue, worker_id: int):
    while True:
        task = await queue.get()

        if task is None:
            queue.task_done()
            break

        task_id, delay = task
        print(f'Воркером {worker_id} начата обработка таска №{task_id}...')
        await asyncio.sleep(delay)
        print(f'№{task_id} завершена!')
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=6)
    num_tasks = 10

    producer_task = asyncio.create_task(producer(queue, num_tasks))
    workers = [asyncio.create_task(worker(queue, i)) for i in range(1,4)]

    await producer_task
    await queue.join()

    await queue.put(None)
    await queue.put(None)
    await queue.put(None)

    await asyncio.gather(*workers)

if __name__ == '__main__':
    asyncio.run(main())