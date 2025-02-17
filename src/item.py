class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError('Количество должно быть числом.')
        if not isinstance(price, int):
            raise ValueError('Цена должна быть числом.')
        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой.')
        self.__name = name
        self.price = price
        self.amount = amount

        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.amount})"

    def __str__(self):
        return self.name

    def calculate_total_price(self) -> float:
        return self.price * self.amount

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = self.name
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file='../src/items.csv'):
        try:
            with open(file, 'r', encoding='latin-1') as file:
                lines = file.readlines()
                lines = lines[1:]
                for row in lines:
                    try:
                        name, price, amount = row.split(',')
                        price = int(price)
                        amount = int(amount)
                        cls(name, price, amount)
                    except Exception:
                        raise InstantiateCSVError

            return cls.all
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(n):
        return int(float(n))

    def __add__(self, other):
        if other.__class__.__name__ == 'Phone' or other.__class__.__name__ == 'Item':
            return self.amount + other.amount
        return None


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл items.csv поврежден'

    def __str__(self):
        return self.message

