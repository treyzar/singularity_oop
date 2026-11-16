import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает его содержимое."""
    with open(path, encoding="utf-8") as file:
        data: list[dict[str, Any]] = json.load(file)
    return data


def create_objects_from_json(data: list[dict[str, Any]]) -> list[Category]:
    """Создает категории с товарами из данных, прочитанных из JSON."""
    categories = []
    for category_data in data:
        products = [Product(**product) for product in category_data.get("products", [])]
        categories.append(Category(category_data["name"], category_data["description"], products))
    return categories


def load_categories(path: str) -> list[Category]:
    """Загружает категории и товары из JSON-файла."""
    return create_objects_from_json(read_json(path))


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    for category in load_categories(file_path):
        print(category.name, len(category.products))
