class Account:
    bank = "ПитонБанк"
    count = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        Account.count += 1

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

a = Account("Аня")
b = Account("Боря", 500)
assert Account.count == 2
assert a.bank == b.bank == "ПитонБанк"

assert a.deposit(300) is True
assert a.deposit(-5) is False
assert a.balance == 300

assert b.withdraw(1000) is False
assert b.withdraw(200) is True
assert b.balance == 300
print("Все тесты пройдены")