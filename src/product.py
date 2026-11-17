from typing import Any


class Product:
    """Товар магазина."""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Общая стоимость двух товаров на складе."""
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict[str, Any], products: list["Product"] | None = None) -> "Product":
        """Создает товар из словаря.

        Если передан список товаров и в нем уже есть товар с таким же названием,
        то новый товар не создается: количество складывается, а цена берется большая.
        """
        if products:
            for product in products:
                if product.name.lower() == product_data["name"].lower():
                    product.quantity += product_data["quantity"]
                    product.price = max(product.price, product_data["price"])
                    return product

        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            try:
                answer = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердить? (y/n): ")
            except EOFError:
                answer = ""
            if answer.strip().lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price
