# Parent Class
class Payment:
    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount

    def process_payment(self):
        print("Processing payment...")


# Child Class 1
class CreditCardPayment(Payment):
    def __init__(self, customer_name, amount, card_number):
        super().__init__(customer_name, amount)
        self.card_number = card_number

    def process_payment(self):
        print(f"Customer: {self.customer_name}")
        print(f"Paid ${self.amount} using Credit Card ending with {self.card_number[-4:]}")
        print("-" * 40)


# Child Class 2
class PayPalPayment(Payment):
    def __init__(self, customer_name, amount, email):
        super().__init__(customer_name, amount)
        self.email = email

    def process_payment(self):
        print(f"Customer: {self.customer_name}")
        print(f"Paid ${self.amount} using PayPal ({self.email})")
        print("-" * 40)


# Child Class 3
class BankTransferPayment(Payment):
    def __init__(self, customer_name, amount, bank_name):
        super().__init__(customer_name, amount)
        self.bank_name = bank_name

    def process_payment(self):
        print(f"Customer: {self.customer_name}")
        print(f"Paid ${self.amount} through {self.bank_name} Bank Transfer")
        print("-" * 40)


# Main Program
payments = [
    CreditCardPayment("Ali", 250, "1234567812345678"),
    PayPalPayment("Sara", 180, "sara@gmail.com"),
    BankTransferPayment("Ahmed", 500, "HBL")
]

# Polymorphism
for payment in payments:
    payment.process_payment()