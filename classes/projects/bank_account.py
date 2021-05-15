class Account:
    def __init__(self, iban, person, balance) -> None:
        self.iban = str(iban)
        self.person = person
        self.balance = float(balance)

    def transfer(self, account, amount):
        if account.balance > float(amount):
            self.balance += amount
            account.balance -= amount
            print(
                f"{float(amount)}$ from {account.person.fullname} were transfered to {self.person.fullname}")
        else:
            print("Not enough credit")


class Person:
    def __init__(self, fullname, age, id) -> None:
        self.fullname = fullname
        self.age = age
        self.id = id


konos = Person("Kon Pap", 25, "AE610512")
kronk = Person("Kon Kronk", 25, "AO124562")

bank_account1 = Account("123456789123456", konos, 666)
bank_account2 = Account("987654321987654", kronk, 3000)


print(bank_account1.balance, bank_account2.balance)
bank_account1.transfer(bank_account2, 500)
print(bank_account1.balance, bank_account2.balance)
