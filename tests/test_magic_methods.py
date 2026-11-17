from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


def test_product_str(phone):
    assert str(phone) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_str(smartphones):
    assert str(smartphones) == "Смартфоны, количество продуктов: 22 шт."


def test_category_str_after_add(smartphones, tv):
    smartphones.add_product(tv)
    assert str(smartphones) == "Смартфоны, количество продуктов: 29 шт."


def test_empty_category_str():
    category = Category("Пусто", "Тут пока ничего нет")
    assert str(category) == "Пусто, количество продуктов: 0 шт."


def test_products_getter(smartphones):
    assert smartphones.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_product_add():
    a = Product("Чай", "Черный", 100, 10)
    b = Product("Кофе", "Молотый", 200, 2)
    assert a + b == 1400


def test_product_add_real_products(phone, second_phone):
    assert phone + second_phone == 210000.0 * 8 + 31000.0 * 14


def test_category_iterator(smartphones, phone, second_phone):
    products = []
    for product in CategoryIterator(smartphones):
        products.append(product)
    assert products == [phone, second_phone]


def test_category_iterator_empty():
    category = Category("Пусто", "Тут пока ничего нет")
    assert list(CategoryIterator(category)) == []
