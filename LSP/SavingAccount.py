from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self._balance - amount >= 100: # Minimum balance must be 100
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")