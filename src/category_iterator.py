from src.category import Category
from src.product import Product


class CategoryIterator:
    """Перебирает товары категории в порядке добавления."""

    def __init__(self, category: Category) -> None:
        self.__products = category.products_list
        self.__index = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает текущий итератор, не сбрасывая его позицию."""
        return self

    def __next__(self) -> Product:
        """Возвращает очередной товар или завершает перебор."""
        if self.__index >= len(self.__products):
            raise StopIteration
        product = self.__products[self.__index]
        self.__index += 1
        return product
