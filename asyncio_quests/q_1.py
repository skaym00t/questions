# 1. Простое: "Привет каждую секунду"
# Задание: Напишите асинхронную функцию, которая выводит «Привет!» каждую секунду 5 раз.
# Подсказка: используйте asyncio.sleep.

import asyncio
async def hello_every_second():
    for i in range(5):
        print('Привет!')
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(hello_every_second())

