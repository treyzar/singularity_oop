import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Обнуляет счетчики, чтобы тесты не влияли друг на друга."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def phone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def second_phone():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def tv():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def smartphones(phone, second_phone):
    return Category("Смартфоны", "Телефоны на любой вкус", [phone, second_phone])


@pytest.fixture
def products_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Телефоны на любой вкус",
            "products": [
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Большие экраны",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7},
            ],
        },
    ]
