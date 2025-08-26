# def dec_start_end(f):
#     def wrapper(*args, **kwargs):
#         print('Старт!')
#         result = f(*args, **kwargs)
#         print('Конец!')
#         return result
#     return wrapper
#
# @dec_start_end
# def sum_(a, b):
#     return print(a + b)
#
# sum_(1, 2)
#
# def dict_diff(old, new):
#     def flatten_dict(d, parent_key='', sep='.'):
#         flattened = {}
#         for k, v in d.items():
#             new_key = f"{parent_key}{sep}{k}" if parent_key else k
#             if isinstance(v, dict):
#                 flattened.update(flatten_dict(v, new_key, sep))
#             else:
#                 flattened[new_key] = v
#         return flattened
#     flat_old = flatten_dict(old)
#     flat_new = flatten_dict(new)
#     diff = []
#     for key in flat_old:
#         if key not in flat_new:
#             diff.append(f'- {key} {flat_old[key]}')
#         elif flat_old[key] != flat_new[key]:
#             diff.append(f'- {key} {flat_old[key]}')
#             diff.append(f'+ {key} {flat_new[key]}')
#     for key in flat_new:
#         if key not in flat_old:
#             diff.append(f'+ {key} {flat_new[key]}')
#     return "\n".join(diff)
#
# print(dict_diff(
#     {'a': {'x': 1}, 'b': 2},
#     {'b': 3, 'c': 4}
# ))

# class DefaultDict(dict):
#     def __missing__(self, key):
#         return []
#
# d = DefaultDict()
# d['sdafd'] = 127
# print(d)

# def counter(num: int = 0):
#     count = num
#     def wrapper(num_2: int = 1):
#         nonlocal count
#         count += num_2
#         return count
#     return wrapper
#
# c = counter(5)
# print(c())
# print(c(2))
# print(c(4))
# print(c())

# from fastapi import FastAPI, HTTPException, Depends
# from tortoise import fields, models
# from tortoise.exceptions import DoesNotExist
#
#
# class Doctor(models.Model):
#     doctor_id = fields.IntField(pk=True)
#     is_on_call = fields.BooleanField(default=False)
#
#
# app = FastAPI()
#
#
# @app.get("/set-off-call")
# async def set_off_call(
#         doctor_id: int,
#         task_producer: CeleryTaskProducer = Depends(),
# ) -> dict:
#     try:
#         current_doctor = await Doctor.get(doctor_id=doctor_id)
#
#         if not current_doctor.is_on_call:
#             return {"status": "success", "message": "Doctor is already off call"}
#
#         doctors_on_call = await Doctor.filter(is_on_call=True).count()
#
#         if doctors_on_call <= 1:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Cannot set off call - at least one doctor must remain on call"
#             )
#
#         await Doctor.filter(doctor_id=doctor_id).update(is_on_call=False)
#
#         task_producer.publish_change_doctor_call_status(
#             doctor_id=doctor_id,
#             is_on_call=False
#         )
#
#         return {"status": "success"}
#
#     except DoesNotExist:
#         raise HTTPException(status_code=404, detail="Doctor not found")
#
# args = (1, 'str', True)
# kwargs = {'a': 1, 'b': 2}
# dict_ = {}
# key = (args, frozenset(kwargs.items()))
# print(key, type(key))
# dict_[str(key)] = 1
# print(dict_)

# class Value:
#     def __init__(self, v):
#         self.v = v
#     def __repr__(self):
#         return f'{self.v}'
#
# storage = set([Value(1), Value(42), Value(1)])
# print(storage)


class Value:
    def __init__(self, v):
        self.v = v

    def __hash__(self):
        # Простая самописная функция хэша с использованием ord
        if isinstance(self.v, str):
            hash_value = 0
            for char in self.v:
                hash_value = (hash_value * 31 + ord(char)) % (2 ** 32)
            return hash_value
        else:
            # Для чисел преобразуем в строку и вычисляем хэш
            # ord возвращает unicode символа
            str_v = str(self.v)
            hash_value = 0
            for char in str_v:
                hash_value = (hash_value * 31 + ord(char)) % (2 ** 32)
            return hash_value

    def __eq__(self, other):
        if isinstance(other, Value):
            return self.v == other.v
        return False

    def __repr__(self):
        return f'Value({self.v})'


storage = set([Value(1), Value(42), Value(1)])
print(storage)

import time
import logging
from functools import wraps

# Инициализация логгера один раз
logger = logging.getLogger(__name__)


def log_execution_time_and_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            result = func(*args, **kwargs)
            execution_time = time.perf_counter() - start_time

            # Лог для бизнеса на INFO - только время выполнения
            logger.info("Function %s executed in %.4f seconds", func.__name__, execution_time)

            # Лог для разработчиков на DEBUG - детальная информация
            logger.debug("Function %s took %.4fs. Arguments: %s, Keyword arguments: %s. Return: %s",
                         func.__name__, execution_time, args, kwargs, result)

            return result

        except Exception as e:
            execution_time = time.perf_counter() - start_time
            # Лог ошибок на ERROR уровне
            logger.error("Function %s failed in %.4fs. Error: %s",
                         func.__name__, execution_time, str(e))
            raise

    return wrapper


# # Пример использования
# @log_execution_time_and_result
# def process_order(order_id, amount):
#     time.sleep(0.2)
#     return f"Order {order_id} processed for ${amount}"
#
#
# # Тестирование
# result = process_order("ORD123", 100)

import aiohttp  # Асинхронные HTTP-запросы
import asyncio  # Асинхронное программирование
from collections import defaultdict  # Словарь с дефолтными значениями
from typing import List, Dict, Any  # Аннотации типов

async def process_arguments(arguments: List[Any]):
    services = [  # Список сервисов для запросов
        ("http://srv1", "srv1"),
        ("http://srv2", "srv2"),
        ("http://srv3", "srv3"),
    ]
    semaphore = asyncio.Semaphore(1000)  # Ограничение одновременных запросов (1000)
    results = defaultdict(dict)  # Результаты: {аргумент: {сервис: результат}}

    async with aiohttp.ClientSession() as session:  # Сессия для HTTP-запросов
        arg_batch_size = 1000  # Размер батча аргументов
        for i in range(0, len(arguments), arg_batch_size):  # Обработка батчами
            batch_args = arguments[i:i + arg_batch_size]  # Текущий батч аргументов
            tasks = [  # Создание задач для каждого аргумента и сервиса
                fetch_service(session, url, arg, name, results, semaphore)
                for arg in batch_args for url, name in services
            ]
            await asyncio.gather(*tasks, return_exceptions=True)  # Параллельное выполнение

    return results  # Возврат сгруппированных результатов

async def fetch_service(session: aiohttp.ClientSession,
                        url: str,
                        arg: Any,
                        name: str,
                        results: Dict,
                        semaphore: asyncio.Semaphore):
    async with semaphore:  # Ограничение одновременных запросов
        try:
            async with session.post(url, json={'arg': arg}) as response:  # POST-запрос
                result = await response.json()  # Парсинг JSON-ответа
                results[arg][name] = result  # Сохранение результата
        except Exception as e:
            results[arg][name] = {'error': str(e)}  # Сохранение ошибки

# Пример использования
if __name__ == "__main__":
    arguments = [...]  # 1 млн аргументов
    results = asyncio.run(process_arguments(arguments))  # Запуск асинхронной обработки

    # Вывод сгруппированных результатов
    for arg, services in results.items():  # Итерация по аргументам
        print(f"Argument {arg}:")
        for service, result in services.items():  # Итерация по сервисам
            print(f"  {service}: {result}")