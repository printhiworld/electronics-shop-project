from src.item import Item


class MixinLog:
    lang = ['EN', 'RU']
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, amount: int,) -> None:
        super().__init__(name, price, amount)
        MixinLog.__init__(self)
