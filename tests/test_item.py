import pytest
from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone



@pytest.fixture
def apple_phone():
    return Item('ipone', 50000, 10)


def test_calculate_price(apple_phone):
    assert apple_phone.calculate_total_price() == 500000


def test_apply_discount(apple_phone):
    Item.pay_rate = 0.5
    apple_phone.apply_discount()
    assert apple_phone.price == 25000


def test_apple_phone_2():
    with pytest.raises(ValueError):
        Item('ipone', '5', 10)


def test_apple_phone_3():
    with pytest.raises(ValueError):
        Item(100, 50000, '10')


def test_string_to_number():
    assert Item.string_to_number("54321") == 54321
    assert Item.string_to_number("4.1") == 4


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


@pytest.fixture
def a_phone():
    return Phone('ipone', 50000, 10, 2)


def test_repr():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 2)"


def test_str():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    assert str(phone1) == 'Смартфон'


def test_add():
    item1= Item('ipone', 50000, 10)
    phone1 = Phone("Смартфон", 10000, 20, 2)
    assert item1 + phone1 == 30


def test_change():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'


def test_change():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"


