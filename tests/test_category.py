import pytest

from src.category import Category
from src.product import Product


def test_category_init(smartphones, phone, second_phone):
    assert smartphones.name == "Смартфоны"
    assert smartphones.description == "Телефоны на любой вкус"
    assert smartphones.products_list == [phone, second_phone]
    assert all(isinstance(product, Product) for product in smartphones.products_list)


def test_category_without_products():
    category = Category("Пусто", "Тут пока ничего нет")
    assert category.products == ""
    assert category.products_list == []
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


def test_products_is_private(smartphones):
    with pytest.raises(AttributeError):
        smartphones.__products


def test_products_getter(smartphones):
    assert smartphones.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_products_getter_cant_be_set(smartphones):
    with pytest.raises(AttributeError):
        smartphones.products = []


def test_products_list_is_copy(smartphones, tv):
    smartphones.products_list.append(tv)
    assert len(smartphones.products_list) == 2


def test_add_product(smartphones, tv):
    result = smartphones.add_product(tv)
    assert result is None
    assert smartphones.products_list[-1] is tv
    assert smartphones.products.endswith('55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n')
    assert Category.product_count == 3


def test_add_product_to_empty_category(tv):
    category = Category("Телевизоры", "Большие экраны")
    category.add_product(tv)
    assert category.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    assert Category.product_count == 1
