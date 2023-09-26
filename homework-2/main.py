from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    item.name = 'СуперСмартфон'

    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 6

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5