import pytest

from src.product import Product


def test_product_init(phone):
    assert phone.name == "Iphone 15"
    assert phone.description == "512GB, Gray space"
    assert phone.price == 210000.0
    assert phone.quantity == 8


def test_product_types(phone):
    assert isinstance(phone.price, float)
    assert isinstance(phone.quantity, int)


def test_price_is_private(phone):
    with pytest.raises(AttributeError):
        phone.__price


def test_price_setter(phone):
    phone.price = 250000.0
    assert phone.price == 250000.0


@pytest.mark.parametrize("bad_price", [0, -100])
def test_price_setter_bad_value(phone, capsys, bad_price):
    phone.price = bad_price
    assert phone.price == 210000.0
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"


def test_new_product():
    data = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_new_product_without_duplicates(phone):
    data = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    product = Product.new_product(data, [phone])
    assert product is not phone
    assert product.name == "Xiaomi Redmi Note 11"


def test_new_product_duplicate_higher_price(phone):
    data = {"name": "iphone 15", "description": "512GB, Gray space", "price": 220000.0, "quantity": 2}
    product = Product.new_product(data, [phone])
    assert product is phone
    assert product.quantity == 10
    assert product.price == 220000.0


def test_new_product_duplicate_lower_price(phone):
    data = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 100000.0, "quantity": 1}
    product = Product.new_product(data, [phone])
    assert product is phone
    assert product.quantity == 9
    assert product.price == 210000.0
