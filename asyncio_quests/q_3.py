# 3. Среднее: "Асинхронная загрузка с aiohttp"
#
# Задание: Используя aiohttp, скачайте содержимое 3-х разных веб-страниц (на твое усмотрение,
# но можешь взять какие нибудь страницы из инета) параллельно. Выведите размер каждой страницы.
# Подсказка: используйте aiohttp.ClientSession и async with (обоснуй тот или иной подход).

import aiohttp
import asyncio

async def fetch_page(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        content = await response.text()
        return {'status': response.status,
                'content': content[:100],
                'size': len(content.encode('utf-8')),
                'len_content': len(content)
                }

async def main():
    urls = [
        'https://slow-aragon-5be.notion.site/Best-Roadmap-Python-Developer-1a8d21f083168043a5a7e6c110c1472d',
        'https://code.yandex-team.ru/6ce63c75-a8a6-4131-9e44-c6242c0e2d1e',
        'https://docs.google.com/spreadsheets/d/1te9vWvlenH4XT7xot_ElpDYB82Vw8P9cJOQyOJYCla8/edit?gid=0#gid=0'
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_page(session, url)) for url in urls]
        for task in tasks:
            result = await task
            print(result)

if __name__ == '__main__':
    asyncio.run(main())