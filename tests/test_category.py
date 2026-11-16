from src.category import Category
from src.product import Product


def test_category_init(smartphones, phone, second_phone):
    assert smartphones.name == "Смартфоны"
    assert smartphones.description == "Телефоны на любой вкус"
    assert smartphones.products == [phone, second_phone]
    assert all(isinstance(product, Product) for product in smartphones.products)


def test_category_without_products():
    category = Category("Пусто", "Тут пока ничего нет")
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_count(smartphones, tv):
    assert Category.category_count == 1
    Category("Телевизоры", "Большие экраны", [tv])
    assert Category.category_count == 2


def test_product_count(smartphones, tv):
    assert Category.product_count == 2
    Category("Телевизоры", "Большие экраны", [tv])
    assert Category.product_count == 3


def test_counters_available_from_object(smartphones):
    assert smartphones.category_count == Category.category_count == 1
    assert smartphones.product_count == Category.product_count == 2
