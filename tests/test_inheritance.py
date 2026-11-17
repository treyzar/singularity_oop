import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def smartphone():
    return Smartphone("Смартфон", "Для связи", 10000.0, 2, 95.5, "Модель 1", 128, "Синий")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Газонная трава", "Для сада", 500.0, 3, "Россия", "7 дней", "Зелёный")


def test_smartphone_attributes(smartphone):
    assert isinstance(smartphone, Product)
    assert (smartphone.name, smartphone.description, smartphone.price, smartphone.quantity) == (
        "Смартфон",
        "Для связи",
        10000.0,
        2,
    )
    assert (smartphone.efficiency, smartphone.model, smartphone.memory, smartphone.color) == (
        95.5,
        "Модель 1",
        128,
        "Синий",
    )


def test_lawn_grass_attributes(lawn_grass):
    assert isinstance(lawn_grass, Product)
    assert (lawn_grass.name, lawn_grass.description, lawn_grass.price, lawn_grass.quantity) == (
        "Газонная трава",
        "Для сада",
        500.0,
        3,
    )
    assert (lawn_grass.country, lawn_grass.germination_period, lawn_grass.color) == ("Россия", "7 дней", "Зелёный")


@pytest.mark.parametrize("fixture_name", ["smartphone", "lawn_grass"])
def test_inherited_price_setter(fixture_name, request, monkeypatch):
    product = request.getfixturevalue(fixture_name)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 100.0
    assert product.price == 100.0
    product.price = 0
    assert product.price == 100.0


def test_inherited_str(smartphone, lawn_grass):
    assert str(smartphone) == "Смартфон, 10000.0 руб. Остаток: 2 шт."
    assert str(lawn_grass) == "Газонная трава, 500.0 руб. Остаток: 3 шт."


def test_add_smartphones(smartphone):
    second = Smartphone("Другой смартфон", "Для работы", 20000.0, 3, 99.0, "Модель 2", 256, "Чёрный")
    assert smartphone + second == 80000.0


def test_add_lawn_grass(lawn_grass):
    second = LawnGrass("Другой газон", "Для парка", 700.0, 4, "Россия", "10 дней", "Зелёный")
    assert lawn_grass + second == 4300.0


@pytest.mark.parametrize(
    "left,right",
    [
        ("smartphone", "lawn_grass"),
        ("lawn_grass", "smartphone"),
        ("phone", "smartphone"),
        ("smartphone", "phone"),
        ("phone", "lawn_grass"),
        ("lawn_grass", "phone"),
    ],
)
def test_add_different_classes_raises(left, right, request):
    with pytest.raises(TypeError):
        request.getfixturevalue(left) + request.getfixturevalue(right)


@pytest.mark.parametrize("invalid", [None, 10, "товар", {}, object(), Product])
def test_add_non_product_raises(phone, invalid):
    with pytest.raises(TypeError):
        phone + invalid


def test_add_smartphone_subclass_raises(smartphone):
    class GamingSmartphone(Smartphone):
        pass

    gaming = GamingSmartphone("Игровой смартфон", "Для игр", 30000.0, 1, 100.0, "Модель 3", 512, "Красный")
    with pytest.raises(TypeError):
        smartphone + gaming
    with pytest.raises(TypeError):
        gaming + smartphone


def test_category_accepts_products_and_subclasses(phone, smartphone, lawn_grass):
    category = Category("Товары", "Все товары")
    for product in (phone, smartphone, lawn_grass):
        category.add_product(product)
    assert category.products_list == [phone, smartphone, lawn_grass]
    assert list(CategoryIterator(category)) == [phone, smartphone, lawn_grass]
    assert Category.product_count == 3
    assert str(category) == "Товары, количество продуктов: 13 шт."


@pytest.mark.parametrize("invalid", [None, 10, "товар", {}, [], object(), Product, Smartphone, LawnGrass])
def test_category_rejects_non_product(smartphones, invalid):
    before = smartphones.products_list
    with pytest.raises(TypeError):
        smartphones.add_product(invalid)
    assert smartphones.products_list == before
    assert Category.product_count == 2
    assert Category.category_count == 1
