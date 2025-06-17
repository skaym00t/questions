class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> 'Temperature':
        """Создает объект Temperature из градусов Фаренгейта"""
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self) -> float:
        """Возвращает температуру в Кельвинах"""
        return self._celsius + 273.15

    @property
    def celsius(self) -> float:
        """Возвращает температуру в Цельсиях"""
        return self._celsius

    @celsius.setter
    def celsius(self, new_cels: float):
        """Меняет температуру в Цельсиях"""
        self._celsius = new_cels

    @property
    def fahrenheit(self) -> float:
        """Возвращает температуру в Фаренгейтах"""
        return self._celsius * 9 / 5 + 32

    @staticmethod
    def freezing_point(celsius: float) -> bool:
        """Проверяет, является ли температура точкой замерзания воды"""
        return celsius <= 0

t1 = Temperature(25)
t2 = Temperature.from_fahrenheit(756)
print(t1.celsius)
print(t2.celsius)