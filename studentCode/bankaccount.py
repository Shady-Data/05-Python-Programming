class BankAccount:

    def __init__(self, p_balance=0.00):
        self.__balance = p_balance

    # The __str__ method returns a string
    # indicating the object's state
    def __str__(self):
        return f'Current balance is ${self.__balance:,.2f}'

    def deposit(self, p_amount):
        self.__balance += p_amount

    def withdraw(self, p_amount):
        if self.__balance >= p_amount:
            self.__balance -= p_amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self):
        return self.__balance
