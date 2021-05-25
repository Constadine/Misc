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
        total_price = 0
        for order in self.orders:
            st += "\n" + str(order)
            total_price += order.payment
        st += f"\nTotal price: {total_price}$"
        return st


class Order:
    def __init__(self, date, payment) -> None:
        self.date = date
        self.payment = payment.price

    def __str__(self) -> str:
        return f"Date: {self.date}. Payment: {self.payment}$"


class Payment:
    def __init__(self, amount) -> None:
        self.price = amount

    def __str__(self) -> str:
        return str(self.amount)


c = Customer("Kostis Pap", "Emo Avenue")

order1, order2, order3 = Order("20201105", Payment(120.21)), Order(
    "20210102", Payment(24.51)), Order("20210312", Payment(12.32))


for i in range(1, 4):
    c.place_order(eval("order"+str(i)))

print(c)
