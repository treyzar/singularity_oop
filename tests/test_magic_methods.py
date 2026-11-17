import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


@pytest.mark.parametrize("price, expected", [(80, "80"), (80.0, "80.0"), (80.5, "80.5")])
def test_строка_товара(price, expected):
    product = Product("Чай", "Черный чай", price, 15)
    assert str(product) == f"Чай, {expected} руб. Остаток: 15 шт."


def test_строка_товара_без_остатка():
    assert str(Product("Чай", "Черный чай", 80, 0)) == "Чай, 80 руб. Остаток: 0 шт."


def test_категория_считает_остатки(smartphones):
    assert str(smartphones) == "Смартфоны, количество продуктов: 22 шт."


def test_пустая_категория():
    assert str(Category("Напитки", "Чай и кофе")) == "Напитки, количество продуктов: 0 шт."


def test_остатки_обновляются(smartphones, phone, tv):
    smartphones.add_product(tv)
    assert str(smartphones) == "Смартфоны, количество продуктов: 29 шт."
    phone.quantity = 0
    assert str(smartphones) == "Смартфоны, количество продуктов: 21 шт."


def test_список_использует_строковое_представление():
    class SpecialProduct(Product):
        def __str__(self):
            return "Товар по акции"

    category = Category("Акции", "Специальные предложения", [SpecialProduct("Чай", "", 80, 15)])
    assert category.products == "Товар по акции\n"


@pytest.mark.parametrize(
    "price1, quantity1, price2, quantity2, expected",
    [(100, 10, 200, 2, 1400), (100, 0, 200, 2, 400), (100, 0, 200, 0, 0), (10.5, 3, 20.25, 2, 72)],
)
def test_сложение_стоимости_остатков(price1, quantity1, price2, quantity2, expected):
    first = Product("Чай", "", price1, quantity1)
    second = Product("Кофе", "", price2, quantity2)
    assert first + second == expected
    assert second + first == expected
    assert (first.price, first.quantity) == (price1, quantity1)
    assert (second.price, second.quantity) == (price2, quantity2)


def test_сложение_товара_с_собой():
    product = Product("Чай", "", 100, 10)
    assert product + product == 2000


@pytest.mark.parametrize("other", [1, "товар", None])
def test_сложение_с_другим_типом(phone, other):
    with pytest.raises(TypeError):
        phone + other


def test_итератор_возвращает_товары(smartphones, phone, second_phone):
    iterator = CategoryIterator(smartphones)
    assert iter(iterator) is iterator
    assert next(iterator) is phone
    assert next(iterator) is second_phone
    with pytest.raises(StopIteration):
        next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


def test_пустой_итератор():
    iterator = CategoryIterator(Category("Напитки", "Чай и кофе"))
    assert list(iterator) == []


def test_независимые_итераторы(smartphones, phone, second_phone):
    first = CategoryIterator(smartphones)
    second = CategoryIterator(smartphones)
    assert next(first) is phone
    assert list(first) == [second_phone]
    assert [product for product in second] == [phone, second_phone]
