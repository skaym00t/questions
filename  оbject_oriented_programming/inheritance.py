import typing

class Employee:
    """Работник"""

    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        """Получить информацию о работнике"""

        return {
            'name': self.name,
            'position': self.position,
            'salary': self.salary
        }

    def __str__(self):
        return f'{self.__dict__}'

class Developer(Employee):
    """Позиция разработчика, с указанием языка программирования"""

    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name=name, position='Developer', salary=salary)
        self.programming_language = programming_language

    def get_info(self):
        """Получить информацию о разработчике"""

        common_info = super().get_info()
        common_info['programming_language'] = self.programming_language
        return common_info

    def __repr__(self):
        return f'{self.__dict__}'

class Manager(Employee):
    """Позиция менеджера + его команда разработчиков"""

    def __init__(self, name: str, salary: float, employees: list[Employee] = None):
        super().__init__(name=name, position='Manager', salary=salary)
        self.employees = employees if employees else []

    def get_info(self):
        """Получить информацию о менеджере"""

        common_info = super().get_info()
        common_info['employees'] = self.employees
        return common_info

    def add_employee(self, employee: Employee):
        """Добавить разработчика в команду"""

        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        """Исключить разработчика из команды"""

        self.employees.remove(employee)

    def __repr__(self):
        return f'{self.__dict__}'


d1 = Developer('Пётр', 150000.00, 'Python')
d2 = Developer('Гурген', 300000.00, 'Go')
d3 = Developer('Кузя', 200000.00, 'Python')
d4 = Developer('Семён', 100.00, 'Javascript')
m1 = Manager('Василий', 50000.00)

employees_list = (d1, d2, d3, d4, m1) # все сотрудники

def get_state(item: typing.Iterable[Employee]):
    """Как работает полиморфизм - получаем штат через общий метод get_info()"""

    print('СПИСОК РАБОТНИКОВ:')
    for employee in item:
        print(employee.get_info())


get_state(employees_list) # выводим информацию о всём штате
print('РАЗРАБОТЧИКИ ЕЩЁ НЕ СФОРМИРОВАНЫ В КОМАНДЫ')

def set_python_developer_from_manager(item: typing.Iterable[Employee]):
    """Добавляем в команду к менеджеру только разработчиков на python"""

    python_developers = []
    manager = None
    for employee in item:
        if hasattr(employee, 'programming_language') and employee.programming_language == 'Python':
            python_developers.append(employee)
        if employee.position == 'Manager':
            manager = employee
    for dev in python_developers:
        manager.add_employee(dev)
        print(f'Добавляем в команду к {manager.name} разработчика {dev.name}')

set_python_developer_from_manager(employees_list) # формируем python-dream-team
get_state(employees_list) # выводим информацию о всём штате ещё раз
print('ТЕПЕРЬ У ВАСИЛИЯ В КОМАНДЕ ПЁТР И КУЗЯ')