from src.product import Product


class Category:
    """Категория товаров."""

    name: str
    description: str

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Список товаров категории строкой, по одному товару на строку."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def products_list(self) -> list[Product]:
        """Копия списка товаров, чтобы с ними можно было работать как с объектами."""
        return list(self.__products)
