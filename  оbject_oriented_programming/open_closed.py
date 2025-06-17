from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def current_payment(self):
        pass

class Crypto(Payment):
    def __init__(self, payment_name: str):
        self.payment_name = payment_name

    def current_payment(self):
        return f'Оплата через {self.payment_name}'

class CreditCard(Payment):
    def __init__(self, payment_name: str):
        self.payment_name = payment_name

    def current_payment(self):
        return f'Оплата через {self.payment_name}'

class PayPal:
    def __init__(self, payment_name: str):
        self.payment_name = payment_name

    def current_payment(self):
        return f'Оплата через {self.payment_name}'


class PaymentProcessor:
    @staticmethod
    def pay(payment: Payment):
        result = payment.current_payment()
        print(result)
        return result

cr = Crypto(payment_name='Trust Wallet')
cc = CreditCard(payment_name='Mastercard')
pp = PayPal(payment_name='PayPal')
PaymentProcessor.pay(cr)
PaymentProcessor.pay(cc)
PaymentProcessor.pay(pp)

