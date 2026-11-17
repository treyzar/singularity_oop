from src.category import Category
from src.product import Product


class CategoryIterator:
    """Итератор по товарам категории."""

    def __init__(self, category: Category) -> None:
        self.products = category.products_list
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration
