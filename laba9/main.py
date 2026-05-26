class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = [f"Открыт счет. Баланс: {self.balance}"]

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
            return
        self.balance -= amount
        self.history.append(f"Снятие: -{amount}. Баланс: {self.balance}")

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self.balance:
            print("Нельзя снять больше, чем есть на счете")
            return
        super().withdraw(amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.history.append(f"Начислены проценты: +{interest}. Баланс: {self.balance}")


class CreditAccount(BankAccount):
    def __init__(self, balance=0, limit=10000, commission=0.02):
        super().__init__(balance)
        self.limit = limit
        self.commission = commission

    def withdraw(self, amount):
        total = amount + amount * self.commission
        if self.balance - total < -self.limit:
            print("Превышен кредитный лимит")
            return
        self.balance -= total
        self.history.append(f"Снятие с комиссией: -{total}. Баланс: {self.balance}")


if __name__ == '__main__':
    acc1 = SavingsAccount(1000, 0.1)
    acc1.deposit(500)
    acc1.withdraw(300)
    acc1.add_interest()
    print(acc1.get_balance())
    print(acc1.get_history())

    acc2 = CreditAccount(5000)
    acc2.withdraw(4000)
    acc2.withdraw(15000)
    print(acc2.get_balance())
    print(acc2.get_history())


