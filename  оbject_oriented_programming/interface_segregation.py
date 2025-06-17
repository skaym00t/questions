from abc import ABC, abstractmethod

class AnimalFly(ABC):
    """Животное летает"""
    @abstractmethod
    def fly(self):
        pass

class AnimalRun(ABC):
    """Животное ходит"""
    @abstractmethod
    def run(self):
        pass

class AnimalSwim(ABC):
    """Животное плавает"""
    @abstractmethod
    def swim(self):
        pass

class Animal(ABC):
    """Инициализация животного"""
    def __init__(self, name: str):
        self.name = name


class Lion(Animal, AnimalRun):
    def run(self):
        return f'{self.name} важно вышагивает по саванне!'

l = Lion('Лев')
print(l.run())
