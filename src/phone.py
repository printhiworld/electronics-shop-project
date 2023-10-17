from src.item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, amount: int, sim) -> None:
        super().__init__(name, price, amount)
        self.__sim = sim

        Phone.all.append(self)

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.amount}, {self.__sim})"

    @property
    def number_of_sim(self):
        return self.__sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        self.__sim = num
