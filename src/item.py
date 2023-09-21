class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError('Количество должно быть числом.')
        if not isinstance(price, int):
            raise ValueError('Цена должна быть числом.')
        self.name = name
        self.price = price
        self.amount = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.amount

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate
