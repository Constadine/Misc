class Customer:
    def __init__(self, full_name, address, orders=None) -> None:
        self.full_name = full_name
        self.address = address
        if orders is None:
            self.orders = []
        else:
            self.orders = orders

    def place_order(self, order):
        self.orders += [order]

    def __str__(self) -> str:
        st = f"\nName: {self.full_name}, Address: {self.address}"
        st += "\n" + "-" * 35
        total = 0
        for order in self.orders:
            st += "\n" + str(order)
            total += order.payment.amount
        st += f"\nTotal: {total}$"
        return st


class Order:
    def __init__(self, date, payment) -> None:
        self.date = date
        self.payment = payment

    def __str__(self) -> str:
        return f"Date: {self.date}. Payment: {self.payment}$"


class Payment:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return str(self.amount)


class Credit(Payment):
    def __init__(self, amount, number, exp_date) -> None:
        super().__init__(amount)
        self.number = number
        self.exp_date = exp_date

    def __str__(self):
        return super().__str__() + ". CREDIT: Number: " + self.number + " Exp.Date" + self.exp_date


class Check(Payment):
    def __init__(self, amount, number, bank_code) -> None:
        super().__init__(amount)
        self.number = number
        self.bank_code = bank_code

    def __str__(self) -> str:
        return f"{super().__str__()} with CHECK: Number: {self.number}, Bank Code: {self.bank_code}"


c = Customer("Kostis Pap", "Emo Avenue")

order1, order2, order3 = Order("20201105", Payment(120.21)), Order(
    "20210102", Credit(24.51, "1512-15215-25626", "02/02/2050")), Order("20210312", Check(1562.32, "124215-215121-5125", "2151256312515"))


for i in range(1, 4):
    c.place_order(eval("order"+str(i)))


print(c)
