import json

from src.category import Category
from src.utils import create_objects_from_json, load_categories, read_json


def test_read_json(tmp_path, products_data):
    path = tmp_path / "products.json"
    path.write_text(json.dumps(products_data, ensure_ascii=False), encoding="utf-8")
    assert read_json(str(path)) == products_data


def test_create_objects_from_json(products_data):
    categories = create_objects_from_json(products_data)
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[0].products_list[1].name == "Xiaomi Redmi Note 11"
    assert categories[1].products_list[0].price == 123000.0
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_load_categories(tmp_path, products_data):
    path = tmp_path / "products.json"
    path.write_text(json.dumps(products_data, ensure_ascii=False), encoding="utf-8")
    categories = load_categories(str(path))
    assert [category.name for category in categories] == ["Смартфоны", "Телевизоры"]
