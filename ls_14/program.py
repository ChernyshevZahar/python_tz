class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Недостаточно средств на счете.")

class Not_gut_valeu(Exception):
    def __init__(self):
        super().__init__('Нельзя добавлять отрецательное число')


class BankAccount:
    def __init__(self,balanse = 0):

        self.balance = balanse

    def deposit(self,num):
        if num <= 0:
            raise ValueError
        self.balance += num

        
    def withdraw(self,num):
        if self.balance < num :
            raise InsufficientFundsError
        self.balance -= num
        
    def get_balance(self):
        return self.balance
    


