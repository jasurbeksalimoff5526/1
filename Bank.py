class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            return f"{self.account_number} xisob raqami balansiga {amount}$ qo'shildi"
        else:
            return "Error"


    def withdraw(self, amount):
        if 0 < amount <= self.balance :
            self.balance -= amount
            return f"{self.account_number} xisob raqami balansidan {amount}$ yechildi"
        else:
            return f"Balans yetarli emas"

    def show_balance(self):
        return f"{self.account_number} xisob raqami balansi: {self.balance}$"


account1 = BankAccount("12345" )
account1.deposit(200)
account1.withdraw(200)
# print(account1.show_balance())


class Client:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def show_info(self):
        return f"Mijoz ismi: {self.name}\nXisob raqami: {self.account.account_number}\nBalans: {self.account.balance}"


client1 = Client("Jasurbek", account1)

print(client1.show_info())