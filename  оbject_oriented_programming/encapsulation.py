class BankAccount:
    """Банковский счёт"""

    def __init__(self, balance: float = 0.00):
        self.__balance = balance if balance > 0 else 0.00

    def get_balance(self):
        """Проверить баланс"""

        return self.__balance

    def deposit(self, amount: float = 0.0):
        """Пополнить баланс"""

        if amount <= 0.0:
            raise ValueError('Сумма пополнения должна быть больше 0.0')
        self.__balance += amount

    def withdraw(self, amount: float = 0.0):
        """Снять деньги"""

        if amount > self.__balance:
            raise ValueError('Недостаточно средств на счете')
        self.__balance -= amount

acc = BankAccount(5000)
print(acc.get_balance(), acc.__dict__)
acc.__dict__['_BankAccount__balance'] = 300 # ломаем инкапсуляцию
print(acc.get_balance())
acc.balance_2 = 1000.00
print(acc.get_balance(), acc.__dict__)
