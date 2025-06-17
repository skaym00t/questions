from abc import ABC, abstractmethod

class Transport(ABC):
    """Интерфейс транспортного средства"""

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    """Автомобиль"""

    def start_engine(self):
        print('Двигатель автомобиля запущен')

    def stop_engine(self):
        print('Двигатель автомобиля остановлен')

    def move(self):
        print('Автомобиль едет')

class Boat(Transport):
    """Лодка"""

    def start_engine(self):
        print('Двигатель лодки запущен')

    def stop_engine(self):
        print('Двигатель лодки остановлен')

    def move(self):
        print('Лодка плывет')

def moving_transport(transport: Transport):
    """Верхнеуровневая функция"""
    transport.start_engine()
    transport.move()
    transport.stop_engine()

c = Car()
b = Boat()

drive = moving_transport(c)
swimming = moving_transport(b)


