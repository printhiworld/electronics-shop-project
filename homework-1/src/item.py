class Item:
    pay_rate = 1
    all = []
    def __init__(self, name, price, amount):
        if not isinstance(amount, int):
            raise ValueError('Количество должно быть числом.')
        if not isinstance(price, int):
            raise ValueError('Цена должна быть числом.')
        self.name = name
        self.price = price
        self.amount = amount

        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.amount

    def apply_discount(self):
        self.price = self.price * self.pay_rate


