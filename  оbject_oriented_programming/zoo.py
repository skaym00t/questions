from abc import ABC, abstractmethod
from multiple_inheritance import Flyable, Swimmable

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Woof!')

    def move(self):
        print('Dog runn!')

class Bird(Animal, Flyable):
    def speak(self):
        print("Tweet!")

    def move(self):
        super().fly()

class Fish(Animal, Swimmable):
    def speak(self):
        print('...')

    def move(self):
        super().swim()

animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.speak()
    animal.move()