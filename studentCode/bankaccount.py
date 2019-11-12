class BankAccount:

    def __init__(self, p_balance=0):
        self.__balance = p_balance

    def deposit(self, p_amount):
        self.__balance += p_amount

    def withdraw(self, p_amount):
        if self.__balance >= p_amount:
            self.__balance -= p_amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self):
        return self.__balance

    
